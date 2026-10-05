"""Ordnet freie Ländereingaben einem Land mit ISO-3166-1-Code zu.

Beispiel:
    >>> finde_land("Deutchland").alpha2
    'DE'
"""

import difflib
import re
import unicodedata
from dataclasses import dataclass

from .daten import LAENDER_ROH

__all__ = ["Land", "finde_land", "alle_laender"]

# Mindestähnlichkeit (0 bis 1) für die Zuordnung trotz Tippfehler.
AEHNLICHKEIT = 0.8


@dataclass(frozen=True)
class Land:
    alpha2: str
    alpha3: str
    name_de: str
    name_en: str


def _normalisiere(text, umlaut_als_e=True):
    """Kleinschreibung, Umlaute und Akzente auflösen, Satzzeichen entfernen."""
    text = text.strip().lower()
    if umlaut_als_e:
        text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    text = text.replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(z for z in text if not unicodedata.combining(z))
    text = text.replace("&", " und ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def _lade_laender():
    laender = []
    namen = {}
    codes = {}
    for zeile in LAENDER_ROH.strip().splitlines():
        alpha2, alpha3, name_de, name_en, weitere = zeile.split("|")
        land = Land(alpha2, alpha3, name_de, name_en)
        laender.append(land)
        codes[alpha2.lower()] = land
        codes[alpha3.lower()] = land
        aliase = [name_de, name_en] + [a for a in weitere.split(";") if a]
        for alias in aliase:
            # "Österreich" soll sowohl als "Oesterreich" als auch "Osterreich" passen.
            for schluessel in {_normalisiere(alias), _normalisiere(alias, umlaut_als_e=False)}:
                vorhanden = namen.setdefault(schluessel, land)
                if vorhanden is not land:
                    raise ValueError(f"Name {alias!r} ist doppelt vergeben")
    return laender, namen, codes


_LAENDER, _NAMEN, _CODES = _lade_laender()


def alle_laender():
    """Liste aller bekannten Länder."""
    return list(_LAENDER)


def finde_land(eingabe):
    """Gibt das passende Land zurück oder None, wenn nichts eindeutig passt.

    Akzeptiert deutsche und englische Namen, gängige Alternativnamen,
    ISO-Codes (Alpha-2 und Alpha-3) sowie kleine Tippfehler.
    """
    if not eingabe or not eingabe.strip():
        return None
    schluessel = _normalisiere(eingabe)

    if schluessel in _NAMEN:
        return _NAMEN[schluessel]
    if schluessel in _CODES:
        return _CODES[schluessel]

    # Tippfehler nur bei längeren Eingaben, sonst wird aus "XY" irgendein Land.
    if len(schluessel) < 4:
        return None
    treffer = difflib.get_close_matches(schluessel, _NAMEN, n=1, cutoff=AEHNLICHKEIT)
    return _NAMEN[treffer[0]] if treffer else None
