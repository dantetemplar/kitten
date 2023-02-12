from aiogram import Router, types
from random import choice
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

captions = [
    "Meow",
    "Meow meow!",
    " =^.^= ",
    " Муррррк ~",
    " ;3 "
    "Purr",
    "Pr..",
    "Prrr",
    "I will take over the world.",
    "For the glory of Satan."
]


class KittenState(StatesGroup):
    default = State()
    cat_with_text = State()


async def get_cat() -> types.InputFile:
    url = "https://cataas.com/cat"
    return types.input_file.URLInputFile(url=url, filename="cat.jpg")


async def get_cat_with_text(text: str) -> types.InputFile:
    url = f"https://cataas.com/cat/says/{text}"
    return types.input_file.URLInputFile(url=url, filename="cat.jpg")


@router.message(Command("cat"))
@router.message(Text("Отправить котика", ignore_case=True))
async def cat(message: types.Message, state: FSMContext):
    await message.answer_photo(
        await get_cat(),
        caption=choice(captions)
    )

    user = await state.get_data()
    await state.set_data({"kitten_count": user.get("kitten_count", 0) + 1})


@router.message(Command("cat_with_text"))
@router.message(Text("Отправить котика с подписью", ignore_case=True))
async def cat_with_text_start(message: types.Message, state: FSMContext):
    await state.set_state(KittenState.cat_with_text)
    await message.answer("Введите подпись к котику")


@router.message(KittenState.cat_with_text)
async def cat_with_text(message: types.Message, state: FSMContext):
    await message.answer_photo(
        await get_cat_with_text(message.text),
    )
    user = await state.get_data()
    await state.set_data({"kitten_count": user.get("kitten_count", 0) + 1})
    await state.set_state(KittenState.default)


@router.message(Command("kitten_count"))
@router.message(Text("Количество котиков", ignore_case=True))
async def kitten_count(message: types.Message, state: FSMContext):
    user = await state.get_data()
    await message.answer(f"Котиков отправлено: {user.get('kitten_count', 0)}")
