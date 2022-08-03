import random

choice = random.randint(1, 10)

print(choice)

if choice in (1, 2 ,3):
    print('ACCESSED')
else:
    print('DENIED')