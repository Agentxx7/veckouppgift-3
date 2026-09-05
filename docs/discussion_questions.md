# Diskussionsfrågor – Veckouppgift 3

## 1. Vad är en regression? När inträffar de oftast under ett projekts livstid?

En regression innebär att funktionalitet som tidigare fungerade slutar
fungera, eller börjar bete sig fel, efter att något i koden har
förändrats. Regressioner uppstår oftast när:

- ny kod läggs till
- befintlig kod ändras eller refaktoreras
- buggar fixas (och fixen råkar påverka något annat)
- beroenden eller integrationer förändras (t.ex. uppdaterade bibliotek)

## 2. Vad är skillnaden mellan enhetstest och regressionstest?

Ett enhetstest testar en liten, isolerad del av programmet, till
exempel en enskild funktion eller klass, för att verifiera att just
den delen fungerar som tänkt.

Ett regressionstest handlar istället om syftet med testet: att
säkerställa att tidigare fungerande funktionalitet fortfarande
fungerar efter en förändring i koden.

Det betyder att ett och samma test kan vara båda sakerna beroende på
när det körs. Ett befintligt enhetstest fungerar som ett
regressionstest när det körs igen efter en kodändring, för att
kontrollera att förändringen inte förstörde något som redan
fungerade.

## 3. Vilka krav på git-kunskap kräver det av utvecklare att jobba med CI?

För att kunna arbeta med CI behöver utvecklare grundläggande
git-kunskap, bland annat:

- `clone` – hämta ner ett repo
- `branch` – skapa och arbeta i egna grenar
- `commit` – spara ändringar med tydliga meddelanden
- `push` – skicka upp commits till en remote
- `pull`/`fetch` – hämta hem andras ändringar
- `merge`/`rebase` på grundläggande nivå – slå ihop grenar
- konflikthantering – kunna lösa merge-konflikter när flera personer
  ändrat samma kod
- förståelse för att commits och pushar (t.ex. till main eller en PR)
  kan trigga CI-pipelines automatiskt, vilket ställer krav på att
  koden man skickar in faktiskt fungerar och är testad.

## 4. Vad är en feature? Hur förhåller det sig till kraven?

En feature är en konkret funktion eller egenskap som systemet
erbjuder användaren eller kunden, till exempel möjligheten att sortera
en lista eller logga in på ett konto.

Krav beskriver vad systemet ska kunna göra eller uppfylla på en mer
övergripande nivå. En eller flera features är det som konkret
implementerar dessa krav i praktiken. Man kan säga att kraven svarar
på "vad som behövs" medan features är "det som byggs" för att uppfylla
det behovet.

## 5. Vilka fördelar får en kund av att utvecklarna jobbar med CD?

Med Continuous Delivery (CD) blir koden alltid redo att levereras,
vilket ger kunden flera fördelar:

- nya funktioner och rättningar kan levereras snabbare
- mindre och tätare releaser innebär lägre risk per release
- kortare tid från att ett behov identifieras till att funktionen
  faktiskt är levererad
- snabbare feedback, eftersom kunden kan testa och tycka till om
  förändringar tidigare
- enklare att rätta problem, eftersom varje release innehåller färre
  förändringar att felsöka i

Det är värt att notera att Continuous Delivery innebär att koden är
redo att släppas när som helst, men det behöver inte betyda att varje
ändring automatiskt går till produktion utan mänskligt beslut — det är
snarare Continuous Deployment som innebär helt automatiska
produktionssättningar.

## 6. Vilka fördelar får utvecklare av att jobba med CD?

Utvecklare får också flera fördelar av att arbeta med CD:

- mindre förändringar per release, vilket gör varje release enklare
  att överblicka
- enklare felsökning, eftersom man snabbare kan peka ut vilken liten
  ändring som orsakade ett problem
- snabb feedback på om koden fungerar, både från automatiska tester
  och från verklig användning
- mindre manuellt releasearbete tack vare automatiserade steg
- färre stora och riskfyllda releaser, istället för sällan
  förekommande "big bang"-releaser
- en tydligare och repeterbar leveransprocess som alla i teamet kan
  lita på och följa

## 7. Varför kan man inte veta exakt hur lång tid det kommer ta att köra kod?

Den faktiska körtiden för ett program påverkas av väldigt många
faktorer utöver själva algoritmen, bland annat:

- datorns CPU och mängd minne
- operativsystemets schemaläggning av processer
- andra processer som körs samtidigt på samma maskin
- cache-beteende
- I/O, t.ex. disk- eller nätverksanrop
- indatans storlek och form
- vilket språk, implementation och interpreter/runtime som används

Eftersom dessa faktorer varierar mellan körningar och mellan olika
datorer går det inte att ange en exakt körtid. Därför använder man
istället tidskomplexitet, som beskriver hur arbetet växer när
indatans storlek växer, oberoende av vilken hårdvara koden körs på.

## 8. Varför skriver man till exempel O(n) men inte O(2*n + 10)?

Big O beskriver hur en algoritms arbete växer när indatastorleken `n`
blir stor. När `n` blir tillräckligt stort är det den snabbast
växande termen som avgör beteendet, medan konstanter och mindre
termer blir försumbara i jämförelse.

För uttrycket:

```
2*n + 10
```

är den dominerande termen `n`. Konstanten `2` (som multiplicerar `n`)
och den konstanta termen `10` ändrar inte hur algoritmen skalar när
`n` växer — de påverkar bara resultatet med en fast faktor/offset, inte
tillväxttakten.

Därför förenklar man och skriver:

```
O(2*n + 10) → O(n)
```
