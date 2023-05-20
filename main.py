from brain import bardBot

flag = 1
from_name = "User"
to_name = "Bard"

def bot_answer_fun(answer):
    print(f"{to_name}: {answer}")

print("\nWelcome to Bard, an AI Assistant app powered by the Bard API.\nWhether you need assistance, creative text generation, or various tasks performed,\nBard is here to help!\nTo exit type--> Bye")

while flag:
  user_que = input(f"\n{from_name}: ")

  if(user_que.lower() == 'Bye'.lower()):
      bot_answer_fun(bardBot("Bye Bard"))
      flag = 0
  
  else:
      bot_answer_fun(bardBot(user_que))
       