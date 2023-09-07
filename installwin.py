from tkinter import *
from tkinter import ttk
from subprocess import run
from threading import Thread
from os.path import basename
from time import sleep
from json import dump

li=[]
curdict={'AUD':'Australia Dollar',
'GBP':'Great Britain Pound',
'EUR':'Euro',
'JPY':'Japan Yen',
'CHF':'Switzerland Franc',
'USD':'USA Dollar',
'AFN':'Afghanistan Afghani',
'ALL':'Albania Lek',
'DZD':'Algeria Dinar',
'AOA':'Angola Kwanza',
'ARS':'Argentina Peso',
'AMD':'Armenia Dram',
'AWG':'Aruba Florin',
'AUD':'Australia Dollar',
'ATS':'Austria Schilling',
'BEF':'Belgium Franc',
'AZN':'Azerbaijan New Manat',
'BSD':'Bahamas Dollar',
'BHD':'Bahrain Dinar',
'BDT':'Bangladesh Taka',
'BBD':'Barbados Dollar',
'BYR':'Belarus Ruble',
'BZD':'Belize Dollar',
'BMD':'Bermuda Dollar',
'BTN':'Bhutan Ngultrum',
'BOB':'Bolivia Boliviano',
'BAM':'Bosnia Mark',
'BWP':'Botswana Pula',
'BRL':'Brazil Real',
'GBP':'Great Britain Pound',
'BND':'Brunei Dollar',
'BGN':'Bulgaria Lev',
'BIF':'Burundi Franc',
'XOF':'CFA Franc BCEAO',
'XAF':'CFA Franc BEAC',
'XPF':'CFP Franc',
'KHR':'Cambodia Riel',
'CAD':'Canada Dollar',
'CVE':'Cape Verde Escudo',
'KYD':'Cayman Islands Dollar',
'CLP':'Chili Peso',
'CNY':'China Yuan/Renminbi',
'COP':'Colombia Peso',
'KMF':'Comoros Franc',
'CDF':'Congo Franc',
'CRC':'Costa Rica Colon',
'HRK':'Croatia Kuna',
'CUC':'Cuba Convertible Peso',
'CUP':'Cuba Peso',
'CYP':'Cyprus Pound',
'CZK':'Czech Koruna',
'DKK':'Denmark Krone',
'DJF':'Djibouti Franc',
'DOP':'Dominican Republich Peso',
'XCD':'East Caribbean Dollar',
'EGP':'Egypt Pound',
'SVC':'El Salvador Colon',
'EEK':'Estonia Kroon',
'ETB':'Ethiopia Birr',
'EUR':'Euro',
'FKP':'Falkland Islands Pound',
'FIM':'Finland Markka',
'FJD':'Fiji Dollar',
'GMD':'Gambia Dalasi',
'GEL':'Georgia Lari',
'GHS':'Ghana New Cedi',
'GIP':'Gibraltar Pound',
'GRD':'Greece Drachma',
'GTQ':'Guatemala Quetzal',
'GNF':'Guinea Franc',
'GYD':'Guyana Dollar',
'HTG':'Haiti Gourde',
'HNL':'Honduras Lempira',
'HKD':'Hong Kong Dollar',
'HUF':'Hungary Forint',
'ISK':'Iceland Krona',
'INR':'India Rupee',
'IDR':'Indonesia Rupiah',
'IRR':'Iran Rial',
'IQD':'Iraq Dinar',
'ILS':'Israel New Shekel',
'ITL':'Italy Lira',
'JMD':'Jamaica Dollar',
'JPY':'Japan Yen',
'JOD':'Jordan Dinar',
'KZT':'Kazakhstan Tenge',
'KES':'Kenya Shilling',
'KWD':'Kuwait Dinar',
'KGS':'Kyrgyzstan Som',
'LAK':'Laos Kip',
'LVL':'Latvia Lats',
'LBP':'Lebanon Pound',
'LSL':'Lesotho Loti',
'LRD':'Liberia Dollar',
'LYD':'Libya Dinar',
'LTL':'Lithuania Litas',
'LUF':'Luxembourg Franc',
'MOP':'Macau Pataca',
'MKD':'Macedonia Denar',
'MGA':'Malagasy Ariary',
'MWK':'Malawi Kwacha',
'MYR':'Malaysia Ringgit',
'MVR':'Maldives Rufiyaa',
'MTL':'Malta Lira',
'MRO':'Mauritania Ouguiya',
'MUR':'Mauritius Rupee',
'MXN':'Mexico Peso',
'MDL':'Moldova Leu',
'MNT':'Mongolia Tugrik',
'MAD':'Morocco Dirham',
'MZN':'Mozambique New Metical',
'MMK':'Myanmar Kyat',
'ANG':'NL Antilles Guilder',
'NAD':'Namibia Dollar',
'NPR':'Nepal Rupee',
'NLG':'Netherlands Guilder',
'NZD':'New Zealand Dollar',
'NIO':'Nicaragua Cordoba Oro',
'NGN':'Nigeria Naira',
'KPW':'North Korea Won',
'NOK':'Norway Kroner',
'OMR':'Oman Rial',
'PKR':'Pakistan Rupee',
'PAB':'Panama Balboa',
'PGK':'Papua New Guinea Kina',
'PYG':'Paraguay Guarani',
'PEN':'Peru Nuevo Sol',
'PHP':'Philippines Peso',
'PLN':'Poland Zloty',
'PTE':'Portugal Escudo',
'QAR':'Qatar Rial',
'RON':'Romania New Lei',
'RUB':'Russia Rouble',
'RWF':'Rwanda Franc',
'WST':'Samoa Tala',
'SAR':'Saudi Arabia Riyal',
'RSD':'Serbia Dinar',
'SCR':'Seychelles Rupee',
'SLL':'Sierra Leone Leone',
'SGD':'Singapore Dollar',
'SKK':'Slovakia Koruna',
'SIT':'Slovenia Tolar',
'SBD':'Solomon Islands Dollar',
'SOS':'Somali Shilling',
'ZAR':'South Africa Rand',
'KRW':'South Korea Won',
'ESP':'Spain Peseta',
'LKR':'Sri Lanka Rupee',
'SHP':'St Helena Pound',
'SDG':'Sudan Pound',
'SRD':'Suriname Dollar',
'SZL':'Swaziland Lilangeni',
'SEK':'Sweden Krona',
'CHF':'Switzerland Franc',
'SYP':'Syria Pound',
'TWD':'Taiwan Dollar',
'TZS':'Tanzania Shilling',
'THB':'Thailand Baht',
'TOP':'Tonga Pa\'anga',
'TTD':'Trinidad/Tobago Dollar',
'TND':'Tunisia Dinar',
'TRY':'Turkish New Lira',
'TMM':'Turkmenistan Manat',
'USD':'USA Dollar',
'UGX':'Uganda Shilling',
'UAH':'Ukraine Hryvnia',
'UYU':'Uruguay Peso',
'AED':'United Arab Emirates Dirham',
'VUV':'Vanuatu Vatu',
'VEB':'Venezuela Bolivar',
'VND':'Vietnam Dong',
'YER':'Yemen Rial',
'ZMK':'Zambia Kwacha',
'ZWD':'Zimbabwe Dollar'}

try:
    import PIL
except ModuleNotFoundError:
    li.append('pillow')
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    li.append('beautifulsoup4')
try:
    import requests
except ModuleNotFoundError:
    li.append('requests')
try:
    import pyperclip
except ModuleNotFoundError:
    li.append('pyperclip')

def install():
    if li:
        for i in li:
            cur.config(text='Installing '+i+'...')
            run(['pip', 'install', i], shell=True, universal_newlines=True)
            perc.config(text=str(eval(perc['text'][:-1])+(100//len(li)))+'%')
            invar.set(invar.get()+(100//len(li)))
        else:
            invar.set(100)
            perc.config(text='100%')
            cur.config(text='Restarting the app...')
            sleep(5)
            run(['python', basename(__file__)])
            installwin.destroy()
    else:
        bt_x.place(x=460, y=10, width=25, height=25)
        state.config(text='Sorting up things for\n you...')
        cur.config(text='Fetching the currency values...')

        val={}
        state.place(x=115, y=90)

        for j in range(len(curdict)):
            url = f'https://www.google.com/search?q={curdict[list(curdict.keys())[j]]}+to+inr'
            res = requests.get(url)
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            text = soup.find_all(text=True)
            output = []
            for t in text:
                if t.parent.name=='div':
                    output += ['{}\n'.format(t)]
            try:
                val[curdict[list(curdict.keys())[j]]]=eval(output[18].split()[0])
            except:
                try:
                    val[curdict[list(curdict.keys())[j]]]=eval(output[22].split()[0])
                except:
                    pass
            perc.config(text=f'{round((j/len(curdict))*100, 2)}%')
            invar.set(round((j/len(curdict))*100, 2))
        else:
            cur.config(text='Processing values...')
            perc.config(text='100%')
            invar.set(100)

        for value in list(val.keys()):
            if type(val[value])!=float and type(val[value])!=int:
                val.pop(value)
        else:
            val['India Rupee']=1.0
        with open('currencyvalues.json', 'w') as f:
            dump(val, f, indent=4)
        sleep(3)
        installwin.destroy()

def transition(label, xstart ,ycoord):
    for ind in range(xstart+20, xstart, -1):
        label.place(x=ind, y=ycoord)
        sleep(0.00001)

installwin=Tk()
installwin.geometry(f'500x260+{installwin.winfo_screenwidth()//2-250}+{installwin.winfo_screenheight()//2-130}')
installwin.attributes('-topmost', True)
header=Label(text='Unit Converter', font='Arial 35')
state=Label(text='Installing some module\n dependencies...', font='Helvetica 20 italic')
cur=Label(text='Preparing to install modules...', font='Arial 18')
invar=IntVar(value=0)
progbar=ttk.Progressbar(length=490, mode='determinate', orient='horizontal', variable=invar)
progbar.place(x=5, y=230)
perc=Label(text='0%', font='Arial 18')
bt_x=Button(text='X',relief='raised', font='Arial 15', bg='darkred', command=lambda :(installwin.destroy(), exit(1)),
fg='white')

for labe, x, y in zip(('header', 'state', 'cur', 'perc'), (90, 100, 1, 420), (0, 90, 190, 190)):
    installwin.after(150, Thread(target=lambda lab=labe, xco=x, yco=y: transition(eval(lab), xco, yco)).start)

installwin.after(800, Thread(target=install, daemon=True).start)
installwin.overrideredirect(True)
installwin.mainloop()
