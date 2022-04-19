import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token="Введите токен вашего сообщества")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, введите id вышего сообщетва)

def sender(id, text):
    vk_session.method('messages.send', {
        'chat_id': id,
        'message': text,
        'random_id': 0,
    })

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:

            id = event.chat_id
            msg = event.object.message['text']

            # Бот отвечает на сообщения пользователя
            if msg == 'Привет':
                sender(id, 'Привет, я бот для беседы в ВК!')
            elif msg == 'Как дела, бот?':
                sender(id,'Отлично! У вас как?')
