
"""
Dictionaries
"""

import speech_recognition as speech
import pyttsx3
import webbrowser

engine=pyttsx3.init()

engine.setProperty('rate',200)

sport={"cricket":["WB","https://www.espncricinfo.com/","Cricket is the most popular game in the world"],
       "football":["Img","It is most popular game in US"],
       "badminton":["Spch","It is one of the games in olympics"],
       "tennis":"Tennis can be played on different types of grounds",
       "basketball":"Each team of basketball has 5 players"}


while True:
    try:
        activate=input("Press s to start and q to quit")
        
        if activate=='s':
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            
            for keyword in sport:
                if keyword in command:
                    if sport[keyword][0]=="Spch":
                        print(sport[keyword][1])
                        engine.say(sport[keyword][1])
                        engine.runAndWait()
                    if sport[keyword][0]=="WB":
                        print(sport[keyword][1])
                        webbrowser.open(sport[keyword][1])
                        
                   
        else:
            break
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    
engine.say("Thanks for interaction!!")
engine.runAndWait()    
print("Thanks for interaction!!")  
           
                


