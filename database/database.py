from dataclasses import dataclass, field
from database.models.character import Character
from database.models.location import Location


@dataclass
class Database:
    characters: list[Character] = field(default_factory=list)
    locations: list[Location] = field(default_factory=list)