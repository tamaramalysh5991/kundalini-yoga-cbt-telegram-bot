from unittest.mock import Mock

from aiogram.types import Message

# Generated by CodiumAI

from bot.db_service import update_user

# Dependencies:
# pip install pytest-mock
import pytest


class TestUpdateUser:

    #  The function updates the user with the provided user_id and message.
    def test_update_user_with_user_id_and_message(self, mocker):
        # Mock the necessary dependencies
        user_collection_bot = mocker.patch("bot.db_service.users_collection")

        # Create a mock message object
        message = Mock()
        message.from_user.username = "test_username"
        message.from_user.first_name = "test_first_name"
        message.from_user.last_name = "test_last_name"
        message.chat.id = 123456789

        # Call the function under test
        result = update_user(123, message)

        # Assert that the user was updated correctly
        assert result == {
            "user_id": 123,
            "username": "test_username",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "chat_id": 123456789,
            "state": "start",
            "status": "active",
            "language": "ru",
            "reminder": "off",
            "reminder_time": "12:00",
        }
        user_collection_bot.update_one.assert_called_once_with(
            {"user_id": 123}, {"$set": result}
        )

    #  The user_id is not provided.
    def test_update_user_without_user_id(self, mocker):
        # Mock the necessary dependencies
        user_collection_mock = mocker.patch("bot.db_service.users_collection")

        # Create a mock message object
        message = Mock()
        message.from_user.username = "test_username"
        message.from_user.first_name = "test_first_name"
        message.from_user.last_name = "test_last_name"
        message.chat.id = 123456789

        # Call the function under test without providing user_id
        result = update_user(None, message)

        # Assert that the user was not updated
        assert result is None
        user_collection_mock.update_one.assert_not_called()