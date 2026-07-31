import asyncio
import random


class Player:
    """Create a Player with their own behavior.

    Attrattributes:
        name: The name of the player.
        health: The current health points of the player.
        damage: The amount of damage dealt per single attack.
        attack_speed: The attack delay interval in seconds.
    """

    def __init__(
        self, name: str, health: float, damage: float, attack_speed: float
    ) -> None:
        """Initializes a Player instance."""

        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed

    async def attack_boss(self, boss: "Boss") -> None:
        """
        Asynchronously simulates a player attacking the boss.

        Used asyncio.Lock for safely boss attack.
        Args:
            player  : The Player instance executing the attack.
            boss    : The Boss instance being attacked.
        """
        while boss.health > 0 and self.health > 0:
            async with boss.lock:
                boss.health -= self.damage
            print(f"{self.name} damaged the {boss.name}")
            await asyncio.sleep(self.attack_speed)
            if boss.health <= 0:
                print(f"{boss.name} was defeated")
                break
            if self.health <= 0:
                print(f"{self.name} was killed")


class Boss:
    """Create a Boss with a built-in asyncio.Lock.

    Attributes:
        name    : The name of the boss.
        health  : The current health points of the boss.
        damage  : The amount of damage dealt per single attack.
        attack_speed    : The attack delay interval in seconds.
        lock : asyncio.Lock
            An asynchronous lock used to ensure safe access to the boss's state.
    """

    def __init__(
        self, name: str, health: float, damage: float, attack_speed: float
    ) -> None:
        """Initializes a Boss instance."""
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed
        self.lock = asyncio.Lock()

    async def boss_attack(self, player_list: list[Player]) -> None:
        """
        Asynchronously simulates the boss attacking random players from a list.

        The attack cycle continues until either the boss dies or all players
        in the list are defeated.
        Args:
            boss: The Boss instance executing the attack.
            player_list: A list of Player instances participating in the raid.
        """
        while self.health > 0 and any(player.health > 0 for player in player_list):
            random_player = random.choice(player_list)
            if random_player.health > 0:
                random_player.health -= self.damage
                print(f"{random_player.name} was damaged by {self.name}")
                await asyncio.sleep(self.attack_speed)
            if not any(player.health > 0 for player in player_list):
                print(f"{self.name} killed everybody")


async def main():
    """Initializes characters and starts the battle simulation."""

    player1 = Player("Wizard", 30, 15, 5.5)
    player2 = Player("Archer", 70.5, 10.7, 3)
    player3 = Player("Knight", 50, 8, 1.5)
    boss = Boss("Dragon", 300, 20, 4)
    player_list = [player1, player2, player3]
    print("Fight started")
    await asyncio.gather(
        player1.attack_boss(boss),
        player2.attack_boss(boss),
        player3.attack_boss(boss),
        boss.boss_attack(player_list),
    )
    print("Fight finished")


asyncio.run(main())
