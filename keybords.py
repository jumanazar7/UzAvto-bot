
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

start_key  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "💰 Avtomabillar narxlari ",callback_data = "Narh") ],
    [InlineKeyboardButton(text = "Sotuvda borligi boyicha malumot",callback_data = "sotuv")],
    [InlineKeyboardButton(text = "Songi yang yiliklar",callback_data = "Narh2")],
    [InlineKeyboardButton(text = "Avtomabillar infarmatsiyasi",callback_data = "Nar1202")]
])


narh_key  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "DAMAS (83,904,000 сўм дан) ",callback_data = "damaslar") ],
    [InlineKeyboardButton(text = "COBALT (124,295,000 сўм дан)",callback_data = "cobilitlar")],
    [InlineKeyboardButton(text = "MALIBU-2 (394,900,000 сўм дан)",callback_data = "malibu")],
    [InlineKeyboardButton(text = "EQUINOX (389,000,000 сўм дан)",callback_data = "equinox")],
    [InlineKeyboardButton(text = "TRAVERSE (647,600,000 сўм дан)",callback_data = "equinox")],
    [InlineKeyboardButton(text = "◀️ Оркага",callback_data = "boshmeniyu")]
])

son_key  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "DAMAS (навбатда 36946 дона) ",callback_data = "damaslar") ],
    [InlineKeyboardButton(text = "COBALT (навбатда 37595 дона)",callback_data = "cobilitlar")],
    [InlineKeyboardButton(text = "MALIBU-2 (сотувда 110 дона)",callback_data = "malibu")],
    [InlineKeyboardButton(text = "EQUINOX (сотувда 40 дона)",callback_data = "equinox")],
    [InlineKeyboardButton(text = "TRAVERSE (навбатда 175 дона)",callback_data = "TRAVERSE")],
    [InlineKeyboardButton(text = "TAHOE (навбатда 111 дона) ",callback_data = "TAHOE") ],
    [InlineKeyboardButton(text = "LACETTI (навбатда 33596 дона)",callback_data = "cobilitlar")],
    [InlineKeyboardButton(text = "NEXIA 3 (сотувда 0 дона)",callback_data = "NEXIA")],
    [InlineKeyboardButton(text = "EQUINOX (сотувда 40 дона)",callback_data = "equinox")],
    [InlineKeyboardButton(text = "SPARK (сотувда 0 дона)",callback_data = "TRAVERSE")],
    [InlineKeyboardButton(text = "TRACKER 2 (сотувда 0 дона)",callback_data = "equinox")],
    [InlineKeyboardButton(text = "◀️ Оркага",callback_data = "boshmeniyu")]
])
damas =   InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "D2 STYLE",callback_data = "damsa2_style") ],
    [InlineKeyboardButton(text = "D3 PLUS",callback_data = "damas3_plus")],
    [InlineKeyboardButton(text = "D3 STYLE",callback_data = "damas3_style")],
    [InlineKeyboardButton(text = "LB2 PLUS",callback_data = "LB2_PLUS")],
    [InlineKeyboardButton(text = "LB3 PLUS",callback_data = "LB3_PLUS")],
    [InlineKeyboardButton(text = "LB3 STYLE",callback_data = "LB3 STYLE") ],
    [InlineKeyboardButton(text = "D11 PLUS (ГРУЗОВОЙ)",callback_data = "d11_plus")],
    [InlineKeyboardButton(text = "D11 STYLE (ГРУЗОВОЙ)",callback_data = "d11_style ")],
    [InlineKeyboardButton(text = "D2 PLUS",callback_data = "damas2_plus")],
    [InlineKeyboardButton(text = "LB2 STYLE",callback_data = "LB2_STYLE")],
    [InlineKeyboardButton(text = "◀️ Оркага",callback_data = "son")]
])