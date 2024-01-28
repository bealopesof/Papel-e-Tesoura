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
import random 
escolha = input('''Qual você escolhe? 
Digite 0 para pedra, 1 para papel ou 2 para tesoura.\n''') 

escolhas_listas = [rock, paper, scissors]
len_escolhas = len(escolhas_listas)

random_choise = random.randint(0, len_escolhas - 1) 

if escolha == "0":
  print(f"Você escolheu:\n {rock}")
  print("O Computador escolheu: " + escolhas_listas[random_choise])
  if random_choise == 0:
    print("Empate")
  elif random_choise == 1:
    print("Você perdeu!")
  else:
    print("Você ganhou!!")
elif escolha == "1":
  print(f"Você escolheu:\n {paper}")
  print("O Computador escolheu: " + escolhas_listas[random_choise])
  if random_choise == 0:
    print("Você ganhou!!")
  elif random_choise == 1: 
    print("Empate")
  else:
    print("Você perdeu!!")
elif escolha == "2":
  print(f"Você escolheu:\n {scissors}")
  print("O Computador escolheu: " + escolhas_listas[random_choise])
  if random_choise == 0: 
    print("Você perdeu!!")
  elif random_choise == 1:
    print("Você ganhou!!!")
  else:
    print("Empate") 
