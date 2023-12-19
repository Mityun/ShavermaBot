
"""
    Sets up custom filters for checking status
    """

from aiogram import Dispatcher
from .is_admin import IsAdmin
from .is_user import IsUser

def setup(dp: Dispatcher):
    """
    Module: setup_filters

    Description: Sets up custom filters for checking if a user is an administrator or a regular user.

    :param dp: The Aiogram Dispatcher object.

    :returns: None
    """
    dp.filters_factory.bind(IsAdmin, event_handlers=[dp.message_handlers])
    dp.filters_factory.bind(IsUser, event_handlers=[dp.message_handlers])