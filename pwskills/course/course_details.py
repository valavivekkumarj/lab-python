import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))


from payment import payment_details

def course_de():
    print("data science master course")

course_de()
payment_details.payment_de()