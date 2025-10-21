
# 📘 ContaPagine — Automazione studio per esami

Questo script serve per **automatizzare la suddivisione delle pagine da studiare ogni giorno** per un esame universitario.

Inserisci i tuoi pdf e la data d'esame: lo script ti dirà esattamente quante pagine studiare al giorno e, se lo vuoi, creerà automaticamente su **Google Calendar** degli eventi giornalieri con il progresso da seguire.

---

## 🧩 Installazione

1. **Clona la repository**
```
   git clone https://github.com/marco-la-rosa/contapagine.git
   cd contapagine
```
2. **Crea a attiva l'ambiente virtuale**
```
  python -m venv .venv
  source .venv/bin/activate        # Linux/macOS
  .venv\Scripts\activate           # Windows
```
3. **Installa i pacchetti necessari**
```
  pip install -r requirements.txt
```

## 🔐 Configurazione

1. **Copia le credenziali di Google Cloud**
  
  - Crea un progetto su [Google Cloud Console](htpps://console.cloud.google.com)
  - Sulla pagina "Client" del progetto crea un client e scarica il file .json
  - Inserisci come URI di reindirezzamento autorizzati `http://localhost:38080/` e salva
  - Rinomina il file .json precedentemente scaricato in `credentials.json` e spostalo in una cartella .env 
  - Sulla pagina "Pubblico" del progetto inserisci la tua email su "Utenti di prova" e salva
2. **Autorizza l'accesso a Google Calendar**
  
  Al primo avvio, lo script aprirà una finestra di login per autorizzare l'uso del tuo calendario.

## 📂 Struttura delle cartelle 
All'interno della cartella principale, deve esserci una directory chiamata `Corsi` con questa struttura:
```
Corsi/
├── Tecnologia/
│   └── Tecnologia.pdf
├── Farmacologia/
│   └── Farmacologia.pdf
└── Chimica Farmaceutica II/
    └── Chimica Farmaceutica II.pdf
```
👉 Ogni sottocartella rappresenta un corso, e deve contenere un unico PDF chiamato esattamente come la cartella.

Se hai più PDF per uno stesso corso, puoi unirli in un unico file usando lo script unisci_pdf.py.

## ▶️ Esecuzione
Per avviare il programma:
```
python contapagine.py
