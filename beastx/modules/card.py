from faker import Faker as dc

from beastx import bot as beast

from ..utils import admin_cmd as wtf

from . import *
@beast.on(wtf("card"))
async def _beastt(bst):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    chris = cyber.credit_card_full()
    await bst.edit(f"βπππ:-\n`{killer}`\n\nπΈπππ£ππ€π€:-\n`{kali}`\n\nβππ£π:-\n`{chris}`")
