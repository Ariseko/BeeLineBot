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
        await message.answer('<b>???? ??????????????????</b> ?? ?????????????? ????????', reply_markup=choose_kb, parse_mode='html')
        await FSMtest.fork.set()
    else:
        await message.answer('<b>???? ??????????????????</b> ?? ?????????????? ????????', reply_markup=loop_kb, parse_mode='html')
        await FSMtest.fork.set()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    checkList.append(message.from_user.id)
    await message.answer('<b>?????? ???????????? ?????????????? ?????????????????????????? =)</b>\n?????????? ???????? ???????????????? ?????? ?? ??????????????:',
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

        #await message.answer('?? ???????? ????????????: ?? ???????????????? ?????? ???????????????????', reply_markup=choose_kb)

        photo = open('victorina/start.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo=photo)

        await message.answer('<b>???????????????????? ???? ?????????????? ?????? ?????????????????????? ???????????? BeeMAN!</b>\n ???????? ???????? 10 ???????????????? ???? '
            '???????????? ????????????   ???????????????????????? ?????????????? ????????????????. ?????????????? ???? ??????, ???? ???????????????? ???????????????????????? '
            '?????????????? ?? ?????????????????????? ???????????????? ???????????????????? ????????. \n\n?????????? ?????????????? 30 ????????????????????, ?????????????? ?????????? ???????????????????????? ???????????????????? ???????????????????? ?????????????? ???? ?????????????????????? ??????????!\n<b>???????????????</b>',
            reply_markup=start_kb, parse_mode='html')
        await FSMtest.victorinaStart.set()
    except:
        await message.answer('???? ?????? ????????????????????????????????', reply_markup=choose_kb)

    #await FSMtest.fork.set()


# @dp.callback_query_handler(state=FSMtest.fork)
# async def activityChoose(callback: types.CallbackQuery, state: FSMContext):
#     if callback.data == 'interview':
#         await callback.message.answer(
#             '<b>???????????????? - ?????? ??????????????????! </b>\n???????????? ???? ?????????????? ???????? ?????????????????? ????????????????, ?????????? ???????????? ?? '
#             '?????????? ?????????????????? ????????????. ???? ?? ????????? \n\n(???????? ??????, ???? ?????????? ?????????????????? ?? ?????????????? ???????? '
#             '???????????????? /menu)', reply_markup=start_kb, parse_mode='html')
#
#         await FSMtest.interviewStart.set()
#
#     elif callback.data == 'victorina':
#
#         photo = open('victorina/start.jpg', 'rb')
#         await bot.send_photo(callback.message.chat.id, photo=photo)
#
#         await callback.message.answer(
#             '<b>???????????????????? ???? ?????????????? ?????? ?????????????????????? ???????????? BeeMAN!</b>\n ???????? ???????? 10 ???????????????? ???? '
#             '???????????? ????????????   ???????????????????????? ?????????????? ????????????????. ?????????????? ???? ??????, ???? ???????????????? ???????????????????????? '
#             '?????????????? ?? ?????????????????????? ???????????????? ???????????????????? ????????. \n\n?????????? ?????????????? ???????????? 30 ????????????????????, ?????????????? ?????????? ???????????????????????? ???????????????????? ???????????????????? ??????????????, ???? ???????????????????? ??????????!\n<b>???????????????</b>',
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
    await callback.message.answer('1. ?????????? ???? ?????????????????? ???????????? ???????????????? ?????????????????? ???????? ?????????????????????? ?????????? ?????????????',
                                  reply_markup=victorina_kb1)
    await FSMtest.victorinaStep2.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep2)
async def victorina2Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '?? 1900 ???? 1920 ?????? <b>?????????????????????????? ????????????</b> ???????? ?????????? ???? ???????????????????????? ???????????? ????????????????. ?????????? ???? ?????? ' \
                 '?????????? ???????? ?????????????????? ???????? ???????????????????? ?????????????????????? ????????????. ???????????? ?? ???????? ???????????????????? ?????????????????????? ' \
                 '??????????, ??????????????, ???????????????????? ?? ??????????????????.'

    if callback.data == 'B':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic1.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question2.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '2. ???????????????????? ?????????? ?????????????????????????? ????????????????, ?????????????????? ?? ?????? ??????????, ???????????????? ?????? ???????????????? ?? '
        '?????? ?????????????? ??????????????????? ', reply_markup=victorina_kb2)

    await FSMtest.victorinaStep3.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep3)
async def victorina3Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '?????????????? ?? ???????????? <b>?????? ??????????????</b> ???????? ?????????????????????????? ???????????????? Chevrolet ?? 1911 ????????. ?????????? ???????? ?????? ???? ' \
                 '???????????? ???????? ????????, ?? ?????????? ?????????????? ?????? ???????????? ?????????????????????????? ????????????????. ???? ?????????? ?????????????? ?????????????????? ?????? ' \
                 '?????????????????? ?? ?????? ???????????????? ???????????????????? ?????????????? ?????????????????? ???? ?????????? Chevrolet ?? ????????????????.'

    if callback.data == 'A':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic2.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question3.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('3. ?????????? ?????????????? ???? ?????????????????????????? ?????????? ?????????????? ????-???????????????????? ??????????????? ',
                                  reply_markup=victorina_kb3)

    await FSMtest.victorinaStep4.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep4)
async def victorina4Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '??????, ?????????????? ????, <b>????????????!</b>\n???? ???????????????? ?????????????? ??1 (????????????), ?????????? ????????????????, ????????????, ????????????????????, ' \
                 '??????????, ????????????. ?????????????????????? ???????????? ???? ?????????????? ???????????????? ?? ?????????? ?????????????? ?????? ???????????? ?????????? ??????????????????. ?? ' \
                 '?????? ?????? ???????????????? ???????????????????????? ?????????????????? ????????????????, ?????????????? ???????????? ???????????????????? ?????????????????????????? ???????????????? ' \
                 '????????.'

    if callback.data == 'D':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic3.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question4.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('4. ?????????? ?????????? ???????????????????? ???????????????? ???????????????? ???????????? ?????????? ?? ????????????????????? ',
                                  reply_markup=victorina_kb4)

    await FSMtest.victorinaStep5.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep5)
async def victorina5Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '???????????? ?????? ?????????????????? ?????????????????????????????????? ???? ?????????????????? ???????????? ???????? ?????????? ?????????? ???? <b>Bottega Veneta.</b>\n\n ' \
                 '?????????????????? ?????? ?? 2016 ????????. ?????????? ???? ?????????? ?????????? ???????????????????? ?????????? ???????????? ????????, ?????? Versace, ' \
                 'Kenzo, Marni ?? Margaret Howell. ?? ???????????? ???????????????????????? ?????? ???????????? ???????????? ?????????? ?? ???????????????????? ' \
                 '?????????????? ?????????????? ?????????????? ?????????? 2016!'

    if callback.data == 'C':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic4.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question5.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('5. ?? ?????????? ???????????????????????? ?????????? ?????????? ???? ?????????????? ???????????? ?????????????',
                                  reply_markup=victorina_kb5)

    await FSMtest.victorinaStep6.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep6)
async def victorina6Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '???????????? ???????????? ???????????????????? ?????????????????????? <b>??????????????????</b>, ?? ?????????????? ???????????????? ?????????????????????? ??????????, ?????????????????????? ' \
                 '?????????????? ???????????????? ????????????. ???????????????????? ????????????, ???????????????????? (?????????????? ????????, ?????????????? ???? ?????????? ???????????? ' \
                 '???????????????????????? ?????????????? ?? ????) ?????????????????????? ?? ???????????? ?????????????? ?????????????????? ????????, ?????????????? ?????? ?????????? ?????????? ' \
                 '???????????? ??????????????. ?? ???????????? ???????? ?????????????????? ????????????, ?????????????? ?????????? ?? ???????? ????????????.'

    if callback.data == 'D':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic5.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question6.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '6. ?????????? ?????? ???????????? ?????????? ?????????????????? ???????????????? ?? ???????????????? ???????????? ???? ?????????????????',
        reply_markup=victorina_kb6)

    await FSMtest.victorinaStep7.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep7)
async def victorina7Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = "???????? ?????????????????????????? ?????? - <b>???????????? ?????????? ???????????????????? ?? ??????????????????????.</b> \n???????????????????? ???? ???????? ?????????????????? ???? ?????????????????????? ?????????? ?? 2014 ????????. ???????????????????? ???????????????????? ???????? ?????????????????? ?????????????????????? ????????????, ?? ?????????? ???? ?????????????? ?????????????????? ???????????????????? Bitcoin-?????????? ?? ???????????? ???????????? ?? BTC, ???????????????????????????? ???? ???????????????? ??????????."

    if callback.data == 'B':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic6.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question7.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('7. ???????????????? ??????????????, ?????????????????????? ?????????????????????? ???????????? ???????????????? ?????? ?????????? ?????????????????????????????? ???? ?????????????????? ??????????????. \n?????? ???? ???????????????????? ?????? ???????????? ???????????',
                                  reply_markup=victorina_kb7)

    await FSMtest.victorinaStep8.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep8)
async def victorina8Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '???????????????????????? ????????????????, ?????? ?????????? ???????????????? ???????????????????? (46%) ?????????????? ?????????? ?????????????????????????????? ???????????? ???????? ?????????????? ???? <b>????????.</b> \n?????????? ?????????????? ?????????????? (18%), ???????????? (11%) ?? ' \
                 '???????? (9%).'

    if callback.data == 'A':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic7.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question8.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('8. ?????????????? ?????????? ???????????????? ????????????????: ???????????? ?? ,?? ??????????, ??????????? ?????????? ??? ?????? ...?? ',
                                  reply_markup=victorina_kb8)

    await FSMtest.victorinaStep9.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep9)
async def victorina9Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '?????????? ???????????????????? ?????????????? ?????????????????? ????????????: <b>???????????? ??? ?????? ?????? ????????????????????.</b> \n?????? ?????????? ?????????? ???? ???????????????? ???? ?????? ?????????? ????-??????????????????????, ?????????????? ?????????????????? ?????????????? ???????????????????????? ?? 2013 ????????.'

    if callback.data == 'C':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic8.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question9.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '9. ?? ?????? ?????????????????????? ?????????????????????? ?????????????? ?????????????? ?????????????? ?? ?????????????? ????????????????, ?????????????? ???????????? '
        '???????????????????? ?????????? 11 ?????????? ???????????????????? ???? ??????-?????????? ?? ??????-???????????????? ?? ???????????????',
        reply_markup=victorina_kb9)

    await FSMtest.victorinaStep10.set()


@dp.callback_query_handler(state=FSMtest.victorinaStep10)
async def victorina10Step(callback: types.CallbackQuery, state: FSMContext):
    answerText = '???????????? ???????????? ?? ???????????? ?????????????? ???????????????????? ?????? 11 ?????????? ???????????????????? <b>?????????????? ????????????</b>. \n???????? ?????????????????? ' \
                 '?????????????????????? ???????????????????? ?? 1930 ????????.'

    if callback.data == 'D':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic9.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    photo = open('victorina/rubriks/question10.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer(
        '10. ?????? ?????????? ?????????? ?????????? ?????????????? Haier CHEF@HOME, ???????????????????????????? ???? ???????????????????? ???????????????? IFA '
        '2022?',
        reply_markup=victorina_kb10)

    await FSMtest.victorinaStepFinal.set()


@dp.callback_query_handler(state=FSMtest.victorinaStepFinal)
async def victorinaFinalStep(callback: types.CallbackQuery, state: FSMContext):
    answerText = '????????????????????! ?????? ???????????????????? ?????????????? ?? ?????????????? ?????????????????? ?????????????? ?????????? <b>???????????????????????? ??????????</b>, ?????????????? ?? ' \
                 '?????? ??????????????????. ???? ???????????? ?????????? ?????? ?????????????????????????? ???????????????????? ?????????????????? ?? ?????????????????????????? ??????????. ???????????????? ?????????????????? ???? ????????, ???? ?????? ?????'

    if callback.data == 'A':
        async with state.proxy() as data:
            data['counter'] += 1
        await callback.message.answer('??????????????????!')

    else:
        await callback.message.answer('?? ??????????????????, ?????? ???????????????????????? ??????????(')

    photo = open('victorina/answerPics/answerPic10.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption=answerText, parse_mode='html')

    await callback.message.answer(
        '<b>??????, ???? ?????? ????????????! ????</b> \n\n???? - ???????????????????? ?????????????? ???? ???????? ???????????????? ?? ?????????????????? ???????????? ???????????? ??????????????!\n ????????????, ?????????? ?????????????? ?? ?????? ?? ?????????? ????????????????????:',
        parse_mode='html')

    photo = open(f'peoplePics/new_{callback.message.chat.username}_img.png', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo)

    await callback.message.answer('????????<b>?????????????? ?????? ?????????????? ????????????, ?????????????? ?????????? ????????????????!</b> ???????????? ???? ?????????????? ???????? ?????????????????? ???????????????? ?? ???????????? ?? ?????????? ?????????????????? ????????????. ???? ?? ????????? (???????? ??????, ?????????? ?????????????????? ?? ?????????????? ???????? ???????????????? /menu)', parse_mode='html', reply_markup=loop_kb)
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
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='???? ????????????????????:', reply_markup=interview_kb1)
    await FSMtest.interviewStep1.set()


@dp.callback_query_handler(state=FSMtest.interviewStep1)
async def interView1Step(callback: types.CallbackQuery, state: FSMContext):
    answer = callback.data
    photo = open('interview/2.jpg', 'rb')
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='???? ???????????????? ???? ??????????:',
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
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='?????????????? ???? ????????????:',
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
    await bot.send_photo(callback.message.chat.id, photo=photo, caption='?????????? ?????????? ??????????????:',
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

    await callback.message.answer('???????????? ??????:', reply_markup=interview_kb5)
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

    await callback.message.answer('???? ???????????? ???????? ??????????????????:', reply_markup=interview_kb6)
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

    await callback.message.answer('???? ???? ???? ?????????? ??????????????????:', reply_markup=interview_kb7)
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

    await callback.message.answer('???? ???????????? ????????:', reply_markup=interview_kb8)
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

    await call.message.answer('???? ???????????? ????????:', reply_markup=interview_kb9)
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

    await call.message.answer('?????? ???? ??????????:', reply_markup=interview_kb10)
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

    await call.message.answer('???? ???? ?????????? ?????????????????? ?? ???????????? ????????????:', reply_markup=interview_kb11)
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

    await call.message.answer('?????????????? ?????????? ??????:', reply_markup=interview_kb12)
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
                                 caption='<b>??????????????????????!</b>???????? \n\n???????? ?????????????????? ?????????? ?????????????? ?? '
                                         '??????????????????. ???? ??????????????, ?????? ?????? ?????????? '
                                         '??????????????????. ?????????? ?????????????? ??? ???? ?????????????????? ?????? '
                                         '???????????? ?????? ???? ???????????????? ???????????????? ???????????? ?? '
                                         '????????????????', parse_mode='html')

        elif answerTotal == 'B':
            photo = open('interview/endPics/B.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo, caption='<b>??????!</b>????????\n\n????????????, ???? ???????????????? ???????????? ????????????????. ???????? '
                                                                            '?????????? ?????????????? ?????????????? ???????????????????? ???????????? ??? ?????? '
                                                                            '???????? ?????????????? ?????????????? ??????????????????. ????????????, '
                                                                            '????????????????????, ???????? ???????????????????? ?? ???? ???????????????? '
                                                                            '??????????????????!', parse_mode='html')

        elif answerTotal == 'C':
            photo = open('interview/endPics/C.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo,
                                 caption='<b>??????!</b>????????\n\n???????? ???? ?????????? ??????????????, ???? ???????? ?????????????????????? '
                                         '?????????????????? ????????. ?????? ??, ?????????????? ?????????? ?????????? '
                                         '?????????????????? ?????? ???????? ???????????? ???????? ????????????. ??????????! ', parse_mode='html')

        else:
            photo = open('interview/endPics/D.jpg', 'rb')
            await bot.send_photo(call.message.chat.id, photo=photo,
                                 caption='<b>???????????????? ??????????!</b> ????????\n\n ????????????, ?????? ???????? ?????????????????? '
                                         '?????????? ??? ???????????? ???????? ?? ???????????????? ?? ?????????????? '
                                         '????????. ???? ??????????, ?????? ?????????? ???????? ?????????????????? '
                                         '?????????????????? ???????????? ?? ?????????????? ?? ??????????????', parse_mode='html')

    photo = open('interview/endPics/cup.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo,
                         caption='?? ?????????? ???????????? ???? ???????????? ???????? ??????????, ?????????? ????????????????. '
                                 ' <b>???? ?? ?????????????? ???????? ?????????? ?????????? ?? ?????????? ???????????? ???? ??????!</b> '
                                 '???????? ????????????????????: https://t.me/addstickers/beemanpack', parse_mode='html')

    photo = open('victorina/endPic.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await state.finish()


executor.start_polling(dp, skip_updates=True)
