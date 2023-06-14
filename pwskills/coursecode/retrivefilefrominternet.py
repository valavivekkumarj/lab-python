#get the data from multiple file using function and threading
import threading
import urllib.request

def file_get(url,filename):
    urllib.request.urlretrieve(url,filename)
    

    #check fuction 
#file_get("https://github.com/valavivekkumarj/solved-problems/blob/main/mergesortpla.java","mfile1.txt")

#now using thread retrive three file
list_url=["https://github.com/valavivekkumarj/solved-problems/blob/main/mergesortpla.java","https://github.com/valavivekkumarj/solved-problems/blob/main/mytictactoegame.java","https://github.com/valavivekkumarj/solved-problems/blob/main/mytictactoegame.java"]
list_file=["file1.txt","fil2.txt","file3.txt"]
thread=[threading.Thread(target=file_get,args=(list_url[i],list_file[i]))for i in range(len(list_url))]

print(thread)

for i in thread:
    i.start()