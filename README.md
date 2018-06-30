# CC Indentifier
###### Credit Card Identifier

# Description:

This is Credit Card Identifer, that detects the `Number` upon entry and states what type of credit card it might be, for example: **Visa, Amex, Discover, Master Card**.

# Preview:
<p align="center">
<img src="https://github.com/abdu1aziz/credit-card-detector/blob/master/icons/pic01.PNG?raw=true" height=350 width=300>
</p>

### Modules Used:
  - Tkinter
  - PIL **(Pillow)**

# How It Works!

  - The first digit of every credit card serves as a major industry identifier, or MII. For example, if the first digit 4 and 5 -- Visa and MasterCard -- relate to the banking and financial industry.

# Behind The Code?
In Technical Words:
  - Uses Virtual Arrays **lists** that are created and stored in memory upon the first run of the program.
  - Once The User Enters The Credit Card Number It is Cross References with the Numbers in *lists* to identify if it matches with some credit card type and that card logo is displaye in the body of the **GUI** (Graphical User Interface) template.

### How To Run?

It Requires Python2.7 installed on the host workstation in order to run it.

Install the dependencies and devDependencies and Run the Program.

```sh
$ pip install Tkinter && pip install pillow
$ cd credit-card-detector
$ python cc-identifier.py
```

