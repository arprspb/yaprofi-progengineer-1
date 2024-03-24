#!/usr/bin/env python3

from random import choice

programmer_name = input()

class EmptryStringException(Exception):
    pass

data = dict()
while True:
    
    try:
        inp = input()
        if inp == '':
            raise EmptryStringException
        
        name, number = inp.split('-')
        data.update({name:number})
    except (EmptryStringException, EOFError):
        break
    except:
        break

values = data.values()

N = len(values)+1

difference = set(range(1, N+1)) - set(values)
if len(difference) == 1:
    print(list(difference)[0])
else:
    print(choice(list(range(1, N+1))))