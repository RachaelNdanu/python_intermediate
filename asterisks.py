my_tuple = (1,2,3)
my_set = {4,5,6}

new_list = [*my_tuple, *my_set]
print(new_list)

dict_a = {'a' : 7 , 'b': 8 }
dict_b = { "c": 9 , "d":9 }

my_dict = {**dict_a , **dict_b}
print(my_dict)