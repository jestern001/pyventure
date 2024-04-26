from database.models.character import Character
from database.models.location import Location


from dataclasses import dataclass, field


@dataclass
class Data:
    _characters: list[Character] = field(default_factory=list)
    _locations: list[Location] = field(default_factory=list)