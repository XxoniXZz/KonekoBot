"""
Player repository.
"""

# Pip
import logging

# Locals
from typing import Optional

from src.utils.database.models import Player
from src.utils.database.repositories.inventory_repository import \
    InventoryRepository

module_logger = logging.getLogger('koneko.PlayerRepository')


class PlayerRepository:
    """Player repository

    Contains methods to work with the Player model."""

    @staticmethod
    async def get(snowflake: int) -> Optional[Player]:
        """ Return a user's player.
        Parameters
        ------------
        snowflake: int [required]
            User id.
        """
        return await Player.filter(
            snowflake=snowflake
        ).first()

    @staticmethod
    async def insert(snowflake: int) -> Player:
        """ Create a player
        Parameters
        ------------
        snowflake: int [required]
            User id.
        """
        return await Player.create(
            snowflake=snowflake,
            inventory=InventoryRepository().insert(snowflake)
        )

    @staticmethod
    async def delete(snowflake: int) -> bool:
        """ Delete a player
        Parameters
        ------------
        snowflake: int [required]
            User id.
        """
        player = await Player.filter(
            snowflake=snowflake
        ).first()
        if player:
            await player.delete()
            return True

        return False
