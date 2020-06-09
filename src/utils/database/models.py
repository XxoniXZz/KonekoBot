"""
Module containing the database models.
"""

# Pip
from tortoise import fields
from tortoise.models import Model


class Currency(Model):
    """Currency table class."""

    id = fields.IntField(pk=True)
    snowflake = fields.TextField(required=True)
    guild = fields.TextField(required=True)
    amount = fields.IntField(required=True)

    class Meta:
        """Model metadata"""
        table = 'balances'

    def __str__(self) -> str:
        return str(self.amount)


class Level(Model):
    """Level table class."""

    id = fields.IntField(pk=True)
    snowflake = fields.TextField(required=True)
    guild = fields.TextField(required=True)
    experience = fields.IntField(null=False, default=0)
    level = fields.IntField(null=False, default=1)
    last_message = fields.DatetimeField(auto_now=True)

    class Meta:
        """Model metadata"""
        table = 'levels'

    def __str__(self) -> str:
        return str(self.level)


class Player(Model):
    """Player table class."""

    snowflake = fields.TextField(pk=True, required=True)
    inventory_id = fields.IntField(unique=True)
    inventory: fields.ReverseRelation["Inventory"]

    class Meta:
        """Model metadata"""
        table = 'Players'


class Inventory(Model):
    """User table class."""

    id = fields.IntField(pk=True)
    user: fields.OneToOneRelation[Player] = fields.OneToOneField(
        "models.Player", related_name="inventory", to_field="inventory_id"
    )
    items: fields.ReverseRelation["Item"]

    class Meta:
        """Model metadata"""
        table = 'Inventories'


class Item(Model):
    """Item table class"""

    id = fields.IntField(pk=True)
    inventory: fields.ForeignKeyRelation[Inventory] = fields.ForeignKeyField(
        "models.Inventory", related_name="items", to_field="id"
    )

    class Meta:
        """Model metadata"""
        table = 'Items'


class Prefix(Model):
    """Prefix table class."""

    id = fields.IntField(pk=True)
    prefix = fields.TextField(required=True)
    guild = fields.TextField(required=True)

    class Meta:
        """Model metadata"""
        table = 'prefixes'

    def __str__(self) -> str:
        return str(self.prefix)


class User(Model):
    """User table class."""

    snowflake = fields.TextField(pk=True, required=True)

    class Meta:
        """Model metadata"""
        table = 'Users'
