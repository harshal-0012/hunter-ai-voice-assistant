import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser as wb
import smtplib
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
"""
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)
#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    #speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
#date()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   
    elif hour>=18 and hour<24:
        speak("Good Evening Sir !")

    else:
        speak("Good Evening Sir!")  

    speak("I am Hunter at your service. Please tell me how can I help you?")       

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshalparmar1212@gmail.com', '@Hunter2003')
    server.sendmail('harshalparmar1212@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:\hunter-ai\hunter-ss\s1.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at usage'+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath ="C:\Program Files\Google\Chrome\Application\chrome.exe %s" 
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play songs' in query:
            music_dir = 'E:\DJ KP\garba'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "parmarharshal012@gmail.com"    
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry !I am unable to send this email")    
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("You said me to remember that" + remember.read())
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done! i have taken screenshot")
        
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            jokes()
            
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'offline' in query:
            quit()
