#Print your Name

print("Mahnoor")

# Q: Store numbers in variables and then print
X=5
print(X)

# Keyboard input
# Q: Make a program that asks a favorite dish
dish=input("enter fav dish ! ")
print(dish)
#Input number and check whether even or odd(IF else)

x=int(input("Enter any number! "))
if x%2==0:
    print("even")
else:
     print("odd")
#
n=[1,2,3]
#print these numbers on separate lines(for loop)
for i in n:
    print(i)
#print square of these numbers on separate lines(for loop)
for i in n:
    print(i*i)
#print all numbers <100(while loop)
num=1
while num<100:
    print(num)
    num=num+1

# Q: Write a function to find sum of two numbers.(Function)
def sum(a,b):
    return a+b

rollNum={6,5,8,9,8,7}
rollNumList=[6,5,8,9,8,7]
print(rollNumList)


#Tuple (ordered, unchangeable, and allow duplicate values)

my_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(my_tuple)

#print second element of my_tuple
print(my_tuple[1])
#print the last item in the list
my_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(my_list[-1])
#insert pineapple in the list
my_list.append("pineapple")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
# Q: join tuples(Hint: using concatenation
tuple3=tuple1+tuple2
# Q: print the number of items in the fruits(Hint : usinf len method
fruits = ("apple", "banana", "cherry")
print(len(fruits ))

#print the third, fourth, and fifth item in the tuple.(Hint: use slicing)
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Check if apple is in the list
fruits_set = ["apple", "banana", "cherry","apple"]
if "apple" in fruits_set:
 print("yes you have!")

# Write multiplication table using for loop.
# 2X1 =2
# 2X2 =4
# 2X3 =6
# 2X4 =8
# 2X5 =10
# 2X6 =12
# 2X7 =14
# 2X8 =16
# 2X9=18
# 2X10=20
numb=2
for i in range(1,11):
    print(numb,"X",i,"=",num*i)
#Make a function that sums the list mylist = [1,2,3,4,5]
mylist = [1,2,3,4,5]
def sumList(listp):
    result=0
    for i in listp:
        result=result+i
    return result

print(sumList(mylist))









