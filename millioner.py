from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api, vk
vk_session = vk_api.VkApi(token='vk1.a.j6NrFQtNoax1X8ZH-negiJhycwa8Kw4ozEs3dQjA5WqrxrjzAah4dlAaQgj4DTOU56IaqAjL66ZPHD-fTGO0_ZOWNcw78S1Lp-ddmwkmZ9Lm2qLGcprXEANpqgGiAvi6xDcMEq9YEPtdZ-8A9uWiPKluNl-sIL-SHEnmO_y4RAxgaOmq6clfCV7Om0pgj8yTF2li2jIcQ7LZDx2hf56Ebw')
# задаем токен полученный в сообществе вк

longpoll = VkLongPoll(vk_session) # задаем longpoll
vk = vk_session.get_api()

def send_message(user_id, message, keyboard=None):
    post = {
                    "user_id": user_id,
                    "message": message,
                    "random_id": 0,
                    "keyboard": keyboard.get_keyboard()
    }
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post
    vk_session.method("messages.send", post)


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        text = event.text
        user_id = event.user_id
        start = {"Начать"}
        retry = {"start"}
        navigation = {"I. 50 на 50", "I. Звонок другу"}
        navigation1 = {"II. 50 на 50", "II. Звонок другу"}
        navigation2 = {"III. 50 на 50", "III. Звонок другу"}
        navigation3 = {"IV. 50 на 50", "IV. Звонок другу"}
        navigation4 = {"V. 50 на 50", "V. Звонок другу"}


        if text == "start":
            keyboard = VkKeyboard(one_time=True)
            for btn in start:
                keyboard.add_button(btn)
            send_message(user_id, "Вас приветсвует программа Кто хочет стать миллионером? и я его ведущий, позвольте представиться, бот. \nОтветьте на 5 вопросов и миллион ваш.", keyboard)

        if text == "Начать":
            keyboard = VkKeyboard()
            keyboard.add_button("I. Малиновый берет.")
            keyboard.add_line()
            keyboard.add_button("II. Черную кепку.")
            keyboard.add_line()
            keyboard.add_button("III. Бежевую панаму.")
            keyboard.add_line()
            keyboard.add_button("IV. Был лысым.")
            keyboard.add_line()
            for btn in navigation:
                keyboard.add_button(btn)
            send_message(user_id, "Какой головной убор был во время бала на Татьяне Лариной, героине романа «Евгений Онегин»?", keyboard)

        if text == "I. 50 на 50":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Малиновый берет.")
            keyboard.add_line()
            keyboard.add_button("IV. Был лысым.")
            keyboard.add_line()
            for btn in navigation:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали подсказку 50 на 50. Два неверных вопроса исчезли", keyboard)

        if text == "I. Звонок другу":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Малиновый берет.")
            keyboard.add_line()
            for btn in navigation:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали звонок другу. Друг подсказывает что это ответ I. Малиновый берет", keyboard)


        if text == "II. Черную кепку.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "III. Бежевую панаму.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "IV. Был лысым.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "I. Малиновый берет.":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Коммивояжером.")
            keyboard.add_line()
            keyboard.add_button("II. Местным шерифом.")
            keyboard.add_line()
            keyboard.add_button("III. Его зубным врачом.")
            keyboard.add_line()
            keyboard.add_button("IV. Его мясником.")
            keyboard.add_line()
            for btn in navigation1:
                keyboard.add_button(btn)
            send_message(user_id, "И это правильный ответ. Следующий вопрос. \nКем был мужчина, послуживший моделью для известной картины «Американская готика» Гранта Вуда?", keyboard)

        if text == "II. Звонок другу":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("III. Его зубным врачом.")
            keyboard.add_line()
            for btn in navigation1:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали звонок другу. Друг подсказывает, что это ответ III. Его зубным врачом", keyboard)

        if text == "II. 50 на 50":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("II. Местным шерифом.")
            keyboard.add_line()
            keyboard.add_button("III. Его зубным врачом.")
            keyboard.add_line()
            for btn in navigation1:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали подсказку 50 на 50. Два неверных вопроса исчезли", keyboard)

        if text == "I. Коммивояжером.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "II. Местным шерифом.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "IV. Его мясником.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "III. Его зубным врачом.":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Мотылек.")
            keyboard.add_line()
            keyboard.add_button("II. Таракан.")
            keyboard.add_line()
            keyboard.add_button("III. Муха.")
            keyboard.add_line()
            keyboard.add_button("IV. Японский хрущик.")
            keyboard.add_line()
            for btn in navigation2:
                keyboard.add_button(btn)
            send_message(user_id, "И это правильный ответ. Следующий вопрос. \nКакое насекомое вызвало короткое замыкание в ранней версии вычислительной машины, тем самым породив термин «компьютерный баг» («баг» в переводе с англ. «насекомое»)?", keyboard)

        if text == "III. Звонок другу":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Мотылек.")
            keyboard.add_line()
            for btn in navigation2:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали звонок другу. Друг подсказывает, что это ответ I.", keyboard)

        if text == "III. 50 на 50":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Мотылек.")
            keyboard.add_line()
            keyboard.add_button("IV. Японский хрущик.")
            keyboard.add_line()
            for btn in navigation2:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали подсказку 50 на 50. Два неверных вопроса исчезли", keyboard)

        if text == "II. Таракан.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "III. Муха.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "IV. Японский хрущик.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "I. Мотылек.":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Ананас.")
            keyboard.add_line()
            keyboard.add_button("II. Вишня.")
            keyboard.add_line()
            keyboard.add_button("III. Абрикос.")
            keyboard.add_line()
            keyboard.add_button("IV. Кокос.")
            keyboard.add_line()
            for btn in navigation3:
                keyboard.add_button(btn)
            send_message(user_id, "И это правильный ответ. Следующий вопрос. \nИз каких плодов можно получить копру?", keyboard)

        if text == "IV. Звонок другу":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("IV. Кокос.")
            keyboard.add_line()
            for btn in navigation3:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали звонок другу. Друг подсказывает, что это ответ IV.", keyboard)

        if text == "IV. 50 на 50":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("III. Абрикос.")
            keyboard.add_line()
            keyboard.add_button("IV. Кокос.")
            keyboard.add_line()
            for btn in navigation3:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали подсказку 50 на 50. Два неверных вопроса исчезли", keyboard)

        if text == "I. Ананас.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "II. Вишня.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "III. Абрикос.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "IV. Кокос.":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Гугол.")
            keyboard.add_line()
            keyboard.add_button("II. Мегатрон.")
            keyboard.add_line()
            keyboard.add_button("III. Гигабит.")
            keyboard.add_line()
            keyboard.add_button("IV. Наномоль.")
            keyboard.add_line()
            for btn in navigation4:
                keyboard.add_button(btn)
            send_message(user_id, "И это правильный ответ. Следующий вопрос. \nПод каким названием известна единица с последующими ста нулями?", keyboard)

        if text == "V. Звонок другу":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Гугол.")
            keyboard.add_line()
            for btn in navigation4:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали звонок другу. Друг подсказывает, что это ответ I.", keyboard)

        if text == "V. 50 на 50":
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button("I. Гугол.")
            keyboard.add_line()
            keyboard.add_button("IV. Наномоль.")
            keyboard.add_line()
            for btn in navigation4:
                keyboard.add_button(btn)
            send_message(user_id, "Вы выбрали подсказку 50 на 50. Два неверных вопроса исчезли", keyboard)

        if text == "I. Гугол.":
            keyboard = VkKeyboard(one_time=True)
            for btn in start:
                keyboard.add_button(btn)
            send_message(user_id, " Поздравляем. Вы ответили правильно на все вопросы. Миллион ваш.", keyboard)

        if text == "II. Мегатрон.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

        if text == "III. Гигабит.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)


        if text == "IV. Наномоль.":
            keyboard = VkKeyboard(one_time=True)
            for btn in retry:
                keyboard.add_button(btn)
            send_message(user_id, "И это неверный ответ. Жаль, миллион был так близко, но не отчаивайтесь, можно начать заново.", keyboard)

