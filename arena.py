from team import Team
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero


class Arena:
    def __init__(self):
        self.team_one = Team("Team1")
        self.team_two = Team("Team2")

    def create_ability(self):
        """Prompt for Ability information.
        return Ability with values from user Input
        """
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        """Prompt user for Weapon information
        return Weapon with values from user input.
        """
        name = input("What is the weapon's name?  ")
        max_damage = input("What is the max damage of the weapon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        """Prompt user for Armor information
        return Armor with values from user input.
        """
        name = input("What is the armor's name?")
        max_block = input("What is the armor's max defense?")
        return Armor(name, max_block)

    def create_hero(self):
        """Prompt user for Hero information
        return Hero with values from user input.
        """
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: "
            )
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor = armor

        return hero

    # build_team_one is provided to you
    def build_team_one(self):
        """Prompt the user to build team_one """
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    # HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        """Prompt the user to build team_two"""
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """Battle team_one and team_two together."""
        self.team_one.attack(self.team_two)

    def show_stats(self):
        """Prints team statistics to terminal."""
        print("\n")

        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        self.getTeamKD(self.team_one)
        self.getTeamKD(self.team_two)

        team_one_survivor_count = self.getSurvivingHeroes(self.team_one)
        team_two_survivor_count = self.getSurvivingHeroes(self.team_two)

        if team_one_survivor_count > team_two_survivor_count:
            print("Team one is the winner!")
        elif team_two_survivor_count > team_one_survivor_count:
            print("Team two is the winner!")
        else:
            print("It was a draw!")

    def getTeamKD(self, team):
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1

        KD = str(team_kills / team_deaths)
        print(team.name + " average K/D was: " + KD)

    def getSurvivingHeroes(self, team):
        survivorCount = 0
        for hero in team.heroes:
            if hero.deaths == 0:
                survivorCount += 1
                print("survived from " + team.name + ": " + hero.name)
        return survivorCount


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()