
"""
Dictionaries
"""

import speech_recognition as speech
import pyttsx3
import pygame
import vlc
import time
import winsound
from datetime import datetime

#Initialize the Speech Generation Library
engine=pyttsx3.init()
engine.setProperty('rate',200)

#Initialize Pygame
pygame.init()

#Create Screen with size 900x600
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('CookBot')

#Display the Background Image
bg=pygame.image.load("images/bg1.jpg").convert_alpha()
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()


#Dictionary for Sport Alexa
actions={
      
      
       "rice":["Video","videos/AyushSpandan.mp4"],
       "poha":["Video","videos/Aneesh & Yash.mp4"],
       "stop":["stop"],
       "schedule":["10:35","Time to drink Water","08:00","Time to breakfast","13:00","Time to have lunch"],
       "exit":["exit","Thanks for Interaction"]}



activate="none"
exitstatus="no"
   

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #To Read whether 'c' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("C pressed")
                    
                    
                
        #            Running time check and generating alarm as per the schedule
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        for i in range(0,5,2):
            if actions["schedule"][i] == current_time:
                winsound.Beep(5000,1000)
                engine.say(actions["schedule"][i+1])
                engine.runAndWait() 
                time.sleep(10)
               
               
                
                
        #If 'c' key is pressed
        if activate=='c':
            #Change the background image to Listening Image
            listenImg=pygame.image.load("images/bg2.jpg").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in actions:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                    
                    #Check the response type for that keyword                    
                  
                    
                        
                         
                    if actions[keyword][0]=="Video":
#                       
                        # creating vlc media player object
                        media = vlc.MediaPlayer(actions[keyword][1])
#                        media = vlc.MediaPlayer("videos/AyushSpandan.mp4")
 
                        # start playing video
                        media.play()
                        
                    if actions[keyword][0]=="stop":
                        media.stop()
                        
                     
                    if actions[keyword][0]=="exit":
                        engine.say(actions[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break

                
            
            #if 'exit' in command then break from while loop        
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("images/bg1.jpg").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                


