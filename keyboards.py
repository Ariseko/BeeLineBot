from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Погнали!', callback_data='go'))

choose_kb = InlineKeyboardMarkup(row_width=2)
choose_kb.add(InlineKeyboardButton(text='Викторина', callback_data='victorina'),
              InlineKeyboardButton(text='Интервью', callback_data='interview'))

loop_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Поехали', callback_data='interview'))

victorina_kb1 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Прыжок в высоту с места', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Перетягивание каната', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Метание гранаты', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Скандинавская ходьба', callback_data='D'))


victorina_kb2 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Луи Шевроле', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Генри Форд', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Готтлиб Даймлер', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Альфьери Мазерати', callback_data='D'))

victorina_kb3 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Пиво', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Бекон', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Мята', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Гранат', callback_data='D'))

victorina_kb4 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Gucci', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Maison Margiela', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Bottega Veneta', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Vivienne Westwood', callback_data='D'))

victorina_kb5 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Погремушка', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Дудка', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Арфа', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Барабан', callback_data='D'))

victorina_kb6 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Калининградский институт психологии', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Высшая школа режиссеров и сценаристов в Санкт-Петербурге', callback_data='B'),
                                                      InlineKeyboardButton(text='C. Российский университет дружбы народов', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Сибирский государственный университет телекоммуникаций и информатики', callback_data='D'))

victorina_kb7 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Лицо', callback_data='A'),
                                                      InlineKeyboardButton(text='В. Запястья', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Ноги', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Волосы', callback_data='D'))

victorina_kb8 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Астон Мартин', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Гиннес', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Ким Кардашьян', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Челси', callback_data='D'))


victorina_kb9 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. По дороге они ели только пончики', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Им обоим было по 84 года', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Во время поездки они непрерывно пели', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Весь путь был проделан задним ходом', callback_data='D'))

victorina_kb10 = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='А. Распознавать блюда', callback_data='A'),
                                                      InlineKeyboardButton(text='B. Определять свежесть продуктов', callback_data='B'),
                                                      InlineKeyboardButton(text='С. Общаться через голосового помощника', callback_data='C'),
                                                      InlineKeyboardButton(text='D. Скачивать новые рецепты из интернета', callback_data='D'))



