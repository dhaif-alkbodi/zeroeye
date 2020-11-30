#------------#
#!/usr/bin/python
# encoding: utf-8
#------------#
"""
  ᴏʟᴅᴠᴇʀꜱɪᴏɴ ꜰʀᴏᴍ 2018 ᴀɴᴅ ᴛʜɪꜱ ᴜᴘᴅᴀᴛᴇ ꜰʀᴏᴍ 2019 ᴀɴᴅ ʀᴇʟᴇᴀꜱᴇ ᴏɴ ɴᴏᴠ 2020 (ɴɪᴄᴇ)
  ᴄʜᴇᴄᴋ ᴍʏ ʟɪɴᴋꜱ : 
  ᴡʜᴀᴛꜱ ɴᴇᴡ ?
   +ɴᴇᴡ ᴀʟɢᴏʀɪᴛʜᴍᴇꜱ
   +ᴇᴀꜱʏ ᴛᴏ ᴍᴀᴋᴇ ᴀɴʏ ɢᴇɴᴇʀᴀᴛᴏʀ 
   +ɢᴇɴᴇʀᴀᴛᴇ ᴀɴʏᴛʜɪɴɢ 
   +ᴠᴀʟɪᴅ ꜰᴏʀᴍᴀᴛꜱ
   +ᴋᴇʏ ɪᴅᴇɴᴛɪꜰʏ+ɢʀᴀʙʙᴇʀ          
 __   __    _   ____    _____ _   _ 
|  \ /  | /  | |  _ \  (_   _) \ | |
|   v   |/ o |_| |_) )  _| | |  \| |
| |\_/| /__   _)  __/ |/ / | |     |
| |   | |  | | | |  |   <| | | |\  |
|_|   |_|  |_| |_|  |_|\_\_| |_| \_| -2020 
                                    
"""
#------------#
import random,string,platform,webbrowser,re,os,time,getpass,sys,os.path
from random import *
import colorama # if u face a problem here type "pip install colorama"
from colorama import *
#------------#
configs=[]
keyz=[]
xnumx=0
#------------#
init()
la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
starend = '\033[24m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
print(blid)
#------------#
def clear():
      if os.name=='nt':
          os.system('cls && title [NEW] ZER0EYE - FULL KEY GENERAT0R BY M4rktn ')
      else :
          os.system('clear')
#------------#
def strounga(x,y):
   omri=la7mar+"["+lasfar+str(x)+la7mar+"] "+lasfar+y
   return omri
#------------#
logo=choice(["""{w}
   ^     . .     ^  
   \ \    V    / /  
   \   \(+ +)/   / {r}({y}Instagram{r}){rr}~~~~~~~~~{r}({y}@cyber.tn{r}){w} 
   \   (  v  )   / {r}({y}Telegram{r}){rr}~~~~~~~~~~{r}({y}@m4rktn{r}){w}
    \____m_m____/   {r}({y}linktr.ee{r}/{y}m4rktn{r}){rr}~~{r}({y}2020{r}){w}
   <[___________]>

""".format(r=la7mar,y=lasfar,rr=ramadi,w=labyadh),
"""                                                   {y}                                                      
d88888P  d8888b  88bd88b d8888b  d8888b?88   d8P  d8888b
   d8P' d8b_,dP  88P'  `d8P' ?88d8b_,dPd88   88  d8b_,dP
 d8P'   88b     d88     88b  d8888b    ?8(  d88  88b    
d88888P'`?888P'd88'     `?8888P'`?888P'`?88P'?8b `?888P'
                                              )88       
                                             ,d8P       
                                          `?888P'       
{rr}*{r} Instagam     {rr}:{y}@cyber.tn
{rr}*{r} Telegram     {rr}:{y}@z4cktn
{rr}*{r} All My Links {rr}:{y}linktr.ee{rr}/{y}m4rktn
{rr}*{r} Last Update  {rr}:{y}Nov{rr}/{y}2020


""".format(r=la7mar,y=lasfar,rr=ramadi,w=labyadh),
"""                                                   {y} 
  /$$$$$$                               
 /$$$_  $$                              
| $$$$\ $$  /$$$$$$  /$$   /$$  /$$$$$$ 
| $$ $$ $$ /$$__  $$| $$  | $$ /$$__  $$
| $$\ $$$$| $$$$$$$$| $$  | $$| $$$$$$$$
| $$ \ $$$| $$_____/| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$
 \______/  \_______/ \____  $$ \_______/
                     /$$  | $$          
                    |  $$$$$$/          
                     \______/           

{rr}\\_{r}Instagam{rr}>{y}@cyber.tn
{rr}\\_{r}Telegram{rr}>{y}@z4cktn
{rr}\\_{r}All-My-Links{rr}>{y}linktr.ee{rr}/{y}m4rktn
{rr}\\_{r}Last-Update{rr}:{y}Nov{rr}/{y}2020


""".format(r=la7mar,y=lasfar,rr=ramadi,w=labyadh)

])
#------------#
#Bank Names#
AmExlis=['AmEx','AmEx Small CorporateCard1','AmEx Small CorporateCard2']
DinersClublis=['DinersClub 1','DinersClub 2','DinersClub 3','DinersClub 4']
CarteBlanchelis=['CarteBlanche']
JCBlis=['JCB(JapaneseCreditBureau)']
Visalis=['Visa','Debit Banca MonteDeiPaschiDiSiena(Italy)','Banca MonteDeiPaschiDiSiena(Italy)','Gold Bank of America','CV/Gold Bank of America','PV Bank of America','CV Wells Fargo','CV','Wells Fargo','Citibank','Bank of America','ElectronPrepaidPosteItaliane(Italy)','Bank of America2','Rockwell Federal CreditUnion','House hold Bank','First Cincinnati','Associates National Bank','Security Pacific','Colonial NationalBank','A.M.C.Federal Credit Union','Valley National Bank','Chemical Bank','Pennsylvania State Employees Credit Union','CV Signet Bank','Union Trust','Marine Midland','CV Citibank','CVCitibank','StateStreetBank','Chase Manhattan Bank','Chase Manhattan Bank','Chase Lincoln FirstC lassic','Chase Lincoln First Classic','Corestates','National Westminster Bank','First Chicago Bank','Consumers Edge','Premiercard Security First','Security First','PV Citibank','Citibank/Citicorp','MonogramBank','H.H.B.C.','First National Bank of Louisville','Gold Dome','First Atlanta','First American Bank','Primerica Bank','N.C.M.B./NationsBank','National Bank of Delaware','National West','BankOne','First Signature Bank & Trust','Gary Wheaton Bank','Firstier Bank Lincoln','Bank of Omaha','Indiana National Bank','Security Pacific National Bank','Bank of Hoven','Security Bank & Trust','MerrilLynch Bank & Trust','Ameri Trust','Premiercard','Empire Affiliates Federal Credit Union','Republic Savings','C.I.B.C.','Canadian Imperial Bank','Belgium A.S.L.K.','Royal Bank of Canada','Toronto Dominion of Canada','Bank of NovaScotia','Bank of NovaScotia2','Barclays(UK)','First Direct','T.S.B.Bank','Citibank','Bank of Queensland','FirstCard','Home Federal','Tompkins County Trust','IBM Credit Union','Rocky Mountain','First Security','WestBank','CV WellsFargo','AT&Ts UniversalCard','AT&Ts UniversalCard','M.B.N.A.North America','Bank of Hawaii','Macom Federal Credit Union','IBM MidAmerica Federal Credit Union','U.S.Bank','Security Pacific Washington','Village Bank of Chicago','HongKong NationalBank','CV BarclayCard(UK)','BancodiNapoli(Italy)','BNL(Italy)','Carta Moneta CARIPLO/Intesa(Italy)','Credito Italiano(Italy)','Gold bank ganaderoBBV(Colombia)','MBNABank']
MasterCardlis=['MasterCard','Maryland of NorthAmerica','South western States Bank ard Association','Universal Travel Voucher','Western States Bank ard Association','Eurocard France','Mountain States Bank ard Association','Credit Systems Inc.','Westpac Banking Corporation','Midamerica Bank ard Association','First Bank Card Center','ComputerCommunications of  America','Bank of Montreal','Mellon Bank N.A.','CentralTrustCompany N.A.','Security Pacific National Bank','Promociony Operacion S.A.','Banco Nacionaldo Mexico','NewEngland Bank ard Association','Million Card Service Co.Ltd.','The Citizens & Southern National Bank','Kokunai Shinpan CompanyLtd.','Chemical BankDelaware','F.C.C.National Bank','The Bank card Association Inc.','Marine Midland Bank N.A.','Old Kent Bank & Trust Co.','Union Trust','Citibank / Citicorp','Central Finance Co.Ltd.','SovranBank / CentralSouth','Standard Bank of SouthAfrica Ltd.','Security Bank & TrustCompany','Trust escnoor National Bank','Midland Bank','First Pennsylvania BankN.A.','Eurocard Ab','Rocky Mountain Bankcard System Inc.','FirstUnionNationalBankofNorthCarolina','Sunwest Bank of Albuquerque N.A.','Harris Trust & Savings Bank','Badische Beamten bank EG','Eurocard Deutschland','Computer Systems Association Inc.','Citibank Arizona','Financial Transaction System Inc.','First Tennessee Bank N.A.','Bank of America','MasterCard (canbeGold) - Bank of America','Home Federal','Signet Bank','Maryland of NorthAmerica','MasterCard Prepaid - PayPal / Lottomaticard (Italy)','Wells Fargo','Wells Fargo','Bank of Hoven','Citibank / Citicorp II','BNL / BNPParibas(Italy)','National Westminster Bank','Chase Manhattan','Bancodi Sardegna (Italy)','Bancolombia Cadenalco (Colombia)','BancodeOccidente (Colombia)','Granahorrar(Colombia)','Granahorrar(Colombia)']
Maestrolis=['BNL/BNPParibas (Italy)']
Discoverlis=['Discover','MBNABank']
#Bins#
Amexbinz=['37','3782','3787']
DinersClubbinz=['30','31','35','36','38']
CarteBlanchebinz=['35']
JCBbinz=['35']
Visabinz=['4', '400314', '400315', '40240238', '4019', '4024', '4040', '4048', '40240071', '4013', '4019', '402360', '4024', '4027', '4032', '4052', '4060', '4070', '4071', '4094', '4113', '4114', '4121', '4121', '4122', '4125', '4128', '4131', '4225', '4226', '4231', '4232', '4239', '4241', '4250', '4253', '42545123', '4254', '4271382', '4271', '4301', '4302', '4311', '4317', '4327', '4332', '4339', '4342', '4356', '4368', '4387', '4388', '4401', '4413', '4418', '4421', '4424', '4428', '4436', '4443', '4447', '4448020', '4452', '4498', '4502', '4503', '4506', '4510', '4520', '4537', '4538', '4539', '4543', '4544', '4556', '4564', '4673', '4678', '4707', '47121250', '4719', '4721', '4722', '4726', '4783', '4784', '4800', '4811', '4819', '4820', '4833', '4842', '4897', '4921', '4929', '45399710', '4557', '4908', '4532', '45475900', '4916']
MasterCardbinz=['5','5031', '5100', '5110', '5120', '5130', '5140', '5150', '5160', '5170', '5172', '518', '519', '5201', '5202', '5204', '5205', '5206', '5207', '5208', '5209', '5210', '5211', '5212', '5213', '5215', '5216', '5217', '5218', '5219', '5220', '5221', '5222', '5223', '5224', '5225', '5226', '5227', '5228', '5229', '5230', '5231', '5232', '5233', '5234', '5235', '5236', '5254', '5273', '5286', '5291', '5329', '533875', '5410', '5412', '5419', '5424', '543013', '5434', '5465', '52550114', '530693', '5406251', '5426', '5406']
Maestrobinz=['581149']
Discoverbinz=['60','6013']
#------------#
#CC Generator v1 by m4rk
class ccSama(object):
    def __init__(self):
        global aaa
        clear()
        self.logon()
        carder=input("%s%sD0ll4r%s%s$%s %s"%(ramadi,star,hell,starend,saker,lazra9))
        if carder in ['01','1']:
         Sa7by=input(" %s[%s$%s] Enter Bin [exemple:491628] %s"%(la7mar,lasfar,la7mar,lazra9));aaa='99'
         while Sa7by.isdigit()!=1 or len(str(Sa7by))==0:
          Sa7by=input("  %s[%s$%s] Enter Bin [exemple:491628] %s"%(la7mar,lasfar,la7mar,lazra9))
         self.gen1(Sa7by)
        elif carder in ['02','2']:
         self.gen2()
        elif carder =='69':
         z4ck()
    def sss(self ,lis,binlis):
      global aaa
      for x,y in enumerate(lis):
        print("%s[%s] %s%s"%(la7mar,x+1,lasfar,y))
      aaa=int(input("%s%sD0ll4r%s%s$%s %s"%(ramadi,star,hell,starend,saker,lazra9)))
      plasty=binlis[int(float(aaa-1))]
      self.gen1(plasty);

    def gen2(self):
      print("""{y}
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$ {r}({b}01{r}){y} American Express       $$
  $$ {r}({b}02{r}){y} Diners Club            $$
  $$ {r}({b}03{r}){y} Visa                   $$
  $$ {r}({b}04{r}){y} MasterCard             $$
  $$ {r}({b}05{r}){y} Discover               $$
  $$ {r}({b}06{r}){y} Maestro                $$
  $$ {r}({b}07{r}){y} CarteBlanche           $$
  $$ {r}({b}08{r}){y} Japanese Credit Bureau $$
  $$ {r}({b}69{r}){y} Back                   $$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  """.format(y=lasfar,r=la7mar,b=lazra9))
      card777=input("%s%sD0ll4r%s%s$%s %s"%(ramadi,star,hell,starend,saker,lazra9))
      if card777 in['01','1']:
        self.sss(AmExlis,Amexbinz)
      elif card777 in['02','2']:
        self.sss(DinersClublis,DinersClubbinz)
      elif card777 in['03','3']:
        self.sss(Visalis,Visabinz)
      elif card777 in['04','4']:
        self.sss(MasterCardlis,MasterCardbinz)
      elif card777 in['05','5']:
        self.sss(Discoverlis,Discoverbinz)
      elif card777 in['06','6']:
        self.sss(Maestrolis,Maestrobinz)
      elif card777 in['07','7']:
        self.sss(CarteBlanchelis,CarteBlanchebinz)
      elif card777 in['08','8']:
        self.sss(JCBlis,JCBbinz)
      elif card777 =='69':
        ccSama()
    def logon(self):
      print("""%s%s
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$ %sccSama - CreditCard Generator%s $$
  $$  £  %sI Feel Like milionair%s  £  $$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$ %s[01]%s Generate With Single Bin %s$$
  $$ %s[02]%s Search & Gen Bin From DB %s$$
  $$ %s[69]%s Back                     %s$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""%(blid,lasfar,lazra9,lasfar,lazra9,lasfar,la7mar,lazra9,lasfar,la7mar,lazra9,lasfar,la7mar,lazra9,lasfar))
    def gen1(self ,Sa7by):#Sa7by Kol Chy Wadha7 W jawna Bahy Brcha xDD...
      if Sa7by !=0:
      #Some Tries
       if aaa in ['02','2','07','7']:
        sensei=12-len(str(Sa7by))
       elif aaa in ['01','1']:
        sensei=13-len(str(Sa7by))
       else:
        sensei=16-len(str(Sa7by))
      binn3r=Sa7by+'x'*sensei
      if aaa!='99':
       print(" %s[%s$%s] Bin %s : %s"%(la7mar,lasfar,la7mar,lazra9,binn3r))
      yearb=input(" %s[%s$%s] Enter Year [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      if len(str(yearb))!=0:
        while yearb.isdigit()!=1 or int(yearb) not in range(2018,2025):
          yearb=input("  %s[%s$%s] Enter Year [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      mounthb=input(" %s[%s$%s] Enter Month [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      if len(str(mounthb))!=0:
        while int(mounthb) not in range(1,31):
          mounthb=input("  %s[%s$%s] Enter Month [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      cvvb=input(" %s[%s$%s] Enter CVV [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      if len(str(cvvb))!=0:
        while cvvb.isdigit()!=1 or len(str(cvvb))!=3:
          cvvb=input("  %s[%s$%s] Enter CVV [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      mouchi=int(input(" %s[%s$%s] How Much ?? %s"%(la7mar,lasfar,la7mar,lazra9)))
      print("%s+%s--------------------------%s+"%(lazra9,la7mar,lazra9))
      with open('zeroeye-results/ccgenerated.txt','a') as escnoor:
        escnoor.write('\n~~ Bin:%s | %s cc ~~ (By ESCAN0R) \n'%(binn3r,mouchi))
      for ii in range(mouchi):
        senpaion = string.digits
        senpai= ''.join(choice(senpaion) for _ in range(sensei))
        yearbn1 = yearb
        mounthbn1 = mounthb
        cvvbn1 = cvvb
        if len(str(mounthb))==0:
          mounthbn = randrange(1,31,1)
          mounthbn1 = mounthbn
          if int(mounthbn1) <= 9:
            mounthbn1 = str('0'+str(mounthbn1))
        if len(str(yearb))==0:
          yearbn = randrange(2020,2030,1)
          yearbn1 = yearbn
        if len(str(cvvb))==0:
          cvvbn = ''.join(choice(string.digits) for _ in range(3))
          cvvbn1 = cvvbn
        sama = ("%s%s|%s|%s|%s"%(Sa7by,senpai,yearbn1,mounthbn1,cvvbn1))
        print(la7mar+sama)
        with open('zeroeye-results/ccgenerated.txt','a') as escnoor:
          escnoor.write(sama+'\n')
      print("%s+%s--------------------------%s+"%(la7mar,lasfar,la7mar))
      print(" %s[%s%s Saved In 'zeroeye-results/ccgenerated.txt'%s]%s"%(la7mar,lasfar,mouchi,la7mar,labyadh))
      so=input("%sContinue %s? %s[%sY%s/%sN%s(%syes%s/%sNo%s)] %s>%s "%(lasfar,ramadi,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,ramadi,labyadh))
      if so.upper() in ['Y','YES','AY']:
            z4ck()
      else:
            exit()
#------------#
#proxy
class ghrab(object):
    def __init__(self):
        clear()
        StartIP = input('%s[%s+%s] Start IP: %s'%(la7mar,lasfar,la7mar,labyadh))
        while not re.match('[0-9]{0,3}\d.[0-9]{0,3}\d.[0-9]{0,3}\d.[0-9]{0,3}\d',StartIP):
          StartIP = input('%s[%s+%s] Start IP: %s'%(la7mar,lasfar,la7mar,labyadh))
        ENDIP = input('%s[%s+%s] End IP: %s'%(la7mar,lasfar,la7mar,labyadh))
        while not re.match('[0-9]{0,3}\d.[0-9]{0,3}\d.[0-9]{0,3}\d.[0-9]{0,3}\d',ENDIP):
          ENDIP = input('%s[%s+%s] End IP: %s'%(la7mar,lasfar,la7mar,labyadh))
        PRoxYPort = input('%s[%s+%s] Enter Proxy port [8080,80]: %s'%(la7mar,lasfar,la7mar,labyadh))
        while not re.match('[0-9]{1,5}\d',PRoxYPort):
          PRoxYPort = input('%s[%s+%s] Enter Proxy port [8080,80]: %s'%(la7mar,lasfar,la7mar,labyadh))
        ip_range = self.Generate_IP(StartIP, ENDIP)
        xXx=0
        for ip in ip_range:
            xXx=xXx+1
            with open('zeroeye-results/Ipgenerated.txt', 'a') as xX:
                xX.write(str(ip) + ':' + str(PRoxYPort) + '\n')
        print("%s[%s%s Ip Saved In 'zeroeye-results/Ipgenerated.txt'%s]%s"%(la7mar,lasfar,xXx,la7mar,labyadh))
        so=input("%sContinue %s? %s[%sY%s/%sN%s(%syes%s/%sNo%s)] %s>%s "%(lasfar,ramadi,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,ramadi,labyadh))
        if so.upper() in ['Y','YES','AY']:
            z4ck()
        else:
            exit()
    def Generate_IP(self, start_ip, end_ip):
        Start = list(map(int, start_ip.split(".")))
        end = list(map(int, end_ip.split(".")))
        rec = Start
        ip_range = []
        ip_range.append(start_ip)
        while rec != end:
            Start[3] += 1
            for i in (3, 2, 1):
                if rec[i] == 256:
                    rec[i] = 0
                    rec[i - 1] += 1
            ip_range.append(".".join(map(str, rec)))
        return ip_range
#------------#
class z4ck(object):
  global configs,xnumx
  def __init__(self):
      clear()
      print(logo)
      LLL=0
      for y,fz in enumerate(configs):
        print(strounga(str(y+1),fz['name']))
      print(strounga(xnumx+1,'CreditCard'))
      print(strounga(xnumx+2,'Phone Numbers'))
      print(strounga(xnumx+3,'Proxy'))
      print(strounga(xnumx+4,'Facebook AcessToken'))
      print(strounga(xnumx+5,'Create your own generator'))
      print(strounga(xnumx+6,'Delete a config'))
      print(strounga(xnumx+7,'About'))
      baka=input('\033[91m[\033[93mm4rktn>\033[91m]\033[00m ')
      while baka=='':
        baka=input('\033[91m[\033[93mm4rktn>\033[91m]\033[00m ')
      baka=int(baka)
      while baka <1 or baka >(xnumx+7):
         baka=int(input('\033[91m[\033[93mm4rktn>\033[91m]\033[00m '))
      if baka<=xnumx:
          ma=int(input('\033[91m[\033[93mHow Much\033[91m]\033[00m '))
          while ma <1:
           ma=int(input('\033[91m[\033[93mHow Much\033[91m]\033[00m '))
          for i in range(ma):
             conf=configs[baka-1]
             print(str(self.x1x(conf['format'])))
             with open('zeroeye-results/%s.txt'%(conf['name']),'a') as L:
               L.write('%s\n'%(self.x1x(conf['format'])))
          print(" %s[%s%s Key Saved In 'zeroeye-results/%s.txt' %s]%s"%(la7mar,lasfar,ma,conf['name'],la7mar,labyadh))
          so=input("%sContinue %s? %s[%sY%s/%sN%s(%syes%s/%sNo%s)] %s>%s "%(lasfar,ramadi,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,ramadi,labyadh))
          if so.upper() in ['Y','YES','AY']:
              z4ck()
          else:
              exit()
      elif baka==xnumx+1:
          ccSama()
      elif baka==xnumx+2:
          self.phnnm()
      elif baka==xnumx+3:
          ghrab()
      elif baka==xnumx+4:
          self.genetok()
      elif baka==xnumx+5:
          self.creat0r()
      elif baka==xnumx+6:
          self.delmyconf()
      elif baka==xnumx+7:
          self.seemydick()

# ! = number | ? = string | # = Random(string/int)
# +!??! ~> + Upper | without + ~> normal letters | *!??! ~> random(Upper/Lower)

#1,2,3 Go!
  def x1x_upMin(self,x,y):
   if x==0:return y.upper()
   elif x==1:return choice([y.lower(),y.upper()]) 
   elif x==2:return y.lower()
  # one key generator from format directly
  def x1x(self,x):
   x444=""
   if x.startswith('+'):ww=0;x=x.replace(x[0],'')
   elif x.startswith('*'):ww=1;x=x.replace(x[0],'')
   else:ww=2
   for ff in x: 
    if ff =='!':
      x444+=str(self.x1x_upMin(ww,''.join(choice(string.digits) for _ in range(1))))
    elif ff =='?':
      x444+=str(self.x1x_upMin(ww,''.join(choice(string.ascii_letters) for _ in range(1))))
    elif ff =='#':
      x444+=choice([str(self.x1x_upMin(ww,''.join(choice(string.digits) for _ in range(1)))),str(self.x1x_upMin(ww,''.join(choice(string.ascii_letters) for _ in range(1))))])
    else:x444+=ff
   return x444
  def phnnm(self):
    if not os.path.isdir('zeroeye-results/phonz'):
     os.mkdir('zeroeye-results/phonz')
    print("""
        Helper:
          +21669666999 : Tunisien Phone
          Country Code : +216
          length : 8
          Start With : 6 or 69 """) 
    iiiiii=input("%s[%s>%s] With Country Code ?? (y/n) %s"%(la7mar,lasfar,la7mar,labyadh))
    if iiiiii.upper() in ['Y','YES','AY','O','OUI']:
      intcd=input("%s[%s>%s] Country Code %s"%(la7mar,lasfar,la7mar,labyadh))
      while not intcd.startswith('+') or intcd.startswith('00') or len(intcd)>5:
        print("%s[%s>%s] WTF Bro ??"%(la7mar,lasfar,la7mar));intcd=input("%s[%s>%s] InterCode %s"%(la7mar,lasfar,la7mar,labyadh))
    else:
      intcd=""
    numbbbb=int(input("%s[%s>%s] length (without Country Code)%s"%(la7mar,lasfar,la7mar,labyadh)))
    startwitth=int(input("%s[%s>%s] Start With %s"%(la7mar,lasfar,la7mar,labyadh)))
    while len(str(startwitth))>numbbbb :
      startwitth=int(input("%s[%s>%s] Start With %s"%(la7mar,lasfar,la7mar,labyadh)))
    Hwmch=int(input("%s[%s>%s] How Much %s"%(la7mar,lasfar,la7mar,labyadh)))
    kifaaacg=numbbbb-len(str(startwitth))
    for i in range(Hwmch):
      bakas=str(intcd)+str(startwitth)+str(self.x1x('!'*kifaaacg))
      ousm='+'+self.x1x(bakas)
      print(ousm)
      with open('zeroeye-results/phonz/C0de_%s.txt'%(str(intcd)),'a') as L:
        L.write('%s\n'%ousm)
    print(" %s[%s%s number phone Saved In 'zeroeye-results/phonz/C0de_%s.txt'%s]%s"%(la7mar,lasfar,Hwmch,str(intcd),la7mar,labyadh))
    so=input("%sContinue %s? %s[%sY%s/%sN%s(%syes%s/%sNo%s)] %s>%s "%(lasfar,ramadi,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,ramadi,labyadh))
    if so.upper() in ['Y','YES','AY']:
           z4ck()
    else:
          exit()
#------------#
#fbtokengen
  def genetok(self):
   zz=input("%s[%s>%s] How Much %s"%(la7mar,lasfar,la7mar,labyadh))
   for az in range(int(zz)):
    escnoor= "EAAAAUaZA8"+''.join(choice(string.ascii_letters + string.digits) for _ in range(randrange(170,220)))
    print(escnoor)
    with open('zeroeye-results/tokens.txt','a') as ttt:
      ttt.write(str(escnoor)+'\n')
   print(" %s[%s%s Token Saved In 'zeroeye-results/tokens.txt'%s]%s"%(la7mar,lasfar,zz,la7mar,labyadh))
   so=input("%sContinue %s? %s[%sY%s/%sN%s(%syes%s/%sNo%s)] %s>%s "%(lasfar,ramadi,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,lasfar,la7mar,ramadi,labyadh))
   if so.upper() in ['Y','YES','AY']:
            z4ck()
   else:
          exit()
#------------#
#Key creator 
  def creat0r(self):
   namme=input('%s[%sName Of Config%s]%s '%(la7mar,lasfar,la7mar,labyadh))
   if len(configs):
    while namme in open('config.ini','r').read():
     namme=input('%s[%s %s Founded In Our Database %s]%s ... \n%s[%s Name Of Config%s]%s '%(la7mar,lasfar,namme,la7mar,labyadh,la7mar,lasfar,la7mar,labyadh));namme=namme.replace('\n','')
   Keyy=input('%s[%skey%s]%s '%(la7mar,lasfar,la7mar,labyadh))
   if not Keyy in open('config.ini','r').read():
     open('config.ini','a').write('\n%s::%s'%(namme,Keyy))
   else:input('%s[%s %s Founded In Our Database %s]%s ... %s[%sPRESS ENTER TO RETRY%s]%s '%(la7mar,lasfar,Keyy,la7mar,labyadh,la7mar,lasfar,la7mar,labyadh));z4ck()
   sys.exit("%s[%sPRESS ENTER AND REOPEN THIS TOOL%s]%s"%(la7mar,lasfar,la7mar,labyadh))
   clear()
  def delmyconf(self):
    global configs
    l=0
    print("""%s[%sFIND CONFIG.INI%s] """%(la7mar,lasfar,la7mar))
    try:
      l=len(configs)
    except:
      sys.exit(input('%s[%sCONFIG.INI NO FOUND !!%s]%s'%(la7mar,lasfar,la7mar,labyadh)))
    print("""%s[%sNUMBER CONFIGS%s]%s %s"""%(la7mar,lasfar,la7mar,labyadh,len(configs)))
    print("""%s[%sCONFIGS%s]"""%(la7mar,lasfar,la7mar))
    for f,i in enumerate(configs): 
      print("   %s[%s%s%s]%s %s"%(la7mar,lasfar,f+1,la7mar,labyadh,i['name']))
    baka=input("""%s[%sWHICH ONE YOU WANT TO DELETE%s]%s """%(la7mar,lasfar,la7mar,labyadh))
    del configs[(int(baka)-1)]
    open('config.ini','w').write('#Free Keys by @0xtn\n')
    for i in configs :
      open('config.ini','a').write('%s::%s\n'%(i['name'],i['format']))
  def seemydick(self):
   print("""{r}
     ({y}Name/Nickname{r}){rr}~~{r}({y}Zack{rr}/{y}M4rktn{r})
     ({y}Contact{r}){rr}~~~~~~~~{r}({y}https{rr}://{y}linktr.ee{rr}/{y}m4rktn{r})
     ({y}Version{r}){rr}~~~~~~~~{r}({y}2.0{r})
     ({y}Release{r}){rr}~~~~~~~~{r}({y}Nov-2020{r})
     {rr}*{y} We make Funny To you {rr}..{y} So Encourage us to make the best 
     {rr}*{y} This Tool Usefull for some checkers 
     {rr}*{y} No checker for Google Play  {rr}..{y} Sorry
     {rr}*{y} Dont Say this tool like a shit {rr}..{y} because you are the shit {rr};) 
     {rr}*{y} You should use vpn if you tried some keys and you take bans {rr}...""".format(r=la7mar,y=lasfar,rr=ramadi))
#------------#    
try:
  if not os.path.isdir('zeroeye-results'):
    os.mkdir('zeroeye-results')
  if not os.path.isfile('config.ini')or len(open('config.ini','r').read())<1:
      rep=input(""" You Dont Have Any Config ... You Want To create new generator?(Y/n)""").upper()
      open('config.ini','w').write('#ZeroEye\n')
      if rep in ['Y','YES']:creat0r()
      else:z4ck()
  else:
   for f in open('config.ini','r').read().splitlines():
    if '::' in f:
      fff={'name':f.split('::')[0],'format':f.split('::')[1]};configs.append(fff)
      xnumx+=1
   for i in "[/] You Have [%s] Configs ... Go !"%(xnumx):
          sys.stdout.write(i)
          sys.stdout.flush()
          time.sleep(0.1)
   z4ck()
except KeyboardInterrupt:
  pass