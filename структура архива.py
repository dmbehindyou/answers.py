import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, group_id)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            response = vk.users.get(user_ids=event.obj.message['from_id'], fields='city')
            print(response)
            if 'city' in response[0]:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Привет, {response[0]['first_name']}!\nКак поживает {response[0]['city']['title']}?",
                                 random_id=random.randint(0, 2 ** 64),
                                 group_id=group_id)
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Привет, {response[0]['first_name']}!",
                                 random_id=random.randint(0, 2 ** 64),
                                 group_id=group_id)


if __name__ == '__main__':
    main()
