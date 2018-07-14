from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot training algorithm')
bot.set_trainer(ListTrainer)

for files in os.listdir('/home/pi/Desktop/AI/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data = open('/home/pi/Desktop/AI/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files , 'r').readlines()
    bot.train(data)
