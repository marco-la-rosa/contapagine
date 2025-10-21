import os
import pypdf
import pickle
from pypdf import PdfReader
from datetime import datetime,  timedelta
from math import ceil
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def salva_corsi():
    pre_corsi = sorted([
        f for f in os.listdir("Corsi") 
        if os.path.isdir(os.path.join("Corsi", f))
        ])

    corsi = {}
    for i, corso in enumerate(pre_corsi, start=1):
        corsi[i] = corso

    return(corsi)

def scelta_corso(corsi):
    print("Ciao Marco! Benvenuto nel tuo software di preparazione allo studio. \nPuoi scegliere di studiare:")
    for numero, corso in corsi.items():
        print(f"{numero}. {corso}")
    
    # Controllo scelta
    while True:
        try:
            num_corso_scelto = int(input("\nInserisci il numero del corso da studiare: "))

            if 1 <= num_corso_scelto <= len(corsi):
                print(f"Hai scelto: {corsi[num_corso_scelto]}")
                break
            else:
                print("Numero non valido, riprova. ")
        except ValueError:
            print("Inserisci un numero!")

    return(corsi[num_corso_scelto])

def calcola_pagine(corso_scelto, giorni_rimanenti):
    pdf_path = ("Corsi/" + corso_scelto + '/' + corso_scelto + '.pdf')
    try:
        reader= PdfReader(pdf_path)
        num_pagine = len(reader.pages)
    except Exception as e:
        print(f"Errore nella lettura del pdf: {e}")
        return
    
    pagine_al_giorno = ceil(num_pagine / giorni_rimanenti) 
    print(f"\nTotale pagine → {num_pagine} pagine")
    print(f"Giorni rimanenti →  {giorni_rimanenti}")
    print(f"Devi studiare circa {ceil(pagine_al_giorno)} pagine al giorno.")
    return(pagine_al_giorno, num_pagine)

def trova_data_esame():
    while True:
        try:
            data_esame_str = input("\nInserisci la data dell'esame (in formato YYYY-MM-DD): ")
            data_esame = datetime.strptime(data_esame_str, "%Y-%m-%d").date()
        except ValueError:
            print("Formato data non valido. Usa YYYY-MM-DD")
            continue

        oggi = datetime.today().date()
        giorni_rimanenti = (data_esame - oggi).days

        if giorni_rimanenti <= 0:
            print("La data dell'esame è già passata! Inserisci una data futura.")
        else:
            return(int(giorni_rimanenti))

def calendar(giorni_rimanenti, pagine_al_giorno, corso_scelto, num_pagine):
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    creds = None
    if os.path.exists('.env/token.pkl'):
        with open('.env/token.pkl', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('.env/credentials.json', SCOPES)
            creds = flow.run_local_server(port=38080)
        with open('.env/token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


    inizio = datetime.now()
    for i in range(giorni_rimanenti):
        start_page = i * pagine_al_giorno + 1
        end_page = min(num_pagine, start_page + pagine_al_giorno - 1)

        data = (inizio + timedelta(days=i)).date().isoformat()
        titolo = f"Studia {corso_scelto} da pag. {start_page} a {end_page}"

        event = {
            'summary': titolo,
            'start': {'date': data, 'timeZone': 'Europe/Rome'},
            'end': {'date': data, 'timeZone': 'Europe/Rome'},
        }

        service.events().insert(calendarId='primary', body=event).execute()
        print(f"Aggiunto evento: {titolo}")

 
def main():
    corsi = salva_corsi()
    corso_scelto = scelta_corso(corsi) 
    giorni_rimanenti = trova_data_esame()
    pagine_al_giorno, num_pagine = calcola_pagine(corso_scelto, giorni_rimanenti)
    while True:
        try:
            res = input("\nVuoi creare le task su Google Calendar con le pagine da studiare giorno per giorno? (y/n) ")
            if res == "y":
                calendar(giorni_rimanenti, pagine_al_giorno, corso_scelto, num_pagine)
                break
            elif res == "n":
                break
            else: 
                print("Formato non valido.")
        except ValueError:
            print("Formato non valido.")
main()
