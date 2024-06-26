import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,10)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "search in google " in query:
        import wikipedia as googleScrap
        query = query.replace("kim","")
        query = query.replace("search in","")
        query = query.replace("google","")
        web  = "https://www.google.com/search?q" + query
        webbrowser.open(web)
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "search in youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("search in","")
        query = query.replace("youtube","")
        query = query.replace("kim","")
        web  = "https://www.youtube.com/results?search_query={query}" 
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")
 
def searchWikipedia(query):
    if "search in wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search in","")
        query = query.replace("kim","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)


def playSong(query):
    if "i am tired" in query:
        query = query.replace("kim","")
        speak("Playing your favourite songs, sir")

        webbrowser.open("https://www.youtube.com/watch?v=KzrtfBtJqrk&list=PLbQK43Ml3sxYZDEiK5eHkymcyUAo40v1z")
    
