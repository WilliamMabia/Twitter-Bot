from getpass import getpass
import logging
import os
import getpass

#Logging
logging.basicConfig(filename='logs/example.log',level=logging.DEBUG) #Logging to file
logging.debug('This message should go to the log file') 
logging.info('Testing logging info')
logging.warning('And this, too')

#os
#print(os.environ)
user_name = os.environ.get('USER') #Get user from environment
current_path = os.environ.get('PWD') #Get current path from environment
env = os.environ.get('ENV')
print(user_name) #print user name gotten from environment
print(current_path) #print current path gotten from environment
print(env)

loga = "i like to eat meat"

dict2  = {'a':1,'b':2,'c':3}

dict = {'a': dict2}


logb = dict['a']['b'] 


print(logb)
print(loga)

url = "https//www.simplilearn.com/tutorials/python-tutorial/strip-in-python"

a = url.split('/')[2].split('.')[0] #split url by '/' and get the second part of the split, split by '.' and get the first part of the split
#b = url.split('/')[2].split('.')[1] #split url by '/' and get the second part and split by '.' and get the second part

print ("a: ", url.split('/'))
#print ("b: ", b)
password = getpass.getpass( 'Enter your password: ')

print(password)