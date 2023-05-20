from bardapi import Bard
import config

token = config.apikey
bard = Bard(token=token)

def bardBot(que):
  return bard.get_answer(que)['content']
    



