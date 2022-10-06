#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
from tkinter.filedialog import askopenfilenames

import PySimpleGUI as sg
import pandas as pd


def merge_csv():

    sg.theme('DarkPurple7')

    window = sg.FlexForm('Merge CSV Files',
                         auto_size_text=True,
                         font=('Ubuntu Mono derivative Powerline', 14))

    layout = [[
        sg.T('Select Multiple "CSV" Files:'),
        sg.B('Browse', size=(15, 0))
    ], [sg.T('Output File Name:'),
        sg.I(size=(25, 0), key='input')], [sg.B('Merge')]]

    window = window.Layout(layout)

    while True:
        event, values = window.read()

        if event == 'Browse':
            files = sorted(list(askopenfilenames(title='Open ".csv" Files')))
            if any('.csv' not in x.lower() for x in files):
                sg.Popup('You can only select CSV files!')

        elif event == 'Merge':
            try:
                files
            except NameError:
                sg.Popup('You have not selected any file to Merge!')
            else:
                combined_csv = pd.concat([pd.read_csv(f) for f in files])
                combined_csv.to_csv(
                    f'{Path(files[0]).parent}/{values["input"]}.csv',
                    index=False,
                    encoding='utf-8-sig')
                sg.Popup('Done!')

        elif event == sg.WIN_CLOSED:
            window.close()
            break


if __name__ == '__main__':
    merge_csv()
