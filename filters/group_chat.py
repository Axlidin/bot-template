from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type in (
            types.ChatType.SUPER_GROUP,
            types.ChatType.GROUP,
        )
        # return message.chat.type == types.ChatType.SUPER_GROUP