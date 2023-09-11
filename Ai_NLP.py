import psutil
from AppOpener import *
from fuzzywuzzy import fuzz


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
close_dict={"google chrome":"chrome","microsoft store":"winstore.app","settings":"systemsettings"}
rev_close_dict={'chrome': 'google chrome', 'winstore.app': 'microsoft store', 'systemsettings': 'settings'}
list_val=list(close_dict.values())
apps = give_appnames()
print(apps)

#open("discord", match_closest=True, output=False)


def response(text):
    flag=0
    arr = text.split(" ")
    for x in stop_words:
        if x in arr:
            # text=text.replace(x,"")
            arr = [yy for yy in arr if yy != x]
    print(arr)
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


def app_close_rspo(text):
    arr = []
    arr2=[]
    cnt=0
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
        for process in psutil.process_iter(attrs=['name']):
            for app in arr:
                try:
                    process_name = str(process.info['name'])
                    print(process_name)
                    if app in close_dict:
                        app=close_dict[app]
                    if process_name.lower() == app+".exe":
                        # if app in list_val:
                        #     app=rev_close_dict[app]
                        arr2.append(app)
                        cnt+=1
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            if cnt >= len(arr):
                 break
        if len(arr2)!=0:
            string = ""
            for o in arr2:
                string += o + ","
                print(string)
            string = string[:-1]
            print(string)
            return string
        else:
            return "App is already closed"
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
    close(text,match_closest=True,output=True)
def crt_nm(text):
    array=text.split(",")
    string=""
    for x in array:
        if x in list_val:
            string+=rev_close_dict[x]+","
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