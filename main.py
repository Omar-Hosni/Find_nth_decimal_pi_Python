import math

def decimals(val):
    pi = round(math.pi, val)
    str_pi = str(pi)
    n_list = list(str_pi)
    return pi

roundTo = input('Enter the number of digits you want after the pi: ')

try:
    rountInt = int(roundTo)
    print(decimals(rountInt))
except:
    print('you did not enter an integer')
