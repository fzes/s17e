#this is the exercise of lessone 17.
d = int(input('enter the date & I will tell the day of week:'))
if d>31 :
    print('It is wrong. the number should be equal to or less than 31.')
elif d%7 == 0 :
    print('day')
    print(d)
    print('is sunday.')
elif d%7 == 1 :
    print('day')
    print(d)
    print('is monday.')
elif d%7 == 2 :
    print('day')
    print(d)
    print('is teusday.')
elif d%7 == 3 :
    print('day')
    print(d)
    print('is wendsday.')
elif d%7 == 4 :
    print('day')
    print(d)
    print('is tursday.')
elif d%7 == 5 :
    print('day')
    print(d)
    print('is friday.')
elif d%7 == 6 :
    print('day')
    print(d)
    print('is saterday.')

