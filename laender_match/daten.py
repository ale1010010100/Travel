"""Länderdaten: ISO-3166-1-Codes mit deutschem und englischem Namen.

Jede Zeile: Alpha-2 | Alpha-3 | deutscher Name | englischer Name | weitere Namen (mit ; getrennt)
"""

LAENDER_ROH = """
AF|AFG|Afghanistan|Afghanistan|
EG|EGY|Ägypten|Egypt|
AL|ALB|Albanien|Albania|
DZ|DZA|Algerien|Algeria|
AD|AND|Andorra|Andorra|
AO|AGO|Angola|Angola|
AG|ATG|Antigua und Barbuda|Antigua and Barbuda|
GQ|GNQ|Äquatorialguinea|Equatorial Guinea|
AR|ARG|Argentinien|Argentina|
AM|ARM|Armenien|Armenia|
AZ|AZE|Aserbaidschan|Azerbaijan|
ET|ETH|Äthiopien|Ethiopia|
AU|AUS|Australien|Australia|
BS|BHS|Bahamas|Bahamas|
BH|BHR|Bahrain|Bahrain|
BD|BGD|Bangladesch|Bangladesh|
BB|BRB|Barbados|Barbados|
BE|BEL|Belgien|Belgium|
BZ|BLZ|Belize|Belize|
BJ|BEN|Benin|Benin|
BT|BTN|Bhutan|Bhutan|
BO|BOL|Bolivien|Bolivia|
BA|BIH|Bosnien und Herzegowina|Bosnia and Herzegovina|Bosnien
BW|BWA|Botswana|Botswana|
BR|BRA|Brasilien|Brazil|
BN|BRN|Brunei|Brunei|
BG|BGR|Bulgarien|Bulgaria|
BF|BFA|Burkina Faso|Burkina Faso|
BI|BDI|Burundi|Burundi|
CL|CHL|Chile|Chile|
CN|CHN|China|China|Volksrepublik China
CR|CRI|Costa Rica|Costa Rica|
CI|CIV|Elfenbeinküste|Côte d'Ivoire|Ivory Coast
DK|DNK|Dänemark|Denmark|
DE|DEU|Deutschland|Germany|Bundesrepublik Deutschland;BRD
DM|DMA|Dominica|Dominica|
DO|DOM|Dominikanische Republik|Dominican Republic|
DJ|DJI|Dschibuti|Djibouti|
EC|ECU|Ecuador|Ecuador|
SV|SLV|El Salvador|El Salvador|
ER|ERI|Eritrea|Eritrea|
EE|EST|Estland|Estonia|
SZ|SWZ|Eswatini|Eswatini|Swasiland;Swaziland
FJ|FJI|Fidschi|Fiji|
FI|FIN|Finnland|Finland|
FR|FRA|Frankreich|France|
GA|GAB|Gabun|Gabon|
GM|GMB|Gambia|Gambia|
GE|GEO|Georgien|Georgia|
GH|GHA|Ghana|Ghana|
GD|GRD|Grenada|Grenada|
GR|GRC|Griechenland|Greece|
GT|GTM|Guatemala|Guatemala|
GN|GIN|Guinea|Guinea|
GW|GNB|Guinea-Bissau|Guinea-Bissau|
GY|GUY|Guyana|Guyana|
HT|HTI|Haiti|Haiti|
HN|HND|Honduras|Honduras|
IN|IND|Indien|India|
ID|IDN|Indonesien|Indonesia|
IQ|IRQ|Irak|Iraq|
IR|IRN|Iran|Iran|
IE|IRL|Irland|Ireland|
IS|ISL|Island|Iceland|
IL|ISR|Israel|Israel|
IT|ITA|Italien|Italy|
JM|JAM|Jamaika|Jamaica|
JP|JPN|Japan|Japan|
YE|YEM|Jemen|Yemen|
JO|JOR|Jordanien|Jordan|
KH|KHM|Kambodscha|Cambodia|
CM|CMR|Kamerun|Cameroon|
CA|CAN|Kanada|Canada|
CV|CPV|Kap Verde|Cabo Verde|Cape Verde
KZ|KAZ|Kasachstan|Kazakhstan|
QA|QAT|Katar|Qatar|
KE|KEN|Kenia|Kenya|
KG|KGZ|Kirgisistan|Kyrgyzstan|
KI|KIR|Kiribati|Kiribati|
CO|COL|Kolumbien|Colombia|
KM|COM|Komoren|Comoros|
CD|COD|Demokratische Republik Kongo|Democratic Republic of the Congo|DR Kongo;Kongo-Kinshasa
CG|COG|Republik Kongo|Republic of the Congo|Kongo;Kongo-Brazzaville;Congo
KP|PRK|Nordkorea|North Korea|
KR|KOR|Südkorea|South Korea|Korea
XK|XKX|Kosovo|Kosovo|
HR|HRV|Kroatien|Croatia|
CU|CUB|Kuba|Cuba|
KW|KWT|Kuwait|Kuwait|
LA|LAO|Laos|Laos|
LS|LSO|Lesotho|Lesotho|
LV|LVA|Lettland|Latvia|
LB|LBN|Libanon|Lebanon|
LR|LBR|Liberia|Liberia|
LY|LBY|Libyen|Libya|
LI|LIE|Liechtenstein|Liechtenstein|
LT|LTU|Litauen|Lithuania|
LU|LUX|Luxemburg|Luxembourg|
MG|MDG|Madagaskar|Madagascar|
MW|MWI|Malawi|Malawi|
MY|MYS|Malaysia|Malaysia|
MV|MDV|Malediven|Maldives|
ML|MLI|Mali|Mali|
MT|MLT|Malta|Malta|
MA|MAR|Marokko|Morocco|
MH|MHL|Marshallinseln|Marshall Islands|
MR|MRT|Mauretanien|Mauritania|
MU|MUS|Mauritius|Mauritius|
MX|MEX|Mexiko|Mexico|
FM|FSM|Mikronesien|Micronesia|
MD|MDA|Moldau|Moldova|Moldawien
MC|MCO|Monaco|Monaco|
MN|MNG|Mongolei|Mongolia|
ME|MNE|Montenegro|Montenegro|
MZ|MOZ|Mosambik|Mozambique|
MM|MMR|Myanmar|Myanmar|Birma;Burma
NA|NAM|Namibia|Namibia|
NR|NRU|Nauru|Nauru|
NP|NPL|Nepal|Nepal|
NZ|NZL|Neuseeland|New Zealand|
NI|NIC|Nicaragua|Nicaragua|
NL|NLD|Niederlande|Netherlands|Holland
NE|NER|Niger|Niger|
NG|NGA|Nigeria|Nigeria|
MK|MKD|Nordmazedonien|North Macedonia|Mazedonien;Macedonia
NO|NOR|Norwegen|Norway|
OM|OMN|Oman|Oman|
AT|AUT|Österreich|Austria|
TL|TLS|Osttimor|Timor-Leste|East Timor
PK|PAK|Pakistan|Pakistan|
PS|PSE|Palästina|Palestine|
PW|PLW|Palau|Palau|
PA|PAN|Panama|Panama|
PG|PNG|Papua-Neuguinea|Papua New Guinea|
PY|PRY|Paraguay|Paraguay|
PE|PER|Peru|Peru|
PH|PHL|Philippinen|Philippines|
PL|POL|Polen|Poland|
PT|PRT|Portugal|Portugal|
RW|RWA|Ruanda|Rwanda|
RO|ROU|Rumänien|Romania|
RU|RUS|Russland|Russia|Russische Föderation;Russian Federation
SB|SLB|Salomonen|Solomon Islands|
ZM|ZMB|Sambia|Zambia|
WS|WSM|Samoa|Samoa|
SM|SMR|San Marino|San Marino|
ST|STP|São Tomé und Príncipe|São Tomé and Príncipe|
SA|SAU|Saudi-Arabien|Saudi Arabia|
SE|SWE|Schweden|Sweden|
CH|CHE|Schweiz|Switzerland|
SN|SEN|Senegal|Senegal|
RS|SRB|Serbien|Serbia|
SC|SYC|Seychellen|Seychelles|
SL|SLE|Sierra Leone|Sierra Leone|
ZW|ZWE|Simbabwe|Zimbabwe|
SG|SGP|Singapur|Singapore|
SK|SVK|Slowakei|Slovakia|
SI|SVN|Slowenien|Slovenia|
SO|SOM|Somalia|Somalia|
ES|ESP|Spanien|Spain|
LK|LKA|Sri Lanka|Sri Lanka|
KN|KNA|St. Kitts und Nevis|Saint Kitts and Nevis|
LC|LCA|St. Lucia|Saint Lucia|
VC|VCT|St. Vincent und die Grenadinen|Saint Vincent and the Grenadines|
ZA|ZAF|Südafrika|South Africa|
SD|SDN|Sudan|Sudan|
SS|SSD|Südsudan|South Sudan|
SR|SUR|Suriname|Suriname|
SY|SYR|Syrien|Syria|
TJ|TJK|Tadschikistan|Tajikistan|
TW|TWN|Taiwan|Taiwan|
TZ|TZA|Tansania|Tanzania|
TH|THA|Thailand|Thailand|
TG|TGO|Togo|Togo|
TO|TON|Tonga|Tonga|
TT|TTO|Trinidad und Tobago|Trinidad and Tobago|
TD|TCD|Tschad|Chad|
CZ|CZE|Tschechien|Czechia|Czech Republic;Tschechische Republik
TN|TUN|Tunesien|Tunisia|
TR|TUR|Türkei|Turkey|Türkiye
TM|TKM|Turkmenistan|Turkmenistan|
TV|TUV|Tuvalu|Tuvalu|
UG|UGA|Uganda|Uganda|
UA|UKR|Ukraine|Ukraine|
HU|HUN|Ungarn|Hungary|
UY|URY|Uruguay|Uruguay|
UZ|UZB|Usbekistan|Uzbekistan|
VU|VUT|Vanuatu|Vanuatu|
VA|VAT|Vatikanstadt|Vatican City|Vatikan;Heiliger Stuhl;Holy See
VE|VEN|Venezuela|Venezuela|
AE|ARE|Vereinigte Arabische Emirate|United Arab Emirates|VAE;UAE;Emirate
GB|GBR|Vereinigtes Königreich|United Kingdom|Großbritannien;Great Britain;England;UK
US|USA|Vereinigte Staaten|United States|Vereinigte Staaten von Amerika;United States of America;Amerika;America
VN|VNM|Vietnam|Vietnam|
BY|BLR|Belarus|Belarus|Weißrussland
CF|CAF|Zentralafrikanische Republik|Central African Republic|
CY|CYP|Zypern|Cyprus|
"""
