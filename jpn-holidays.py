import jpholiday
from pandas import DataFrame as df
import PySimpleGUI as sg
import pyperclip

sg.theme('SandyBeach')

layout = [
    [sg.Text('Year.')],
    [sg.InputText(key='-IN-')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Japanese Holidays', layout)

event, values = window.read()
window.close()

text_input = values['-IN-']
df = df(jpholiday.year_holidays(int(text_input)))
df = df.rename(columns={0: '日付', 1: '祝日'})
df = df.shift()[1:]

sg.popup('Result', df)

pyperclip.copy(df.to_string())
