#without exeception

# file=open("vivek.txt","r")
# print("file is opened")
#print("addition of 3+5 = "+str(3+5))


#with exeception
"""
import logging
logging.basicConfig(filename="logging_file",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s ")
try:
    logging.info("try to open not available file")
    file=open("vivek.txt","r")
except Exception as e:
    logging.info("exeception genrate")
    logging.info(e)
    print("exeption handling",e)
    logging.info("addition of 3+5 = "+str(3+5))
    print("addition of 3+5 = "+str(3+5))
"""

"""
import logging
logging.basicConfig(filename="logging_file",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s ")
try:
    logging.info("try to open not available file")
    file=open("vivek.txt","w")
    file.write("hwello vivek vala")
except Exception as e:
    logging.info("exeception genrate")
    logging.info(e)
    print("exeption handling",e)
    logging.info("addition of 3+5 = "+str(3+5))
    print("addition of 3+5 = "+str(3+5))
else:
    file.close()
    logging.info("else block execute so no error by tyr block")
    print("else block execute so no error by tyr block")
    """

import logging
logging.basicConfig(filename="logging_file.log",level=logging.DEBUG,format="%(asctime)s %(name)s %(levelname)s %(message)s")

try:
    logging.info(file=open("text3.txt","r"))
    file=open("text3.txt","r")
finally:
    logging.info("finaly block always executed ")
    print("finaly block always executed ")