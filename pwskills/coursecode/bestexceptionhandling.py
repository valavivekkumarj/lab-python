#best practise to exception handling

#  1.  use specific exception not use Exception in every erro handling
#  2.  use logging in every code for practise or projects
#  3.  not use multiple exception avoid use of multiple exception
import logging
logging.basicConfig(filename="prac2.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")

try:
    a=100/0
except ZeroDivisionError as e:
    logging.error("handling zero division error {}".format(e))

    #avoid use of multiple exception

try:
    a=100/0
except AttributeError as e:
    logging.error("handling attribute error {}".format(e))
except FileNotFoundError as e:
    logging.error("handling attribute error {}".format(e))
except ZeroDivisionError as e:
    logging.error("handling zero division error {}".format(e))


    ##always document all the error
    ##always clean up all the resources use in code 

    #example:

try:
    f=open("vivek.txt",'r')
    print(f.read())
except FileNotFoundError as e:
    logging.error("file not found {}".format(e))
finally:
    f.close()

