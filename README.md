
> Otevřít tuto stránku v aplikaci [https://barborateclova.github.io/hlasovani/](https://barborateclova.github.io/hlasovani/)

## Použít jako rozšíření

Toto úložiště lze přidat jako **rozšíření** v aplikaci MakeCode.

* otevřít [https://makecode.microbit.org/](https://makecode.microbit.org/)
* klikněte na možnost **Nový projekt**
* klikněte na možnost **Rozšíření** v nabídce s ozubeným kolem
* vyhledat **https://github.com/barborateclova/hlasovani** a importovat

## Upravit tento projekt ![Odznak stavu sestavení](https://github.com/barborateclova/hlasovani/workflows/MakeCode/badge.svg)

Slouží k úpravě tohoto úložiště v aplikaci MakeCode.

* otevřít [https://makecode.microbit.org/](https://makecode.microbit.org/)
* klikněte na možnost **Import** a poté na **Import adresy URL**
* vložte **https://github.com/barborateclova/hlasovani** a klikněte na možnost import

## Náhled bloků

Tento obrázek znázorňuje kód z Bloků od posledního potvrzení v hlavní verzi.
Tento obrázek se může aktualizovat až za několik minut.

![Vykreslený náhled bloků](https://github.com/barborateclova/hlasovani/raw/master/.github/makecode/blocks.png)

#### Metadata (slouží k vyhledávání, vykreslování)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>

#klient "ví", že může nebo nemůže hlasovat
#hlas lze změnit (např. z C na B) když je hlasování povoleno
#započítává se pouze poslední odeslaný hlas (v př. o řádek výše to je B)
#klient indikuje (LEDky nebo speaker) serverem úspěšně zaznamenaný hlas
#ze serveru lze hlasování povolit/zakázat, vynulovat hlasování
#server "nějak" zobrazí výsledky (klidně do konzole)