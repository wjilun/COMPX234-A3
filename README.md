In this programm,I realise the function of communication between users and server,as follow I will tell you how I finish it.

First:
I create a tuple_space,actually I should create user_class firstly,but it's OK.In this tuple_space,I put tuples to store my 
tuples,and add the stats like error count to this class,making this to serve my later server class.

Second:
I create my user_class to make creating user instance easier later.In this class,I create encode_request to formate the information
read from file,and create other method like read_file and Get method to make a connection with server and change or get something
from server's tuple_space.

third:
I create server response my user's sending information,and in this class,I create threadings to handle the sending message and one
to execute the print_status misssion.

finally:
I create the instance of user_class,and run the codes, check the logic whether correct. 
