# Calendario di Graziana

Un sito web semplice e chiaro per visualizzare:
- La raccolta differenziata di oggi e domani
- I compleanni della settimana corrente

## Come usare

### 1. Configura i compleanni

Modifica il file `birthdays.json` con i compleanni della tua famiglia:

```json
[
  {
    "name": "Nome Persona",
    "month": 3,
    "day": 15
  }
]
```

- `name`: il nome della persona
- `month`: il mese (1-12)
- `day`: il giorno del mese

### 2. Apri il sito web

Hai diverse opzioni:

#### Opzione A: Apri direttamente il file
Doppio click su `index.html` - funzionerà nella maggior parte dei browser moderni.

#### Opzione B: Usa un server locale
Se il browser blocca il caricamento dei file JSON, avvia un server locale:

```bash
# Con Python 3
python3 -m http.server 8000

# Oppure con Python 2
python -m SimpleHTTPServer 8000

# Oppure con Node.js (se hai npx)
npx http-server
```

Poi apri il browser su `http://localhost:8000`

#### Opzione C: Metti online (per accedere da qualsiasi dispositivo)

1. Carica tutti i file su un servizio gratuito come:
   - GitHub Pages (gratis)
   - Netlify (gratis)
   - Vercel (gratis)

2. Oppure mettili in una cartella condivisa sul tuo server/NAS se ne hai uno

## Installazione come App su Android/iPhone

Il sito può essere installato come app sul telefono!

### Su Android:
1. Apri il sito nel browser Chrome
2. Tocca i tre puntini in alto a destra
3. Seleziona "Installa app" o "Aggiungi a schermata Home"
4. L'app apparirà nella home come una normale applicazione

### Su iPhone:
1. Apri il sito in Safari
2. Tocca il pulsante Condividi (quadrato con freccia)
3. Scorri e seleziona "Aggiungi a Home"
4. Conferma il nome e tocca "Aggiungi"

## Caratteristiche

- ✨ **Zero dipendenze** - solo un file HTML
- 🔄 **Auto-refresh** - si aggiorna automaticamente a mezzanotte
- 📱 **Responsive** - funziona su telefoni e tablet
- 📲 **Installabile** - può essere installata come app nativa
- 💾 **Funziona offline** - dati salvati nella cache
- 🇮🇹 **Tutto in italiano**
- 👀 **Testo grande e chiaro** - facile da leggere

## File

- `index.html` - il sito web principale
- `motta_2026_recycling_calendar_full.json` - calendario raccolta differenziata
- `birthdays.json` - lista compleanni da modificare

## Note

Il sito si aggiorna automaticamente ogni giorno a mezzanotte. Se il browser rimane aperto, vedrai sempre le informazioni corrette per il giorno attuale.
