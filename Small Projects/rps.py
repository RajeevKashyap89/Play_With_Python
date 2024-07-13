import random


rock = '''
	_______
---'   ____)
	  (_____)
	  (_____)
	  (____)
---.__(___)
'''

paper = '''
	_______
---'   ____)____
		  ______)
		  _______)
		 _______)
---.__________)
'''

scissors = '''
	_______
---'   ____)____
		  ______)
	   __________)
	  (____)
---.__(___)
'''

choice = input('what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n0/1/2:')
computer_choice = random.randint(0,2)

if not choice.isdigit():
	print('Invalid choice, please try again by choosing the number between 0-2.')
else :
	choice = int(choice)
	if choice > 2:
		print('Invalid choice, please try again by choosing the number between 0-2.')
	elif choice == 0 or choice == 1 or choice == 2:
		if choice == 0:
			print(f'you chose: Rock {rock}')
		elif choice == 1:
			print(f'you chose: Paper {paper}')
		elif choice == 2:
			print(f'you chose: Scissors {scissors}')

		if computer_choice == 0:
			print(f'The computer chose: Rock {rock}')
			if choice == 2:
				print(f'you loose, Rock wins against scissors. Try Again!!')
			elif choice == 0:
				print('Its a Draw!, Try Again!!') 
			else:
				print('You Win!!!, Congratulations :)')

		elif computer_choice == 1:
			print(f'The computer chose: Paper {paper}')
			if choice == 0:
				print(f'you loose, paper wins against rock. Try Again!!')
			elif choice == 1:
				print('Its a Draw!, Try Again!!')  
			else:
				print('You Win!!!, Congratulations :)')	
		
		elif computer_choice == 2:
			print(f'The computer chose: Scissors {scissors}')
			if choice == 1:
					print(f'you loose, Scissors wins against paper. Try Again!!')
			elif choice == 2:
				print('Its a Draw!, Try Again!!') 
			else:
				print('You Win!!!, Congratulations :)')