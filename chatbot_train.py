from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')


bot = ListTrainer(bot)

trainer = ListTrainer(ChatBot)


for files in os.listdir('C://Users//nb291\\Desktop\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english//'):
           data = open('C://Users//nb291\\Desktop\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english//' + files , 'r').readlines()
           bot.train(data)

while True:
           message = input('You : ')
           if message.strip() != 'Bye':
                    reply = bot.get_response(message)
                    print('NishBot : ',reply)
           if message.strip() == 'Bye':
                    print('NishBot : Bye')
                    break
