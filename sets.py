
myset = {1,2,3}


'''if 5 in myset:
    print ("yes")
else:
    print("no such value")'''


setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.intersection_update(setB)
print(setA)