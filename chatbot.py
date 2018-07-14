from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Chatbot for youtube', logic_adapters=[
                                            {
                                                'import_path': 'chatterbot.logic.BestMatch'
                                            },

                                            {
                                                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                                                'threshold': 0.65,
                                                'default_response': 'I am Sorry, but I do not understand.'
                                            }
                                        ]
              )
bot.set_trainer(ListTrainer)
    
while True:
    message = raw_input('You: ')    
    if message.strip() != 'Bye':                
        os.system("espeak -ven+m3 -k5 -s150 " + "'" + message + "'")        
        reply = str(bot.get_response(message))
        reply = reply.replace("-","")
        print('ChatBot:',reply)        
        os.system("espeak -ven+f3 -k5 -s150 " + "'" + reply + "'")
        
        
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break
