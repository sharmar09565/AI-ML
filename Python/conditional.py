# age = int(input("Enter your age:"))

# if(age<18):
#     print("Underage")
# elif(age>=18):
#     print("Adult")
# else:
#     print("Old")


# Q1

# def printEven(a,b):
#     for i in range(a,b):
#         if(i%2==0):
#             print(i)
    
# printEven(2,10)


#Q2

# def printDigit(n):
#     sum=0 
#     count=0

#     while(n!=0):
#         rem = n%10
#         print(rem)
#         sum+=rem
#         count+=1
#         n = int(n/10)
    
#     print("Sum =",sum)
#     print("Digits =",count)

# printDigit(325)


#Q3

# for i in range(1,100):
#     if(i%3==0 and i%5==0):
#         print(i)


#Q4
# n = None

# while(True):
#     n = input("Enter n: ")
#     if(n=="Quit" or n=="quit"):
#         break
#     print(n)


#Q5

# def calculator(a,b,op):
#     match op:
#         case '+':
#             print(a+b)
#         case '-':
#             print(a-b)
#         case '*':
#             print(a*b)
#         case '/':
#             print(a/b)
#         case _:
#             print("Enter valid operand")
    
# a = int(input("Enter a: "))
# op = str(input("Enter operand: "))
# b = int(input("Enter b: "))

# calculator(a,b,op)


#Q6

# def is_prime(n):

#     if(n<2):
#         print("It is not prime")
#         return
    
#     isPrime = True
#     for i in range(2,n//2):     # // use floor division  5/2 = 2.5 but 5//2 = 2
#         if(n%i==0):
#             isPrime = False
#             break
#     if(isPrime):
#         print("It is prime")
#     else:
#         print("It is not prime")

# n = int(input("Enter a num: "))

# is_prime(n)



#Q7

n = 12
x = int(input("Guess a num between 1-100: "))
while(True):
    if(x<1 or x>100):
        x = int(input("Guess a num between 1-100: "))
    if(n==x):
        print("You guessed right")
        break
    elif(n>x):
        x = int(input("Guess higher num: "))
    else:
       x = int(input("Guess lower num: "))
        