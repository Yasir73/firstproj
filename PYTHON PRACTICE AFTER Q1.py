# a = 10
# print(a)
# a = 23.1
# print(a)
# a = True
# print(a)
# a="THis is string\n this is second line"
# print(a)
# a="THis is string\tthis is second line"
# print(a)
# a,b="THis is string","this is second line"
# print(a,b)
# a,b= 10 , 20
# print(a,b)
# a,b,c= True , False,10
# print(a,b,c)
# lst = [10,20,13,14,15,False,True,2.10,"string"]
# print(lst)
# lst = list()
# lst.append("yasir")
# print(type(lst),lst)
# a = 11
# print(type(a),a)
# a = True
# print(type(a),a) type is the function which can tell the type of an expression
# a = 2+3*5-6/3  PEDMAS (Parentheses, Exponents, Division, Multiplication, Addition)
# print(a) 
# a = 2^4 this opeartion is called XOR 0010 xor 1000 is equal to 1010 whic is 6 in des
# print(a)
# a = 8//3 this is opeation devsion and gives the 2 which is 8/3 = 6   
# print(a)
# a = 7%4 this opeatiohn is equal to 3 
# print(a)
# this symbol is used for comment and can not be read by compiler or interpreter
# a = 2^3^2 this is equal to 10 XOR 11 equal to 01 and 01 Xor 10 equal to 3
# print(a)
# a = 2**4 this opeartion return 16
# print(a)
# a = 2%7 this opeation retuwn 2 becuse 2 is smaller than 7 if this heppens it returns 2 top velue
# print(a)
# a= int() this operation convert a to int class
# a = list() this opeation convert a to list class and so on
#  print(type(a))
# a = input() this operation gets value with empty message and print it 
# print(a)
# a = print("this is string") this operation print this is string and second statement print none
# print(a)
# a = 12
# if a == 13:
#     print("THE VALUE OF A IS =",13)
# else:
#     print ("THE VALUE OF A IS NOT =",13)
# a = 13
# if a <=13:
#     print("a is less than or equal to 13")
# elif  a>=13 and a<=14:
#     print("a is more than or equal to 13 ")
# elif  a>=14 and a<=16:
#     print("a is more than 14 and greater than 14")
# else:
#     print("the value is differnet")
# a =1
# if a == 1:
#     print("a is 1")
#     a == 0
#     if  a<2 and a==0:
#         print("a is on and a is greater than 2")
# a = tuple() a is tuple which is not change able
# print(type(a))
# a = 12,42,34,35 this is how you assign value to tuple
# print(a)
# a = {"name":"yasir","fathername":"Liaqat Ali","Roll NO":16,"City":"Sialkot"}
# print(a.keys())
# print(a.values())
# print(a.items())
# a = 3
# b = 4
# c = 5
# print("THE VALUE OF A IS {} THE VALUE OF B IS {} THE VALUE OF C IS {}".format(a,b,c))
# a = [10,20,30,40,50,60]
# print(a)
# a.append(70)
# print(a)
# a.append("THIS IS THE TEXT AFTER APPEND")
# print(a)
# a = [1,2]
# b = [1]
# print(a+b)
# print(b-a) this operation does work with list
# a = ["ali","usman"]
# b = ["Ahmed","umer"]
# print(a+b)
# a = [1,2,3]
# b = a.copy()
# print(b)
# a.append(4) this append does not copy the 4 to list b
# print()
# a = [[1,2],[2,3]] list within a list
# print(a[0][1]) this prints a list index 0 list and 1 value which is 2
# a = ["yasir","ali","ali"] in this list ali is come 2 times
# print(a.count("ali")) and count function count ali and print 2 on the screen
# a = ["kashif","saqib","yasir"] this function pop(remove) kashif on index 0
# b = a.pop(0) in assigmen kashif to b 
# print(b)
# print(a)
# a = 10
# print(a is a)
# b = 3
# print(a is b )
# a = 5 
# b = 3
# print(a is not b)
# a = ["p","q","r"] extend function extend s to the end of list a
# print(a)
# a.extend("s") this is the function
# print(a)
# a = 8                     a is 8 and a.bitlenght function tells us bits lenght of 8 which is 4
# print(a.bit_length())
# a = 5 +9              a is9 +5 14 conjugate means melap 
# print(a.conjugate())
# a = int(3/4)              this function returns 1 becuse 3/4 ko divide karenay say denominator 1 ata hai
# b = a.denominator
# print(b)
# a = int(4/3) this time 4 is up and 3 is down so numerator is 1
# b = a.numerator
# print(b)
# a = (1+3J) + (3J) real no is 1
# print(a.real) 
# a = (1+3J)+(1+3J) and imag no is 6J
# print(a.imag)
# a = "Yasir Liaqat Ali" this function make Y copital letter and reset small letters
# print(a.capitalize())
# a = "The quick brown fox jumps over the lazy dog"    this function convert The quick brown fox jumps to Upper letters
# print(a.upper())
# a = "Second text" this function convert First S if small and first t for text to captial letters
# print(a.title())
# a = "Yasir liaqat ali" this function Swap the text case of Yasir liaqat ali
# print(a.swapcase())
# a = "Ali Kashif Liaqat Ali Father Name Liaqat Ali" this function remove First Ali and Last Ali and strip it form the variagble a
# print(a.strip("Ali"))
# a = "usman" this function returns True
# print(a.startswith("u"))
# a = "You \n are \n right" this function split line to ['You , 'are','right']
# print(a.splitlines())
# a = "My name is yasir" this function splic line to ['My','name','is','yasir']
# print(a.split())
# a = "I m Happy today today         *"  this function remove or strip * from right side
# print(a.rstrip("*"))
# a = "*              I m feeling sad today" this function removeor strip * form left side of text
# print(a.lstrip("*"))
# a = "Duck Duck is good search engine" #this function convert text to lower
# print(a.lower())
# a = "I am Learing Python" this function replace L with K
# print(a.replace("L","K"))
# a = "good day today" this function join good day with good day today text
# print(a.join("good day"))
# a = "I am good enough " this function check if the vairable a text is print able
# print(a.isprintable())
# a = "I am feeling great" this function checks is the value of a is numeric a is not numeric so it print False
# print(a.isnumeric())
# a = "Happy new islamic year" this function checks is a is isdigit or not
# print(a.isdigit())
# a = "it is raining in karachi" this function checks if text endswith hi
# print(a.endswith("hi"))
# a = "Today is 11 Muharram" this function print the text of a in 100 center vlaue
# print(a.center(100))
# a = "I m Learning PytHon" this function changes the text of a and make I L and H smaller
# print(a.casefold())
# a = "I am writing english text" this fuction is telling the no form left to write of text
# print(a.find("writing"))
# a = 10
# b = 11
# c =12
# if a==10 and b==11 and c==12 : This if condition compare 3 values with the above value and print the result 
#     print("a ={} b = {} c= {}".format(a,b,c))
# else:
#     print("a is not 10","b is not 12","c is not 13")
# a = input("Enter your name") this program compare input with yasir and print is other wise quit if i can not print quite statement it does give error
# if a=="yasir":
#     print("a = {}".format(a))
  
# else:
#     quit
# print(copyright) this statement print python copyrights
# print(credits) this statement prints  creadits for the people who participated in python
# a = "yasir liaqat ali" this function retuns 16
# print(len(a))
# a = [1,2,3,4,5,6,7] this function retrun 7 of list a maximum value
# print(max(a))
# a = [3,56,7,890] this function return 3 of list a minmum value
# print(min(a))
# a = "the quick brown fox jumps over the lazy dog" this function return z of variable a z because z is the max value in a
# print(max(a))
# a = {1,2,3},{25,434,68,89},{123,678,6,5343},{1,3,5}
# print(type(a))
# a = [{"Name":"Yasir","FatherN":"Liaqat ali"},{"id":"01","Address":"Local Area"}] a dic within a list
# print(a[1])
# Sch_class = ["NOofclass","Name of class","color of class","section of class"], this is a list in a list first there are labels and then there is class data
# cla1_data = [[[1,"firstclass","pink","pink1"],
#            [2,"firstclass","yellow","pink2"],
#            [3,"firstclass","brown","pink3"]],
#            [[1,"secondclass","orange","orange1"],
#            [2,"secondclass","orange","orange2"],
#            [3,"secondclass","orange","orange3"]]]
# print(cla1_data[1][1])
# a =((1,2,3),(4,5,6)) tuple within in a tuple 
# print(a[1][2])
# a = [[1,2,3],(4,5,6)] tuple within a list
# print(a[1][2])
# a = ([1,2,3],(4,5,6)) list within tuple
# print(a[0][2])
# a = {"yasir": [1,2,3,4,5,6]} list in a dictionary a has values of a and for loop gives us the values of list with in the list
# b = a.values()
# print(b)
# for i in b:
#     print(i[5])
# a = {"yasir": [[1,2,3],[4,5,6]]}  dictionary within a value and accessing thir value with for loop
# b = a.values()
# print(b)
# for i in b:
#     print(i[1][1])
# for i in range(1,10): this function create no from 1 to 9 and convert it to str and print the result
#     i = str(i)
#     print(i.splitlines())
# a = 0                 this while loops prints the value form 1 to 10 
# while a<10:
#     print(a)
#     a+=1
# a = 10                    create a beautifull lines of 0 and 00 and 0000 with while loops
# while a > 0:
   
#     print(a *[[0],[00],[000]])
#     a -= 1
# def myfunc(): this function create line of This is the basic function time the charctors
#     a = "This is the basic function created by ali"
#     for i in a :
#         print(a)
    
# myfunc()
# def myfunc():  this function create the lines of a text on time
#     a = "This is the basic function created by ali"
#     for i in a :
#         print(i)
    
# myfunc()
# def plus(a,b): this function print the sum of a and b and after calling the function and providing arguments it print 7
#     print(a+b)
    
# plus(3,4)
# a = [1,2,3]               sum the function and its use
# num = sum(a , 10)
# print(num)
print("second file")
#lkjkjlkjkj
# rrttrerttrrretrtrt