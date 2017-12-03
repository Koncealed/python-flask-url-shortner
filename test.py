import random,string

print(''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(4, 9))))