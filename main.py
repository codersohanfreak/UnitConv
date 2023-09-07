#Importing all modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from subprocess import run
from os.path import basename, exists
import sys
from time import sleep
from threading import Thread
from socket import gethostbyname, gethostname
from json import load
import webbrowser

#Function to open subwindow
def subwindow(title, dictin): #dictin parameter is the dictionary with keys as units and values as values wrt si units

    #Function to clear the input output entries
    def p():
        l2.config(state=NORMAL)
        l1.delete(0,'end')
        l2.delete(0,'end')
        l1.focus()
        l2.config(state=DISABLED)

    #Function to convert the units other than temperature
    def x(e=None):
        inp=default1.get()
        out=default2.get()
        if inp not in dictin or out not in dictin:
            mb.showerror('Invalid Unit','Enter a valid unit or currency.')
            groot.focus_force()
            l1.focus()
            p()
            return
        if l1.get().replace('.', '').replace('e', '').isdigit() and l1.get().count('.')<=1:
            val=eval(l1.get())
            l2.config(state=NORMAL)
            l2.delete(0,"end")
            if title!='Currency':
                b=str(float((l[out]/l[inp]*val)))
            else:
                b=str(float((l[inp]/l[out]*val)))
            l2.insert(0,b)
            l1.focus()
            l2.config(state=DISABLED)
        else: #Blank input entry
            mb.showerror("Input Error", "Invalid Input!")
            groot.focus_force()
            l1.focus()
            l2.config(state=NORMAL)
            l2.delete(0, END)
            l2.config(state=DISABLED)
            return

    #Function to convert unit
    def xtemp(c=None):
        inp=default1.get()
        out=default2.get()
        if inp not in ['celsius','kelvin','fahrenheit'] or out not in ['celsius','kelvin','fahrenheit']:
            mb.showerror('Invalid Unit','Enter a valid temperature unit.')
            groot.focus_force()
            l1.focus()
            p()
            return
        val=l1.get()
        l2.config(state=NORMAL)
        l2.delete(0, END)
        if val and val.replace('.', '').replace('e', '').isdigit() and l1.get().count('.')<=1:
            if out=='celsius':
                if inp=='kelvin':
                    l2.insert(0, (float(val)-273.15))
                elif inp=='fahrenheit':
                    l2.insert(0, (float(val)-32)*0.56)
                else:
                    l2.insert(0, val)
            elif out=='kelvin':
                if inp=='celsius':
                    l2.insert(0, float(val)+273.15)
                elif inp=='fahrenheit':
                    l2.insert(0, (float(val)-32)*0.555+273.15)
                else:
                    l2.insert(0, val)
            else:
                if inp=='celsius':
                    l2.insert(0, 1.8*(float(val))+32)
                elif inp=='kelvin':
                    l2.insert(0, ((float(val)-273.15)*1.8)+32)
                else:
                    l2.insert(0, val)
        else: #Blank entry box or invalid input
            mb.showerror("Input Error", "Invalid Input!")
            groot.focus_force()
            l1.focus()
            l2.config(state=NORMAL)
            l2.delete(0, END)
            l2.config(state=DISABLED)
            return
        l2.config(state=DISABLED)

    #Function to copy output to clipboard
    def cp():
        if l2.get():
            copy(l2.get())
            mb.showinfo('Copied', 'Copied output to clipboard successfully.')
            groot.focus_force()
            l1.focus()
        else:
            mb.showerror('Error','Cannot copy empty output.')
            groot.focus_force()
            l1.focus()

    #Dictionary which holds all icons of respective quantities
    imgdict={'Energy': r'.\images\energy.ico', 'Area': r'.\images\area.ico',
    'Astronomical Length':r'.\images\au.ico', 'Volume':r'.\images\cube.ico', 'Currency':r'.\images\currency.ico',
    'Length':r'.\images\length.ico', 'Mass':r'.\images\mass.ico', 'Temperature':r'.\images\temp.ico',
    'Power':r'.\images\power.ico', 'Pressure':r'.\images\pressure.ico', 'Speed':r'.\images\speed.ico'}

    #The subwindow
    groot=Toplevel()
    groot.title(f'{title} Converter')
    groot.configure(bg='#4268ff')
    groot.resizable(0,0)
    groot.protocol('WM_DELETE_WINDOW', lambda:(groot.destroy(), root.focus_force()))
    groot.iconbitmap(imgdict[title])
    groot.focus_force()
    groot.geometry('700x400+150+10')
    Label(groot,text=f'{title} Converter', font='Arial 30 italic bold underline',bg='#4268ff', fg='white').pack(pady=7, side='top')

    #Defining a style for ttk buttons
    style1=ttk.Style(groot)
    style1.configure("TButton", background='#4268ff', borderwidth=10, font='Arial 20')

    #create options list of units [eg for length]
    l=dictin
    options = list(l.keys())

    #String Containers for output and input dropboxes
    default1 = StringVar()
    default1.set(options[0])
    default2 = StringVar()
    default2.set(options[0])

    #Creating output and input dropboxes
    outop = ttk.Combobox(groot, values=options, textvariable=default2, font='Arial 18')
    inop = ttk.Combobox(groot, values=options, textvariable=default1, font='Arial 18')
    inop.place(x=480,y=130,width=175,height=30)
    outop.place(x=480,y=230,width=175,height=30)

    #Prevents highlight of combobox when any unit is selected
    outop.bind("<<ComboboxSelected>>",lambda e: l1.focus())
    inop.bind("<<ComboboxSelected>>",lambda e: l1.focus())

    #Button to convert
    if title!='Temperature': #if its not temperature
        bt1=ttk.Button(groot, text='Convert',command=x, cursor='hand2')
    else:
        bt1=ttk.Button(groot, text='Convert',command=xtemp, cursor='hand2')

    #Buttons to clear and copy
    bt2=ttk.Button(groot, text='Clear',command=p, cursor='hand2')
    bt3=ttk.Button(groot, text='Copy to clipboard',command=cp, cursor='hand2')

    #positioning of buttons
    bt1.place(x=50,y=300, width = 150, height=45)
    bt2.place(x=225,y=300, width = 150, height=45)
    bt3.place(x=400,y=300, width = 250, height=45)

    #Entry boxes for input and output
    Label(groot, text='Input:', font='Arial 20', bg='#4268ff', fg='white').place(x=70, y=90)
    l1=ttk.Entry(groot, font='Arial 18')
    l1.place(x=70,y=130,width = 400, height=30)
    l1.focus()
    Label(groot, text='Output:', font='Arial 20', bg='#4268ff', fg='white').place(x=70, y=190)
    l2=Entry(groot, font='Arial 18', state=DISABLED, disabledforeground='black', disabledbackground='white')
    l2.place(x=70,y=230,width = 400, height=30)

    #Binding the return(ie Enter button on keyboard) to call x or xtemp function
    if title!='Temperature':
        groot.bind('<Return>',x)
    else:
        groot.bind('<Return>', xtemp)

    groot.mainloop()

#Function to show about window
def about():
    #Creating a window
    aboutroot=Toplevel(root)
    aboutroot.config(bg='#4268ff')
    aboutroot.title('About')
    aboutroot.focus_force()
    aboutroot.grab_set()
    aboutroot.resizable(0,0)
    aboutroot.iconbitmap(r'.\images\about.ico')
    aboutroot.geometry('450x450+150+10')

    #Creating labels
    Label(aboutroot, text='Unit Converter', font='Arial 30', bg='#4268ff', fg='white').pack()
    Label(aboutroot, text='Version 1.0.0', font='Arial 20', bg='#4268ff', fg='white').pack(padx=50)

    Label(aboutroot, text='Created By:Team-1', font='Arial 20', bg='#4268ff', fg='white').place(x=0, y=100)
    Label(aboutroot, text='Team Members:\nPushkar S\nShrujan V\nSohan Shanbhag\nTejas Pai', font='Arial 20', justify='left', bg='#4268ff', fg='white').place(x=0, y=150)
    Label(aboutroot, text='Images and icon Source:', font='Arial 20', bg='#4268ff', fg='white').place(x=0, y=350)

    #Creating a clickable link for convinience of the user
    l=Label(aboutroot, text='https:\\\\www.vectorstock.com', font='Arial 20 italic underline', fg='blue', cursor='hand2', bg='white')
    l.place(x=0, y=385)

    #Webbrowser modules opens a link in default browser. 2 specifies to open the link in a seperate browser window
    l.bind('<1>', lambda _: webbrowser.open('https:\\\\www.vectorstock.com', 2))

    aboutroot.mainloop()

def move(but, direc):
    #Moves the buttons
    if direc=='up':
        #Moves the button up when the cursor moves in
        eval(but).config(bg='lightblue', relief='raised')
        eval(but).place(x=butt_coord[but][0], y=butt_coord[but][1]-10, width=175, height=175)
    else:
        #Moves the button down when the cursor moves out
        eval(but).config(bg='white', relief='groove')
        eval(but).place(x=butt_coord[but][0], y=butt_coord[but][1], width=175, height=175)

def transition(butobj, xcoord, ycoord):
    #Animation of moving buttons up
    for i in range(700, ycoord-40, -10):
        butobj.place(x=xcoord, y=i, width=175, height=175)
        sleep(0.01)
    else:
        #Animation of moving buttons down
        for j in range(i, i+40, 10):
            butobj.place(x=xcoord, y=j, width=175, height=175)
            sleep(0.03)

try:
    #Trying to import the external modules
    from PIL import Image, ImageTk
    from pyperclip import copy
    installflag=False
except:
    #The external modules are not found
    installflag=True

if not exists(r'.\images'):
    #Images directory does'nt exist
    mb.showerror('Files not found', 'Directory images not found.')
    exit(1)
else:
    #Images directory exists but a particular image does not exist
    existdict={'about': exists(r'.\images\about.png'), 'energy': exists(r'.\images\energy.png'), 'area': exists(r'.\images\area.png'),
    'au':exists(r'.\images\au.png'), 'cube':exists(r'.\images\cube.png'), 'currency': exists(r'.\images\currency.png'), 
    'icon':exists(r'.\images\icon.ico'), 'length':exists(r'.\images\length.png'), 'mass':exists(r'.\images\mass.png'),
    'power':exists(r'.\images\power.png'), 'pressure':exists(r'.\images\pressure.png'), 'speed':exists(r'.\images\speed.png'),
    'temp':exists(r'.\images\temp.png')}
    notaval=[]
    for i,j in existdict.items():
        if not j:
            notaval.append(i+('.png ' if i!='icon' else '.ico'))
    if notaval:
        mb.showerror('Files not found', 'Files '+','.join(notaval)+'not found.')
        exit(1)

#Checks whether system is connected to internet
flag1=False
if str(gethostbyname(gethostname()))=='127.0.0.1':
    flag1=True

#Checks whether currency json file is present or not
valueflag=False
sys.argv.append('\'a\'')
if not exists('currencyvalues.json') or \
(eval(sys.argv[1]) and mb.askyesno('Fetch currency','Do you want to update with new currency values?')):
    valueflag=True

currencyflag=True
if (installflag or valueflag) and not flag1: #If modules not found and system is connected to net
    run(['python', 'installwin.py'])
    run(['python', basename(__file__), 'False'])
    exit(1)
elif flag1 and installflag: #If modules not found and system is not connected to net
    mb.showerror('No internet connection', 'Connect your system to internet to run this.')
    exit(1)
elif flag1 and valueflag: #If currencyvales.json not found and system is not connected to net
    mb.showwarning('No internet connection', 'You might not get currency\nconversion as there is no internet connection.')
    currencyflag=False

#Main Window
root=Tk()
root.title('Unit Converter')
root.config(bg='#4268ff')
root.geometry('800x700+150+10')
root.resizable(0, 0)
root.iconbitmap(r'.\images\icon.ico')
root.focus_force()

#Header Labels
Label(root, text='Unit Converter', font='Arial 35 italic bold underline', bg='#4268ff', fg='white').pack(pady=5, side='top')
Label(root, text='Choose the physical quantity:', font='Arial 20 italic', bg='#4268ff', fg='white').pack(pady=5, side='top')

#Importing images of various units into code
im1=ImageTk.PhotoImage(Image.open(r'.\images\length.png'))
im2=ImageTk.PhotoImage(Image.open(r'.\images\area.png'))
im3=ImageTk.PhotoImage(Image.open(r'.\images\currency.png'))
im4=ImageTk.PhotoImage(Image.open(r'.\images\cube.png'))
im5=ImageTk.PhotoImage(Image.open(r'.\images\power.png'))
im6=ImageTk.PhotoImage(Image.open(r'.\images\pressure.png'))
im7=ImageTk.PhotoImage(Image.open(r'.\images\temp.png'))
im8=ImageTk.PhotoImage(Image.open(r'.\images\speed.png'))
im9=ImageTk.PhotoImage(Image.open(r'.\images\mass.png'))
im10=ImageTk.PhotoImage(Image.open(r'.\images\au.png'))
im11=ImageTk.PhotoImage(Image.open(r'.\images\energy.png'))
im12=ImageTk.PhotoImage(Image.open(r'.\images\about.png'))

try:
    #Loading currencies from the json file
    f=open('currencyvalues.json')
    currencydict=load(f)
    f.close()
except:
    #Currencyvalues.json file not found
    currencyflag=False

#Defining buttons for various quantities
b_l=Button(root, image=im1, text='Length', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=lambda: subwindow('Length', {'meters':1,'millimeters':1000,'centimeters':100,'kilometers':0.001,'inches':39.37,'feet':3.28,'yards':1.094,'miles':0.0006213,'mils':39370.078}))
b_a=Button(root, image=im2, text='Area', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=lambda: subwindow('Area', {'metersquare':1,'acres':0.000247,'ares':0.01,'hectares':0.0001,'cm':10**4,'squarefeet':10.764,'squareinches':1550.003}))
b_c=Button(root, image=im3, text='Currency', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2',command=lambda: subwindow('Currency', currencydict))
b_v=Button(root, image=im4, text='Volume', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=lambda: subwindow('Volume', {'mcube':1,'cmcube':10**(-6),'liter':0.001,'gallon':0.00378541,'milliliter':10**(-6),'cubicfoot':0.0283168,
'pint':0.000473176,'quart':0.000946353,'tablespoon':1.4787*(10**(-5))}))
b_p=Button(root, image=im5, text='Power', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2',command=lambda: subwindow('Power', {'watt':1,'kilowatt':1000,'horsepower':745.7,'british thermal unit per hour':0.29307,
'calories per second':4.1667}))
b_pr=Button(root, image=im6, text='Pressure', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2',command=lambda: subwindow('Pressure', {'pascal':1,'psi':1.45038*(10**(-4)),'atm':101325,'kilopascal':1000,'bar':10**5,'torr':133.322}))
b_t=Button(root, image=im7, text='Temperature', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=lambda: subwindow('Temperature', {'kelvin':1, 'celsius':1, 'fahrenheit':1}))
b_s=Button(root, image=im8, text='Speed', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=lambda: subwindow('Speed', {'meterpersecond':1,'kilometerpersecond':0.001,'kilometerperhour':3.6,'inchespersecond':39.37,'inchesperhour':141732.28,'feetpersecond':3.281,'feetperhour':11811.024,
'milespersecond':0.00062,'milesperhour':2.237,'knots':1.9438}))
b_m=Button(root, image=im9, text='Mass', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=lambda: subwindow('Mass', {'kilogram':1,'tons':0.001,'pounds':2.2046,'ounces':35.2740,'grams':1000}))
b_au=Button(root, image=im10, text='Astronomical\nLength', compound=TOP, font='Arial 20', bg='white', 
relief='groove', cursor='hand2',command=lambda: subwindow('Astronomical Length', {'m':1,'km':1000,'Lightyr':9.461*(10**15),'AU':1.496*(10**11),'parsec':3.086*(10**16),'lightsec':2.998*(10**8)}))
b_deg=Button(root, image=im11, text='Energy', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2',command=lambda: subwindow('Energy', {'eV':6.242*(10**(18)),'J':1,'kJ':1000,'cal':4.184,'kcal':4184, 'Wh':3600,'kWh':3.6*(10**6), 'BTU':1055.06, 'US-T':1.055*(10**8),'ftPd':1.35582}))
b_ab=Button(root, image=im12, text='About', compound=TOP, font='Arial 20', bg='white', relief='groove', 
cursor='hand2', command=about)
f.close()

#Positioning buttons with for loop
varlist=['l','a','c','v','p','pr','t','s','m','au','deg', 'ab']
index=0;butt_coord={};timevar=500
for i in range(120, 521, 200):
    for j in range(13, 614, 200):
        #Position button at coordinate x,y wrt window top left corner which is origin
        root.after(timevar, lambda obj=eval('b_'+varlist[index]), x=j, y=i:Thread(target=transition, args=(obj, x, y), daemon=True).start())
        #Storing the coordinates in a dictionary
        butt_coord['b_'+varlist[index]]=(j, i)
        #Binding the function to make the button move up when cursor moves in
        if varlist[index]=='c':
            funcid1=eval('b_'+varlist[index]).bind('<Enter>', lambda _, bu='b_'+varlist[index]:move(bu, 'up'))
        else:
            eval('b_'+varlist[index]).bind('<Enter>', lambda _, bu='b_'+varlist[index]:move(bu, 'up'))
        #Binding the function to make the button move down when cursor moves out
        if varlist[index]=='c':
            funcid2=eval('b_'+varlist[index]).bind('<Leave>', lambda _, bu='b_'+varlist[index]:move(bu, 'down'))
        else:
            eval('b_'+varlist[index]).bind('<Leave>', lambda _, bu='b_'+varlist[index]:move(bu, 'down'))
        index+=1
        timevar+=300

#If no currencyvalues.json file and user is not interested to download currencyvalues
if not currencyflag and not exists('.\currencyvalues.json'):
    b_c.config(state=DISABLED, cursor='arrow')
    b_c.unbind('<Enter>', funcid1)
    b_c.unbind('<Leave>', funcid2)

root.mainloop()
