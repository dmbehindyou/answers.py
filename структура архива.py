import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from config import TOKEN, LOGIN, PASSWORD, ALBUM_ID, OWNER_ID, GROUP_ID


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            response = vk.users.get(user_ids=event.obj.message['from_id'])
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Привет, {response[0]['first_name']}!",
                             attachment=f"photo{OWNER_ID}_{get_picture()}",
                             random_id=random.randint(0, 2 ** 64),
                             group_id=GROUP_ID)


def get_picture():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    res = vk.photos.get(album_id=ALBUM_ID, owner_id=OWNER_ID)
    ans = []
    for i in res['items']:
        ans.append(i['id'])
    return ans[random.randrange(len(ans))]


if __name__ == '__main__':
    main()
