from dataclasses import dataclass


@dataclass
class Character:
    name: str = "Flip"
    location_name: str | None = None