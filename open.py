import os
import pandas as pd
import re
from urllib.parse import quote
import webbrowser

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito' 
cwd = os.getcwd()
count = 0
filepath = f'{cwd}\\files\\'
os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', "open") 
for filename in os.listdir(filepath):
    if not re.search("#$", filename):
        xl = pd.ExcelFile(f'{cwd}\\files\\' + filename)
        df = xl.parse("Sheet1")
        df = df.sort_values('Desc')
        for item_description in df['Desc']:
            if count > 9:
                input("Press Enter to continue...")
                count = 0
            webbrowser.get(chrome_path).open("https://www.google.com.tr/search?q=" + quote(item_description))
            count = count + 1