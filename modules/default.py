from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import modules.keyboard as kb

router = Router()

@router.message(CommandStart())
async def def_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\nДля взаимодействия с ботом нажми на любую кнопку ниже или введи /help',
    reply_markup=kb.reply)

@router.message(Command('help'))
@router.message(F.text==('Помощь ℹ️'))
async def def_help(message: Message):
    await message.answer('Список команд:\n/start - Начало работы с ботом\n/link - Конект бота с группой\n/add - Добавлене бота в группу\n/help - Список доступных команд')

@router.message(Command('add'))
@router.message(F.text==('Добавить бота ➕'))
async def def_add(message: Message):
    await message.answer('Для добавления бота в чат нажми кнопку ниже',
    reply_markup=kb.inline)

@router.message(Command('link'))
async def def_link(message: Message):
    await message.answer('Команда находится в разработке')

@router.callback_query(F.data == 'add')
async def callback_def_add(callback: CallbackQuery):
    await callback.answer('')