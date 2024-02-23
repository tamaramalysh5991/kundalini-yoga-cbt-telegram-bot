from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from db_service import users_collection

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:

    """
    This handler receives messages with `/start` command
    """
    user_info = {
        "user_id": message.from_user.id,
        "username": message.from_user.full_name,
        "chat_id": message.chat.id,
        "status": "active",
    }
    existing_user = users_collection.find_one({"user_id": user_info["user_id"]})

    if existing_user:
        users_collection.update_one(
            {"user_id": user_info["user_id"]}, {"$set": {"status": "active"}}
        )
        await message.reply("C возвращением!")

    users_collection.insert_one(user_info)
    await message.answer(f"Привет {message.from_user.full_name}!")


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command
    """
    await message.answer(
        "Это бот для кундалини йоги. Он поможет вам следить за вашими достижениями и прогрессом."
        "Для начала работы введите команду /start."
    )
