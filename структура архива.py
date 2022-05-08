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
    res = vk.photos.get(album_id=ALBUM_ID, owner_id=OWNER_ID, photo_sizes=1)
    for i in res['items']:
        print(f"url: {i['sizes'][0]['url']}, высота: {i['sizes'][0]['height']}, ширина: {i['sizes'][0]['width']};")


if __name__ == '__main__':
    main()
