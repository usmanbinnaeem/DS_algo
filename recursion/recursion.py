def basepow(base, pow):
    if(pow == 1):
        return base
    if(pow != 1):
        return basepow(base, pow-1) * base


print('5 power 5 is ', basepow(5, 3))
