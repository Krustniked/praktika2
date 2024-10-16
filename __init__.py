import requests
from telebot import TeleBot
import json

API_TOKEN = 'ЗДЕСЬ ВАШ ТОКЕН' 
API_URL = 'http://127.0.0.1:5000/api/AskQuestion'  

bot = TeleBot(API_TOKEN)

@bot.message_handler()
def get_answer(message):
    try:
        # Получаем текст сообщения от пользователя
        user_text = message.text  
       

        text_to_send = user_text

        
        response_data = {
            
            'question': text_to_send
        }

        
        response = requests.post(API_URL, json=response_data)

        
        if response.status_code != 200:
            return bot.reply_to(message, "Ошибка при обращении к API.")
            
        
       

        api_response = response.json()  
        answer = api_response.get("answer")
        
        if not answer:
            return bot.reply_to(message, "на данный вопрос к сожалению нет ответа в моей базе, но я уведомлю об этом хозяина, вы можете позвонить по номерам телефонов (+7 495 800–10–01) и (+7 800 100–00–11)")

        bot.reply_to(message, f"{answer}")

    except Exception as e:
        bot.reply_to(message, "Произошла ошибка: " + str(e))

if __name__ == '__main__':
    bot.polling()
