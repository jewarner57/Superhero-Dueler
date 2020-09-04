from random import choice


class Team:
    def __init__(self, name):
        """Initialize your team with its team name and an
        empty list of heroes"""
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        """Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        """Prints all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        """Add Hero object to self.heroes."""
        self.heroes.append(hero)

    def stats(self):
        """Print team statistics."""
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        """ Battle each team against each other."""

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            current_hero = choice(living_heroes)
            # get current deaths of hero
            hero_deaths = current_hero.deaths

            current_opponent = choice(living_opponents)
            # get current deaths of opponent
            opponent_deaths = current_opponent.deaths

            # start the fight
            current_hero.fight(current_opponent)

            # check if deaths of hero or opponent changed
            if hero_deaths < current_hero.deaths:
                living_heroes.remove(current_hero)
            elif opponent_deaths < current_opponent.deaths:
                living_opponents.remove(current_opponent)