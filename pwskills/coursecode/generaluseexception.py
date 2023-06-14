try:
    import vivek

except ImportError as e:
    print(e)
    def name():
        print("vala vivek")
    name()


dic={"key1":"vala","key2":"vivek",3:"john"}
try:
  print(dic["key3"])
except KeyError as e:
    print(e)


list=[1,2,3,4,5,6]
try:
    print(list[10])
except IndexError as e:
    print(e)

try:
    print(vivek)
except Exception as e:
    print(e)

try:
    print(vivek)
except NameError as e:
    print(e)

#syntax error

try:
    rint("vala vivek")
except Exception as e:
    print(e)

try:
    print("vala vivek")
except SyntaxError as e:
    print(e)
    print("vala vivek")
obj=10


try:
    print(len(obj))
except ValueError as e:
    print(e)

try:
    print(len(obj))
except Exception as e:
    print(e)