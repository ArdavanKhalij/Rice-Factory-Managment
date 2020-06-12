from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import urllib
from urllib import request
import requests

####################### GLOBAL VARS #######################
valuelistForNamesOfComboBox = []
myname1 = " "
myname2 = " "
NameOfUser = "ADMIN"
internetConnectionFlag = False
sabteKeshavarzPOST = {}
global shaliForPrintToPDF
shaliForPrintToPDF = []
####################### GLOBAL VARS #######################

root = Tk()
root.title("مدیریت شالی ها")
root.configure(bg='#E3F0EB')

class all() :
    def sabteShaliPage(self):
        self.sabteShaliPageRoot = Tk()
        self.sabteShaliPageRoot.configure(bg='#E3F0EB')
        self.sabteShaliPageRoot.title("ثبت شالی")
        self.space = Label(self.sabteShaliPageRoot, text=" ", bg='#E3F0EB')
        self.space1 = Label(self.sabteShaliPageRoot, text=" ", bg='#E3F0EB')
        self.space2 = Label(self.sabteShaliPageRoot, text=" ", bg='#E3F0EB')
        self.space3 = Label(self.sabteShaliPageRoot, text=" ",bg='#E3F0EB')
        self.title = Label(self.sabteShaliPageRoot, text="ثبت شالی", font=('IRANYekan', '22'), bg='#E3F0EB')
        self.farmerNameTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.farmerNameTextLabel.insert(0, "نام کشاورز")
        self.shaliBagNumberTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliBagNumberTextLabel.insert(0, "تعداد کیسه شالی")
        self.shaliWeightTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliWeightTextLabel.insert(0, "وزن شالی")
        self.shaliKindTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliKindTextLabel.insert(0, "نوع شالی")
        self.phoneTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.phoneTextLabel.insert(0, "تلفن")
        self.driverTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.driverTextLabel.insert(0, "راننده")
        self.shaliPlaceTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliPlaceTextLabel.insert(0, "مکان شالی")
        self.shaliTozihTextLabel = Entry(self.sabteShaliPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliTozihTextLabel.insert(0, "توضیحات")
        self.sabt = Button(self.sabteShaliPageRoot, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '20'), command= ALLPages.postorSaveThenPost)
        self.sabt.config(height=1, width=20)
        clear = Button(self.sabteShaliPageRoot, text="پاک", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.clearSabteShali)
        clear.config(height=1, width=20)
        self.space.pack()
        self.title.pack()
        self.space1.pack()
        self.farmerNameTextLabel.pack()
        self.shaliBagNumberTextLabel.pack()
        self.shaliWeightTextLabel.pack()
        self.shaliKindTextLabel.pack()
        self.phoneTextLabel.pack()
        self.driverTextLabel.pack()
        self.shaliPlaceTextLabel.pack()
        self.shaliTozihTextLabel.pack()
        self.space2.pack()
        clear.pack()
        self.sabt.pack()
        self.space3.pack()

    def clearSabteShali(self):
        print("Clear")
        self.farmerNameTextLabel.delete(first=0,last=100)
        self.shaliBagNumberTextLabel.delete(first=0,last=100)
        self.shaliWeightTextLabel.delete(first=0,last=100)
        self.shaliKindTextLabel.delete(first=0,last=100)
        self.phoneTextLabel.delete(first=0,last=100)
        self.driverTextLabel.delete(first=0,last=100)
        self.shaliPlaceTextLabel.delete(first=0,last=100)
        self.shaliTozihTextLabel.delete(first=0,last=100)

    def editShali(self):
        self.listBox.bind('<Button-1>', self.editShali)
        curItem = self.listBox.focus()
        k = self.listBox.item(curItem)
        try:
            urlSabeKeshavarz = "https://shali-firstsite.fandogh.cloud/api/keshavarz/search/"+str(k['values'][5])+"/"
        except:
            messagebox.showinfo('عدم انتخاب','.موردی را برای ویرایش انتخاب نکردید')
            self.shaliHayeSabtShodePageRoot.destroy()
            ALLPages.shaliHayeSabtShodePage()
            self.sabteShodeHaPageRoot.destroy()
            ALLPages.sabtShodeHaPage()
        r = requests.get(urlSabeKeshavarz)
        self.sabteShaliPageRoott = Tk()
        self.sabteShaliPageRoott.configure(bg='#E3F0EB')
        self.sabteShaliPageRoott.title("ثبت شالی")
        self.space = Label(self.sabteShaliPageRoott, text=" ", bg='#E3F0EB')
        self.space1 = Label(self.sabteShaliPageRoott, text=" ", bg='#E3F0EB')
        self.space2 = Label(self.sabteShaliPageRoott, text=" ", bg='#E3F0EB')
        self.space3 = Label(self.sabteShaliPageRoott, text=" ", bg='#E3F0EB')
        self.titlee = Label(self.sabteShaliPageRoott, text="ویرایش شالی", font=('IRANYekan', '22'), bg='#E3F0EB')
        self.farmerNameTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.farmerNameTextLabele.insert(0, k['values'][5])
        self.shaliBagNumberTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliBagNumberTextLabele.insert(0, k['values'][3])
        self.shaliWeightTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliWeightTextLabele.insert(0, k['values'][2])
        self.shaliKindTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliKindTextLabele.insert(0, k['values'][4])
        self.phoneTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.phoneTextLabele.insert(0, k['values'][0])
        self.driverTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.driverTextLabele.insert(0, k['values'][1])
        self.shaliPlaceTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.shaliPlaceTextLabele.insert(0, str(r.json()[0]['makan']))
        self.shaliTozihTextLabele = Entry(self.sabteShaliPageRoott, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        urlSabeKeshavarz = "https://shali-firstsite.fandogh.cloud/api/shali/"+str(k['values'][6])+"/"
        r2 = requests.get(urlSabeKeshavarz)
        self.shaliTozihTextLabele.insert(0, str(r2.json()['tozihat']))
        self.sabte = Button(self.sabteShaliPageRoott, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '20'), command= ALLPages.editButton)
        self.sabte.config(height=1, width=20)
        self.space.pack()
        self.titlee.pack()
        self.space1.pack()
        self.farmerNameTextLabele.pack()
        self.shaliBagNumberTextLabele.pack()
        self.shaliWeightTextLabele.pack()
        self.shaliKindTextLabele.pack()
        self.phoneTextLabele.pack()
        self.driverTextLabele.pack()
        self.shaliPlaceTextLabele.pack()
        self.shaliTozihTextLabele.pack()
        self.space2.pack()
        self.sabte.pack()
        self.space3.pack()

    def postorSaveThenPost(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        if internetConnectionFlag:
            urlSabeKeshavarz = "https://shali-firstsite.fandogh.cloud/api/keshavarz/new/"
            makan = str(self.farmerNameTextLabel.get())
            nam = str(self.farmerNameTextLabel.get())
            ranande = str(self.driverTextLabel.get())
            telefon = str(self.phoneTextLabel.get())
            nam_ijad_konande = NameOfUser
            sabteKeshavarzPOST = {'makan': makan, 'nam': nam, 'ranande': ranande, 'telefon': telefon, 'nam_ijad_konande': nam_ijad_konande}
            r = requests.post(urlSabeKeshavarz, data=sabteKeshavarzPOST)
            print(r.status_code)
            print(r.text)
            try:
                CodeOfKeshavars = int(r.json()['code'])
            except:
                messagebox.showinfo('خطا در ورودی', '.به ورودی های خود دقت کنید')
                return
            print(CodeOfKeshavars)
            urlSabeteShali = "https://shali-firstsite.fandogh.cloud/api/shali/new/"
            noe_shali = str(self.shaliKindTextLabel.get())
            try:
                tedad_shali = int(self.shaliBagNumberTextLabel.get())
            except:
                messagebox.showinfo('مشکل ورودی در تعداد شالی','.لطفا ورودی تعداد شالی های خود را بررسی کنید. در نوع و یا تعداد مشکلی وجود دارد')
                self.sabteShaliPageRoot.destroy()
                return
            try:
                vazn_shali = int(self.shaliWeightTextLabel.get())
            except:
                messagebox.showinfo('مشکل ورودی در وزن شالی','.لطفا ورودی وزن شالی های خود را بررسی کنید. در نوع و یا تعداد مشکلی وجود دارد')
                self.sabteShaliPageRoot.destroy()
                self.shaliHayeSabtShodePageRoot.destroy()
                self.shaliHayeSabtShodePage()
            tozihat = str(self.shaliTozihTextLabel.get())
            nam_ijad_konande = str(NameOfUser)
            sabteShaliPOST = {'noe_shali': noe_shali, 'tedad_shali': tedad_shali, 'vazn_shali': vazn_shali, 'keshavarz': CodeOfKeshavars, 'nam_ijad_konande': nam_ijad_konande, 'tozihat': tozihat}
            r1 = requests.post(urlSabeteShali, data=sabteShaliPOST)
            print(r1.status_code)
            print(r1.text)
            if makan=='' or nam=='' or ranande=='' or telefon=='' or nam_ijad_konande=='' or tedad_shali=='' or noe_shali=='' or vazn_shali=='' or tozihat=='':
                messagebox.showinfo('ورودی ناقص', '.تمام فیلد هارا پر کنید')
        else:
            print("NOOOO")
        self.sabteShaliPageRoot.destroy()
        self.shaliHayeSabtShodePageRoot.destroy()
        self.shaliHayeSabtShodePage()


    def sabtShodeHaPage(self):
        self.sabteShodeHaPageRoot = Tk()
        self.sabteShodeHaPageRoot.configure(bg='#E3F0EB')
        self.sabteShodeHaPageRoot.title("ثبت شده ها")
        self.title = Label(self.sabteShodeHaPageRoot, text="ثبت شده ها", font=('IRANYekan', '22'), bg='#E3F0EB')
        self.space = Label(self.sabteShodeHaPageRoot, text=" ", bg='#E3F0EB')
        self.space1 = Label(self.sabteShodeHaPageRoot, text=" ", bg='#E3F0EB')
        self.space2 = Label(self.sabteShodeHaPageRoot, text=" ", bg='#E3F0EB')
        self.space3 = Label(self.sabteShodeHaPageRoot, text=" ", bg='#E3F0EB')
        self.space4 = Label(self.sabteShodeHaPageRoot, text=" ", bg='#E3F0EB')
        self.space5 = Label(self.sabteShodeHaPageRoot, text=" ", bg='#E3F0EB')
        self.shaliHayeSabtShodeButton = Button(self.sabteShodeHaPageRoot, text="شالی های ثبت شده", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.shaliHayeSabtShodePage)
        self.berenjHayeSabtShodeButton = Button(self.sabteShodeHaPageRoot, text="برنج های ثبت شده", bg='#4C967D', fg='white', font=('IRANYekan', '20'), command=ALLPages.berenjHayeSabtShodePage)
        self.tahvilHayeSabtShode = Button(self.sabteShodeHaPageRoot, text="تحویل ها", bg='#A2DDA5',font=('IRANYekan', '20'), command=ALLPages.tahvilHaKol)
        self.keshavarzHayeSabtShode = Button(self.sabteShodeHaPageRoot, text="کشاورز ها", bg='#4C967D',fg='white',font=('IRANYekan', '20'), command=ALLPages.keshavarzha)
        self.shaliHayeSabtShodeButton.config(height=2, width=80)
        self.berenjHayeSabtShodeButton.config(height=2, width=80)
        self.tahvilHayeSabtShode.config(height=2, width=80)
        self.keshavarzHayeSabtShode.config(height=2, width=80)
        self.space.pack()
        self.title.pack()
        self.space1.pack()
        self.space2.pack()
        self.shaliHayeSabtShodeButton.pack()
        self.space3.pack()
        self.berenjHayeSabtShodeButton.pack()
        self.space5.pack()
        self.tahvilHayeSabtShode.pack()
        self.space4.pack()
        self.keshavarzHayeSabtShode.pack()
        self.space5.pack()

    def keshavarzha(self):
        print("aaaaaaaaaaaaaaaaaaaaa")
        self.keshavarzhapageroot=Tk()
        self.keshavarzhapageroot.configure(bg='#E3F0EB')
        self.keshavarzhapageroot.title("کشاورز ها")
        self.space = Label(self.keshavarzhapageroot, text=" ", bg='#E3F0EB')
        self.space1 = Label(self.keshavarzhapageroot, text=" ", bg='#E3F0EB')
        self.space2 = Label(self.keshavarzhapageroot, text=" ", bg='#E3F0EB')
        self.space3 = Label(self.keshavarzhapageroot, text=" ", bg='#E3F0EB')
        self.space4 = Label(self.keshavarzhapageroot, text=" ", bg='#E3F0EB')
        self.space5 = Label(self.keshavarzhapageroot, text=" ", bg='#E3F0EB')
        self.title = Label(self.keshavarzhapageroot, text="کشاورز ها", font=('IRANYekan', '22'), bg='#E3F0EB')
        cols = ('کد کشاورز', 'نام کشاورز', 'ساعت', 'تاریخ')
        self.listBoxz = ttk.Treeview(self.keshavarzhapageroot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxz.yview)
        self.listBoxz.configure(yscrollcommand=vsb.set)
        self.listBoxz.column("0", width=280, anchor="c")
        self.listBoxz.column("1", width=280, anchor="c")
        self.listBoxz.column("2", width=280, anchor="c")
        self.listBoxz.column("3", width=280, anchor="c")
        self.listBoxz.config(height=28)
        for col in cols:
            self.listBoxz.heading(col, text=col)
        url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/list/'
        r = requests.get(url)
        for i in range(0, len(r.json())):
            self.listBoxz.insert("", "end", values=(
                str(r.json()[i]['code']),
                str(r.json()[i]['nam']),
                str(r.json()[i]['saat']),
                str(r.json()[i]['tarikh'])
            ))
        self.space1.pack()
        self.title.pack()
        self.space2.pack()
        self.listBoxz.pack()
        self.space3.pack()

    def tahvilHaKol(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.tahvikHayeSabtShodeRoot = Tk()
        self.tahvikHayeSabtShodeRoot.configure(bg='#E3F0EB')
        self.tahvikHayeSabtShodeRoot.title("تحویل ها")
        self.space = Label(self.tahvikHayeSabtShodeRoot, text=" ", bg='#E3F0EB')
        self.space1 = Label(self.tahvikHayeSabtShodeRoot, text=" ", bg='#E3F0EB')
        self.space2 = Label(self.tahvikHayeSabtShodeRoot, text=" ", bg='#E3F0EB')
        self.space3 = Label(self.tahvikHayeSabtShodeRoot, text=" ", bg='#E3F0EB')
        self.space4 = Label(self.tahvikHayeSabtShodeRoot, text=" ", bg='#E3F0EB')
        self.space5 = Label(self.tahvikHayeSabtShodeRoot, text=" ", bg='#E3F0EB')
        self.title = Label(self.tahvikHayeSabtShodeRoot, text="تحویل ها", font=('IRANYekan', '22'), bg='#E3F0EB')
        cols = ('وزن نیمدانه', 'وزن اضافه', 'تعداد کیسه سبوس', 'تعداد کیسه برنج', 'کد کشاورز', 'کد برنج', 'ساعت', 'تاریخ')
        self.listBoxxxx = ttk.Treeview(self.tahvikHayeSabtShodeRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxxxx.yview)
        self.listBoxxxx.configure(yscrollcommand=vsb.set)
        self.listBoxxxx.column("0", width=150, anchor="c")
        self.listBoxxxx.column("1", width=150, anchor="c")
        self.listBoxxxx.column("2", width=150, anchor="c")
        self.listBoxxxx.column("3", width=150, anchor="c")
        self.listBoxxxx.column("4", width=150, anchor="c")
        self.listBoxxxx.column("5", width=150, anchor="c")
        self.listBoxxxx.column("6", width=150, anchor="c")
        self.listBoxxxx.column("7", width=150, anchor="c")
        self.listBoxxxx.config(height=20)
        # set column headings
        for col in cols:
            self.listBoxxxx.heading(col, text=col)
        self.tozihh = Button(self.tahvikHayeSabtShodeRoot, text="توضیحات", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.tozihTahvil)
        self.tozihh.config(height=1, width=20)
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/list/'
            r = requests.get(url)
            print(len(r.json()[0]['berenj']['tahvilha']))
            for i in range(0, len(r.json())):
                if r.json()[i]['berenj']:
                    if r.json()[i]['berenj']['tahvilha'] :
                        for j in range(0, len(r.json()[i]['berenj']['tahvilha'])):
                            self.listBoxxxx.insert("", "end", values=(
                                str(r.json()[i]['berenj']['tahvilha'][j]['vazn_nimdane']),
                                str(r.json()[i]['berenj']['tahvilha'][j]['vazn_ezafe']),
                                str(r.json()[i]['berenj']['tahvilha'][j]['tedad_kise_saboos']),
                                str(r.json()[i]['berenj']['tahvilha'][j]['tedad_kise_berenj']),
                                str(r.json()[i]['code']),
                                str(r.json()[i]['berenj']['id']),
                                str(r.json()[i]['berenj']['tahvilha'][j]['saat']),
                                str(r.json()[i]['berenj']['tahvilha'][j]['tarikh'])
                            ))
        else:
            print("NOOOO")
        self.space.pack()
        self.title.pack()
        self.space1.pack()
        self.listBoxxxx.pack()
        self.space2.pack()
        self.tozihh.pack()
        self.space3.pack()

    def tozihTahvil(self):
        self.listBoxxxx.bind('<Button-1>', self.tozihTahvil)
        curItem = self.listBoxxxx.focus()
        k = self.listBoxxxx.item(curItem)
        try:
            print(k['values'][0])
        except:
            messagebox.showinfo('عدم انتخاب','برنجی برای نمایش انتخاب نکردید')
            self.tahvikHayeSabtShodeRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.tahvilHaKol()
            self.sabtShodeHaPage()
            return
        tozihTahvilRoot = Tk()
        tozihTahvilRoot.configure(bg='#E3F0EB')
        tozihTahvilRoot.title("اطلاعات کامل تحویل")
        title = Label(tozihTahvilRoot, text="اطلاعات کامل تحویل (رسید)", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space1 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space2 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space3 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space4 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space5 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space6 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space7 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space8 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space9 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space10 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        space11 = Label(tozihTahvilRoot, text=" ", bg='#E3F0EB')
        one = Label(tozihTahvilRoot, text='تاریخ: ' + k['values'][7], font=('IRANYekan', '17'), bg='#E3F0EB', fg='#4C967D')
        two = Label(tozihTahvilRoot, text='ساعت: ' + k['values'][6], font=('IRANYekan', '17'), bg='#E3F0EB')
        three = Label(tozihTahvilRoot, text='کد برنج: ' + str(k['values'][5]), font=('IRANYekan', '17'), bg='#E3F0EB')
        four = Label(tozihTahvilRoot, text='کد کشاورز: ' + str(k['values'][4]), font=('IRANYekan', '17'), bg='#E3F0EB')
        five = Label(tozihTahvilRoot, text='تعداد کیسه برنج: ' + str(k['values'][3]), font=('IRANYekan', '17'), bg='#E3F0EB')
        six = Label(tozihTahvilRoot, text='تعداد کیسه سبوس: ' + str(k['values'][2]), font=('IRANYekan', '17'), bg='#E3F0EB')
        seven = Label(tozihTahvilRoot, text='وزن اضافه: ' + str(k['values'][1]), font=('IRANYekan', '17'), bg='#E3F0EB')
        eight = Label(tozihTahvilRoot, text='وزن نیمدانه: ' + str(k['values'][1]), font=('IRANYekan', '17'),bg='#E3F0EB')
        chap = Button(tozihTahvilRoot, text="چاپ", bg='#A2DDA5', font=('IRANYekan', '15'))
        chap.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        one.pack()
        space2.pack()
        two.pack()
        space3.pack()
        three.pack()
        space4.pack()
        four.pack()
        space5.pack()
        five.pack()
        space6.pack()
        six.pack()
        space7.pack()
        seven.pack()
        space8.pack()
        eight.pack()
        space9.pack()
        chap.pack()
        space10.pack()

    def shaliHayeSabtShodePage(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.shaliHayeSabtShodePageRoot = Tk()
        self.shaliHayeSabtShodePageRoot.configure(bg='#E3F0EB')
        self.shaliHayeSabtShodePageRoot.title("شالی های ثبت شده")
        self.space = Label(self.shaliHayeSabtShodePageRoot, text=" ",bg='#E3F0EB')
        self.space1 = Label(self.shaliHayeSabtShodePageRoot, text=" ",bg='#E3F0EB')
        self.space2 = Label(self.shaliHayeSabtShodePageRoot, text=" ",bg='#E3F0EB')
        self.space3 = Label(self.shaliHayeSabtShodePageRoot, text=" ",bg='#E3F0EB')
        self.space4 = Label(self.shaliHayeSabtShodePageRoot, text=" ",bg='#E3F0EB')
        self.space5 = Label(self.shaliHayeSabtShodePageRoot, text=" ",bg='#E3F0EB')
        self.title = Label(self.shaliHayeSabtShodePageRoot, text="شالی های ثبت شده", font=('IRANYekan', '22'), bg='#E3F0EB')
        cols = ('تلفن','راننده','وزن شالی','تعداد کیسه','نوع شالی','نام کشاورز', 'کد شالی', 'ساعت', 'تاریخ')
        self.listBox = ttk.Treeview(self.shaliHayeSabtShodePageRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=vsb.set)
        self.listBox.column("0", width=240, anchor="c")
        self.listBox.column("1", width=240, anchor="c")
        self.listBox.column("2", width=80, anchor="c")
        self.listBox.column("3", width=80, anchor="c")
        self.listBox.column("4", width=150, anchor="c")
        self.listBox.column("5", width=240, anchor="c")
        self.listBox.column("6", width=100, anchor="c")
        self.listBox.column("7", width=100, anchor="c")
        self.listBox.column("8", width=100, anchor="c")
        if internetConnectionFlag:
            urlViewInListViewShaliHayeSabtShode = "https://shali-firstsite.fandogh.cloud/api/keshavarz/list/"
            r2 = requests.get(urlViewInListViewShaliHayeSabtShode)
            for i in range(0, len(r2.json())):
                if len(r2.json()[i]['shaliha']) != 0:
                    for j in range(0, len(r2.json()[i]['shaliha'])):
                        self.listBox.insert("", "end", values=(r2.json()[i]['telefon'],
                                                               r2.json()[i]['ranande'],
                                                               str(r2.json()[i]['shaliha'][j]['vazn_shali']),
                                                               str(r2.json()[i]['shaliha'][j]['tedad_shali']),
                                                               r2.json()[i]['shaliha'][j]['noe_shali'],
                                                               r2.json()[i]['nam'],
                                                               r2.json()[i]['shaliha'][j]['id'],
                                                               r2.json()[i]['shaliha'][j]['saat'],
                                                               r2.json()[i]['shaliha'][j]['tarikh']))
                        # addToListForPrint1 = '  تاریخ: '+r2.json()[i]['shaliha'][j]['tarikh']+'  ساعت: '+r2.json()[i]['shaliha'][j]['saat']+'  کد شالی: '+str(r2.json()[i]['shaliha'][j]['id'])+'  نام کشاورز: '+r2.json()[i]['nam']+'  نوع شالی: '+r2.json()[i]['shaliha'][j]['noe_shali']
                        # addToListForPrint2 = '  تعداد کیسه:'+str(r2.json()[i]['shaliha'][j]['tedad_shali'])+'  وزن شالی: '+str(r2.json()[i]['shaliha'][j]['vazn_shali'])+'  راننده: '+r2.json()[i]['ranande']+'  تلفن: '+r2.json()[i]['telefon']
                        # shaliForPrintToPDF.append(addToListForPrint1)
                        # shaliForPrintToPDF.append(addToListForPrint2)
        else:
            print("Not Completed")
        self.listBox.config(height=12)
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        self.sabt = Button(self.shaliHayeSabtShodePageRoot, text="ثبت شالی دیگر", bg='#A2DDA5', font=('IRANYekan', '15'), command=ALLPages.sabteShaliPage)
        self.sabt.config(height=1, width=20)
        self.delete = Button(self.shaliHayeSabtShodePageRoot, text="حذف", bg='#A2DDA5', font=('IRANYekan', '15'), command = ALLPages.deleteFromShali)
        self.delete.config(height=1, width=20)
        self.edit = Button(self.shaliHayeSabtShodePageRoot, text="ویرایش", bg='#A2DDA5', font=('IRANYekan', '15'), command = self.editShali)
        self.edit.config(height=1, width=20)
        self.tozih = Button(self.shaliHayeSabtShodePageRoot, text="توضیحات", bg='#A2DDA5', font=('IRANYekan', '15'),command=ALLPages.tozihshali)
        self.tozih.config(height=1, width=20)
        chap = Button(self.shaliHayeSabtShodePageRoot, text="چاپ", bg='#A2DDA5', font=('IRANYekan', '15'))
        chap.config(height=1, width=20)
        self.space.pack()
        self.title.pack()
        self.space1.pack()
        self.listBox.pack()
        self.space2.pack()
        self.sabt.pack()
        self.edit.pack()
        self.delete.pack()
        self.tozih.pack()
        chap.pack()
        self.space3.pack()

    # def shaliChap(self):
    #     MakePDF('Shali haye sabt shode.pdf', 'شالی های ثبت شده', shaliForPrintToPDF)
    #     shaliForPrintToPDF.clear()

    def deleteFromShali(self):
        self.listBox.bind('<Button-1>', self.deleteFromShali)
        curItem = self.listBox.focus()
        wannaDelete = self.listBox.item(curItem)
        try:
            print(wannaDelete['values'][6])
        except:
            messagebox.showinfo('عدم انتخاب', 'موردی برای حذف انتخاب نشده است')
            self.shaliHayeSabtShodePageRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.shaliHayeSabtShodePage()
            self.sabtShodeHaPage()
        urlForDeleteShali = 'https://shali-firstsite.fandogh.cloud/api/shali/' + str(wannaDelete['values'][6]) + '/'
        x = requests.delete(urlForDeleteShali)
        print(x.text)
        self.shaliHayeSabtShodePageRoot.destroy()
        self.shaliHayeSabtShodePage()

    def editButton(self):
        print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
        self.listBox.bind('<Button-1>', self.editButton)
        curItem = self.listBox.focus()
        wannaEdit = self.listBox.item(curItem)
        print("XXXXXXXXXXXXXX")
        print(wannaEdit['values'][6])
        urlForEditShali = 'https://shali-firstsite.fandogh.cloud/api/shali/' + str(wannaEdit['values'][6]) + '/'
        r = requests.get(urlForEditShali)
        urlForEditkeshavarz = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/' + str(r.json()['keshavarz']) + '/'
        print(r.json())
        CodeOfKeshavars = int(r.json()['id'])
        print(CodeOfKeshavars)
        noe_shali = str(self.shaliKindTextLabele.get())
        tedad_shali = int(self.shaliBagNumberTextLabele.get())
        vazn_shali = int(self.shaliWeightTextLabele.get())
        tozihat = str(self.shaliTozihTextLabele.get())
        nam_ijad_konande = str(NameOfUser)
        tozihat = str(self.shaliTozihTextLabele.get())
        EditShaliPOST = {'noe_shali': noe_shali, 'tedad_shali': tedad_shali, 'vazn_shali': vazn_shali, 'keshavarz': CodeOfKeshavars, 'nam_ijad_konande': nam_ijad_konande, 'tozihat': tozihat }
        makan = str(self.farmerNameTextLabele.get())
        nam = str(self.farmerNameTextLabele.get())
        ranande = str(self.driverTextLabele.get())
        telefon = str(self.phoneTextLabele.get())
        nam_ijad_konande = NameOfUser
        EditKeshavarzPOST = {'makan': makan, 'nam': nam, 'ranande': ranande, 'telefon': telefon, 'nam_ijad_konande': nam_ijad_konande}
        x = requests.put(urlForEditShali, data=EditShaliPOST)
        y = requests.put(urlForEditkeshavarz, data=EditKeshavarzPOST)
        print(x.status_code)
        print(x.text)
        self.sabteShaliPageRoott.destroy()
        self.shaliHayeSabtShodePageRoot.destroy()
        self.shaliHayeSabtShodePage()

    def tozihshali(self):
        self.listBox.bind('<Button-1>', self.tozihshali)
        curItem = self.listBox.focus()
        k = self.listBox.item(curItem)
        try:
            showTozih = k['values'][6]
        except:
            messagebox.showinfo('عدم انتخاب', 'موردی برای توضیح انتخاب نشده است')
            self.shaliHayeSabtShodePageRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.shaliHayeSabtShodePage()
            self.sabtShodeHaPage()
        urlForShowShali = 'https://shali-firstsite.fandogh.cloud/api/shali/' + str(showTozih) + '/'
        r3 = requests.get(urlForShowShali)
        r3.json()['tozihat']
        tozihShaliRoot = Tk()
        tozihShaliRoot.title("اطلاعات کامل شالی")
        tozihShaliRoot.configure(bg='#E3F0EB')
        title = Label(tozihShaliRoot, text="اطلاعات کامل شالی", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space1 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space2 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space3 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space4 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space5 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space6 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space7 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space8 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space9 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space10 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        space11 = Label(tozihShaliRoot, text=" ", bg='#E3F0EB')
        one = Label(tozihShaliRoot, text='تاریخ: '+str(k['values'][8]), font=('IRANYekan', '15'), bg='#E3F0EB')
        two = Label(tozihShaliRoot, text='ساعت: '+str(k['values'][7]), font=('IRANYekan', '15'), bg='#E3F0EB')
        three = Label(tozihShaliRoot, text='کد شالی: '+str(k['values'][6]), font=('IRANYekan', '15'), bg='#E3F0EB')
        four = Label(tozihShaliRoot, text='نام کشاورز: '+str(k['values'][5]), font=('IRANYekan', '15'), bg='#E3F0EB')
        five = Label(tozihShaliRoot, text='نوع شالی: '+str(k['values'][4]), font=('IRANYekan', '15'), bg='#E3F0EB')
        six = Label(tozihShaliRoot, text='تعداد کیسه ها: '+str(k['values'][3]), font=('IRANYekan', '15'), bg='#E3F0EB')
        seven = Label(tozihShaliRoot, text='وزن شالی: '+str(k['values'][2]), font=('IRANYekan', '15'), bg='#E3F0EB')
        eight = Label(tozihShaliRoot, text='راننده: '+str(k['values'][1]), font=('IRANYekan', '15'), bg='#E3F0EB')
        nine = Label(tozihShaliRoot, text='تلفن: '+str(k['values'][0]), font=('IRANYekan', '15'), bg='#E3F0EB')
        ten = Label(tozihShaliRoot, text='توضیحات: '+str(r3.json()['tozihat']), font=('IRANYekan', '12'), bg='#E3F0EB')
        print(r3.json())
        print("OK")
        space.pack()
        title.pack()
        space1.pack()
        one.pack()
        space2.pack()
        two.pack()
        space3.pack()
        three.pack()
        space4.pack()
        four.pack()
        space5.pack()
        five.pack()
        space6.pack()
        six.pack()
        space7.pack()
        seven.pack()
        space8.pack()
        eight.pack()
        space9.pack()
        nine.pack()
        space10.pack()
        ten.pack()
        space11.pack()

    def berenjHayeSabtShodePage(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.berenjHayeSabtShodePageRoot = Tk()
        self.berenjHayeSabtShodePageRoot.configure(bg='#E3F0EB')
        self.berenjHayeSabtShodePageRoot.title("برنج های ثبت شده")
        self.title = Label(self.berenjHayeSabtShodePageRoot, text="برنج های ثبت شده", font=('IRANYekan', '22'), fg='#0B2110', bg='#E3F0EB')
        self.space = Label(self.berenjHayeSabtShodePageRoot, text=" ", bg='#E3F0EB')
        self.space1 = Label(self.berenjHayeSabtShodePageRoot, text=" ", bg='#E3F0EB')
        self.space2 = Label(self.berenjHayeSabtShodePageRoot, text=" ", bg='#E3F0EB')
        self.space3 = Label(self.berenjHayeSabtShodePageRoot, text=" ", bg='#E3F0EB')
        self.space4 = Label(self.berenjHayeSabtShodePageRoot, text=" ", bg='#E3F0EB')
        self.space5 = Label(self.berenjHayeSabtShodePageRoot, text=" ", bg='#E3F0EB')
        cols = ('وزن اضافه', 'وزن نیم دانه', 'تعداد کیسه سبوس','وزن کیسه برنج','تعداد کیسه برنج', 'کد کشاورز', 'ساعت', 'تاریخ')
        self.listBoxx = ttk.Treeview(self.berenjHayeSabtShodePageRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxx.yview)
        self.listBoxx.configure(yscrollcommand=vsb.set)
        self.listBoxx.column("0", width=170, anchor="c")
        self.listBoxx.column("1", width=170, anchor="c")
        self.listBoxx.column("2", width=170, anchor="c")
        self.listBoxx.column("3", width=170, anchor="c")
        self.listBoxx.column("4", width=170, anchor="c")
        self.listBoxx.column("5", width=170, anchor="c")
        self.listBoxx.column("6", width=170, anchor="c")
        self.listBoxx.column("7", width=170, anchor="c")
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/list/'
            r = requests.get(url)
            for i in range(0, len(r.json())):
                if r.json()[i]['berenj']:
                    self.listBoxx.insert("", "end", values=( str(r.json()[i]['berenj']['vazn_ezafe'])
                                                            ,str(r.json()[i]['berenj']['vazn_nimdane'])
                                                            ,str(r.json()[i]['berenj']['tedad_kise_saboos'])
                                                            ,str(r.json()[i]['berenj']['vazn_kise_berenj'])
                                                            ,str(r.json()[i]['berenj']['tedad_kise_berenj'])
                                                            ,str(r.json()[i]['code'])
                                                            ,str(r.json()[i]['berenj']['saat'])
                                                            ,str(r.json()[i]['berenj']['tarikh'])))
        else:
            print('NOOOOOOOO')
        self.listBoxx.config(height=12)
        # set column headings
        for col in cols:
            self.listBoxx.heading(col, text=col)
        self.delete = Button(self.berenjHayeSabtShodePageRoot, text="حذف", bg='#A2DDA5', font=('IRANYekan', '15'), command=ALLPages.deletFromBerenj)
        self.delete.config(height=1, width=20)
        self.edit = Button(self.berenjHayeSabtShodePageRoot, text="ویرایش", bg='#A2DDA5', font=('IRANYekan', '15'), command=ALLPages.editBerenj)
        self.edit.config(height=1, width=20)
        self.tozih = Button(self.berenjHayeSabtShodePageRoot, text="توضیحات", bg='#A2DDA5', font=('IRANYekan', '15'),command=ALLPages.tozihBerenj)
        self.tozih.config(height=1, width=20)
        self.sabt = Button(self.berenjHayeSabtShodePageRoot, text="ثبت برنج", bg='#A2DDA5', font=('IRANYekan', '15'),command=ALLPages.sabteBerenjPage2)
        self.sabt.config(height=1, width=20)
        self.chap = Button(self.berenjHayeSabtShodePageRoot, text="چاپ", bg='#A2DDA5', font=('IRANYekan', '15'))
        self.chap.config(height=1, width=20)
        self.space.pack()
        self.title.pack()
        self.space1.pack()
        self.listBoxx.pack()
        self.space2.pack()
        self.sabt.pack()
        self.edit.pack()
        self.delete.pack()
        self.tozih.pack()
        self.chap.pack()
        self.space3.pack()

    def deletFromBerenj(self):
        self.listBoxx.bind('<Button-1>', self.deletFromBerenj)
        curItem = self.listBoxx.focus()
        wannaDelete = self.listBoxx.item(curItem)
        try:
            print(wannaDelete['values'][5])
        except:
            messagebox.showinfo('عدم انتخاب','برنجی برای حذف انتخاب نکردید')
            self.berenjHayeSabtShodePageRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.berenjHayeSabtShodePage()
            self.sabtShodeHaPage()
            return
        urlForDeleteBerenj = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/' + str(wannaDelete['values'][5]) + '/'
        x = requests.get(urlForDeleteBerenj)
        url = 'https://shali-firstsite.fandogh.cloud/api/berenj/'+str(x.json()['berenj']['id'])
        x2 = requests.delete(url)
        print(x2.text)
        self.berenjHayeSabtShodePageRoot.destroy()
        self.berenjHayeSabtShodePage()

    def editBerenj(self):########################
        self.listBoxx.bind('<Button-1>', self.editBerenj)
        curItem = self.listBoxx.focus()
        k = self.listBoxx.item(curItem)
        try:
            print(k['values'][5])
        except:
            messagebox.showinfo('عدم انتخاب','برنجی برای ویرایش انتخاب نکردید')
            self.berenjHayeSabtShodePageRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.berenjHayeSabtShodePage()
            self.sabtShodeHaPage()
            return
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.sabteBerenjChoosenPageRoot = Tk()
        self.sabteBerenjChoosenPageRoot.configure(bg='#E3F0EB')
        self.sabteBerenjChoosenPageRoot.title("ثبت برنج")
        title = Label(self.sabteBerenjChoosenPageRoot, text="ثبت برنج", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.sabteBerenjChoosenPageRoot, text=" ",bg='#E3F0EB')
        space2 = Label(self.sabteBerenjChoosenPageRoot, text=" ",bg='#E3F0EB')
        space3 = Label(self.sabteBerenjChoosenPageRoot, text=" ",bg='#E3F0EB')
        space4 = Label(self.sabteBerenjChoosenPageRoot, text=" ",bg='#E3F0EB')
        space5 = Label(self.sabteBerenjChoosenPageRoot, text=" ",bg='#E3F0EB')
        space6 = Label(self.sabteBerenjChoosenPageRoot, text=" ",bg='#E3F0EB')
        CodeAndNameAndPhoneAndDriverName = Label(self.sabteBerenjChoosenPageRoot)
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/'+str(k['values'][5])+'/'
            r = requests.get(url)
            CodeAndNameAndPhoneAndDriverName.configure(text="   نام کشاورز: " + str(r.json()['nam']) + "   کد: " + str(k['values'][5]) + "   راننده: " + str(r.json()['ranande']) + "   تلفن: " + str(r.json()['telefon']), font=('IRANYekan', '18'), bg='#E3F0EB')
        else:
            CodeAndNameAndPhoneAndDriverName.configure(bg='#E3F0EB', text="کد: 101    نام: اردوان خلیج    تلفن: 09120864054    راننده: مسعود خداوردبان", font=('IRANYekan', '18'))

        self.numberx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.numberx.insert(0, k['values'][4])
        self.weightx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.weightx.insert(0, k['values'][3])
        self.extrax = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.extrax.insert(0, k['values'][0])
        self.halfx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.halfx.insert(0, k['values'][1])
        self.sabusx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.sabusx.insert(0, k['values'][2])
        self.descx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        urlForDeleteBerenj = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/' + str(
            k['values'][5]) + '/'
        x = requests.get(urlForDeleteBerenj)
        url = 'https://shali-firstsite.fandogh.cloud/api/berenj/' + str(x.json()['berenj']['id'])
        x2 = requests.get(url)
        self.descx.insert(0, x2.json()['tozihat'])
        self.locx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.locx.insert(0, x2.json()['makan_berenj'])
        self.karmozdx = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.karmozdx.insert(0, x2.json()['karmozd'])
        sabt = Button(self.sabteBerenjChoosenPageRoot, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '20'), command = ALLPages.editButtonB)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        CodeAndNameAndPhoneAndDriverName.pack()
        space2.pack()
        space3.pack()
        space4.pack()
        self.numberx.pack()
        self.weightx.pack()
        self.extrax.pack()
        self.halfx.pack()
        self.sabusx.pack()
        self.locx.pack()
        self.karmozdx.pack()
        self.descx.pack()
        space5.pack()
        sabt.pack()
        space6.pack()

    def editButtonB(self):
        self.listBoxx.bind('<Button-1>', self.editButtonB)
        curItem = self.listBoxx.focus()
        wannaEdit = self.listBoxx.item(curItem)
        print("XXXXXXXXXXXXXX")
        print(wannaEdit['values'][5])
        keshavarz = int(wannaEdit['values'][5])
        makan_berenj = str(self.locx.get())
        tedad_kise_berenj = int(self.numberx.get())
        tedad_kise_saboos = int(self.sabusx.get())
        vazn_ezafe = int(self.extrax.get())
        vazn_kise_berenj = int(self.weightx.get())
        vazn_nimdane = int(self.halfx.get())
        karmozd = int(self.karmozdx.get())
        nam_ijad_konande = str(NameOfUser)
        tozihat = str(self.descx.get())
        url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/'+str(wannaEdit['values'][5])+'/'
        r = requests.get(url)
        print(r.json()['berenj']['id'])
        url2 = 'https://shali-firstsite.fandogh.cloud/api/berenj/'+str(r.json()['berenj']['id'])
        rr = requests.put(url2, data={'keshavarz': keshavarz,'makan_berenj':makan_berenj,
                                 'tedad_kise_berenj':tedad_kise_berenj,'tedad_kise_saboos':tedad_kise_saboos,
                                 'vazn_ezafe':vazn_ezafe,'vazn_kise_berenj':vazn_kise_berenj,
                                 'vazn_nimdane': vazn_nimdane, 'karmozd':karmozd,'nam_ijad_konande':nam_ijad_konande,
                                 'tozihat':tozihat})
        print(rr.status_code)
        print(rr.text)
        self.sabteBerenjChoosenPageRoot.destroy()
        self.berenjHayeSabtShodePageRoot.destroy()
        self.berenjHayeSabtShodePage()

    def tozihBerenj(self):
        self.listBoxx.bind('<Button-1>', self.tozihBerenj)
        curItem = self.listBoxx.focus()
        k = self.listBoxx.item(curItem)
        try:
            showTozih = k['values'][5]
        except:
            messagebox.showinfo('عدم انتخاب','برنجی برای نمایش انتخاب نکردید')
            self.berenjHayeSabtShodePageRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.berenjHayeSabtShodePage()
            self.sabtShodeHaPage()
            return
        print(showTozih)
        urlForShowShali = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/search/' + str(showTozih) + '/'
        r3 = requests.get(urlForShowShali)
        print(r3.status_code)
        print(r3.text)
        tozihBerenjRoot = Tk()
        tozihBerenjRoot.configure(bg='#E3F0EB')
        tozihBerenjRoot.title("اطلاعات کامل برنج")
        title = Label(tozihBerenjRoot, text="اطلاعات کامل برنج", font=('IRANYekan', '22'), fg='#0B2110', bg='#E3F0EB')
        space = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space1 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space2 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space3 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space4 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space5 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space6 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space7 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space8 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space9 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space10 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space11 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        space12 = Label(tozihBerenjRoot, text=" ",bg='#E3F0EB')
        one = Label(tozihBerenjRoot, text='تاریخ: ' + k['values'][7], font=('IRANYekan', '14'),bg='#E3F0EB')
        two = Label(tozihBerenjRoot, text='ساعت: ' + k['values'][6], font=('IRANYekan', '14'),bg='#E3F0EB')
        three = Label(tozihBerenjRoot, text='کد برنج: ' + str(r3.json()[0]['berenj']['id']), font=('IRANYekan', '14'),bg='#E3F0EB')
        four = Label(tozihBerenjRoot, text='نام کشاورز: ' + str(r3.json()[0]['nam']), font=('IRANYekan', '14'),bg='#E3F0EB')
        five = Label(tozihBerenjRoot, text='کد کشاورز: ' + str(k['values'][5]), font=('IRANYekan', '14'),bg='#E3F0EB')
        six = Label(tozihBerenjRoot, text='تعداد کیسه برنج: ' + str(k['values'][4]), font=('IRANYekan', '14'),bg='#E3F0EB')
        seven = Label(tozihBerenjRoot, text='وزن کیسه برنج: ' + str(k['values'][3]), font=('IRANYekan', '14'),bg='#E3F0EB')
        eight = Label(tozihBerenjRoot, text='تعداد کیسه سبوس: ' + str(k['values'][2]), font=('IRANYekan', '14'),bg='#E3F0EB')
        nine = Label(tozihBerenjRoot, text='وزن نیمدانه: ' + str(k['values'][1]), font=('IRANYekan', '14'),bg='#E3F0EB')
        ten = Label(tozihBerenjRoot, text='وزن اضافه: ' + str(k['values'][0]), font=('IRANYekan', '14'),bg='#E3F0EB')
        eleven = Label(tozihBerenjRoot, text='توضیحات: ' + str(r3.json()[0]['berenj']['tozihat']), font=('IRANYekan', '12'),bg='#E3F0EB')
        print(r3.json())
        print("OK")
        space.pack()
        title.pack()
        space1.pack()
        one.pack()
        # space2.pack()
        two.pack()
        # space3.pack()
        three.pack()
        # space4.pack()
        four.pack()
        # space5.pack()
        five.pack()
        # space6.pack()
        six.pack()
        # space7.pack()
        seven.pack()
        # space8.pack()
        eight.pack()
        # space9.pack()
        nine.pack()
        # space10.pack()
        ten.pack()
        # space11.pack()
        eleven.pack()
        space12.pack()

    def showSearch(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        WordToSearch = str(self.search.get())
        urlForSearch = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/search/' + WordToSearch + '/'
        if internetConnectionFlag:
            r = requests.get(urlForSearch)
            print(r.json())
            if len(r.json())>0:
                for i in self.shaliTreeList.get_children():
                    self.shaliTreeList.delete(i)
                for i in range(0, len(r.json())):
                    for j in range(0, len(r.json()[i]['shaliha'])):
                        self.shaliTreeList.insert("", "end", values=(
                        str(r.json()[i]['shaliha'][j]['id']),
                        str(r.json()[i]['nam']),
                        str(r.json()[i]['code']),
                        str(r.json()[i]['tarikh']),
                        str(r.json()[i]['saat'])))
        else:
            print("NOOOOO")

    def sabteBerenjPage2(self):
        sabteBerenjPageRoot = Tk()
        sabteBerenjPageRoot.configure(bg='#E3F0FB')
        sabteBerenjPageRoot.title("ثبت برنچ")
        space = Label(sabteBerenjPageRoot, text=" ", bg='#E3F0FB')
        space1 = Label(sabteBerenjPageRoot, text=" ", bg='#E3F0FB')
        space2 = Label(sabteBerenjPageRoot, text=" ", bg='#E3F0FB')
        space3 = Label(sabteBerenjPageRoot, text=" ", bg='#E3F0FB')
        space4 = Label(sabteBerenjPageRoot, text=" ", bg='#E3F0FB')
        title = Label(sabteBerenjPageRoot, text="انتخاب شالی", font=('IRANYekan', '22'), bg='#E3F0FB')
        self.search = Entry(sabteBerenjPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.search.insert(0, "جستجو")
        sabt = Button(sabteBerenjPageRoot, text="انتخاب", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.sabteBerenjChoosen2)
        searching = Button(sabteBerenjPageRoot, text="جستجو", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.showSearch)
        sabt.config(height=1, width=20)
        searching.config(height=1, width=20)
        cols = ('نام کشاورز', 'کد کشاورز', 'تاریخ', 'ساعت')
        self.shaliTreeList = ttk.Treeview(sabteBerenjPageRoot, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.shaliTreeList.heading(col, text=col)
        self.shaliTreeList.column("0", anchor="c")
        self.shaliTreeList.column("1", anchor="c")
        self.shaliTreeList.column("2", anchor="c")
        self.shaliTreeList.column("3", anchor="c")
        vsb = ttk.Scrollbar(orient="vertical", command=self.shaliTreeList.yview)
        self.shaliTreeList.configure(yscrollcommand=vsb.set)
        space.pack()
        title.pack()
        space1.pack()
        self.search.pack()
        space2.pack()
        self.shaliTreeList.pack()
        space4.pack()
        searching.pack()
        sabt.pack()
        space3.pack()

    def sabteBerenjChoosen2(self):
        self.shaliTreeList.bind('<Button-1>', self.sabteBerenjChoosen)
        curItem = self.shaliTreeList.focus()
        k = self.shaliTreeList.item(curItem)
        try:
            self.shomareKeshavarzBarayeSabteBerenj = str(k['values'][1])
        except:
            messagebox.showinfo('عدم انتخاب', 'شالی انتخاب نشده')
            self.berenjHayeSabtShodePageRoot.destroy()
            self.sabteShodeHaPageRoot.destroy()
            self.berenjHayeSabtShodePage()
            self.sabtShodeHaPage()
            return
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.sabteBerenjChoosenPageRoot = Tk()
        self.sabteBerenjChoosenPageRoot.title("ثبت برنج")
        self.sabteBerenjChoosenPageRoot.configure(bg='#E3F0EB')
        title = Label(self.sabteBerenjChoosenPageRoot, text="ثبت برنج", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space2 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space3 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space4 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space5 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space6 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        CodeAndNameAndPhoneAndDriverName = Label(self.sabteBerenjChoosenPageRoot)
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/'+str(k['values'][1])+'/'
            r = requests.get(url)
            CodeAndNameAndPhoneAndDriverName.configure(text="   نام کشاورز: " + str(k['values'][0]) + "   کد: " + str(k['values'][1]) + "   راننده: " + str(r.json()['ranande']) + "   تلفن: " + str(r.json()['telefon']), font=('IRANYekan', '18'), bg='#E3F0EB')
        else:
            CodeAndNameAndPhoneAndDriverName.configure(text="کد: 101    نام: اردوان خلیج    تلفن: 09120864054    راننده: مسعود خداوردبان", font=('IRANYekan', '18'), bg='#E3F0EB')
        self.number = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.number.insert(0, "   تعداد کیسه برنج")
        self.weight = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.weight.insert(0, "   وزن کیسه برنج")
        self.extra = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.extra.insert(0, "   وزن اضافه")
        self.half = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.half.insert(0, "   وزن نیم دانه")
        self.sabus = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.sabus.insert(0, "   تعداد کیسه سبوس")
        self.desc = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.desc.insert(0, "   توضیحات")
        self.loc = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.loc.insert(0, "   مکان")
        self.karmozd = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.karmozd.insert(0, "   کارمزد")
        sabt = Button(self.sabteBerenjChoosenPageRoot, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '20'), command = ALLPages.postOrSaveBerenj2)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        CodeAndNameAndPhoneAndDriverName.pack()
        space2.pack()
        space3.pack()
        space4.pack()
        self.number.pack()
        self.weight.pack()
        self.extra.pack()
        self.half.pack()
        self.sabus.pack()
        self.loc.pack()
        self.karmozd.pack()
        self.desc.pack()
        space5.pack()
        sabt.pack()
        space6.pack()

    def postOrSaveBerenj2(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        tedadeBerenj = int(self.number.get())
        vazneBerenj = int(self.weight.get())
        ezafe = int(self.extra.get())
        nimdane = int(self.half.get())
        sabusha = int(self.sabus.get())
        tozihat = str(self.desc.get())
        locationOfBerenj = str(self.loc.get())
        km = int(self.karmozd.get())
        keshavarz = self.shomareKeshavarzBarayeSabteBerenj
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/berenj/new/'
            r = requests.post(url, data={'keshavarz': keshavarz, 'makan_berenj': locationOfBerenj,
                                     'tedad_kise_berenj': tedadeBerenj, 'tedad_kise_saboos': sabusha,
                                     'vazn_ezafe': ezafe, 'vazn_kise_berenj': vazneBerenj, 'vazn_nimdane': nimdane,
                                     'karmozd': km, 'nam_ijad_konande': NameOfUser, 'tozihat': tozihat})
            print(r.status_code)
            print(r.text)
            self.berenjHayeSabtShodePageRoot.destroy()
            self.berenjHayeSabtShodePage()
            self.sabteBerenjChoosenPageRoot.destroy()
        else:
            print("NOOOO")

    def sabteBerenjPage(self):
        self.sabteBerenjPageRoot = Tk()
        self.sabteBerenjPageRoot.configure(bg='#E3F0EB')
        self.sabteBerenjPageRoot.title("ثبت برنچ")
        space = Label(self.sabteBerenjPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.sabteBerenjPageRoot, text=" ", bg='#E3F0EB')
        space2 = Label(self.sabteBerenjPageRoot, text=" ", bg='#E3F0EB')
        space3 = Label(self.sabteBerenjPageRoot, text=" ", bg='#E3F0EB')
        space4 = Label(self.sabteBerenjPageRoot, text=" ", bg='#E3F0EB')
        title = Label(self.sabteBerenjPageRoot, text="انتخاب شالی", font=('IRANYekan', '22'), bg='#E3F0EB')
        self.search = Entry(self.sabteBerenjPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.search.insert(0, "جستجو")
        sabt = Button(self.sabteBerenjPageRoot, text="انتخاب", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.sabteBerenjChoosen)
        searching = Button(self.sabteBerenjPageRoot, text="جستجو", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.showSearch)
        sabt.config(height=1, width=20)
        searching.config(height=1, width=20)
        cols = ('کد شالی','نام کشاورز', 'کد کشاورز', 'تاریخ', 'ساعت')
        self.shaliTreeList = ttk.Treeview(self.sabteBerenjPageRoot, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.shaliTreeList.heading(col, text=col)
        self.shaliTreeList.column("0", anchor="c")
        self.shaliTreeList.column("1", anchor="c")
        self.shaliTreeList.column("2", anchor="c")
        self.shaliTreeList.column("3", anchor="c")
        self.shaliTreeList.column("4", anchor="c")
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        urlForSearch = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/list/'
        if internetConnectionFlag:
            r = requests.get(urlForSearch)
            print(r.json())
            if len(r.json())>0:
                for i in self.shaliTreeList.get_children():
                    self.shaliTreeList.delete(i)
                for i in range(0, len(r.json())):
                    for j in range(0, len(r.json()[i]['shaliha'])):
                        self.shaliTreeList.insert("", "end", values=(
                        str(r.json()[i]['shaliha'][j]['id']),
                        str(r.json()[i]['nam']),
                        str(r.json()[i]['code']),
                        str(r.json()[i]['tarikh']),
                        str(r.json()[i]['saat'])))
        else:
            print("NOOOOO")
        vsb = ttk.Scrollbar(orient="vertical", command=self.shaliTreeList.yview)
        self.shaliTreeList.configure(yscrollcommand=vsb.set)
        space.pack()
        title.pack()
        space1.pack()
        self.search.pack()
        space2.pack()
        self.shaliTreeList.pack()
        space4.pack()
        searching.pack()
        sabt.pack()
        space3.pack()

    def sabteBerenjChoosen(self):
        self.shaliTreeList.bind('<Button-1>', self.sabteBerenjChoosen)
        curItem = self.shaliTreeList.focus()
        k = self.shaliTreeList.item(curItem)
        try:
            self.shomareKeshavarzBarayeSabteBerenj = str(k['values'][1])
        except:
            messagebox.showinfo('عدم انتخاب','شالی انتخاب نکردید')
            self.sabteBerenjPageRoot.destroy()
            self.sabteBerenjPage()
            return
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.sabteBerenjChoosenPageRoot = Tk()
        self.sabteBerenjChoosenPageRoot.title("ثبت برنج")
        self.sabteBerenjChoosenPageRoot.configure(bg='#E3F0EB')
        title = Label(self.sabteBerenjChoosenPageRoot, text="ثبت برنج", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space2 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space3 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space4 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space5 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        space6 = Label(self.sabteBerenjChoosenPageRoot, text=" ", bg='#E3F0EB')
        CodeAndNameAndPhoneAndDriverName = Label(self.sabteBerenjChoosenPageRoot)
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/'+str(k['values'][2])+'/'
            r = requests.get(url)
            CodeAndNameAndPhoneAndDriverName.configure(text="   نام کشاورز: " + str(k['values'][0]) + "   کد: " + str(k['values'][2]) + "   راننده: " + str(r.json()['ranande']) + "   تلفن: " + str(r.json()['telefon']), font=('IRANYekan', '18'), bg='#E3F0EB')
        else:
            CodeAndNameAndPhoneAndDriverName.configure(text="کد: 101    نام: اردوان خلیج    تلفن: 09120864054    راننده: مسعود خداوردبان", font=('IRANYekan', '18'))
        self.number = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.number.insert(0, "تعداد کیسه برنج")
        self.weight = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.weight.insert(0, "وزن کیسه برنج")
        self.extra = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.extra.insert(0, "وزن اضافه")
        self.half = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.half.insert(0, "وزن نیم دانه")
        self.sabus = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.sabus.insert(0, "تعداد کیسه سبوس")
        self.desc = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.desc.insert(0, "توضیحات")
        self.loc = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.loc.insert(0, "مکان")
        self.karmozd = Entry(self.sabteBerenjChoosenPageRoot, width=70, justify='right', font=('IRANYekan', 16), fg='#4C967D')
        self.karmozd.insert(0, "کارمزد")
        sabt = Button(self.sabteBerenjChoosenPageRoot, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '20'), command = ALLPages.postOrSaveBerenj)
        sabt.config(height=1, width=20)
        space.pack()
        title.pack()
        space1.pack()
        CodeAndNameAndPhoneAndDriverName.pack()
        space2.pack()
        space3.pack()
        space4.pack()
        self.number.pack()
        self.weight.pack()
        self.extra.pack()
        self.half.pack()
        self.sabus.pack()
        self.loc.pack()
        self.karmozd.pack()
        self.desc.pack()
        space5.pack()
        sabt.pack()
        space6.pack()

    def postOrSaveBerenj(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        tedadeBerenj = int(self.number.get())
        vazneBerenj = int(self.weight.get())
        ezafe = int(self.extra.get())
        nimdane = int(self.half.get())
        sabusha = int(self.sabus.get())
        tozihat = str(self.desc.get())
        locationOfBerenj = str(self.loc.get())
        km = int(self.karmozd.get())
        keshavarz = self.shomareKeshavarzBarayeSabteBerenj
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/berenj/new/'
            r = requests.post(url, data={'keshavarz': keshavarz, 'makan_berenj': locationOfBerenj,
                                     'tedad_kise_berenj': tedadeBerenj, 'tedad_kise_saboos': sabusha,
                                     'vazn_ezafe': ezafe, 'vazn_kise_berenj': vazneBerenj, 'vazn_nimdane': nimdane,
                                     'karmozd': km, 'nam_ijad_konande': NameOfUser, 'tozihat': tozihat})
            print(r.status_code)
            print(r.text)
            self.sabteBerenjChoosenPageRoot.destroy()
        else:
            print("NOOOO")

    def tahvilPage(self):
        self.berenjnumForSabtNewTahvil = 0
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.tahvilPageRoot = Tk()
        self.tahvilPageRoot.configure(bg='#E3F0EB')
        self.tahvilPageRoot.title("تحویل")
        title = Label(self.tahvilPageRoot, text="تحویل", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        space2 = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        space3 = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        space4 = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        space5 = Label(self.tahvilPageRoot, text=" ", bg='#E3F0EB')
        cols = ('وزن اضافه', 'وزن نیم دانه', 'تعداد کیسه سبوس','وزن کیسه برنج','تعداد کیسه برنج', 'کد کشاورز', 'ساعت', 'تاریخ')
        self.listBoxxx = ttk.Treeview(self.tahvilPageRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxxx.yview)
        self.listBoxxx.configure(yscrollcommand=vsb.set)
        self.listBoxxx.column("0", width=150, anchor="c")
        self.listBoxxx.column("1", width=150, anchor="c")
        self.listBoxxx.column("2", width=150, anchor="c")
        self.listBoxxx.column("3", width=150, anchor="c")
        self.listBoxxx.column("4", width=150, anchor="c")
        self.listBoxxx.column("5", width=150, anchor="c")
        self.listBoxxx.column("6", width=150, anchor="c")
        self.listBoxxx.column("7", width=150, anchor="c")
        self.listBoxxx.config(height=20)
        # set column headings
        for col in cols:
            self.listBoxxx.heading(col, text=col)
        sabt = Button(self.tahvilPageRoot, text="تحویل", bg='#A2DDA5', font=('IRANYekan', '18'), command=ALLPages.choosenToDelivery)
        sabt.config(height=1, width=20)
        if internetConnectionFlag:
            r = requests.get('https://shali-firstsite.fandogh.cloud/api/keshavarz/list/')
            for i in range(0, len(r.json())):
                if r.json()[i]['berenj']:
                    self.listBoxxx.insert("", "end", values=(str(r.json()[i]['berenj']['vazn_ezafe']),
                                                        str(r.json()[i]['berenj']['vazn_nimdane']),
                                                        str(r.json()[i]['berenj']['tedad_kise_saboos']),
                                                        str(r.json()[i]['berenj']['vazn_kise_berenj']),
                                                        str(r.json()[i]['berenj']['tedad_kise_berenj']),
                                                        str(r.json()[i]['code']),
                                                        str(r.json()[i]['berenj']['saat']),
                                                        str(r.json()[i]['berenj']['tarikh'])))
        else:
            print("NOOO")
        space.pack()
        title.pack()
        space1.pack()
        self.listBoxxx.pack()
        space2.pack()
        sabt.pack()
        space3.pack()

    def choosenToDelivery(self):
        self.listBoxxx.bind('<Button-1>', self.choosenToDelivery)
        curItem = self.listBoxxx.focus()
        k = self.listBoxxx.item(curItem)
        try:
            url = 'https://shali-firstsite.fandogh.cloud/api/keshavarz/'+str(k['values'][5])+'/'
        except:
            messagebox.showinfo('عدم انتخاب', 'برنجی جهت تحویل انتخاب نشده است')
            self.tahvilPageRoot.destroy()
            self.tahvilPage()
            return
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        self.choosenToDeliveryPageRoot = Tk()
        self.choosenToDeliveryPageRoot.configure(bg='#E3F0EB')
        self.choosenToDeliveryPageRoot.title("تحویل")
        title = Label(self.choosenToDeliveryPageRoot, text="تحویل", font=('IRANYekan', '22'), bg='#E3F0EB')
        space = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space1 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space2 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space3 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space4 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space5 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space6 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        space7 = Label(self.choosenToDeliveryPageRoot, text=" ", bg='#E3F0EB')
        if internetConnectionFlag:
            r = requests.get(url)
            farmerInfo = Label(self.choosenToDeliveryPageRoot, bg='#4C967D', fg='white', text="   کد کشاورز: " + str(k['values'][5]) + "   نام کشاورز: " + str(r.json()['nam']) + "   تلفن: " + str(r.json()['telefon']),
                               font=('IRANYekan', '16'),borderwidth=2, relief="groove")
        else:
            print("NOO")
        cols = ('تلفن' ,'راننده','وزن شالی' , 'تعداد کیسه' ,'نوع شالی','نام کشاورز', 'کد شالی', 'ساعت', 'تاریخ')
        listBoxxxx = ttk.Treeview(self.choosenToDeliveryPageRoot, columns=cols, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=listBoxxxx.yview)
        listBoxxxx.configure(yscrollcommand=vsb.set)
        listBoxxxx.column("0", width=150, anchor="c")
        listBoxxxx.column("1", width=150, anchor="c")
        listBoxxxx.column("2", width=150, anchor="c")
        listBoxxxx.column("3", width=150, anchor="c")
        listBoxxxx.column("4", width=150, anchor="c")
        listBoxxxx.column("5", width=150, anchor="c")
        listBoxxxx.column("6", width=150, anchor="c")
        listBoxxxx.column("7", width=150, anchor="c")
        listBoxxxx.column("8", width=150, anchor="c")
        listBoxxxx.config(height=3)
        for col in cols:
            listBoxxxx.heading(col, text=col)
        if internetConnectionFlag:
            r2 = requests.get(url)
            if len(r2.json()['shaliha']) != 0:
                for j in range(0, len(r2.json()['shaliha'])):
                    listBoxxxx.insert("", "end", values=(r2.json()['telefon'],
                                                           r2.json()['ranande'],
                                                           str(r2.json()['shaliha'][j]['vazn_shali']),
                                                           str(r2.json()['shaliha'][j]['tedad_shali']),
                                                           r2.json()['shaliha'][j]['noe_shali'],
                                                           r2.json()['nam'],
                                                           r2.json()['shaliha'][j]['id'],
                                                           r2.json()['shaliha'][j]['saat'],
                                                           r2.json()['shaliha'][j]['tarikh']))
        else:
            print("NOOO")
        farmerInfosub = Label(self.choosenToDeliveryPageRoot, text="اطلاعات شالی ها", font=('IRANYekan', '12'), bg='#E3F0EB')
        berenjInfosub = Label(self.choosenToDeliveryPageRoot, text="اطلاعات برنج", font=('IRANYekan', '12'), bg='#E3F0EB')
        deliveryInfosub = Label(self.choosenToDeliveryPageRoot, text="اطلاعات تحویل", font=('IRANYekan', '12'), bg='#E3F0EB')
        if internetConnectionFlag:
            r3 = requests.get(url)

            shali1 = Label(self.choosenToDeliveryPageRoot,bg='#E3F0EB', text= "   تاریخ: "+str(r3.json()['berenj']['tarikh'])
                                                   +"   ساعت: "+str(r3.json()['berenj']['saat'])
                                                   +"   تعداد کیسه برنج: "+str(r3.json()['berenj']['tedad_kise_berenj'])
                                                   +"   وزن کیسه برنج: "+str(r3.json()['berenj']['vazn_kise_berenj'])
                                                   +"   تعداد کیسه سبوس: "+str(r3.json()['berenj']['tedad_kise_saboos']), font=('IRANYekan', '15'))
            shali2 = Label(self.choosenToDeliveryPageRoot,bg='#E3F0EB', text="   وزن نیم دانه:"+str(r3.json()['berenj']['vazn_nimdane'])
                                                   +"   وزن اضافه: "+str(r3.json()['berenj']['vazn_ezafe'])
                                                   +"   کل: "+str(r3.json()['berenj']['vazn_kol'])
                                                   +"   کارمزد: "+str(r3.json()['berenj']['karmozd'])
                                                   +"   مکان برنج: "+str(r3.json()['berenj']['makan_berenj']), font=('IRANYekan', '15'))
            self.berenjnumForSabtNewTahvil = r3.json()['berenj']['id']
        else:
            print("NOOO")
        cols2 = ('وزن نیمدانه', 'وزن اضافه', 'تعداد کیسه سبوس', 'تعداد کیسه برنج', 'کد برنج', 'ساعت', 'تاریخ')
        self.listBoxxxx2 = ttk.Treeview(self.choosenToDeliveryPageRoot, columns=cols2, show='headings')
        vsb = ttk.Scrollbar(orient="vertical", command=self.listBoxxxx2.yview)
        self.listBoxxxx2.configure(yscrollcommand=vsb.set)
        self.listBoxxxx2.column("0", width=150, anchor="c")
        self.listBoxxxx2.column("1", width=150, anchor="c")
        self.listBoxxxx2.column("2", width=150, anchor="c")
        self.listBoxxxx2.column("3", width=150, anchor="c")
        self.listBoxxxx2.column("4", width=150, anchor="c")
        self.listBoxxxx2.column("5", width=150, anchor="c")
        self.listBoxxxx2.column("6", width=150, anchor="c")
        self.listBoxxxx2.config(height=3)
        # set column headings
        for col in cols2:
            self.listBoxxxx2.heading(col, text=col)
        if internetConnectionFlag:
            r = requests.get(url)
            if r.json()['berenj']:
                if r.json()['berenj']['tahvilha'] :
                    for j in range(0, len(r.json()['berenj']['tahvilha'])):
                        self.listBoxxxx2.insert("", "end", values=(
                            str(r.json()['berenj']['tahvilha'][j]['vazn_nimdane']),
                            str(r.json()['berenj']['tahvilha'][j]['vazn_ezafe']),
                            str(r.json()['berenj']['tahvilha'][j]['tedad_kise_saboos']),
                            str(r.json()['berenj']['tahvilha'][j]['tedad_kise_berenj']),
                            str(r.json()['berenj']['id']),
                            str(r.json()['berenj']['tahvilha'][j]['saat']),
                            str(r.json()['berenj']['tahvilha'][j]['tarikh'])
                        ))
        else:
            print("NOOOO")
        self.numberrr = Entry(self.choosenToDeliveryPageRoot, width=70, justify='right', font=('IRANYekan', 12))
        self.numberrr.insert(0, "تعداد کیسه برنج")
        self.numSabusrr = Entry(self.choosenToDeliveryPageRoot, width=70, justify='right', font=('IRANYekan', 12))
        self.numSabusrr.insert(0, "تعداد کیسه سبوس")
        self.extrarr = Entry(self.choosenToDeliveryPageRoot, width=70, justify='right', font=('IRANYekan', 12))
        self.extrarr.insert(0, "وزن اضافه برنج")
        self.halfrr = Entry(self.choosenToDeliveryPageRoot, width=70, justify='right', font=('IRANYekan', 12))
        self.halfrr.insert(0, "وزن نیم دانه")
        sabt = Button(self.choosenToDeliveryPageRoot, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '15'), command=self.sabtTahvil)
        sabt.config(height=1, width=20)
        # space.pack()
        title.pack()
        # space1.pack()
        farmerInfo.pack()
        space2.pack()
        listBoxxxx.pack()
        farmerInfosub.pack()
        # space3.pack()
        shali1.pack()
        shali2.pack()
        berenjInfosub.pack()
        # space4.pack()
        self.listBoxxxx2.pack()
        deliveryInfosub.pack()
        # space5.pack()
        self.numberrr.pack()
        self.numSabusrr.pack()
        self.extrarr.pack()
        self.halfrr.pack()
        space6.pack()
        sabt.pack()
        space7.pack()

    def sabtTahvil(self):
        try:
            urllib.request.urlopen('http://google.com')
            internetConnectionFlag = True
        except:
            internetConnectionFlag = False
        try:
            tedad_kise_berenj = int(self.numberrr.get())
        except:
            messagebox.showinfo('داده نامعتبر','.تعداد کیسه های برنج را به درستی وارد کنید .توجه کنید که داده باید عدد و مقدار باید کمتر و یا مساوی برنج موجود باشد')
            self.choosenToDeliveryPageRoot.destroy()
            self.choosenToDelivery()
            return
        try:
            tedad_kise_sabus = int(self.numSabusrr.get())
        except:
            messagebox.showinfo('داده نامعتبر','.تعداد کیسه های سبوس را به درستی وارد کنید .توجه کنید که داده باید عدد و مقدار باید کمتر و یا مساوی برنج موجود باشد')
            self.choosenToDeliveryPageRoot.destroy()
            self.choosenToDelivery()
            return
        try:
            vazn_ezafe = int(self.extrarr.get())
        except:
            messagebox.showinfo('داده نامعتبر','.وزن اضافه را به درستی وارد کنید .توجه کنید که داده باید عدد و مقدار باید کمتر و یا مساوی برنج موجود باشد')
            self.choosenToDeliveryPageRoot.destroy()
            self.choosenToDelivery()
            return
        try:
            vazn_nimdane = int(self.halfrr.get())
        except:
            messagebox.showinfo('داده نامعتبر','.وزن اضافه را به درستی وارد کنید .توجه کنید که داده باید عدد و مقدار باید کمتر و یا مساوی برنج موجود باشد')
            self.choosenToDeliveryPageRoot.destroy()
            self.choosenToDelivery()
            return
        nam_ijad_konande = str(NameOfUser)
        berenj = int(self.berenjnumForSabtNewTahvil)
        if internetConnectionFlag:
            url = 'https://shali-firstsite.fandogh.cloud/api/tahvil/new/'
            r = requests.post(url, data={'berenj': berenj,
                                     'tedad_kise_berenj': tedad_kise_berenj,
                                     'tedad_kise_saboos': tedad_kise_sabus,
                                     'vazn_ezafe': vazn_ezafe,
                                     'vazn_nimdane': vazn_nimdane,
                                     'nam_ijad_konande':nam_ijad_konande})
            print(r.text)
            print(r.status_code)
        else:
            print("NOOO")
        self.choosenToDeliveryPageRoot.destroy()
        self.choosenToDelivery()

ALLPages = all()

def amarVaGozareshatPage():
    amarVaGozareshatPageRoot = Tk()
    amarVaGozareshatPageRoot.title("آمار و گزارشات")

def menu():
    addToNames = name2.get()
    myname2 = addToNames
    myname1 = name.get()
    isItInThere = False
    for i in valuelistForNamesOfComboBox:
        if i==addToNames:
            isItInThere = True
            break
        else:
            isItInThere = False
    if not isItInThere:
        valuelistForNamesOfComboBox.append(addToNames)
    with open('listfile.txt', 'w', encoding="utf-8") as filehandle:
        for listitem in valuelistForNamesOfComboBox:
            if listitem!="" and listitem!= "  نام و نام خانوادگی":
                filehandle.write('%s\n' % listitem)
    root.destroy()
    Menu = Tk()
    Menu.configure(bg='#E3F0EB')
    #Menu['background'] = '#E3F0EB'
    Menu.state('zoomed')
    Menu.title("مدریت شالی ها")
    space = Label(Menu, text=" ", bg='#E3F0EB')
    space1 = Label(Menu, text=" ", bg='#E3F0EB')
    space2 = Label(Menu, text=" ", bg='#E3F0EB')
    space3 = Label(Menu, text=" ", bg='#E3F0EB')
    space4 = Label(Menu, text=" ", bg='#E3F0EB')
    title = Label(Menu, text="مدریت شالی ها", font=('IRANYekan', '22'), bg='#E3F0EB')
    sabteShali = Button(Menu, text="ثبت شالی", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.sabteShaliPage)
    sabtShodeHa = Button(Menu, text="ثبت شده ها", bg='#4C967D', font=('IRANYekan', '20'), fg='white', command=ALLPages.sabtShodeHaPage)
    sabteBerenj = Button(Menu, text="ثبت برنج", bg='#A2DDA5', font=('IRANYekan', '20'), command=ALLPages.sabteBerenjPage)
    tahvil = Button(Menu, text="تحویل", bg='#4C967D', font=('IRANYekan', '20'), fg='white', command=ALLPages.tahvilPage)
    # amarVaGozareshat = Button(Menu, text="آمار و گزارشات", bg='#BC01FE', font=('IRANYekan', '20'), command=amarVaGozareshatPage)
    sabteShali.config(height=2, width=80)
    sabtShodeHa.config(height=2, width=80)
    sabteBerenj.config(height=2, width=80)
    tahvil.config(height=2, width=80)
    # amarVaGozareshat.config(height=4, width=80)
    space1.pack()
    title.pack()
    space.pack()
    sabteShali.pack()
    space2.pack()
    sabtShodeHa.pack()
    space3.pack()
    sabteBerenj.pack()
    space4.pack()
    tahvil.pack()
    space.pack()
    # amarVaGozareshat.pack()
    if myname1 != "  نام و نام خانوادگی" or myname1 != " ":
        global NameOfUser
        NameOfUser = myname1
    else:
        NameOfUser = myname2
    try:
        urllib.request.urlopen('http://google.com')
        internetConnectionFlag = True
    except:
        internetConnectionFlag = False
    print(internetConnectionFlag)
    if internetConnectionFlag:
        messagebox.showinfo("اتصال اینترنت", ".اینترنت شما متصل است")
    else:
        messagebox.showinfo("اتصال اینترنت", ".اینترنت شما متصل نیست")

space = Label(root, text=" ", bg='#E3F0EB')
space1 = Label(root, text=" ", bg='#E3F0EB')
space2 = Label(root, text=" ", bg='#E3F0EB')
space3 = Label(root, text=" ", bg='#E3F0EB')
space4 = Label(root, text=" ", bg='#E3F0EB')
title = Label(root, text=".سلام، خوش آمدید", font=('IRANYekan', '22'), bg='#E3F0EB')
title1 = Label(root, text="لطفاً نام و نام خانوادگی خود را در صورت موجود بودن در لیست انتخاب کنید", font=('IRANYekan', '20'), bg='#E3F0EB')
title3 = Label(root, text=".و در غیر این صورت نام و نام خانوادگی خود را وارد کنید", font=('IRANYekan', '20'), bg='#E3F0EB')

name2 = Entry(root, width=62, justify='right', font=('IRANYekan', 12))
name2.insert(0, "نام و نام خانوادگی")
name = ttk.Combobox(root, width=60, justify='right', font=('IRANYekan', 12))
valuelistForNamesOfComboBox.clear()

with open('listfile.txt', 'r', encoding="utf-8") as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        if currentPlace!="" and currentPlace!= "نام و نام خانوادگی":
            valuelistForNamesOfComboBox.append(currentPlace)

name['values'] = valuelistForNamesOfComboBox
name.insert(0, "  نام و نام خانوادگی")

sabtname = Button(root, text="ثبت", bg='#A2DDA5', font=('IRANYekan', '20'), command=menu)
sabtname.config(height=1, width=20)
space.pack()
title.pack()
space1.pack()
title1.pack()
title3.pack()
space4.pack()
name2.pack()
name.pack()
space2.pack()
sabtname.pack()
space3.pack()

# MakePDF('ardavanxxx.pdf', 'نام و نام خانوادگی', ['نام و نام خانوادگی'])

root.mainloop()