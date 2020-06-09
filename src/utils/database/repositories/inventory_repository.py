"""
Prefix repository.
"""

# Pip
import logging

# Locals
from src.utils.database.models import Inventory

module_logger = logging.getLogger('koneko.PrefixRepository')


class InventoryRepository:
    """Inventory repository

    Contains methods to work with the Inventory model."""

    async def get(self, snowflake: int) -> Inventory:
        """ Return a user's player.
        Parameters
        ------------
        snowflake: int [required]
            User id.
        """
        inventory = await Inventory.filter(
            snowflake=snowflake
        ).first()

        if inventory is None:
            inventory = await self.insert(snowflake)
        return inventory

    @staticmethod
    async def insert(snowflake: int) -> Inventory:
        """ Create a player inventory
        Parameters
        ------------
        snowflake: int [required]
            User id.
        """
        return await Inventory.create(
            snowflake=snowflake,
        )

    @staticmethod
    async def delete(snowflake: int) -> bool:
        """ Delete a player
        Parameters
        ------------
        snowflake: int [required]
            User id.
        """
        inventory = await Inventory.filter(
            snowflake=snowflake
        ).first()
        if inventory:
            await inventory.delete()
            return True

        return False
