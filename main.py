# This is a sample Python script.
import tkinter as tk
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter import ttk
import serial
# from serial import serial
import time
import os
import numpy as np

# outputFile = "C:/Users/Stasy/Desktop/output2FLASH.txt"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def selectOutputDir():
    OutputDir = filedialog.askdirectory(parent=window)
    outputFile = OutputDir
    text1.insert(INSERT, outputFile)
    # return outputFile
    # outputFile = 'C:/Users/Stasy/Desktop/output2FLASH.txt'

def take_a_photo():
    def write_read(x):
        ser.write(bytes(x, 'd'))
        # time.sleep(0.05)
        output = ser.read(100)
        print('output')
        return output

def take_a_video():
    text1.insert(INSERT, 'video')

def stop_a_video():
    text1.insert(INSERT, 'stop')

speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']

def open_COM_port():
    data = ser.readline(10)
    text1.insert(INSERT, data)
    print(data)
    return data

def close_COM_port():
    text1.insert(INSERT, 'port is closed')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ser = serial.Serial(port='COM19', baudrate=1000000,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS, timeout=0.1)
    window = Tk()
    window.geometry('900x500')
    window.title("HTPA_VIEWER")
    # app = tk.Tk()
    # app.geometry('200x100')
    labelTop = tk.Label(window, text="Выбор COM порта")
    labelTop.grid(column=0, row=0)
    comboExample = ttk.Combobox(window, values=['a', 'b'])
    print(dict(comboExample))
    comboExample.grid(column=0, row=1)
    comboExample.current(1)
    print(comboExample.current(), comboExample.get())

    text1 = Text(width=30, height=1)
    text1.grid(column=3, row=0, sticky=(W))

    btn0 = Button(window, text="output dir", command=selectOutputDir)
    btn0.grid(column=1, row=0)
    btn1 = Button(window, text="Фото", command=take_a_photo)
    btn1.grid(column=5, row=0)
    btn2 = Button(window, text="Запись", command=take_a_video)
    btn2.grid(column=6, row=0)
    btn3 = Button(window, text="Стоп", command=stop_a_video)
    btn3.grid(column=7, row=0)
    btn4 = Button(window, text="Открыть порт", command=open_COM_port)
    btn4.grid(column=1, row=1)
    btn5 = Button(window, text="Закрыть порт", command=close_COM_port)
    btn5.grid(column=2, row=1)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

