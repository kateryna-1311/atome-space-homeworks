import asyncio
import random 

class Player():
    '''
    Create a Player with their own behavior.
    '''
    def __init__(self, name: str, health: float, damage: float, attack_speed: float) -> None:
        '''Initializes a Player instance.

        Args:
            name: The name of the player.
            health: The current health points of the player.
            damage: The amount of damage dealt per single attack.
            attack_speed: The attack delay interval in seconds.
        '''
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed

class Boss():
    '''
    Create a Boss with a built-in asyncio.Lock.
    '''
    def __init__(self, name: str, health: float, damage: float, attack_speed: float) -> None:
        '''Initializes a Boss instance.

        Args:
            name: The name of the player.
            health: The current health points of the player.
            damage: The amount of damage dealt per single attack.
            attack_speed: The attack delay interval in seconds.
        '''
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed
        self.lock = asyncio.Lock()

async def attack_boss(player: Player, boss: Boss) -> None:
    '''
    Asynchronously simulates a player attacking the boss.

    Used asyncio.Lock for safely boss attack.
    Args:
        player: The Player instance executing the attack.
        boss: The Boss instance being attacked.
    '''
    while boss.health > 0 and player.health > 0:
        async with boss.lock:
            boss.health -= player.damage
        print(f"{player.name} damaged the {boss.name}")
        await asyncio.sleep(player.attack_speed)
        if boss.health <= 0:
            print(f"{boss.name} was defeated")
            break
        if player.health <= 0:
            print(f"{player.name} was killed")

async def boss_attack(boss: Boss, player_list: list[Player]) -> None:
    '''
    Asynchronously simulates the boss attacking random players from a list.

    The attack cycle continues until either the boss dies or all players
    in the list are defeated.
    Args:
        boss: The Boss instance executing the attack.
        player_list: A list of Player instances participating in the raid.
    '''
    while boss.health > 0 and any(player.health > 0 for player in player_list):
        random_player = random.choice(player_list)
        if random_player.health > 0:
            random_player.health -= boss.damage
            print(f"{random_player.name} was damaged by {boss.name}")
            await asyncio.sleep(boss.attack_speed)
        if not any(player.health > 0 for player in player_list):
            print(f"{boss.name} killed everybody")

async def main():
    '''
    Initializes characters and starts the battle simulation.
    '''
    player1 = Player("Wizard", 30, 15, 5.5)
    player2 = Player("Archer", 70.5, 10.7, 3)
    player3 = Player("Knight", 50, 8, 1.5)
    boss = Boss("Dragon", 300, 20, 4)
    player_list = [player1, player2, player3]
    print("Fight started")
    await asyncio.gather(
        attack_boss(player1, boss),
        attack_boss(player2, boss),
        attack_boss(player3, boss),
        boss_attack(boss, player_list)
    )
    print("Fight finished")

asyncio.run(main())