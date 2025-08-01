"""
Unit tests for AsyncPrBot
"""

from unittest.mock import Mock

import pytest

from asyncprbot.asyncprbot import AsyncPrBot


def test_work_on_ticket_success():
    mock_client = Mock()
    mock_response = Mock()
    mock_response.content = [Mock(text="def add(a, b):\n    return a + b")]
    mock_client.messages.create.return_value = mock_response

    bot = AsyncPrBot(mock_client)

    result = bot.work_on_ticket("original code", "add function")

    assert result == "def add(a, b):\n    return a + b"
    mock_client.messages.create.assert_called_once()


def test_work_on_ticket_api_error():
    mock_client = Mock()
    mock_client.messages.create.side_effect = Exception("API Error")

    bot = AsyncPrBot(mock_client)

    with pytest.raises(Exception, match="Failed to process code with Claude"):
        bot.work_on_ticket("code", "instructions")
