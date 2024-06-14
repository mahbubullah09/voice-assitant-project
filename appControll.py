import os 
import pyautogui
import webbrowser
import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

appList = {"command prompt":"cmd","brave":"brave","word":"winword","sheet":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openapp(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("kim","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(appList.keys())
        for app in keys:
            if app in query:
                os.system(f"start {appList[app]}")

def closeapp(query):
    speak("Closing,sir")
    

    
    keys = list(appList.keys())
    for app in keys:
        if app in query:
            os.system(f"taskkill /f /im {appList[app]}.exe")
