#  https://music.youtube.com/search?q=mann+mera+mane+na
#  https://open.spotify.com/search/mann%20mera%20mane%20na
#  https://music.amazon.in/search/maan+mera
#  https://www.jiosaavn.com/search/song/maan%20mera%20mane%20na
#  https://music.apple.com/in/search?term=arijit%20singh%20
#  https://gaana.com/search/maan%20mera

import speech_recognition as sr
import random
def music_process():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    try:
        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source,timeout=5)
    except:
        pass

    # Recognize the speech using Google Web Speech API


    try:
        musictext = recognizer.recognize_google(audio)
        musictext = musictext.lower().strip()

    except sr.UnknownValueError:
        musictext = "Sorry, I could not understand gaana"

    except sr.RequestError as e:
        musictext = "Sorry, an error occurred"

    return musictext

def musicSearch(musictext):
    flag=-1
    flag1 = utubemusic(musictext)
    flag2 = spotify(musictext)
    flag3 = amazonmusic(musictext)
    flag4 = gaana(musictext)
    flag5 = applemusic(musictext)
    flag6 = gaana(musictext)
    flag7 = nomusic(musictext)
    flag8= notmusic(musictext)
    flagarr = [flag1, flag2, flag3, flag4, flag5, flag6, flag7 ,flag8]
    for i in flagarr:
        if (i != None):
            flag = i
            break
    if (flag==-1):
        array =[flag,"Please use mic button to do other tasks"]
        return array
    filteredarray=filtertext(musictext)
    filteredarray.pop(len(filteredarray)-1)
    if (flag=="gsearch"):
        flag=randommusic()
    if (flag=="search"):
        search = ""
        for x in filteredarray:
            search += x + " "
        array = [-2, search]
        return array
    if flag==1:
        search ="https://music.youtube.com/search?q="
        for x in filteredarray:
            search += x + "+"
        array = [10, search]
        return array
    if flag==2:
        search ="https://open.spotify.com/search/"
        for x in filteredarray:
            search += x + "%20"
        array = [20, search]
        return array
    if flag==3:
        search ="https://music.amazon.in/search/"
        for x in filteredarray:
            search += x + "+"
        array = [30, search]
        return array
    if flag==4:
        search ="https://www.jiosaavn.com/search/song/"
        for x in filteredarray:
            search += x + "%20"
        array = [40, search]
        return array
    if flag==5:
        search ="https://music.apple.com/in/search?term="
        for x in filteredarray:
            search += x + "%20"
        array = [50, search]
        return array
    if flag==6:
        search ="https://gaana.com/search/"
        for x in filteredarray:
            search += x + "%20"
        array = [60, search]
        return array
    return [-1,"Please use mic button to do other tasks"]
def notmusic(text):
    array = text.split(" ")
    if ("play" not in array[0] and "gaana" not in array[0] and "search" not in array[0] and "open" not in array[0] and "close" not in array[0]):
        return "search"
def nomusic(text):
    array=text.split(" ")
    if ("play" in array or "gaana" in array):
        return "gsearch"
def spotify(text):
    array=text.split(" ")
    if ("spotify" in array):
        return 2

def utubemusic(text):
    array=text.split(" ")
    if ("utube" in array or "youtube" in array or "youtubemusic" in array or ("youtube" in array and "music" in array)):
        return 1

def amazonmusic(text):
    array=text.split(" ")
    if ("amazon" in array or "amazonmusic" in array or ("amazon" in array and "music" in array) ):
        return 3

def  jiosaavn(text):
    array = text.split(" ")
    if ("jio" in array or "jiosaavn" in array or ("jio" in array and "music" in array) or "jiomusic" in array or "jiosavan" in array):
        return 4

def applemusic(text):
    array = text.split(" ")
    if ("apple" in array or "applemusic" in array or ("apple" in array and "music" in array) or "itunes" in array):
        return 5

def gaana(text):
    array = text.split(" ")
    if ("gaana" in array):
        return 6

def randommusic():
    flag = random.randint(1, 6)
    return flag
def filtertext(text):
    array = text.split(" ")
    if ("search" in array):
        array.remove("search")
    if ("gaana" in array):
        array.remove("gaana")
    if ("amazon" in array):
        array.remove("amazon")
    if ("music" in array):
        array.remove("music")
    if ("apple" in array):
        array.remove("apple")
    if ("play" in array):
        array.remove("play")
    if ("youtube" in array):
        array.remove("youtube")
    if ("spotify" in array):
        array.remove("spotify")
    if ("jiosaavn" in array):
        array.remove("jiosaavn")
    if ("jiosaavn" in array):
        array.remove("jiosavan")
    if ("jio" in array):
        array.remove("jio")
    if ("jiomusic" in array):
        array.remove("jiomusic")
    return array