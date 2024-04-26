
from database.database import Database
from database.models.character import Character


if __name__ == "__main__":
    db = Database()
    name = input("What's your name? ")
    player = Character()
    db.add_character(player)
    print(f"Hello {player.name}")
