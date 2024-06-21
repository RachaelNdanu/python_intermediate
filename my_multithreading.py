import time
import threading



def calculate_squares (arr):
    for x in arr:
        time.sleep(0.2)
        print(f" square of {x}: {x**2}")


def calculate_cube (arr):
    for i in arr:
        time.sleep(0.2)
        print(f"cube of {i}: {i**3}")



arr = [2,4,6,9]

t =time.time()

t1 = threading.Thread(target=calculate_squares, args=(arr,))
t2 = threading.Thread(target=calculate_cube ,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("done in:" , time.time()-t)





