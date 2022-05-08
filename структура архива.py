import vk_api, datetime


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5)
    if response['items']:
        for i in response['items']:
            dt = str(datetime.datetime.fromtimestamp(i['date'])).split(' ')
            print(f"{i['text']};\ndate: {dt[0]}, time: {dt[1]}")


if __name__ == '__main__':
    main()
