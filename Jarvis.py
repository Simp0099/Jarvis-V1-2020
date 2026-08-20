import pyttsx3
from pytube.__main__ import YouTube
import speech_recognition as sr 
import datetime
import pyautogui
import wikipedia
import webbrowser
import os
import smtplib
import requests
import pyjokes
import psutil
from playsound import playsound
from requests.api import request 
from bs4 import BeautifulSoup
import pyjokes
from wikipedia.wikipedia import search
from pywikihow import search_wikihow
from PyDictionary import PyDictionary as Diction
import keyboard
import random


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        a = "Good Morning Boss!"  , "Whats Up Boss!" , "I'm Here Boss !" , "Ready For some work Boss !" "servers online Boss !" "GM Boss" "How was your sleep Boss" "Todays Day Is Gorgeous" 
        say(random.choice(a))   

    elif hour>=12 and hour<18:
        b = "Good Afternoon Boss!" , "Whats Up Boss!" , "I'm Here Boss" , "welcome Back Boss !" , "BhelCome Back Boss!" "How was your day boss!"
        say(random.choice(b))   

    else:
        c = "Good Evening Boss!" , "Whats Up Boss!" , "I'm Here Boss" , "Welcome Back Boss !" , "Bhelcome boss !"
        say(random.choice(c))

    say("Friday On The  Service !")      
     



def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()

def DateConvertor(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")  
    Date = Date.replace(" ","")   
    
    return str(Date)

def Temp():
    search ="Temperature In delhi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak(f"The Temperature Outside is {temperature}")



def screenshot():
        speak("Ok Boss , What Should I Name That File ?")
        path = takeCommand()
        path1name = path + ".png"
        path1 = "C:\\Users\\Sony\\OneDrive\\Desktop\Jarvis\\ScreenShot DataBase\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\Sony\\OneDrive\\Desktop\\Jarvis\\ScreenShot DataBase\\")
        speak("Here Is Your ScreenShot Boss")   



def Dict():
        speak("Activated Dictionary!")
        speak("Tell Me The Problem!")
        probl = takeCommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("meaning of","")
            result = Diction.meaning(probl)
            speak(f"The Meaning For {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("synonym of","")
            result = Diction.synonym(probl)
            speak(f"The Synonym For {probl} is {result}")    

        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of","")
            probl = probl.replace("antonym of","")
            result = Diction.antonym(probl)
            speak(f"The Antonym For {probl} is {result}")     

        speak("Exited Dictionary!")

def Music():
        speak("Tell Me The Name of The Song!")
        musicName = takeCommand()

        if 'akeli' in musicName:
            os.startfile('E:\\Songs\\akeli.mp3')

        elif 'Bhola Parvat ka' in musicName:
            os.startfile('D:\\Songs\\Bhola Parvat Ka.mp3')

        speak("Your Song Has Been Started! , Enjoy Boss!")





def sendEmail(to, content):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    gmail_user = os.getenv('GMAIL_USER')
    gmail_password = os.getenv('GMAIL_PASSWORD')
    
    if not gmail_user or not gmail_password:
        speak("Gmail credentials not configured. Please set GMAIL_USER and GMAIL_PASSWORD in .env file")
        return
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'how are you' in query:
            speak("I Am Fine Boss!")
            speak("Whats About YOU?")

        elif 'you need a break' in query:
            speak("Ok Boss ! , You Can Call Me Anytime !")
            break

        elif 'what are you doing' in query:
            speak("Nothing Just At Your Service Boss !")

        elif 'wanna go for a drink' in query:
            speak("Sure!  why not")
            speak("i'll Buy the whole stall !")  

        elif 'say the magic words' in query:
            speak("Yes  Daddy !")

        elif 'I am sad' in query:
            speak("Who did that to my boss! Hello John Wick !")

        elif 'Tik Tok' in query: 
            ("Tiktok Tatti Hai") 
 
        elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/?reload=9")

        elif 'open google' in query:
           webbrowser.open("https://www.google.com/")
        
        elif 'open gaana' in query:
           webbrowser.open("https://gaana.com/")               
       
        elif 'open gmail' in query:
           webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 
        
        elif 'open intel' in query:   
           webbrowser.open("https://www.intel.com/content/www/us/en/homepage.html") 
        
        elif 'open google photos' in query:
           webbrowser.open("https://photos.google.com/u/0/albums") 

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Boss, the time is {strTime}")

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'replay' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'theatre mode' in query:
            keyboard.press('t')
        
        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')   

        elif 'open microsoft edge' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath) 
 
        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
    
        elif 'open obs' in query:
            codePath = "D:\\StreamLabs\\Streamlabs OBS\\Streamlabs OBS.exe"
            os.startfile(codePath)

        elif 'open itunes' in query:
            codePath = "C:\\Program Files\\iTunes\\iTunes.exe"
            os.startfile(codePath)

        elif 'open python' in query:
            codePath = "C:\\Users\\Sony\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
            os.startfile(codePath)

        elif 'open send anywhere' in query:
            codePath = "C:\\Users\\Sony\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
            os.startfile(codePath)

        elif 'set an alarm' in query:
             speak("Whats The Time !")
             time = input("Enter The Time :")
            
             while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")  

                if now == time:
                    speak("time To Wake Up Boss !")
                    playsound("C:\\Users\\Sony\\OneDrive\\Desktop\\Jarvis\\Resources\\MP3\\Jarvis Wake Up.mp3")
                    speak("Alarm Closed !")

                elif now>time:
                    break
                
        elif 'tell me some space news' in query:
            speak("Tell which day's Space News You Wanna Know")
                  
            Date = takeCommand()
 
            Value = DateConvertor(Date)

            from Nasa import NasaNews

            NasaNews(Value)



        elif 'tell me a joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'tell me another joke' in query:
            get = pyjokes.get_joke()
            speak(get)
        
        elif 'take a screenshot' in query:
            screenshot()

        elif 'send an email' in query:
            try:
                speak("Who should I send this email to?")
                to = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss I am not able to send this Email") 

         
        elif 'email to mom' in query:
            try:
                speak("Boss What should I say?")
                content = takeCommand()
                speak("What is mom's email address?")
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss I am not able to send this Email")   

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

       
        elif 'temperature' in query:
            Temp()         
        
        elif 'Friday youtube search' in query:
            speak("OK Boss , This Is What I found For Your Search!")
            query = query.replace("Friday","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Showing You The Results Boss!")
        
        
        #elif  'google search' in query:
         #   import wikipedia as googleScrap
          #  query = query.replace("Friday","")
           # query = query.replace("google search","")
            #query = query.replace("google","")
            #speak ("This what i found on Web !")
            #pywhatkit.search(query)
            
            
           # try:
            #    result = googleScrap.summary(query,3)
             #   speak(results)

            #except:
            #    speak("Boss There Is No Data Available")    
            


        elif 'how to' in query:
            speak("Extracting Data")
            op = query.replace ("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            speak(how_to_func[0].summary)


        elif 'open website' in query:
            speak("Ok Boss , Launching.....")
            query = query.replace("open","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Website Launched!")    


        elif 'repeat my word' in query:
            speak("Speak Boss!")
            jj = takeCommand()
            speak(f"You Said : {jj}")

        elif 'my location' in query:
            speak("Ok Boss , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@28.5161339,77.2944539,17z')

        elif 'Dictionary' in query:
            Dict() 
     
        elif 'play music' in query:
            Music()


        













