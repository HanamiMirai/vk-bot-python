##### Простенький вк бот на Python который будет отвечать на сообщения.
---
Настройка бота:
1. [Как скачать Python](https://www.youtube.com/watch?v=KY9jJ3kghq4) и [как установить vk api](https://habr.com/ru/post/319178/)
2. [Настройка вашего сообщетсва для бота](https://scripthub.ru/bots/bots-vk/11-nastrojka-bota-v-gruppe.html)
3. Введите токен вашего сообщества (строка 4), [как получить токен сообщества вк.](https://pechenek.net/social-networks/vk/api-vk-poluchaem-klyuch-dostupa-token-gruppy/)
    `vk_session = vk_api.VkApi(token="Введите токен вашего сообщества")`
3. Введите id вашего сообщества (строка 6), [как узнать id моего сообщества.](https://regvk.com/id/)
    `longpoll = VkBotLongPoll(vk_session, введите id вашего сообщества)`
---
Ну вот и все, вы подключили ваше сообщество, теперь можете поэкспериментировать с кодом, например добавить отправку картинок, видео или аудио по команде.
Ознакомиться с Vk Api можете на [официальном сайте](https://dev.vk.com/api/getting-started).
