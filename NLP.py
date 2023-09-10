import speech_recognition as sr


def lang_process():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    try:
        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source,timeout=5)
    except:
        print("error")

    # Recognize the speech using Google Web Speech API


    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"You said: {text}")
    except sr.UnknownValueError:
        text = "Sorry, I could not understand your speech."
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        text = "Sorry, an error occurred"
        print(f"Sorry, an error occurred: {e}")

    #arr = [True, text]
    return text


#lang_process()
