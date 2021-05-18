# -*- coding: utf-8 -*-
"""
Types of Responses
1. Speech           ::Spch
2. image + Speech   ::imgSpch
3. image            ::img
4. Diagnostic Qs

----for future work---
5. Ask Options      ::opt
6. Video            ::vid
7. Text             ::txt
"""

keys_Action={"picture":["img","corona3"], 
             "spread":["img","coronamap"], 
             
             "infect":["imgSpch","People of all ages can be infected by the new coronavirus (2019-nCoV). Older people, and people with pre-existing medical conditions (such as asthma, diabetes, heart disease) appear to be more vulnerable to becoming severely ill with the virus.","risk"],
             "transmission":["imgSpch","Coronavirus disease spreads primarily through contact with an infected person when they cough or sneeze. It also spreads when a person touches a surface or object that has the virus on it, then touches their eyes, nose, or mouth.","transmit"], 
             
             "virus":["Spch","Viruses are microscopic parasites, generally much smaller than bacteria. They lack the capacity to thrive and reproduce outside of a host body."],
             "corona":["Spch","Coronavirus disease (COVID-19) is an infectious disease caused by a new virus."],             
             
             
             "exit":["exit","Good Bye and Take Care friend !"],
             "close":["exit","Have a nice Day!"]
             
             }