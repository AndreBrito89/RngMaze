
#battle
def battle(player, enemy):
    while True:
        escapeState = ''
        
        print()
        print(f"Um {enemy.name} apareceu!")
        print(f"{player.name} HP: {player.healthPoints}/{player.maxHealthPoints}  |  SP: {player.sP}/{player.maxSP}")
        print(f"{enemy.name} HP: {enemy.healthPoints}/{enemy.maxHealthPoints}")
        print()
        print("O que deseja fazer?")
        print("1 - Attack")
        print("2 - Use item")
        print("3 - Attempt to escape")
        choice = input()
        
        # player attack
        if(int(choice) == 1):
            escapeState = False
            enemy.defend(player.attack())
            print(f"O jogador {player.name} atacou o {enemy.name} com {player.equipedWeapon.weaponName} e o dano foi: {player.attack()}")
            # enemy attack
            player.defend(enemy.attack())
            print(f"O {enemy.name} atacou o jogador! O dano recebido foi: {enemy.attackDmg}")
        # player uses item
        elif(int(choice) == 2):
            escapeState = False
            print("work in progress, cant use items yet")
        # attempts to escape
        elif(int(choice) == 3):
            escapeValue = random.randint(1,100)
            escapeState = player.escape(escapeValue)
            if(escapeState):
                print(f"{player.name} escapou!")
            else:
                print(f"Fuga mal sucedida, {enemy.name} errou seu ataque!")


        # after choosing option
        # checks if player successfully escaped
        if(escapeState):
            break
        # checks if player died
        if (player.healthPoints <= 0):
            print("Você morreu!")
            break
        # checks if enemy died
        if(enemy.healthPoints <= 0):
            print(f"O {enemy.name} morreu!")
            player.xpPoints += enemy.xpReward
            print(f"Voce recebeu {enemy.xpReward} xp.")
            print()
            createChest()
            break