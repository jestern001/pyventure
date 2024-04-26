from dataclasses import dataclass


@dataclass
class Player:
    name: str
    DEFAULT_PLAYER_NAME = "Flip"


def player_factory() -> Player:
    name = input("What's your name? ")
    return Player(name=Player.DEFAULT_PLAYER_NAME)


if __name__ == "__main__":
    player = player_factory()

