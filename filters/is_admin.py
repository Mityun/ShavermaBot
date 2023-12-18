"""
Module: admin_filters

Description: Contains a filter to check whether the user is in the list of administrators.
"""

from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS

class IsAdmin(BoundFilter):
    """
    Filter to check whether the user is in the list of administrators.
    """

    async def check(self, message: Message):
        """ Checks if the message sender is an administrator

               :param message: The message object
               :type message: object
               :raise TypeError: If the data type is incorrect

               :returns: True if the user is not an administrator, otherwise False

               :rtype: bool
        """
        return message.from_user.id in ADMINS