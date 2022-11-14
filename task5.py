


from random import sample
import string
from string import ascii_letters, digits

def get_random_password(n=8) -> str:
    str_ = sample(ascii_letters + digits, n)
    return "-".join(str_)

print(get_random_password())
