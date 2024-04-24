from aiogram.dispatcher.filters.state import StatesGroup, State


class Person_datas(StatesGroup):
    firstname = State()
    age = State()
    email = State()
    phone = State()