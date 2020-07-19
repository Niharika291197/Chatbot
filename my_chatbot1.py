from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

corpus_path = ('C://Users//nb291\\Desktop\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english//')

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)
while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('NishBot: Bye')
        break










    else:
        reply = bot.get_response(message)
        print('NishBot:', reply)
