# Travel

## Länder-Zuordnung

`laender_match.finde_land()` ordnet freie Ländereingaben einem Land mit ISO-3166-1-Code zu.
Erkannt werden deutsche und englische Namen, gängige Alternativnamen (z. B. „Holland“, „UK“),
Alpha-2- und Alpha-3-Codes, Umlaute in jeder Schreibweise sowie kleine Tippfehler.

```python
from laender_match import finde_land

land = finde_land("Deutchland")
land.alpha2   # 'DE'
land.alpha3   # 'DEU'
land.name_de  # 'Deutschland'
land.name_en  # 'Germany'

finde_land("Atlantis")  # None
```

Tests ausführen (nur Python-Standardbibliothek nötig):

```sh
python3 -m unittest -v
```
