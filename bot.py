from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image, ImageDraw, ImageFont

from datetime import datetime
from inlineKeyboards.interviewKeyboardsInline import *
from inlineKeyboards.Inlinekeyboards import *

import os
import json
import requests
import random
import sqlite3 as sq


hookURL = 'https://hook.eu1.make.com/l22pqcigfqm286out21fe66axr0hq5mr'
victorinaHookURL = 'https://hook.eu1.make.com/ndw976q0pjanoalr5cjjt4du33kg71h2'

base = sq.connect('quest.db')

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

storage = MemoryStorage()
bot = Bot(token='-')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['menu'], state='*')
async def menu(message: types.Message):
    await message.answer('<b>Вы вернулись</b> в главное меню', reply_markup=choose_kb, parse_mode='html')
    await FSMtest.fork.set()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('<b>Для начала немного формальностей =)</b>\nВпиши свои реальные имя и фамилию:', parse_mode='html')
    await FSMtest.getRealName.set()
