from AppOpener import *
from fuzzywuzzy import fuzz
import os
import difflib
import pandas as pd
import pywhatkit as kit

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
Search_words = ["search",
                "research",
                "find"]

Useless_words = [
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
close_dict = {"google chrome": "chrome", "microsoft store": "winstore.app", "settings": "systemsettings",
              "microsoft office": "webviewhost", "task manager": "taskmgr"}

list_val = list(close_dict.values())
apps = give_appnames()

drive_list = ['drive c', 'drive d', 'drive e', 'drive f', 'drive g', 'drive h', 'drive i', 'drive j', 'drive k',
              'drive l', 'drive m', 'drive n', 'drive o', 'drive p', 'drive q', 'drive r', 'drive s', 'drive t',
              'drive u', 'drive v', 'drive w', 'drive x', 'drive y', 'drive z' ,
              'c drive', 'd drive', 'e drive', 'f drive', 'g drive', 'h drive', 'i drive', 'j drive', 'k drive', 'l drive',
              'm drive', 'n drive', 'o drive', 'p drive', 'q drive', 'r drive', 's drive', 't drive', 'u drive',
              'v drive', 'w drive', 'x drive', 'y drive', 'z drive',
              'disk c', 'disk d', 'disk e', 'disk f', 'disk g', 'disk h', 'disk i', 'disk j', 'disk k', 'disk l',
              'disk m', 'disk n', 'disk o', 'disk p', 'disk q', 'disk r', 'disk s', 'disk t', 'disk u', 'disk v',
              'disk w', 'disk x', 'disk y', 'disk z',
              'c disk', 'd disk', 'e disk', 'f disk', 'g disk', 'h disk', 'i disk', 'j disk', 'k disk', 'l disk',
              'm disk', 'n disk', 'o disk', 'p disk', 'q disk', 'r disk', 's disk', 't disk', 'u disk', 'v disk',
              'w disk', 'x disk', 'y disk', 'z disk']

abs_path = ""   #empty string to store path
g_dir = []
username = os.environ.get("USERNAME")
custom_dir = {"documents": "C:\\Users\\" + username + "\\documents",
              "pictures": "C:\\Users\\" + username + "\\pictures",
              "downloads": "C:\\Users\\" + username + "\\downloads", "music": "C:\\Users\\" + username + "\\music",
              "viedos": "C:\\Users\\" + username + "\\viedos", "desktop": "C:\\Users\\" + username + "\\desktop"}


# 1= open 2= close 3= dir 4= search 5 =custom 6= muscic search
def response(text):
    flag = 0
    chflag=initi(text)
    if (chflag==0):
        flag="init"
        array=[flag,"Hi "+username.capitalize()+"\n How can i help you?\n These are the keywords to interact with me--> \n 1. Open to play with file explorer"
                    "and to open apps. \n 2. Close to close opened software \n 3. Set keywordname =/equal(s) task to set custom task. \n"
                    " 4. Search to search on google."]
        return array
    text = single_line(text)
    text = check_for_cust_comm(text)
    if os.path.isdir(text):
        flag = 3
        array = [flag, text]
        return array
    arr = text.split(" ")

    if arr[0] == "set" and (arr[2] == "=" or arr[2] == "equal" or arr[2] == "equals"):
        flag = 5
        array = [flag, text]
        return array

    if (Search_words[0] in arr or Search_words[1] in arr or Search_words[2]  in arr):
        if (Search_words[0] == arr[0] or Search_words[0] == arr[len(arr)-1] or Search_words[1] == arr[0] or Search_words[1] == arr[len(arr)-1] or Search_words[2] == arr[0] or Search_words[2] == arr[len(arr)-1]):
            flag=4
            array=[flag,text]
            return array
        else:
            flag=-4
            array=[flag,"Please enter search input properly"]
            return array

    for x in Useless_words:
        if x in arr:
            arr = [yy for yy in arr if yy != x]

    for chk in custom_dir:
        found = difflib.get_close_matches(chk, arr, n=1, cutoff=0.85)
        if found:
            flag = 3
            array = [flag, custom_dir[chk]]
            return array
    text = ""
    for kll in arr:
        text += kll + " "
    text = text.strip()
    for dr in drive_list:
        if dr in text:
            flag = 3
            arr2 = [flag, text]

            return arr2
    for y in Open_keywords:
        if y in arr:
            flag = 1
            break
    for y in close_keywords:
        if y in arr:
            flag = 2
            break

    text = ""
    for kl in arr:
        text += kl + " "
    text = text.strip()
    respo = [flag, text]
    return respo



def check_for_cust_comm(text):
    if len(text.split(" ")) == 1:

        text = use_cust_comm(text)

        return text
    else:
        return text


def single_line(text):
    arr = text.split("\n")
    string = ""
    for x in arr:
        string += x + " "
    return string.strip()


def use_cust_comm(key):
    try:
        df = pd.read_csv("Custom Commands.csv")

        key_df = df[df["Custom key"] == key]
        command = key_df["Command"].values[0]
        if command is not None and command != "":
            return command
        else:
            return key
    except:
        return key


def cust_set(text):
    arr = text.split(" ")
    key = arr[1]
    work = ""
    for x in range(3, len(arr)):
        work += arr[x] + " "
    set_file(key, work.strip())
    return key + ":" + work.strip()


def set_file(key, work):
    data = {"Custom key": [key],
            "Command": [work]}
    df = pd.DataFrame(data)
    file_name = "Custom Commands.csv"
    if os.path.exists(file_name):

        dff = pd.read_csv(file_name)
        key_mask = dff["Custom key"] == key
        if key_mask.any():
            dff.loc[key_mask, "Command"] = work
            dff.to_csv(file_name, mode="w", header=True, index=False)
        else:
            df.to_csv(file_name, mode="a", header=False, index=False)
    else:
        df.to_csv(file_name, mode="a", header=True, index=False)


def dirct_rspo(text):  #dfdfedfd
    global abs_path
    path = ""
    if os.path.isdir(text):
        abs_path = text
        return abs_path

    for drive in drive_list:
        if fuzz.partial_ratio(drive, text) >= 90:
            tmp = drive.split(" ")

            if len(tmp[0]) == 1:

                try:
                    tomp = os.listdir(tmp[0] + ":\\")

                    path = tmp[0] + ":\\"
                    abs_path = tmp[0] + ":\\"

                    break
                except:
                    pass

            else:
                try:
                    tomp = os.listdir(tmp[1] + ":\\")

                    path = tmp[1] + ":\\"
                    abs_path = tmp[1] + ":\\"

                    break
                except:
                    pass

    tmp = dir_con(path, text)
    if abs_path != "":
        return abs_path
    else:
        return "Disk/Drive not found"


def opn_dir(path):
    os.startfile(os.path.realpath(path))


def dir_con(path, text):   #fdfdf
    global abs_path
    global g_dir

    try:
        g_dir = os.listdir(path)

    except:
        abs_path = ""

        return path
    dirct = []
    for x in g_dir:
        dirct.append(x.lower())

    for nm in dirct:
        if fuzz.partial_ratio(nm, text) >= 87:
            path += nm + "\\"
            abs_path += nm + "\\"

            dir_con(path, text)


def app_close_rspo(text):
    arr = []

    for z in apps:
        if fuzz.partial_ratio(z, text) >= 83:
            arr.append(z)
    if len(arr) != 0:

        string = ""
        for o in arr:
            string += o + ","

        string = string[:-1]

        return string

    else:
        return "App not Found"


def app_open_rspo(text):
    arr = []

    for z in apps:
        if fuzz.partial_ratio(z, text) >= 83:
            arr.append(z)
    if len(arr) != 0:
        string = ""
        for o in arr:
            string += o + ","

        string = string[:-1]

        return string
    else:
        return "App not Found"


def opn_app(text):
    open(text, match_closest=True, output=False)


def cls_app(text):
    close(text, match_closest=True, output=False)


def crt_nm(text):  #corerect name
    array = text.split(",")
    string = ""

    for x in array:
        if x in close_dict:
            string += close_dict[x] + ","
        else:
            string += x + ","
    string = string[:-1]
    return string

def filter_google(text):
    text = text.strip()
    googlearr = text.split(" ")
    if (googlearr[0] == "search"):
        googlearr.pop(0)
    elif (googlearr[len(googlearr) - 1] == "search"):
        googlearr.pop(len(googlearr) - 1)
    elif (googlearr[0] == "research"):
        googlearr.pop(0)
    elif (googlearr[len(googlearr) - 1] == "research"):
        googlearr.pop(len(googlearr) - 1)
    elif (googlearr[0] == "find"):
        googlearr.pop(0)
    elif (googlearr[len(googlearr) - 1] == "find"):
        googlearr.pop(len(googlearr) - 1)
    else:
        return text
    searchString = ""
    for i in googlearr:
        searchString += i + " "
    return searchString
def clear_google(text):
    text = text.strip()
    gr = text.split(" ")
    i = 0
    i2 = 0
    if ("google" in gr):
        i = gr.index("google")
        i2 = gr.index("on")
    if (i == i2 + 1):
        gr.pop(i)
        gr.pop(i2)
    Search=""
    for i in gr:
        Search += i + " "
    return Search
def search_google(text):
    kit.search(text)

def initi(text):
    text.strip()
    arrc=text.split(" ")
    if (arrc[0]=="hi" or arrc[0]=="hello" or arrc[0]=="kcleary"):
        return 0

