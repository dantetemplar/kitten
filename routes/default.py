from aiogram import Router, types
from aiogram.filters import Command

from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


def get_cat_kb() -> types.ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.row(
        types.KeyboardButton(text="Отправить котика"),
        types.KeyboardButton(text="Отправить котика с подписью")
    )

    kb.row(
        types.KeyboardButton(text="Количество котиков", ),
    )

    return kb.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Что мне сделать?"
    )


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Вас приветствует котик-бот!",
        reply_markup=get_cat_kb()
    )
