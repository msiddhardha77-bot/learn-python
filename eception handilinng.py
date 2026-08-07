##exception handling
##try-> instructions from which we are expecting the exceptions
##except-> exceptionns are raised in try block it will be handle by this block
##else->no exceptions(optional)(it works after the try is correct)
##finally->always it will display

'''while True:
    try:
        a=int(input("enter a value"))
        b=int(input("ENTER B VALUE"))
        c=a//b
        print(c)
    except:
        print("excception raised")
    else:
        print("no exception raised")
    finally:
        print("program ends...")'''

#file handlind
#write()
'''a=open("siddu.txt","w")
b=a.write("pyhton full stack 22")
a.close()'''

'''a=open("siddu.txt","w")
b=a.write("codegnan it sulutions")
a.close()'''

'''c=input("enter the info")
a=open("siddu.txt","w")
b=a.write(c)
a.close()'''
'''a=open("siddu.txt","w")
b=a.write(input("enter the info"))
a.close()'''

#append()
'''a=open("siddu.txt","a")
b=a.write("\nnew batch")
a.close()'''

'''a=open("siddu.txt","w")
b=a.write(input("enter the values"))
a.close()'''
#readlines()
a=open("siddu.txt")
#print(a.read())#it will display entire content in the file
#print(a.readline())#it will display first line
#print(a.readlines())#it will display entire data  in list format
#print(a.read(50))#it will display no.of characters in file

#writelines()->it makes every object side by side
'''a=open("siddhardh.txt","w")
b=["siddu","srinath","vasu","roopa"]
a.writelines(b)
a.close()'''
#append values in one by one 
'''a=open("siddhardh.txt","w")
b=["siddu","srinath","vasu","roopa"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("functiions.py")
print(a.read())'''

'''a=open("C:\\Users\\ASUS\\Downloads\\python learning\\functiions.py")
print(a.read())'''

