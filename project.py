import pyttsx3
import speech_recognition 
import datetime
import requests
from bs4 import BeautifulSoup
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        # greetings 
        query = takeCommand().lower()
        if "wake up" in query:
            from greeting import geeting
            geeting()

            # sleep command 
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
                # talk with ai 
                elif "hello" in query:
                    speak("Hello Mr. Mahbub, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    
                    
                elif "open" in query:
                    from appControll import openapp
                    openapp(query)
                elif "close" in query:
                    from appControll import closeapp
                    closeapp(query)
                 
                #  google search    
                elif "google" in query:
                    from webSearch import searchGoogle
                    searchGoogle(query)
                    
                # youtube search     
                elif "youtube" in query:
                    from webSearch import searchYoutube
                    searchYoutube(query)
                # controll video     
                elif "pause" in query:
                    pyautogui.press("space")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("space")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "full screen" in query:
                    pyautogui.press("f")
                    speak("full screen")
                elif "default screen" in query:
                    pyautogui.press("f")
                    speak("default screen")
                
                # wikipedia search     
                elif "wikipedia" in query:
                    from webSearch import searchWikipedia
                    searchWikipedia(query)
                 
                # weather update    
                elif "tell me weather update" in query:
                    search = "temperature in dhaka"
                    from weatherUpdate   import getWeather
                    getWeather(search)
                    
                # time 
                elif "tell me the time " in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                 
                # remember somthing     
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me "+rememberMessage)
                    remember = open("remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt","r")
                    speak("You told me " + remember.read())
                elif "delete all your memory" in query:
                    remember = open("remember.txt","w")
                    remember.write("")
                    speak("All remembered items have been deleted.")
                    
                    
                    
                    