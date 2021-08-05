from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
import time
from tkinter import filedialog
from openpyxl import *
import xlsxwriter
import os

os.chdir('/Users/neigelinerivollat/Desktop/Projet Amélie')

### Will be used
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('younk2.json', scope)
gc = gspread.authorize(credentials)
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1mQntzD_eqv_fph6ktlh68TIDUiYYGEFej5z8aUYDCyM/edit#gid=1363881611').sheet1
wks = gc.open("eurocup_2020_results").sheet1
data = wks.get_all_values()
headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)


### Code starts
root = Tk()
root.title("Amélie Application")
root.geometry("700x500")

myLabel1 = Label(root, text = "Bonjour Amélie.")
myLabel2 = Label(root, text = "Dit moi quelles sont les charactéristiques que tu souhaites rechercher pour ton candidat.")

myLabel1.pack()
myLabel2.pack()

Answer1 = StringVar
Answer2 = StringVar
Answer3 = StringVar

def addBox():
    my_ADD_entries = []
    ent = tk.Entry(root, textvariable = Answer3)
    ent.pack()
    my_ADD_entries.append((ent.get()))

add = Button(root, text="Ajouter characteristique", command=addBox).pack()




e1 = tk.Entry(root, textvariable = Answer1)
e2 = tk.Entry(root, textvariable = Answer1)
e1.pack()
e2.pack()




def open():
    ## First it finds the results in the background
    global df
    my_entries = []
    my_entries.append(e1.get())
    my_entries.append(e2.get())
    ## Redefine list

    df = df.astype(str)

    ## Code to retrieve
    for char in my_entries:
        mask = np.column_stack([df[col].str.contains(char, na=False) for col in df])
        df = df.loc[mask.any(axis=1)]
        df = pd.DataFrame(df)
    candidates = df[['stage','date']]
    print(candidates[['stage','date']])


    ## Then it opens a new window
    top = Toplevel()
    lbl = Label(top, text='Candidats potentiels')
    lbl.pack()

    lbl = tk.Label(top, text=str(candidates)) # other option
    lbl.pack()







btn = Button(root, text="Rechercher resultats", command=open).pack(side = BOTTOM, pady =10, padx = 3)

root.mainloop()