from keybords import start_key,narh_key,son_key,damas
from Token1 import TOKEN
from aiogram import Bot, Dispatcher,executor,types
import logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def get_start(message: types.Message):
    await message.answer("UzAuto ботга хуш келибсиз, керакли бўлимни танланг👇", reply_markup=start_key)


@dp.callback_query_handler(text = "Narh")
async def get_narh(call: types.CallbackQuery):
    await call.message.answer(text= "Пастдаги рўйхатдан машинани танланг ⬇️" ,reply_markup=narh_key)
    await call.message.delete()

@dp.callback_query_handler(text = "boshmeniyu")
async def get_narh(call: types.CallbackQuery):
    await call.message.answer(text= "UzAuto ботга хуш келибсиз, керакли бўлимни танланг👇" ,reply_markup=start_key)
    await call.message.delete()

@dp.callback_query_handler(text = "sotuv")
async def get_narh(call: types.CallbackQuery):
    await call.message.answer(text= "Пастдаги рўйхатдан машинани танланг ⬇️" ,reply_markup=son_key)
    await call.message.delete()

@dp.callback_query_handler(text = "son")
async def get_narh(call: types.CallbackQuery):
    await call.message.answer(text= "Пастдаги рўйхатдан машинани танланг ⬇️" ,reply_markup=narh_key)
    await call.message.delete()

s3 = """Комплектасияни рўйхатдан танланг 

1. D2 STYLE   (86,971,000 сўм)
2. D3 PLUS  (86,031,000 сўм)
3. D3 STYLE (86,397,000 сўм)
4. LB2 PLUS  (87,446,000 сўм)
5. LB3 PLUS (84,910,000 сўм)
6. LB3 STYLE  (85,124,000 сўм)
7. D11 PLUS (ГРУЗОВОЙ) (83,904,000 сўм)
8. D11 STYLE  (ГРУЗОВОЙ) (84,309,000 сўм)
9. D2 PLUS (86,605,000 сўм)
10. LB2 STYLE (87,660,000 сўм)"""

@dp.callback_query_handler(text = "damaslar")
async def get_narh(call: types.CallbackQuery):
    await call.message.answer(text = s3 ,reply_markup=damas)
    await call.message.delete()

if __name__ == "__main__": 
    executor.start_polling(dp,skip_updates=True) 