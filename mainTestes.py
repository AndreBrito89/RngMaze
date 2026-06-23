from Enemies.Enemy import Boss, Enemy
from game_logic import (
    attempt_player_escape as logic_attempt_player_escape,
    createNewWeapon,
    create_player_from_choice,
    list_player_consumables,
    resolve_enemy_attack as logic_resolve_enemy_attack,
    resolve_player_attack as logic_resolve_player_attack,
    use_player_consumable,
)


def read_choice(valid_choices):
    valid_choices = {str(choice) for choice in valid_choices}
    while True:
        choice = input().strip()
        if choice in valid_choices:
            return int(choice)
        print(f"Opcao invalida. Escolha uma das opcoes: {', '.join(sorted(valid_choices))}")


def show_consumables_menu(player):
    consumables = list_player_consumables(player)
    if not consumables:
        print("Inventario vazio.")
        return None

    print("Escolha um item para usar:")
    for display_index, (_, slot) in enumerate(consumables, start=1):
        print(f"{display_index} - {slot.consumable.name} x{slot.quantity} ({slot.consumable.description})")
    print("0 - Voltar")

    valid_choices = [0] + list(range(1, len(consumables) + 1))
    choice = read_choice(valid_choices)
    if choice == 0:
        return None

    slot_index, _ = consumables[choice - 1]
    return slot_index


#create new player
def createNewPlayer():
    print("Digite seu nome:")
    playerNameInput = input()
    
    print("Gostaria de usar os pontos extras em")
    print("1 - HP")
    print("2 - DMG")
    print("3 - SP")
    choice = read_choice([1, 2, 3])

    player = create_player_from_choice(playerNameInput, choice)


    print(f"Jogador {player.name} criado com sucesso!")
    return player


def resolve_player_attack(player, enemy):
    return logic_resolve_player_attack(player, enemy)


def resolve_enemy_attack(player, enemy):
    return logic_resolve_enemy_attack(player, enemy)


def attempt_player_escape(player, escape_value=None):
    return logic_attempt_player_escape(player, escape_value=escape_value)




#battle
def battle(player, enemy):
    while True:
        escapeState = ''
        #add option to:
        # * attack -> attack enemy / enemy attacks
        # * use consumable -> uses consumable / enemy attacks
        # * run -> uses stamina and attempts to evade battle / enemy whiffs attack

        print()
        print(f"Um {enemy.name} apareceu!")
        print(f"{player.name} HP: {player.playerClass.healthPoints}/{player.playerClass.maxHealthPoints}  |  SP: {player.playerClass.sP}/{player.playerClass.maxSP}")
        print(f"{enemy.name} HP: {enemy.healthPoints}/{enemy.maxHealthPoints}")
        print()
        print("O que deseja fazer?")
        print("1 - Attack")
        print("2 - Use item")
        print("3 - Attempt to escape")
        choice = read_choice([1, 2, 3])
        
        # player attack
        if(choice == 1):
            escapeState = False
            attack_damage, applied_player_damage = resolve_player_attack(player, enemy)
            print(f"O jogador {player.name} atacou o {enemy.name} com {player.playerClass.equipedWeapon.weaponName} e o dano foi: {attack_damage} (efetivo: {applied_player_damage})")
            # enemy attack
            enemy_attack_damage, applied_enemy_damage = resolve_enemy_attack(player, enemy)
            print(f"O {enemy.name} atacou o jogador! O dano recebido foi: {enemy_attack_damage} (efetivo: {applied_enemy_damage})")
        # player uses item
        elif(choice == 2):
            escapeState = False
            slot_index = show_consumables_menu(player)
            if slot_index is None:
                continue

            success, message = use_player_consumable(player, slot_index)
            print(message)

            # Using consumable spends a turn.
            enemy_attack_damage, applied_enemy_damage = resolve_enemy_attack(player, enemy)
            print(f"O {enemy.name} atacou o jogador! O dano recebido foi: {enemy_attack_damage} (efetivo: {applied_enemy_damage})")
        # attempts to escape
        elif(choice == 3):
            escapeState = attempt_player_escape(player)
            if(escapeState):
                print(f"{player.name} escapou!")
            else:
                print(f"Fuga mal sucedida, {enemy.name} errou seu ataque!")


        # after choosing option
        # checks if player successfully escaped
        if(escapeState):
            break
        # checks if player died
        if (player.playerClass.healthPoints <= 0):
            print("Você morreu!")
            break
        # checks if enemy died
        if(enemy.healthPoints <= 0):
            print(f"O {enemy.name} morreu!")
            player.xpPoints += enemy.xpReward
            print(f"Voce recebeu {enemy.xpReward} xp.")
            print()
            break



if __name__ == "__main__":
    # enemy
    rato = Enemy('Rat', 12, 12, 3, 0, 20) #name, maxHp, hp, dmg, armor, xp
    ogre = Enemy ('Ogre', 21, 21, 9, 1, 50)
    lich = Boss('Lich', 69, 69, 12, 4, 100)

    # player
    jogador = createNewPlayer()
    print(f"Arma: {jogador.playerClass.equipedWeapon.weaponName} | Dano base: {jogador.playerClass.equipedWeapon.baseDamage} | Dano total: {jogador.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogador.playerClass.equipedWeapon.weaponRarity}")

    # 1st battle simulation
    battle(jogador, rato)

    # weapon drop simulation
    arma = createNewWeapon()
    jogador.playerClass.equipedWeapon = arma
    print("Voce encontrou uma nova arma!")
    print(f"Arma: {jogador.playerClass.equipedWeapon.weaponName} | Dano base: {jogador.playerClass.equipedWeapon.baseDamage} | Dano total: {jogador.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogador.playerClass.equipedWeapon.weaponRarity}")

    # 2nd battle simulation
    battle(jogador, ogre)

    # boss battle simulation
    battle(jogador, lich)
    if lich.healthPoints <= 0:
        boss_drop = lich.drop_weapon()
        jogador.playerClass.equipedWeapon = boss_drop
        print("O boss derrubou uma arma especial!")
        print(f"Arma: {jogador.playerClass.equipedWeapon.weaponName} | Dano base: {jogador.playerClass.equipedWeapon.baseDamage} | Dano total: {jogador.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogador.playerClass.equipedWeapon.weaponRarity}")


