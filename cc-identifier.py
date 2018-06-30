#!/usr/bin/python2.7
#
#
# Author: Abdul Aziz
#
# Description:
#         This is a Graphical User Interface Program, that identify's the credit card Type Upon Entering CC# (Credit Card Number).
#

from Tkinter import *
from PIL import Image, ImageTk


DEFAULT_BG          = "WHITE"
DEFAULT_SYSTEM      = "SYSTEM"
#ABSOLUTE_PATH = "C:/Users/Abdul Aziz/Dropbox/Python Projects 2018/credit-card-detector/"
ABSOLUTE_PATH = ""
VISA_CARD_CHECK     = ["4", "4026", "417500", "4405", "4508", "4844", "4913", "4917"]
DISCOVER_CARD_CHECK = ["6011", "65", "622", '644', '645', '646', '647', '648', '649']
MASTER_CARD_CHECK   = []
AMEX_CARD_CHECK     = ["34", "37"]

""" GENERATING NUMBERS FOR DISCOVER CREDIT CARDS """
for ccn01 in range(644, 650):
    DISCOVER_CARD_CHECK.append(str(ccn01))

""" GENERATING NUMBERS FOR MASTER CARDS """
for ccn02 in range(50, 56):
    MASTER_CARD_CHECK.append(str(ccn02))
#print DISCOVER_CARD_CHECK

def select_all_entry_box(event):
    e1.select_range(0, 'end')
    e1.icursor('end')

def check_card_number(e):
    try:
        cc_number = e1.get()
        print cc_number

        if cc_number[0:1] == "4" or cc_number in VISA_CARD_CHECK:
            CHOOSEN_PHOTO = ABSOLUTE_PATH + "icons/img/visa_card.png"

        elif cc_number[0:3] in DISCOVER_CARD_CHECK or cc_number[0:4] in DISCOVER_CARD_CHECK:
            CHOOSEN_PHOTO = ABSOLUTE_PATH + "icons/img/discover_card.png"

        elif cc_number[0:2] in AMEX_CARD_CHECK:
            CHOOSEN_PHOTO = ABSOLUTE_PATH + "icons/img/amex_card.png"

        elif cc_number[0:2] in MASTER_CARD_CHECK:
            CHOOSEN_PHOTO = ABSOLUTE_PATH + "icons/img/master_card.png"

        else:
            CHOOSEN_PHOTO = ABSOLUTE_PATH + "icons/img/default_card.png"

        img2 = ImageTk.PhotoImage(Image.open(CHOOSEN_PHOTO))
        panel.configure(image=img2)
        panel.image = img2
    except:
        pass

windows = Tk()
windows.geometry("400x400+450+150")
windows.config(bg=DEFAULT_BG)
windows.title("CyberAmor Presents")

Heading_01 = "Abdul's Credit Card Identifier."
l1 = Label(windows, text=Heading_01, font=DEFAULT_SYSTEM, bg=DEFAULT_BG)
l1.pack(pady=15)

Heading_02 = "Enter Credit Card Number"
l2 = Label(windows, text=Heading_02, font=DEFAULT_SYSTEM, bg=DEFAULT_BG)
e1 = Entry(windows, width=35, font=DEFAULT_SYSTEM, bg=DEFAULT_BG)
l2.pack()
e1.pack(padx=0, pady=15)
e1.focus()
windows.bind("<Key>", check_card_number)
windows.bind("<Control-A>", select_all_entry_box)
windows.bind("<Control-a>", select_all_entry_box)

img = Image.open(ABSOLUTE_PATH + "icons/img/default_card.png")
cropped_img = img.resize((400, 200), Image.ANTIALIAS)
img01 = ImageTk.PhotoImage(cropped_img)
panel = Label(windows, image=img01, bg=DEFAULT_BG)
panel.pack(side="bottom", fill="both", expand="yes")

windows.mainloop()
