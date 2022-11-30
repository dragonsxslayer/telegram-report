import requests

def report(message):  
    params = {
    "text": message,
    "parse_mode": "Markdown"}   
    bot_token = "bot_token"
    bot_chatID = "ChatId"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID
    response = requests.get(send_text,params=params)
    return response.json()
