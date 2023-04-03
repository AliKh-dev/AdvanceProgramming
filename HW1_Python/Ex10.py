import random
secret_number = random.randint(1,1000)
counter = 0
while True:
    entery_number = int(input())
    if entery_number == secret_number:
        print("You won this game!")
        break
    elif entery_number < secret_number:
        print("It is too small")
    else:
        print("It is too big")
    counter += 1

print(f"{counter} tries")