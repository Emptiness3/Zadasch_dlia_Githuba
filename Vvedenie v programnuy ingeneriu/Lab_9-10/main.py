from brain import Brain
 
brain = Brain()
prompt = "Я отвечу на любой вопрос да или нет, каков он будет?"
 
question = " "
while question != "Прекрати": 
    print(prompt, end = ' ')
    answer = brain.think(input())
    print(answer)