"""
Prefix repository.
"""

# Pip
import configparser
import logging

# Locals
from src.utils.database.models import User

config = configparser.ConfigParser()
config.read('config.ini')

module_logger = logging.getLogger('koneko.PrefixRepository')


class PrefixRepository:
    """Prefix repository

    Contains methods to work with the Prefix model."""

    async def get(self, snowflake: int) -> User:
        """ Return an user object
        ------------
        snowflake: int [required]
            The snowflake for the user.
        """
        user = await User.filter(
            snowflake=snowflake
        ).first()

        if user is None:
            user = await self.insert(snowflake)
        return user

    @staticmethod
    async def insert(snowflake: int) -> User:
        return await User.create(snowflake=snowflake)

    @staticmethod
    async def delete(snowflake: int) -> bool:
        user = await User.filter(
            snowflake=snowflake
        ).first()
        if user:
            await user.delete()
            return True

        return False
