## About
I created this script for personal use, just to keep track of how much did i need to study until the exam date. 
It can also create **daily Google Calendar events** in order to track your progress. 

Just input your pdfs and the exam date: the script will do everything.

---

## Installing
1. **Clone the repo**
```
   git clone https://github.com/marco-la-rosa/contapagine.git
   cd contapagine
```
2. **Create the virtual environment**
```
  python -m venv .venv
  source .venv/bin/activate        # Linux/macOS
  .venv\Scripts\activate           # Windows
```
3. **Install the dependencies**
```
  pip install -r requirements.txt
```

---

## Configuration
  - Create a project in [Google Cloud Console](https://console.cloud.google.com)
  - Download the .json file on the "Client" page of the project
  - Write as an "Authorized redirect URIs" `http://localhost:38080/` and save
  - Rename the .json file `credentials.json` and move it to a .env folder
  - Write your email in "Test Users" on the "Public" page of the project and save
  - Authorize the login on the first start


## Folder structure 
On the main folder there has to be a `Corsi` folder with this structure:

```
Corsi/
├── Exam Name 1/
│   └── Exam Name 1.pdf
├── Exam Name 2/
│   └── Exam Name 2.pdf
└── Exam Name .../
    └── Exam Name ....pdf
```
Each subfolder has to contain exactly one pdf named as the subfolder but ending in .pdf.

I included a little script done by me called `unisci_pdf.py` to merge multiple pdfs into one if you need it.

## Execution
To start the script simply type on the terminal:
```
python contapagine.py
```
