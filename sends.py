import requests
def send_message(url,chat_id: int, text, parse_mode=None):
    endpoint = "/sendMessage"
    url+=endpoint
    payload = {
        "chat_id":chat_id,
        "text":text
    }
    if parse_mode:
        payload['parse_mode']="HTML"
    requests.get(url,params=payload)
def send_contact(url,chat_id: int, phone_number:str,first_name:str,last_name:str, parse_mode=False):
    endpoint = "/sendContact"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "phone_number":phone_number,
        "first_name":first_name,
        "last_name":last_name
    }
    if parse_mode:
        payload['parse_mode'] = True
    requests.get(url,params=payload)

def send_photo(url,chat_id: int, photo, has_spoiler,parse_mode=False):
    endpoint = "/sendPhoto"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "photo":photo,
        "has_spoiler":has_spoiler
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)

def send_location(url:str,chat_id: int,latitude, longitude,heading,protect_content,parse_mode=False):
    endpoint = "/sendLocation"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "latitude":latitude,
        "longitude":longitude,
        "heading":heading,
        "protect_content":protect_content

    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)

def send_audio(url,chat_id: int, audio,caption, parse_mode=False):
    endpoint = "/sendAudio"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "audio":audio,
        "caption":caption
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)

def send_document(url,chat_id: int, document,caption, protect_content,parse_mode=False):
    endpoint = "/sendDocument"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "document":document,
        "caption": caption,
        "protect_content":protect_content
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)

def send_dice(url,chat_id: int, dice, disable_notification,parse_mode=False):
    endpoint = "/sendDice"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "emoji":dice,
        "disable_notification":disable_notification
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)
def send_animation(url,chat_id: int, animation,duration, parse_mode=False):
    endpoint = "/sendAnimation"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "animation":animation,
        "duration":duration
    }
    if parse_mode :
        payload["parse_mode"] = "HTML"
    requests.get(url,params=payload)

def send_poll(url,chat_id: int,question, options, parse_mode=False):
    endoint = "/sendPoll"
    url += endoint
    payload = {
        "chat_id":chat_id,
        "question":question,
        "options":options
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)

def send_venue(url,chat_id: int, latitude,longitude,title,address, parse_mode=False):
    endpoint = "/sendVenue"
    url += endpoint
    payload = {
        "chat_id":chat_id,
        "latitude":latitude,
        "longitude":longitude,
        "title":title,
        "address":address
    }
    if parse_mode:
        payload['parse_mode'] = "HTML"
    requests.get(url,params=payload)