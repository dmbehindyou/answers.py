import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime


def main():
    vk_session = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(vk_session, 180690386)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            flag = True
            for i in ['время', 'число', 'дата', 'день']:
                if i in event.obj.message['text']:
                    resp = f"{datetime.datetime.now()} {datetime.datetime.now().strftime('%A')}"
                    print(resp)
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=resp,
                                     random_id=random.randint(0, 2 ** 64),
                                     group_id=group_id)
                    flag = False
                    break
            if flag:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Напишите одно из следующих слов, чтобы "
                                         "получить время по МСК: время, число, дата, день.",
                                 random_id=random.randint(0, 2 ** 64),
                                 group_id=group_id)


if __name__ == '__main__':
    main()
