import psutil
from AppOpener import *
from fuzzywuzzy import fuzz
import os


Open_keywords = [
    "open",
    "launch",
    "start",
    "access",
    "run",
    "initiate",
    "begin",
    "commence",
    "show",
    "display"]
close_keywords = [
    "close",
    "exit",
    "terminate",
    "shutdown",
    "turnoff",
    "end",
    "quit",
    "stop",
    "off",
    "shut",
    "finish",
    "kill",
    "deactivate",
    "suspend",
    "cease",
    "halt",
    "abort",
]

stop_words = [
    "and",
    "but",
    "or",
    "nor",
    "for",
    "so",
    "yet",
    "as",
    "because",
    "although",
    "while",
    "if",
    "unless",
    "since",
    "when",
    "after",
    "before",
    "though",
    "whereas",
    "a",
    "an",
    "the"
]
close_dict={"google chrome":"chrome","microsoft store":"winstore.app","settings":"systemsettings","microsoft office":"webviewhost","task manager":"taskmgr"}
#rev_close_dict={'chrome': 'google chrome', 'winstore.app': 'microsoft store', 'systemsettings': 'settings'}
list_val=list(close_dict.values())
apps = give_appnames()
#print(apps)
drive_list=[ 'drive c', 'drive d', 'drive e', 'drive f', 'drive g', 'drive h', 'drive i', 'drive j', 'drive k', 'drive l', 'drive m', 'drive n', 'drive o', 'drive p', 'drive q', 'drive r', 'drive s', 'drive t', 'drive u', 'drive v', 'drive w', 'drive x', 'drive y', 'drive z'
    , 'c drive', 'd drive', 'e drive', 'f drive', 'g drive', 'h drive', 'i drive', 'j drive', 'k drive', 'l drive', 'm drive', 'n drive', 'o drive', 'p drive', 'q drive', 'r drive', 's drive', 't drive', 'u drive', 'v drive', 'w drive', 'x drive', 'y drive', 'z drive',
             'disk c', 'disk d', 'disk e', 'disk f', 'disk g', 'disk h', 'disk i', 'disk j', 'disk k', 'disk l', 'disk m', 'disk n', 'disk o', 'disk p', 'disk q', 'disk r', 'disk s', 'disk t', 'disk u', 'disk v', 'disk w', 'disk x', 'disk y', 'disk z',
             'c disk', 'd disk', 'e disk', 'f disk', 'g disk', 'h disk', 'i disk', 'j disk', 'k disk', 'l disk', 'm disk', 'n disk', 'o disk', 'p disk', 'q disk', 'r disk', 's disk', 't disk', 'u disk', 'v disk', 'w disk', 'x disk', 'y disk', 'z disk']


abs_path=""
g_dir=[]

#open("discord", match_closest=True, output=False)


def response(text):
    flag=0
    arr = text.split(" ")
    for x in stop_words:
        if x in arr:
            # text=text.replace(x,"")
            arr = [yy for yy in arr if yy != x]
    print(arr)
    text = ""
    for kll in arr:
        text += kll + " "
    text = text.strip()
    for dr in drive_list:
        if dr in text:
            flag=3
            arr2=[flag,text]
            print("arr2 printing ",arr2)
            return arr2
    for y in Open_keywords:
        if y in arr:

            print(y+" "+str(flag))
            flag = 1
            break
    for y in close_keywords:
        if y in arr:

            print(y+" "+str(flag))
            flag = 2
            break
    print("Outer "+str(flag))
    text = ""
    for kl in arr:
        text += kl + " "
    text = text.strip()
    respo=[flag,text]
    return respo


def dirct_rspo(text):
    global abs_path
    path=""
    for drive in drive_list:
        if fuzz.partial_ratio(drive,text)>=90:
            tmp=drive.split(" ")
            print("tmp printing ",tmp)
            if len(tmp[0])==1:
                print("printing before try ",tmp[0])

                try:
                    tomp = os.listdir(tmp[0]+":\\")
                    #print("correct")
                    path = tmp[0] + ":\\"
                    abs_path = tmp[0] + ":\\"
                    print("correct ", path," tmp 0 ",tmp[0])
                    break
                except:
                    print("eception1")
                # path=tmp[0]+":\\"
                # abs_path=tmp[0]+":\\"
                # break
            else:
                try:
                    tomp = os.listdir(tmp[1] + ":\\")
                    #print("correct")
                    path = tmp[1] + ":\\"
                    abs_path = tmp[1] + ":\\"
                    print("correct ",path)
                    break
                except:
                    print("eception1")
    print("path 0 ",path)
    tmp=dir_con(path,text)
    if abs_path!="":
        return abs_path
    else:
        return "Disk/Drive not found"


def opn_dir(path):
    os.startfile(os.path.realpath(path))
def dir_con(path,text):
    global abs_path
    global g_dir
    print("path =",path)
    try:
        g_dir=os.listdir(path)
        print("correct 2")
    except:
        abs_path=""
        print("eception 2")
        return path
    dirct=[]
    for x in g_dir:
        dirct.append(x.lower())
    print("dir= ",dirct)
    for nm in dirct:
        if fuzz.partial_ratio(nm,text)>=85:
            print("nm =",nm,"dir 2=",dirct)
            path+=nm+"\\"
            abs_path+=nm+"\\"
            print("printing = ",path)
            print("++1")
            dir_con(path,text)
    #return path

def app_close_rspo(text):
    arr = []
    # arr2=[]
    # cnt=0
    # for z in apps:
    #     if z in text:
    #         arr.append(z)
    for z in apps:
        if fuzz.partial_ratio(z,text)>=83:
            arr.append(z)
    if len(arr)!=0:
        #app_name = app_name.lower()
        # for window in gw.getAllTitles():
        #     for app in arr:
        #         print(str(window.title()).lower())
        #         if str(window.title()).lower() == app:
        #             arr2.append(app)
        #             cnt+=1
        #             break
        #     if cnt>=len(arr):
        #         break
        # print("printing arr ",arr)
        # for process in psutil.process_iter(attrs=['name']):
        #     for app in arr:
        #         try:
        #             process_name = str(process.info['name'])
        #             #print(process_name)
        #             if app in close_dict:
        #                 app=close_dict[app]
        #             if process_name.lower() == app+".exe":
        #                 # if app in list_val:
        #                 #     app=rev_close_dict[app]
        #                 arr2.append(app)
        #                 cnt+=1
        #                 break
        #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        #             pass
        #     if cnt >= len(arr):
        #          break
        # print("printing arr2 ",arr2)
        #if len(arr2)!=0:
            string = ""
            for o in arr:
                string += o + ","
                print(string)
            string = string[:-1]
            print(string)
            return string
        # else:
        #     return "App is already closed"
    else:
        return "App not Found"
def app_open_rspo(text):
    arr = []
    # for z in apps:
    #     if z in text:
    #         arr.append(z)
    for z in apps:
        if fuzz.partial_ratio(z,text)>=83:
            arr.append(z)
    if len(arr)!=0:
        string = ""
        for o in arr:
            string += o + ","
            print(string)
        string = string[:-1]
        print(string)
        return string
    else:
        return "App not Found"
    #open(string, match_closest=True, output=False)

def opn_app(text):
    open(text, match_closest=True, output=True)
    #print(hh)
def cls_app(text):
    print("closing..........................................",text)
    close(text,match_closest=True,output=True)
def crt_nm(text):
    array=text.split(",")
    string=""
    print(array)
    for x in array:
        if x in close_dict:
            string+=close_dict[x]+","
        else:
            string+=x+","
    string=string[:-1]
    return string


#response("hey can you open the app discord,proton vpn")
# happen("hey can you open the app discord")
#open("open whatsapp and discord", match_closest=True, output=True)
#cls_app("netflix")
#close('microsoft store',match_closest=True,output=True,throw_error=True)
# for window in gw.getAllTitles():
#     # for app in arr:
#     #     if window.title.lower() == app:
#     #         arr2.append(app)
#     #         cnt += 1
#     #         break
#     # if cnt >= len(arr):
#     #     break
#     print(str(window.title()).lower())
#close("winstore",match_closest=True,output=True)
#os.startfile(os.path.realpath(r"d:\\zz\\loop (86)"))
# print(os.environ.get("USERNAME"))

# print(dir)
# tm=dir_con("d:\\","open ptw spy classrooms in movies folder")
# print("abs path ",abs_path)
#close("explorer.exe",match_closest=True,output=True)
# for process in psutil.process_iter(attrs=['name']):
#
#         try:
#             process_name = str(process.info['name'])
#             print(process_name)
#
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass