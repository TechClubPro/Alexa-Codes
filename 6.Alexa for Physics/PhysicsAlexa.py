import pyttsx3
import speech_recognition as speech
import pygame, sys
import time
import keysDict as keys

screen =[]
words=''
state="wait"
imagePath=""
key_flag = 'z'

def UI_init(bg):
    width=900
    height= 600
    global screen
    screen=pygame.display.set_mode( ( width, height) )
    
    #Set a Title of Screen
    pygame.display.set_caption('Covexa')
    bg=pygame.image.load("images/"+ bg +".jpg").convert_alpha()
    screen.blit(bg,(0,0))
    pygame.display.update()
    
def show_image(img):
    if img!= '':        
        image=pygame.image.load("images/"+ img +".jpg")
        image=pygame.transform.scale(image, (813,375))
        screen.blit(image,(45,145))
            
def start_listening():
            
    r = speech.Recognizer() 
    with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            print("Speak:")
            audio = r.listen(source)
    command=r.recognize_google(audio)
    print("You said" + command)
    return command 


def parseInput(keyword):
    
    __path =''
    __imgpath=''
    __state=''
    time.sleep(0.1)
    for i in keys.keys_Action:
        
        if i in keyword :
            
            if keys.keys_Action[i][0]=="img":
               __state="showImg"
               __imgpath=keys.keys_Action[i][1]
               
            if keys.keys_Action[i][0]=="imgSpch":
               __state="ImgSpch"
               __imgpath=keys.keys_Action[i][2]
               __path = keys.keys_Action[i][1]             
            
               
            if keys.keys_Action[i][0]=="Spch":
               __state="speak"
               __path = keys.keys_Action[i][1]
               
            if keys.keys_Action[i][0]=="exit":
               __state="exit"
               __path = keys.keys_Action[i][1] 
               
    return __state,__path,__imgpath

"""
"""

engine = pyttsx3.init()
engine.setProperty("rate",152)
pygame.init()
UI_init('bg1')
pygame.display.update()

while True: 
    
    
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#                movie.stop()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    key_flag = 'c'
                    print("C pressed")
                    
               
        if state=="wait":             
            if key_flag == 'c':
                UI_init('bg2')
                pygame.display.update()
                
                state="listen"
                
        if state=="listen":            
            words = start_listening().lower()
            parsed = parseInput(words)
                        
            if parsed[0] == "showImg":
                UI_init('bg1')
                
                show_image(parsed[2])
                state="reset"
                
            elif parsed[0]=="speak":
                UI_init('bg1')
                
                engine.say(parsed[1])
                engine.runAndWait() 
                state="reset"
                
            elif parsed[0]=="ImgSpch":
                UI_init('bg1')
                
                show_image(parsed[2])
                pygame.display.update()
                
                engine.say(parsed[1])
                engine.runAndWait()
                state="reset"
                
            elif parsed[0]=="exit":
                            
                engine.say(parsed[1])
                engine.runAndWait()
                break
            else:
                UI_init('bg1')
                state ="reset"
            
        if state=="reset":
            key_flag='z'
            state="wait" 
   
        pygame.display.update()
        time.sleep(0.1)
        
   
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    
print ('Closing')
pygame.quit()
sys.exit()