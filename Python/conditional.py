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

def printDigit(n):
    sum=0, count=0

    while(n!=0):
        rem = n%10
        print(rem)
        sum+=rem
        count+=1
        n = int(n/10)
    
    print(sum)
    print(count)

printDigit(325)