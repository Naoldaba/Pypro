

import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
numbers="123456789"
symbols="!@#$%^&*?/><,."

this_str=upper+lower#+numbers+symbols
length=8
password="".join(random.sample(this_str,length))
print(f'your generated password is {password}')



















