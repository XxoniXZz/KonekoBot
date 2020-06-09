"""
Item repository.
"""

# Builtins
import logging
from typing import List

# Locals
from src.utils.database.models import Inventory, Item

module_logger = logging.getLogger('koneko.PrefixRepository')


class ItemRepository:
    """Inventory repository

    Contains methods to work with the Inventory model."""

    @staticmethod
    async def get(inventory: Inventory) -> List[Item]:
        """ Return the items in the inventory.
        Parameters
        ------------
        inventory: Inventory [required]
            Inventory the item belongs to.
        """
        return await Item.filter(
            inventory=inventory
        )

    @staticmethod
    async def insert(inventory: Inventory) -> Item:
        """ Create an item
        Parameters
        ------------
        inventory: Inventory [required]
            Inventory the item belongs to.
        """
        return await Item.create(
            inventory=inventory,
        )

    @staticmethod
    async def delete(item_id: int) -> bool:
        """ Delete an item from the inventory
        Parameters
        ------------
        item_id: int [required]
            Item id.
        """
        item = await Item.filter(
            id=item_id
        ).first()
        if Item:
            await item.delete()
            return True

        return False
