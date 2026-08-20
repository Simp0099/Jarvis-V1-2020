from sys import int_info
import requests
import os
import pyttsx3
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Get NASA API key from environment variable
Api_Key = os.getenv('NASA_API_KEY')
if not Api_Key:
    print("WARNING: NASA_API_KEY not found in .env file")
    speak("NASA API key is not configured. Please set NASA_API_KEY in your .env file")

def NasaNews(Date):

    speak("Searching Through Nasa's DataBase.")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)

    Params = {'date':str(Date)}

    r = requests.get(Url,params = Params)

    Data = r.json()
    
    Info = Data['explanation']
     
    Title = Data['title'] 

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    
    FileName = str(Date) + '.jpg'


    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\Sony\\OneDrive\\Desktop\\Jarvis\\" + str(FileName)

    Path_2 = "C:\\Users\\Sony\\OneDrive\\Desktop\\Jarvis\\Nasa's DataBase\\" + str(FileName)

    os.rename(Path_1,Path_2)
 
    img = Image.open(Path_2)

    img.show()

    speak(f"Title : {Title}") 
    speak(f"According To Nasa {Info}") 

  

    
     
