"""

import logging
logging.basicConfig(filename="prac2.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")

#write exception for age input
#we use custom exeception


class validate_age(Exception):
    def __init__(self,msg):
        self.msg=msg

def validate(age):
    logging.info("check age valid or not")
    if age<0:
        logging.info("negative age entered")
        raise validate_age("negative age is not valid")
    elif age>200:
        logging.info("very high age entered")
        raise validate_age("to much high age not possible")
    else:
        logging.info("valid age entered")
        print("valid age")
try:
    age=int(input("enter age"))
    validate(age)
except validate_age as e:
    print(e)
"""

#write code to enter mobile number and valid it must be 10 digit 
import logging
logging.basicConfig(filename="prac2.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")


class validate_number(Exception):
    def __init__(self,msg):
        self.msg=msg

def validate(number):
    strnumber=str(number)
    logging.info("checking for valid number")
    logging.info(number)
    if len(strnumber)!=10:
        logging.info("not valid number")
        raise validate_number("not valid number")
    else:
        logging.info("valid number")
        print("valid number")

try:
    number=int(input("enter mobile number =  "))
    validate(number)
except validate_number as e:
    logging.info(e)
    print(e)