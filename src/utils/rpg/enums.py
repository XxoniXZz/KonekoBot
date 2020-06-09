from enum import auto, Enum


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class PlayerClasses(AutoName):
    warrior = auto()
    assassin = auto()
    ranger = auto()
    mage = auto()


class PlayerRaces(AutoName):
    human = auto()
    dwarf = auto()
    elf = auto()
    orc = auto()


class PlayerStats(AutoName):
    attack = auto()
    defence = auto()
    health = auto()
