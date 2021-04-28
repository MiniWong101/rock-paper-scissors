print("Welcome to rock paper scissors games")
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

choice = [rock,paper,scissors]


user = int(input("What whould you choose? Type 0 for rocks, 1 for paper or 2 for scissors\n"))
if user >=3 or user<0:
  print("Invalid Number")
else:
  print(choice[user])



  computer = random.randint(0,2)
  print("computer choose: ")
  print(choice[computer])

  if user == 0 and computer == 2:
   print("You win!")
  elif computer == 0 and user == 2:
   print("You lose!")
  elif computer > user:
   print("You lose!")
  elif user > computer:
   print("You win!")
  elif user == computer:
   print("Draw")




