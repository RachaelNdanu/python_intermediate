import logging

#create our logger (should always be on top) --step 1
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG) #set logging level --step 6

 
formatter = logging.Formatter( '%(asctime)s-%(name)s-%(message)s') #creating our formatter --step 4

#creating our file handler as a file in our folder-- step 2
file_handler = logging.FileHandler("log.log")
file_handler.setFormatter(formatter) #assign the formatter to the file we have our logs --step 5


#assigninng our file handler to our logger (the one we created) -- step 3
logger.addHandler(file_handler)

logger.debug ("Bug!")

 