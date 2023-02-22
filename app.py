import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image, ImageDraw, ImageFont
from keyboards import *
from datetime import datetime
from interviewKeyboards import *
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

import time
import os
import json
import requests
import random
import sqlite3 as sq

hookURL = 'https://hook.eu1.make.com/l22pqcigfqm286out21fe66axr0hq5mr'
victorinaHookURL = 'https://hook.eu1.make.com/68vjopg1h0anw104m24vrabymm3atuag'


class FSMtest(StatesGroup):
    start = State()
    getRealName = State()
    fork = State()
    newFork = State()

    interviewStart = State()
    interviewStep1 = State()
    interviewStep2 = State()
    interviewStep3 = State()
    interviewStep4 = State()
    interviewStep5 = State()
    interviewStep6 = State()
    interviewStep7 = State()
    interviewStep8 = State()
    interviewStep9 = State()
    interviewStep10 = State()
    interviewStep11 = State()
    interviewStep12 = State()
    interviewStepFinal = State()

    victorinaStart = State()
    victorinaStep1 = State()
    victorinaStep2 = State()
    victorinaStep3 = State()
    victorinaStep4 = State()
    victorinaStep5 = State()
    victorinaStep6 = State()
    victorinaStep7 = State()
    victorinaStep8 = State()
    victorinaStep9 = State()
    victorinaStep10 = State()
    victorinaStepFinal = State()

    getUserName = State()


checkList = []

storage = MemoryStorage()
bot = Bot(token='6004408832:AAGUScIPnYkCCg1GuMfxAbeiDpbsBkC-zvE')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['menu'], state='*')
async def menu(message: types.Message):
    if message.from_user.id in checkList:
        await message.answer('<b>Вы вернулись</b> в главное меню', reply_markup=choose_kb, parse_mode='html')
        await FSMtest.fork.set()
    else:
        await message.answer('<b>Вы вернулись</b> в главное меню', reply_markup=loop_kb, parse_mode='html')
        await FSMtest.fork.set()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    checkList.append(message.from_user.id)
    await message.answer('<b>Для начала немного формальностей =)</b>\nВпиши свои реальные имя и фамилию:',
                         parse_mode='html')
    await FSMtest.getRealName.set()


@dp.message_handler(state=FSMtest.getRealName)
async def gettingRealName(message: types.Message):
    try:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        data = {
            'date': f'{dt_string}',
            'username': f'{message.from_user.username}',
            'name': f'{message.text}',
            'id': f'{message.from_user.id}',
        }
        r = requests.post(hookURL, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        image = Image.open(f"pics/{random.randrange(1, 10)}.png")

        font = ImageFont.truetype("font/BeelineSans-Regular.ttf", 64)
        drawer = ImageDraw.Draw(image)

        drawer.text((1190 // 2, 1385), message.text.upper(), anchor='mm', font=font, fill='white')

        image.save(f'peoplePics/new_{message.from_user.username}_img.png')

        #await message.answer('С чего начнем: с интервью или викторины?', reply_markup=choose_kb)

        photo = open('victorina/start.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo)

        await message.answer('<b>👌🏻Сейчас мы соберем наш праздничный выпуск BeeMAN!</b>\n Тебя ждет 10 вопросов из '
            'разных рубрик   классических мужских журналов. Ответив на них, ты получишь персональную '
            'обложку и возможность выиграть брутальный приз. \n\nПризы получат 30 участников, которые дадут максимальное количество правильных ответов за минимальное время!\n<b>Поехали?</b>',
            reply_markup=start_kb, parse_mode='html')
        await FSMtest.victorinaStart.set()
    except:
        await message.answer('Вы уже зарегестрированы', reply_markup=choose_kb)

    #await FSMtest.fork.set()


# @dp.callback_query_handler(state=FSMtest.fork)
# async def activityChoose(callback: types.CallbackQuery, state: FSMContext):
#     if callback.data == 'interview':
#         await callback.message.answer(
#             '<b>Интервью - это прекрасно! </b>\nСейчас мы зададим тебе несколько вопросов, чтобы узнать о '
#             'твоем идеальном вечере. Ты в деле? \n\n(если что, то можно вернуться в главное меню '
#             'командой /menu)', reply_markup=start_kb, parse_mode='html')
#
#         await FSMtest.interviewStart.set()
#
#     elif callback.data == 'victorina':
#
#         photo = open('victorina/start.jpg', 'rb')
#         await bot.send_photo(callback.message.chat.id, photo=photo)
#
#         await callback.message.answer(
#             '<b>👌🏻Сейчас мы соберем наш праздничный выпуск BeeMAN!</b>\n Тебя ждет 10 вопросов из '
#             'разных рубрик   классических мужских журналов. Ответив на них, ты получишь персональную '
#             'обложку и возможность выиграть брутальный приз. \n\nПризы получат первые 30 участников, которые дадут максимальное количество правильных ответов, за минимально время!\n<b>Поехали?</b>',
#             reply_markup=start_kb, parse_mode='html')
#         await FSMtest.victorinaStart.set()


@dp.callback_query_handler(state=FSMtest.victorinaStart)
async def victorina1Step(callback: types.CallbackQuery, state: FSMContext):
    now = datetime.now()
    dt_start = now.strftime("%d/%m/%Y %H:%M:%S")
    async with state.proxy() as data:
        data['counter'] = 0
        data['dateStart'] = dt_start

    photo = open('victorina/rubriks/question1.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)
    await callback.message.answer('1. Какая из дисциплин лёгкой атлетики перестала быть олимпийским видом спорта?',
                                  reply_markup=victorina_kb1)
    await FSMtest.victorinaStep2.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep2)
async def victorina2Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'С 1900 по 1920 год <b>перетягивание каната</b> было одной из составляющих легкой атлетики. Всего за это ' \
                 'время было разыграно пять комплектов олимпийских наград. Медали в этой дисциплине завоёвывали ' \
                 'шведы, датчане, американцы и англичане.'

    if callback.data == 'B':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic1.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question2.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '2. Основатель какой автомобильной компании, названной в его честь, вынужден был работать в '
        'ней простым механиком? ', reply_markup=victorina_kb2)

    await FSMtest.victorinaStep3.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep3)
async def victorina3Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Инженер и гонщик <b>Луи Шевроле</b> стал сооснователем концерна Chevrolet в 1911 году. Через пять лет он ' \
                 'продал свою долю, а затем учредил ряд других автомобильных компаний. Во время Великой депрессии Луи ' \
                 'разорился и был вынужден устроиться простым механиком на завод Chevrolet в Детройте.'

    if callback.data == 'A':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic2.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question3.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('3. Какой продукт из перечисленных можно назвать по-настоящему мужским? ',
                                  reply_markup=victorina_kb3)

    await FSMtest.victorinaStep4.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep4)
async def victorina4Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Это, конечно же, <b>гранат!</b>\nОн содержит витамин В1 (тиамин), много марганца, селена, триптофана, ' \
                 'белка, магния. Благотворно влияет на мужское здоровье и очень полезен для работы всего организма. А ' \
                 'еще это отличная профилактика различных болезней, которым иногда подвержены представители сильного ' \
                 'пола.'

    if callback.data == 'D':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic3.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question4.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('4. Какой бренд официально разрешил мужчинам носить носки с сандалиями? ',
                                  reply_markup=victorina_kb4)

    await FSMtest.victorinaStep5.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep5)
async def victorina5Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Первым это сочетание продемонстрировал на миланской неделе моды Томас Майер из <b>Bottega Veneta.</b>\n\n ' \
                 'Произошло это в 2016 году. Тогда же новый тренд поддержали такие модные дома, как Versace, ' \
                 'Kenzo, Marni и Margaret Howell. А модный обозреватель Тим Бланкс назвал носки с сандалиями ' \
                 'главным обувным трендом весны 2016!'

    if callback.data == 'C':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic4.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question5.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('5. С каким инструментом часто ходят на рыбалку жители Судана?',
                                  reply_markup=victorina_kb5)

    await FSMtest.victorinaStep6.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep6)
async def victorina6Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Жители Судана пользуются специальным <b>барабаном</b>, с помощью которого извлекаются звуки, имитирующие ' \
                 'падение дождевых капель. Поддавшись обману, протоптеры (местная рыба, которая во время засухи ' \
                 'закапывается глубоко в ил) просыпаются и издают громкий чмокающий звук, выдавая тем самым место ' \
                 'своего укрытия. А подчас даже выползают наружу, попадая прямо в руки ловцов.'

    if callback.data == 'D':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic5.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question6.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '6. Какой вуз России решил принимать биткоины в качестве оплаты за обучение?',
        reply_markup=victorina_kb6)

    await FSMtest.victorinaStep7.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep7)
async def victorina7Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = "Этот прогрессивный вуз - <b>Высшая школа режиссеров и сценаристов.</b> \nОбъявление об этом появилось на официальном сайте в 2014 году. Соискателю достаточно было отправить электронное письмо, в ответ на которое высылался уникальный Bitcoin-адрес с точной суммой в BTC, сформированной по текущему курсу."

    if callback.data == 'B':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic6.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question7.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('7. Согласно опросам, большинство современных мужчин называют ЭТО самым привлекательным во внешности женщины. \nЧто же привлекает вас больше всего?',
                                  reply_markup=victorina_kb7)

    await FSMtest.victorinaStep8.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep8)
async def victorina8Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Исследования показали, что почти половина участников (46%) считает самой привлекательной частью тела женщины её <b>лицо.</b> \nДалее следуют ягодицы (18%), волосы (11%) и ' \
                 'ноги (9%).'

    if callback.data == 'A':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic7.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question8.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('8. Закончи фразу Джейсона Стэтхэма: «Какой я ,к черту, бренд? Бренд – это ...» ',
                                  reply_markup=victorina_kb8)

    await FSMtest.victorinaStep9.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep9)
async def victorina9Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Самый цитируемый мужчина Голливуда сказал: <b>«Бренд – это Ким Кардашьян».</b> \nЭта фраза взята из интервью «Я всё делаю по-настоящему», данного Стэтхэмом журналу «Психология» в 2013 году.'

    if callback.data == 'C':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic8.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question9.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '9. В чём заключалась особенность рекорда Джеймса Харгиса и Чарльза Крейтона, которые вдвоём '
        'преодолели свыше 11 тысяч километров из Нью-Йорка в Лос-Анджелес и обратно?',
        reply_markup=victorina_kb9)

    await FSMtest.victorinaStep10.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep10)
async def victorina10Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Джеймс Харгис и Чарльз Крейтон преодолели все 11 тысяч километров <b>«задним ходом»</b>. \nЭтот необычное ' \
                 'путешествие состоялось в 1930 году.'

    if callback.data == 'D':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic9.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question10.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '10. Что умеет новая умная духовка Haier CHEF@HOME, представленная на берлинской выставке IFA '
        '2022?',
        reply_markup=victorina_kb10)

    await FSMtest.victorinaStepFinal.set()


@dp.callback_query_handler(state=FSMtest.victorinaStepFinal)
async def victorinaFinalStep(callback: types.CallbackQuery, state: FSMContext):
    answerText = 'Фантастика! Эта встроенная духовка с большим сенсорным экраном умеет <b>распознавать блюда</b>, которые в ' \
                 'неё поставили. На основе этого она автоматически выставляет настройки и температурный режим. Отличная помощница по дому, не так ли?'

    if callback.data == 'A':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('Правильно!')

    else:
        await callback.message.answer('К сожалению, это неправильный ответ(')

    photo = open('victorina/answerPics/answerPic10.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    await callback.message.answer(
        '<b>Ура, ты это сделал! 🏆</b> \n\nТы - признанный эксперт во всех областях и настоящая звезда нашего выпуска!\n Смотри, какая обложка у нас с тобой получилась:',
        parse_mode='html')

    photo = open(f'peoplePics/new_{callback.message.chat.username}_img.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('👌🏻<b>Обложка для журнала готова, настало время интервью!</b> Сейчас мы зададим тебе несколько вопросов и узнаем о твоем идеальном вечере. Ты в деле? (если что, можно вернуться в главное меню командой /menu)', parse_mode='html', reply_markup=loop_kb)
    os.remove(f'peoplePics/new_{callback.message.chat.username}_img.png')

    await FSMtest.interviewStart.set()


    async with state.proxy() as data:

        print("amount" + f'{data["counter"]}')
        print(data["dateStart"])

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        print(dt_string)

        dataToSend = {
            'username': f'{callback.message.chat.username}',
            'dateStart': f'{data["dateStart"]}',
            'dateEnding': f'{dt_string}',
            'id': f'{callback.message.chat.id}',
            'amount': f'{data["counter"]}',
        }
        r = requests.post(victorinaHookURL, data=json.dumps(dataToSend), headers={'Content-Type': 'application/json'})


# -----------------------------------------------------------------------------

@dp.callback_query_handler(state=FSMtest.interviewStart)
async def interViewStartStep(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['A'] = 0
        data['B'] = 0
        data['C'] = 0
        data['D'] = 0

    photo = open('interview/1.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='Ты чувствуешь:', reply_markup=interview_kb1)
    await FSMtest.interviewStep1.set()


@dp.callback_query_handler(state=FSMtest.interviewStep1)
async def interView1Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/2.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='Ты достаешь из шкафа:',
                         reply_markup=interview_kb2)

    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await FSMtest.interviewStep2.set()


@dp.callback_query_handler(state=FSMtest.interviewStep2)
async def interView2Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/3.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='Главное не забыть:',
                         reply_markup=interview_kb3)

    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await FSMtest.interviewStep3.set()


@dp.callback_query_handler(state=FSMtest.interviewStep3)
async def interView3Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/4.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='Лучше всего поехать:',
                         reply_markup=interview_kb4)

    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await FSMtest.interviewStep4.set()


@dp.callback_query_handler(state=FSMtest.interviewStep4)
async def interView4Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/5.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await callback.message.answer('Музыка дня:', reply_markup=interview_kb5)
    await FSMtest.interviewStep5.set()


@dp.callback_query_handler(state=FSMtest.interviewStep5)
async def interView5Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/6.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await callback.message.answer('По дороге надо заскочить:', reply_markup=interview_kb6)
    await FSMtest.interviewStep6.set()


@dp.callback_query_handler(state=FSMtest.interviewStep6)
async def interView6Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/7.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await callback.message.answer('Ты бы не хотел встретить:', reply_markup=interview_kb7)
    await FSMtest.interviewStep7.set()


@dp.callback_query_handler(state=FSMtest.interviewStep7)
async def interView7Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/8.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)
    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await callback.message.answer('Ты будешь есть:', reply_markup=interview_kb8)
    await FSMtest.interviewStep8.set()


@dp.callback_query_handler(state=FSMtest.interviewStep8)
async def interView8Step(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    photo = open('interview/9.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await call.message.answer('Ты будешь пить:', reply_markup=interview_kb9)
    await FSMtest.interviewStep9.set()


@dp.callback_query_handler(state=FSMtest.interviewStep9)
async def interView9Step(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    photo = open('interview/10.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await call.message.answer('Вид за окном:', reply_markup=interview_kb10)
    await FSMtest.interviewStep10.set()


@dp.callback_query_handler(state=FSMtest.interviewStep10)
async def interView10Step(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    photo = open('interview/11.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await call.message.answer('Ты бы хотел оказаться в разгар вечера:', reply_markup=interview_kb11)
    await FSMtest.interviewStep11.set()


@dp.callback_query_handler(state=FSMtest.interviewStep11)
async def interView11Step(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    photo = open('interview/12.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

    await call.message.answer('Главное слово дня:', reply_markup=interview_kb12)
    await FSMtest.interviewStep12.set()


@dp.callback_query_handler(state=FSMtest.interviewStep12)
async def interView12Step(call: types.CallbackQuery, state: FSMContext):
    answer = call.data
    async with state.proxy() as data:
        if answer == 'A':
            data['A'] += 1
        elif answer == 'B':
            data['B'] += 1
        elif answer == 'C':
            data['C'] += 1
        else:
            data['D'] += 1

        print(f"A:{data['A']}")
        print(f"B:{data['B']}")
        print(f"C:{data['C']}")
        print(f"D:{data['D']}")

        sum = {
            'A': f'{data["A"]}',
            'B': f'{data["B"]}',
            'C': f'{data["C"]}',
            'D': f'{data["D"]}',
        }

        answerTotal = max(sum, key=sum.get)
        print(answerTotal)

        if answerTotal == 'A':
            photo = open('interview/endPics/A.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo,
                                 caption='<b>Поздравляем!</b>👏🏻 \n\nТвой идеальный вечер пройдёт в '
                                         'ресторане. Мы уверены, что всё будет '
                                         'прекрасно. Самое главное ‒ не встретить там '
                                         'бывшую или не заказать случайно гренки с '
                                         'чесноком', parse_mode='html')

        elif answerTotal == 'B':
            photo = open('interview/endPics/B.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo, caption='<b>Ого!</b>👏🏻\n\nПохоже, ты настроен весьма серьёзно. Ведь '
                                                                            'самый главный элемент идеального вечера ‒ это '
                                                                            'твоя любимая игровая приставка. Только, '
                                                                            'пожалуйста, будь внимателен и не обожгись '
                                                                            'дошираком!', parse_mode='html')

        elif answerTotal == 'C':
            photo = open('interview/endPics/C.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo,
                                 caption='<b>Ого!</b>👏🏻\n\nСудя по твоим ответам, ты явно собираешься '
                                         'навестить тёщу. Что ж, сделать такой вечер '
                                         'идеальным под силу только тебе самому. Удачи! ', parse_mode='html')

        else:
            photo = open('interview/endPics/D.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo,
                                 caption='<b>Отличный выбор!</b> 👏🏻\n\n Похоже, что твой идеальный '
                                         'вечер ‒ шумная туса с друзьями в любимом '
                                         'баре. Но помни, что здесь есть опасность '
                                         'встретить бывшую и махнуть в Сызрань', parse_mode='html')

    photo = open('interview/endPics/cup.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo,
                         caption='В любом случае ты можешь быть таким, каким захочешь. '
                                 ' <b>Мы в билайне тебя очень ценим и любим именно за это!</b> '
                                 'Лови приятность: https://t.me/addstickers/beemanpack', parse_mode='html')

    photo = open('victorina/endPic.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await state.finish()


executor.start_polling(dp, skip_updates=True)
