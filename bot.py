import requests
from settings import url
from time import sleep
from sends import send_message,send_contact,send_photo,send_location,send_audio,send_document,send_dice,send_animation
from sends import send_poll,send_venue
def get_updets(url:str):
    endpoint = "/getUpdates"
    url += endpoint
    respons = requests.get(url)
    if respons.status_code == 200:
        result = respons.json()['result']
        if len(result)!=0:
            return result[-1]
        else:
            return 404
    else:
        respons.status_code
# print(get_updets(url))
def main(url:str):
    last_update_id = -1
    while True:
        curent_update = get_updets(url)
        if curent_update['update_id']!=last_update_id:
            user = curent_update['message']['from']
            text1 = curent_update['message'].get('text')
            text2 = curent_update['message'].get('contact')
            text3 = curent_update['message'].get('photo')
            text4 = curent_update['message'].get('location')
            text5 = curent_update['message'].get("audio")
            doc = curent_update['message'].get("document")
            dice = curent_update['message'].get("dice")
            animat = curent_update['message'].get("animation")
            poll = curent_update['message'].get("poll")
            venue = curent_update['message'].get('venue')
            if text1!=None:
                send_message(url,user['id'],text1)
            elif text2!=None:
                send_contact(url,user['id'],text2['phone_number'],text2['first_name'],text2['last_name'])
            elif text3!=None:
                print(text3)
                send_photo(url=url,chat_id=user['id'],photo=text3[0]['file_id'],has_spoiler=True)
            elif text4!=None:
                print(text4)
                send_location(url=url,chat_id=user['id'],latitude=text4['latitude'],longitude=text4['longitude'],heading=2,protect_content=True)
            elif text5!=None:
                send_audio(url,user['id'],text5['file_id'],caption="Audio file ")
            elif doc!=None:
                send_document(url,user['id'],doc['file_id'],caption="Documitatsiya",protect_content=True)
            elif dice!=None:
                send_dice(url,user['id'],dice['emoji'],disable_notification=True)
            elif animat != None:
                print(animat)
                send_animation(url,user['id'],animat,duration=10)
            elif poll != None:
                print(poll['question'])
                send_poll(url,user['id'],question=poll['question'],options=poll['options'])
            elif venue != None:
                print(venue)
                send_venue(url,user['id'],latitude = 12, longitude=15,title="Python SendVenue",address="Samarqand viloyati")
            last_update_id = curent_update['update_id']
        sleep(0.3)
main(url)