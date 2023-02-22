from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


interview_kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb1_A = KeyboardButton('A. Прилив сил')
interview_kb1_B = KeyboardButton('B. Невесомость')
interview_kb1_C = KeyboardButton('C. Атмосферное давление')
interview_kb1_D = KeyboardButton('D. Жажду')
interview_kb1.add(interview_kb1_A).add(interview_kb1_B).add(interview_kb1_C).add(interview_kb1_D)

interview_kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb2_A = KeyboardButton('A. Смокинг')
interview_kb2_B = KeyboardButton('B. Треники')
interview_kb2_C = KeyboardButton('C. Джемпер с оленями')
interview_kb2_D = KeyboardButton('D. Любимый мерч от билайн')
interview_kb2.add(interview_kb2_A).add(interview_kb2_B).add(interview_kb2_C).add(interview_kb2_D)

interview_kb3 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb3_A = KeyboardButton('A. Пачку купюр')
interview_kb3_B = KeyboardButton('B. Пароль доступа')
interview_kb3_C = KeyboardButton('C. Носовой платок')
interview_kb3_D = KeyboardButton('D. Телефон')
interview_kb3.add(interview_kb3_A).add(interview_kb3_B).add(interview_kb3_C).add(interview_kb3_D)

interview_kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb4.\
    add(KeyboardButton('A. На Ягуаре')).\
    add(KeyboardButton('B. На ракете')).\
    add(KeyboardButton('C. На малиновой Ладе')).\
    add(KeyboardButton('D. На электросамокате'))

interview_kb5 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb5.\
    add(KeyboardButton('A. Måneskin')).\
    add(KeyboardButton('B. Баста')).\
    add(KeyboardButton('C. Филипп Киркоров')).\
    add(KeyboardButton('D. Nirvana'))

interview_kb6 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb6.\
    add(KeyboardButton('A. За цветами')).\
    add(KeyboardButton('B. На Альдебаран')).\
    add(KeyboardButton('C. В кондитерскую')).\
    add(KeyboardButton('D. Обкашлять вопросики'))

interview_kb7 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb7.\
    add(KeyboardButton('A. Бывшую')).\
    add(KeyboardButton('B. Чужого')).\
    add(KeyboardButton('C. Кавказскую овчарку')).\
    add(KeyboardButton('D. Начальника'))

interview_kb8 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb8.\
    add(KeyboardButton('A. Дефлопе с семечками кациуса')).\
    add(KeyboardButton('B. Доширак')).\
    add(KeyboardButton('C. Гренки с чесноком')).\
    add(KeyboardButton('D. Художник должен быть голодным ☝🏻'))

interview_kb9 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb9.\
    add(KeyboardButton('A. Просеко')).\
    add(KeyboardButton('B. Колу')).\
    add(KeyboardButton('C. Чёрный кофе')).\
    add(KeyboardButton('D. Пенное'))

interview_kb10 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb10.\
    add(KeyboardButton('A. Романтический закат')).\
    add(KeyboardButton('B. Не имеет значения')).\
    add(KeyboardButton('C. Детская площадка')).\
    add(KeyboardButton('D. Огни большого города'))

interview_kb11 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb11.\
    add(KeyboardButton('A. На модном показе')).\
    add(KeyboardButton('B. На концерте бардовской песни')).\
    add(KeyboardButton('C. На работе')).\
    add(KeyboardButton('D. В Сызрани'))

interview_kb12 = ReplyKeyboardMarkup(resize_keyboard=True)
interview_kb12.\
    add(KeyboardButton('A. Ok')).\
    add(KeyboardButton('B. Да ладно')).\
    add(KeyboardButton('C. Спасибо')).\
    add(KeyboardButton('D. Будем!'))
