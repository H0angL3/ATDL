import random
import string
char = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
digist = random.randint(10, 99)
print('{}_{}'.format(char,digist))