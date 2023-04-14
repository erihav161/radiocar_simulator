# Radio Car Simulator
Kodtest för att simulera simulering av radio bil i ett rum där användaren väljer storleken på rummet (antalet celler), startposition för radiobilen samt riktning, och kommandon för hur bilen ska röra sig.

## Specifikationer
**Färger och linande har implementerats med hjälp av ramverket *blessed***
Kan installeras med hjälp av
`pip install blessed`

## Kör programmet
I terminalen:
`python3 main.py`

## Tillåtna kommandon
Simuleringen följer instruktionerna för kodtestet

**Storlek på rummet**
Ange två nummer `h w` avseende höjden och bredden på rummet, och tryck `Enter`. Skapar ett rutnät med *h* x *w* celler.

**Radiobilens startposition och riktning**
Ange två nummer `y x` (där `0 0` är positionerat längs ned i vänstra hörnet) samt en bokstav `R` (möjliga rikningar är *N, E, S, W*) och tryck `Enter`. Den valda cellen markeras med blått.

**Kommandon**
Ange ett antal bokstäver (möjliga kommandon är *F, B, L, R*) och avsluta med `Enter`. Rutnätet uppdateras utefter att bilen exekverar givna kommandon.

## Slut
Går allt bra avslutas simuleringen med nuvarande position och riktning på bilen.

Har fel eller ej tillåtna argument givits eller kör bilen in i väggen avslutas simuleringen och errormeddelande visas.
