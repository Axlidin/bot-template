from aiogram.dispatcher.filters.state import State, StatesGroup

class NewPost(StatesGroup):
    newMessage = State()
    confirm = State()