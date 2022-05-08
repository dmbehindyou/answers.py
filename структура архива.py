import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    answer = []
    response = vk.friends.get(fields='bdate')
    if response['items']:
        for i in response['items']:
            if 'bdate' in i:
                answer.append(f"{i['last_name']} {i['first_name']} {i['bdate']}")
            else:
                answer.append(f"{i['last_name']} {i['first_name']}")
    answer.sort()
    for people in answer:
        print(people)


if __name__ == '__main__':
    main()
