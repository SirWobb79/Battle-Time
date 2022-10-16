from time import sleep
import os
from random import randint

print("<Battle Time 1.0>\n")

name = input("Enter a name: ")

os.system("cls" if os.name == "nt" else "clear")

start_health = 25
start_defence = 3
start_mana = 5

player_health = start_health
player_defence = start_defence
player_mana = start_mana

cpu_health = start_health
cpu_defence = start_defence
cpu_mana = start_mana

print("<Battle Time 1.0>\n")

skip = False

game = True
while game:
	if player_health <= 0:
		player_health = 0
		print("\nYou Lose")
		
		replay = input("Do you want to play again? (Y/N)")
			
		if replay == "y":
			player_health = start_health
			player_defence = start_defence
			player_mana = start_mana
			
			cpu_health = start_health
			cpu_defence = start_defence
			cpu_mana = start_mana

			skip = False
		else:
			break
		
	elif player_defence < 0:
		player_defence = 0
		
	elif player_mana < 0:
		player_mana = 0

	print(f"{name}'s Turn\n\n")
    
	print(f"{name}'s Stats:")
	print(f"{player_health} HP\n{player_defence} DEF\n{player_mana} MANA")
	
	print("\nCPU's Stats:")
	print(f"{cpu_health} HP\n{cpu_defence} DEF\n{cpu_mana} MANA")
	
	action = input(f"\nWhat will {name} do?\n\n1: Attack (@CPU: -5 HP reduced by 2 if DEF is not 0, -1 DEF)\n2: Defend (@Player: +1 DEF)\n3: Magic (@CPU: -10 HP, -1 MANA)\n4: Heal (@Player: +5 HP, -1 MANA)\n>")
    
	if action == "1":
		if cpu_defence > 0:
			cpu_health -= 3
		else:
			cpu_health -= 5
		
		if cpu_defence > 0:
			cpu_defence -= 1
			
		skip = False
		print(f"{name} used Attack!")
		
	elif action == "2":
		player_defence += 1
		
		skip = False
		print(f"{name} used Defend!")
	
	elif action == "3":
		if player_mana > 0:
			cpu_health -= 10
			player_mana -= 1
			print(f"{name} used Magic!")
		else:
			skip = True
			print("You do not have enough MANA to use that move.")
		
	elif action == "4":
		if player_mana > 0:
			player_health += 5
			player_mana -= 1
			print(f"{name} used Heal!")
		else:
			skip = True
			print("You do not have enough MANA to use that move.")
				
	if skip == False:
		if cpu_health <= 0:
			cpu_health = 0
			print("\nYou Win")
			
			replay = input("Do you want to play again? (Y/N)")
			
			if replay == "y":
				player_health = start_health
				player_defence = start_defence
				player_mana = start_mana

				cpu_health = start_health
				cpu_defence = start_defence
				cpu_mana = start_mana

				skip = False
			else:
				break
		
		elif cpu_defence < 0:
			cpu_defence = 0
		
		elif cpu_mana < 0:
			cpu_mana = 0
		
		print("CPU's Turn\n\n")
    
		print(f"{name}'s Stats:")
		print(f"{player_health} HP\n{player_defence} DEF\n{player_mana} MANA")
	
		print("\nCPU's Stats:")
		print(f"{cpu_health} HP\n{cpu_defence} DEF\n{cpu_mana} MANA")
		
		print("\nCPU is thinking...")
		sleep(3)
	
		if cpu_mana > 0:
			cpu_action = randint(1,4)
		
		elif cpu_mana <= 0:
			cpu_action = randint(1,2)
	
		if cpu_action == 1:
			if player_defence > 0:
				player_health -= 3
			else:
				player_health -= 5
		
			if player_defence > 0:
				player_defence -= 1
			
			print("CPU used Attack!")
		
		elif cpu_action == 2:
			cpu_defence += 1
		
			print("CPU used Defend!")
		
		elif cpu_action == 3:
			player_health -= 10
			cpu_mana -= 1
		
			print("CPU used Magic!")
		
		elif cpu_action == 4:
			cpu_health += 5
			cpu_mana -= 1
		
			print("CPU used Heal!")