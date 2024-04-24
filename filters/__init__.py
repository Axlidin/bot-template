from loader import dp
from .admin_chat import IsAdmins
from .private_chat import IsPrivate
from .group_chat import IsGroup


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmins)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
