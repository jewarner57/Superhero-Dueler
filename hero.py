from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health

    def fight(self, opponent):
        """Current Hero will take turns fighting
        the opponent hero passed in."""

        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")

        while opponent.is_alive() and self.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

        if opponent.is_alive():
            print(f"{opponent.name} won!")
        elif self.is_alive():
            print(f"{self.name} won!")

    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""
        self.abilities.append(weapon)

    def add_ability(self, ability):
        """ Add ability to abilities list """
        self.abilities.append(ability)

    def attack(self):
        """Calculate the total damage from all ability attacks.
        return: total_damage:Int
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def add_armor(self, armor):
        """Add armor to self.armors
        Armor: Armor Object
        """
        self.armors.append(armor)

    def defend(self):
        """Calculate the total block amount from all armor blocks.
        return: total_block:Int"""
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        """Updates self.current_health to reflect the
        damage minus the defense."""
        defense = self.defend()
        damage_taken = damage - defense
        if damage_taken < 0:
            damage_taken = 0
        self.current_health -= damage_taken

    def is_alive(self):
        """Return True or False depending on whether
        the hero is alive or not."""
        return self.current_health > 0


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
