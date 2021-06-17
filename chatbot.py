from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
print("Required modules are successfully imported....")
my_bot = ChatBot(name='MyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
talk1 = ['hi there!',
              'hi!',
              'how do you do?',
              'Cool as always'
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'good',
              'Thats awesome to hear'
         'not so good',
              'sorry to hear that.',
              'I need your assistance regarding my order',
              'Please, Provide me with your order id',
              'I have a complaint.',
              'Please elaborate, your concern',
              'How long it will take to receive an order ?',
              'An order takes 3-5 Business days to get delivered.',
              'The product delivered is damaged',
              'Oh! we are really sorry for! please provide your order'
talk2 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
         list_trainer = ListTrainer(my_bot)
for item in (talk1, talk2):
    list_trainer.train(item)
print("Training of chatbot is completed")
name=input("Enter Your Name: ")
print("Hey welcome " + name + "! Let's chat!!!")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Ok Bye. See you then!!')
        break
    else:
        response=my_bot.get_response(request)
        print('Bot:',response)
