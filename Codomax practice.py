
#VARIABLES
name=("john")
print(name)

a=(1,2,3,4,5,6)
print(a)

hai=("sana","hana",1,2,34)
print(hai)

#LOOPS

#for loop
for i in range(1,10):
    print(i)

for i in range(1,20,3): #start,end,step
    print(i)

    #WHILE LOOP
    #wap to print your name

print("shaziya")
print("shaziya")
print("shaziya")
print("shaziya")
print("shaziya")

i=1
while i<=5:
    print("hello")
    i=i+1


    #FUNCTIONS
    def add(a, b):
     print(a + b)

add(10, 20)


#LIST
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

NAMES=["SANA","HANA","SHAFI"]

print(NAMES)

CINEMA=["RANABALI","KABIR SINGH","ANJALI123"]
print(CINEMA)

#basic python programs

#ADDITION OF TWO NUMBERS
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=a+b
print(c)

#even or odd
num=int(input("enter a number:"))
if num%2==0:
   print("even")
else:
   print("odd")

#factorial of a number
#factorial=3!=3*2*1=6

num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)