import string
import random

password = []

def show_left_chars():
    print("Pozostało wolnych znaków: ",character_left)

def character_input(character):
    global character_left
    while character > character_left or character < 0:
        character = int(input("Spróbuj jeszcze raz! Ile ma byc duzych liter? "))
    character_left -= character


password_lenght = int(input("Jak długie ma być hasło? "))
while password_lenght<=5:
    print("Hasło powinno mieć więcej niż 5 znaków ! Spróbuj jescze raz! ")
    password_lenght = int(input("Jak długie ma być hasło? "))
character_left = password_lenght
show_left_chars()

uppercase_letters = int(input("Ile ma byc duzych liter? "))
character_input(uppercase_letters)
show_left_chars()


lowercase_letters = int(input("Ile ma byc malych liter? "))
character_input(lowercase_letters)
show_left_chars()


special_chars = int(input("Ile ma byc znakow specjalnych? "))
character_input(special_chars)
show_left_chars()

digit = int(input("Ile ma byc liczb?"))
character_input(digit)
show_left_chars()


for i in range(password_lenght):
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        uppercase_letters -= 1
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        lowercase_letters -= 1
    if special_chars > 0:
        password.append(random.choice(string.punctuation))
        special_chars -= 1
    if digit > 0:
        password.append(random.choice(string.digits))
        digit -= 1


random.shuffle(password)
print("".join(password))
