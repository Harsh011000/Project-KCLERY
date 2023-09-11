from AppOpener import *

App_keywords = [
    "open",
    "launch",
    "start",
    "access",
    "run",
    "initiate",
    "begin",
    "commence"]
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
    for y in App_keywords:
        if y in arr:

            print(y+" "+str(flag))
            flag = 1
            break
    print("Outer "+str(flag))
    text = ""
    for kl in arr:
        text += kl + " "
    text = text.strip()
    respo=[flag,text]
    return respo


def app_open_rspo(text):
    arr = []
    for z in apps:
        if z in text:
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
    open(text, match_closest=True, output=False)


#response("hey can you open the app discord,proton vpn")
# happen("hey can you open the app discord")
# open("edge", match_closest=True, output=False)
