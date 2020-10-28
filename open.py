import os
import webbrowser
import pandas as pd

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' 
cwd = os.getcwd()
count = 0
files = os.listdir(f'{cwd}\\files\\')
os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', "open")
xl = pd.ExcelFile(f'{cwd}\\files\\' + 'file.xls')
df = xl.parse("Sheet1")
for item in df['Desc']:
    if count > 9:
        input("Press Enter to continue...")
        count = 0
    webbrowser.get(chrome_path).open('https://www.google.com.tr/search?q=' + item)
    count = count + 1