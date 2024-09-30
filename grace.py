import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import cv2 as cv
import pyautogui
import langchain
import requests
import wolframalpha
import pywhatkit
import smtplib
from email.message import EmailMessage
import pyjokes
import random
from googletrans import Translator
import ast
import fileinput
import sys
import psutil 
import pyjokes 
import speedtest 
from requests import get
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

def take_picture():
    ec.capture(0, "camera_capture", "img.jpg")

def sendEmail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sbaijal55@gmail.com", "gckqxyohsacbrynf")
    server.send_message(msg)
    server.close()
    
def capture_video(duration):
    speak("Recording started. Press 'q' to stop recording.")
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'mp4v'))  # Specify MP4 codec
    cap.set(cv.CAP_PROP_FPS, 30)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

    fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Specify MP4 codec
    out = cv.VideoWriter('output.mp4', fourcc, 30, (640, 480))  # Save as MP4 file

    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow('Video', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    out.release()
    cv.destroyAllWindows()

    # Check if video file exists and has a non-zero size
    if os.path.exists('output.mp4') and os.path.getsize('output.mp4') > 0:
        speak("Video captured successfully!")
        return True
    else:
        speak("Failed to capture video!")
        return False

def take_screenshot():
    pass

def create_note(note_title, note_content):
    pass

def answer_question(question):
    pass

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)
def remove(string):
    return string.replace(" ", "")

def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("voice changed")



def sendEmail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sbaijal55@gmail.com", "gckqxyohsacbrynf")
    server.send_message(msg)
    server.close()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def jokes():
    speak(pyjokes.get_joke()) 

def takeCommand():
    r=sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio)
            print(f"user said:{statement}\n")

        except Exception as e:
            
            speak("I can't hear you clearly, please speak again")
            return "None"
        return statement

try:    
    response = requests.get("https://www.google.com")
    
except:    
    speak("Internet is not connected. Try again later")
    exit()
import pywhatkit


speak('Hello! I am Grace, your personal voice assistant.')

wishMe()



if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Grace is shutting down, Good bye')
            print('your personal assistant Grace is shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            try:
                # Open the Wikipedia page directly
                webbrowser.open_new_tab(wikipedia.page(statement).url)
            except wikipedia.exceptions.DisambiguationError as e:
                # If multiple options found, open the disambiguation page
                webbrowser.open_new_tab(wikipedia.disambiguation_url(statement))
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find information on that.")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"Temperature in kelvin unit is {current_temperature}, humidity in percentage is {current_humidity}, and description is {weather_description}")
                print(f"Temperature in kelvin unit = {current_temperature}, humidity (in percentage) = {current_humidity}, description = {weather_description}")
            else:
                speak("City Not Found")

        elif 'time' in statement:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Grace version 1.0, your personal assistant. I am programmed to perform minor tasks like opening YouTube, Google Chrome, Gmail, and Stack Overflow, predicting time, taking photos, searching Wikipedia, predicting weather in different cities, getting top headlines news from Times of India, and answering computational or geographical questions.')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Harshada")
            print("I was built by Harshada")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India. Happy reading!')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            take_picture()
            speak("Photo taken successfully!")
            time.sleep(6)

        elif 'record video' in statement:
            speak("For how many seconds you want to record the video?")
            video_duration = takeCommand()
            duration = int(video_duration.replace("seconds", ""))
            capture_video(duration)
            speak("Video captured successfully!")

        elif 'take a screenshot' in statement:
            take_screenshot()
            speak("Screenshot taken!")

        elif 'create a note' in statement:
            speak("What should be the title of the note?")
            note_title = takeCommand()
            speak("What should be the content of the note?")
            note_content = takeCommand()
            create_note(note_title, note_content)
            speak("Note created successfully!")

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your PC will log off in 10 seconds. Make sure you exit from all applications.")
            subprocess.call(["shutdown", "/l"])


        elif 'open word' in statement:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
            speak("Microsoft Word has been opened.")

        elif 'open powerpoint' in statement:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
            speak("Microsoft PowerPoint has been opened.")

        elif 'open paint' in statement:
            os.startfile("mspaint")
            speak("Paint has been opened.")

        elif 'joke' in statement:
            jokes()

        elif 'how much power left' in statement or 'how much power we have' in statement or 'battery' in statement:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Our system has {percentage} percent battery")
            if percentage==100:
                speak("Our system has full power. No need to charge")
            elif percentage>=75:
                speak("We have enough power to continue our work")
            elif percentage>=50 and percentage<=75:
                speak("We should plug our system to charging point to charge our battery")
            elif percentage>=15 and percentage<=50:
                speak("We don't have enough power to work, please plug our system to charge")
            elif percentage<=15:
                speak("Immediately plug our system to charge") 

        elif 'alarm' in statement:
            speak("Please tell me the time to set the alarm. For example, set alarm to 5:00 p.m.")
            tt = takeCommand()
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            import Alarm  # Import the Alarm module
            Alarm.alarm(tt)  # Call the alarm function from the Alarm module
        
        elif 'game' in statement:
            speak("Starting the snake game")
            import snakeGame  # Import the SnakeGame module
            snakeGame.start()  # Call the start function from the SnakeGame module

        elif 'open notepad' in statement:
            notepadPath = "C:/WINDOWS/system32/notepad.exe"
            os.startfile(notepadPath)

        elif 'close notepad' in statement:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in statement or 'open cmd' in statement:
            os.system('start cmd')

        elif 'close command prompt' in statement or 'close cmd' in statement:
            os.system("taskkill /f /im cmd.exe")   

        elif 'internet speed' in statement:
            intSpeedst = speedtest.Speedtest()
            intSpeeddl = intSpeedst.download()
            intSpeedup = intSpeedst.upload()
            speak(f"We have {intSpeeddl} bit per second downloading speed and {intSpeedup} bit per uploading speed")
        
        elif 'ip address' in statement:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}") 
        
        elif 'search in chrome' in statement:
            speak("What Should I Search in Google Chrome?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            searchInChrome = takeCommand().lower()
            webbrowser.get(chromepath).open_new_tab(searchInChrome+'.com')
        
        elif 'currency converter' in statement or "currency exchange" in statement or "currency" in statement:            
            speak("What is the currency CODE from which you what to convert: ")
            c1=takeCommand()            
            speak("What is the currency CODE to which you what to convert: ")
            c2=takeCommand()            
            speak("What is the the amount: ")
            amt=float(takeCommand())
            url = "https://currency-exchange.p.rapidapi.com/exchange"
            querystring = {"from": c1,"to": c2}
            headers={                
                "X-RapidAPI-Key": "4a7bf47ff1mshc831d0864665364p1c6871jsnbae885015071",
                "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            if response.text=="0" and amt!=0:
                speak("Invalid currency code entered")                
            result=float(response.text)*amt
            speak(f"{amt:.2f} {c1} is equal to {result:.2f} {c2}")
        
        elif "movie" in statement or "series" in statement or "tv show" in statement or "film" in statement:
            speak("what is the name of the movie or series")
            name=takeCommand()            
            base_url="https://api.popcat.xyz/imdb?q="
            complete_url=base_url+name
            response = requests.get(complete_url)
            n=response.json()
            try:                
                title=n['title']
                director=n['director']
                plot=n['plot']                
                speak(f"{title} is directed by {director}")                
                speak(f"It is about {plot}")
            except Exception as e:
                print(e)
                speak("unable to get the movie/series details, try again")  

        elif "voice" in statement:           
            speak("for female voice say `female` and, for male voice say `masculine`")
            
            q = takeCommand()
            if ("female" in q):

                voice_change(1)
            elif ("masculine" in q):

                voice_change(0)
            else:
                speak("Voice not changed, invalid input given")              
        
        elif "message" in statement:  #whatsapp web must be logged in 
                        
            speak("Which number would you like to send the message to")
            number=takeCommand()
            speak("What is the content of your message")
            wmsg=takeCommand()
            try:
                                
                speak("sending message, kindly be patient")
                pywhatkit.sendwhatmsg_instantly(f"+91{remove(number)}", wmsg, 15)
                speak("message sent")
            except Exception as e:
                print(e)
                speak("Invalid number mentioned. Try again with a valid 10 digit number") 

        elif "stock" in statement:
            speak("what is the symbol of the stock")
            symbol=takeCommand()
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={remove(symbol)}&apikey=5YIZ9GTZQDZ475XJ'
            r = requests.get(url)
            data = r.json()
            try:
                num=data["Global Quote"]
                    
                speak(f"current stock price of {num['01. symbol']} is {num['05. price']}")
            except Exception as e:                
                speak("Error. Invalid stock name") 

        elif 'song'  in statement or 'music' in statement:       
            speak('Which song do you want me to play')
            song = takeCommand()
            speak(f"playing {song}")
            pywhatkit.playonyt(song)        
            time.sleep(6)       
                           
        elif "translate" in statement or "translator" in statement:
            translator = Translator()
            speak("speak the text that you want to translate")
            text=takeCommand()
                
            speak("which language do you want to translate it to")
            lang=takeCommand()
            try:                                         
                translated_text = translator.translate(text,dest=lang)
                    
                speak(f"The translated text is: `{translated_text.text}`")
            except Exception as e:
                print(e)
                speak("Unable to translate the text. Try again")
        
        elif "do i have any reminders" in statement or "current reminders" in statement or "show reminders" in statement or "all reminders" in statement:
            reminder_file = open("data.txt", 'r')
            if os.stat("data.txt").st_size == 0:
                speak("You have no reminders")                
                    
            else:                
                speak("The reminders include: " + reminder_file.read())

        elif "clear reminders" in statement or "delete reminders" in statement or "remove reminders" in statement:
            reminder_file = open("data.txt", 'w')
            speak("All the reminders have been cleared")
        
        elif "new reminder" in statement or "create reminder" in statement or "add reminder" in statement or "create a reminder" in statement or "add a reminder" in statement:
            speak("What is the reminder?")
            data = takeCommand()
            speak("The following has been added as a reminder" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

        elif "create contact" in statement or "new contact" in statement or "add contact" in statement or "create a contact" in statement or "add a contact" in statement:
            speak("What name would you like to save it with")
            cname=takeCommand()
            speak("Enter the email id of the contact")
            mail=input("Email: ")
            try:                  
                file=open('email.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)
                    
                if cname in r.keys():
                    print("contact with name already exists") 
                    break                                                

                dict2={cname:mail}
                r.update(dict2)
                file.truncate(0)
                file.close()
                file=open('email.txt','w')
                w=file.write(str(r))
                file.close()
                speak("contact has been saved")
            except:
                file=open('email.txt','w')
                pp=str({cname:mail})
                file.write(pp)                
                file.close()
                speak("contact has been saved")
            
        elif "delete contact" in statement or "remove contact" in statement or "delete a contact" in statement or "remove a contact" in statement:
            file=open('email.txt','r')
            d=file.read()
            dr=ast.literal_eval(d)                
            file.close()
            speak("Whom do you want to remove")
            email=takeCommand()
            if email in dr.keys():                
                replaceAll("email.txt",email,"")
                replaceAll("email.txt",dr[email],"")
                speak(f"{email} has been removed from your contracts")
            else:
                speak("The name doesn't exist in your contracts")

        elif "email" in statement or "mail" in statement:
            try:
                speak("To whom shall I send it?")
                to = takeCommand()
                file=open('email.txt','r')
                d=file.read()
                r=ast.literal_eval(d)                
                file.close()
                if to in r.keys():           
                    To=r[to]
                else:
                    speak("This contact doesn't exist, you can add contacts by saying `create contact`")
                    break  
                speak("What is your email subject")
                subject = takeCommand()
                speak("What is the message for the email")
                content = takeCommand()
                                    
                msg = EmailMessage()
                                
                msg.set_content(content)
                msg['Subject'] = subject
                msg['From'] = "sbaijal55@gmail.com"
                msg['To'] = To

                sendEmail(msg)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")
                
        # elif 'volume up' in statement:
        #     pyautogui.press("volumeup")

        # elif 'volume down' in statement:
        #     pyautogui.press("volumedown")

        # elif 'mute the volume' in statement or 'volume mute':
        #     pyautogui.press("volumemute")

        elif 'shut down' in statement:
            os.system("shutdown /s /t /s")  

        elif 'restart' in statement:
            os.system("restart /r /t /s")

        elif 'sleep' in statement:
            os.system("rundll32.exe powrproof.dll,SetSuspendState 0,1,0")    

        elif 'offline' in statement or 'thank you' in statement:
            sys.exit() 

time.sleep(3)
