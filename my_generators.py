def countdown(num):
    print('starting to count')
    while num >= 0:
        yield num
        num -=1


cd = countdown(5)

value =next (cd)
print(value)

value =next (cd)
print(value)

print(next(cd))
   