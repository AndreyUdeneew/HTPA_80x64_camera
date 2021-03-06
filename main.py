# This is a sample Python script.
import tkinter as tk
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
from tkinter import ttk
import matplotlib.pyplot as plt
import serial
import cv2

from numpy import uint16, double
# import pyserial

# port_list = list(serial.tools.list_ports.comports())
# print(port_list)
# from serial import serial
import time
import os
import numpy as np

import serial.tools.list_ports

comlist = serial.tools.list_ports.comports()
connectedPorts = []
for element in comlist:
    connectedPorts.append(element.device)
print("Connected COM ports: " + str(connectedPorts))

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
    print("taking photo is about to begin")
        # ser.write(b'd')
        # data = ser.read()
        # print(data)

    # time.sleep(0.05)
    # output = ser.read(80*64).decode().strip()
    # output = ser.readline()
    # print(output.hex())
    # output=output.hex()
    # output_dec = int(output, 16)
    print(output)
    temps = [double(t) for t in output.split(",")]
    print(temps)
    print(len(temps))
    data = np.array(temps).reshape((2, 119))
    ax.imshow(data)
    ax2.plot(temps)
    # h.set_data(data)
    plt.show()
    return output

def take_a_video():
    text1.insert(INSERT, 'video')

def stop_a_video():
    text1.insert(INSERT, 'stop')

# speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']

def videoPreview():
    values = []
    with serial.Serial() as ser:
        ser.port = combobox.get()
        print(ser.port)
        ser.baudrate = 500000
        print(ser.baudrate)
        ser.port = connectedPorts[1]
        ser.timeout = 2
        ser.open()
        if ser.is_open == True:
            print("\nAll right, serial port now open. Configuration:\n")
            print(ser, "\n")  # print serial parameters
        data = ser.read(10)
        print(data)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        frameNum=0;
        if ser.is_open == True:
            while True:
                ser.write(b"d")
                data = ser.read(5120*4)
                for i in range(len(data)):
                    values.append(int(data[i]))
                valuesArray = np.array(values, dtype=np.uint8)
                values = []
                values32 = valuesArray.view(dtype=np.uint32)
                values32 = np.resize(values32, (64, 80))
                frameNum += 1
                print(frameNum)
                plt.imshow(values32)
                plt.pause(0.05)
                # plt.cla()
                # plt.show()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

def close_COM_port():
    text1.insert(INSERT, 'port is closed')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ser = serial.Serial(port='COM6', baudrate=1000000, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
    # bytesize=serial.EIGHTBITS, timeout=0.1)
    window = Tk()
    window.geometry('900x500')
    window.title("HTPA_VIEWER")

    # fig = plt.figure()
    # ax = fig.add_subplot(2, 1, 1)
    # ax2 = fig.add_subplot(2, 1, 2)

    # app = tk.Tk()
    # app.geometry('200x100')
    labelTop = tk.Label(window, text="?????????? COM ??????????")
    labelTop.grid(column=0, row=0)
    combobox = ttk.Combobox(window, values=connectedPorts)
    # print(dict(comboExample))
    combobox.grid(column=0, row=1)
    combobox.current(1)
    # print(comboExample.current(), comboExample.get())

    text1 = Text(width=30, height=1)
    text1.grid(column=3, row=0, sticky=(W))

    btn0 = Button(window, text="output dir", command=selectOutputDir)
    btn0.grid(column=1, row=0)
    btn1 = Button(window, text="????????", command=take_a_photo)
    btn1.grid(column=5, row=0)
    btn2 = Button(window, text="????????????", command=take_a_video)
    btn2.grid(column=6, row=0)
    btn3 = Button(window, text="????????", command=stop_a_video)
    btn3.grid(column=7, row=0)
    btn4 = Button(window, text="videoPreview", command=videoPreview)
    btn4.grid(column=1, row=1)
    btn5 = Button(window, text="?????????????? ????????", command=close_COM_port)
    btn5.grid(column=2, row=1)

    window.mainloop()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

