import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime
from config import TOKEN, GROUP_ID
people_stats = []


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if event.obj.message['from_id'] in people_stats:
                try:
                    a = [int(i) for i in event.obj.message['text'].split('-')]
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"{datetime.date(a[0], a[1], a[2]).strftime('%A')}",
                                     random_id=random.randint(0, 2 ** 64),
                                     group_id=GROUP_ID)
                except:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"Пожалуйста введите дату в формате YYYY-MM-DD",
                                     random_id=random.randint(0, 2 ** 64),
                                     group_id=GROUP_ID)
            else:
                people_stats.append(event.obj.message['from_id'])
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Привет,  я могу сказать в какой день недели была"
                                         " какая-нибудь дата. Введите дату в формате YYYY-MM-DD",
                                 random_id=random.randint(0, 2 ** 64),
                                 group_id=GROUP_ID)


if __name__ == '__main__':
    main()
