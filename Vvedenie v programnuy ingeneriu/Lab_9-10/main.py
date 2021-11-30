'___________________'
'Гадалка'
'___________________'
from brain import Brain
 
brain = Brain()
prompt = "Что Вас интересует?"
 
question = ""
while question != "хватит": 
    print(prompt, end = ' ')
    answer = brain.think(input())
    if brain.think(input()) == 'хватит':
        exit()
    else:
        print(answer)