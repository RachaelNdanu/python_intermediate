import logging


logging.basicConfig (filename='test.log' , level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add (x, y):
    return x+y


def subtract (x, y):
    return x-y


def multiply (x, y):
    return x*y

def divide (x, y):
    return x/y

x = 20
y = 10

add_result = add(x,y)
logging.debug ('Add: {} + {} = {}'.format(x,y,add_result))

subt_result = subtract(x,y)
logging.debug ('subt: {} - {} = {}'.format(x,y,subt_result))

mult_result = multiply(x,y)
logging.debug ('mult: {} * {} = {}'.format(x,y,mult_result))

div_result = divide(x,y)
logging.debug ('div: {} / {} = {}'.format(x,y,div_result))