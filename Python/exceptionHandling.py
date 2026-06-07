# try - block of code that can cause an error is written inside it

try:
    x = int(input("ENter a num:"))
    ans = 10/x

# except - type of error that can occur. It can be built or user defined
except ZeroDivisionError:       # it is a builtin exception.
    print("Divisible by 0 is not possible")

except ValueError:      # invalid input exception. Like input is any string.
    print("Invalid input")

# else - if there is no exception/error then else block run
else:
    print(f"ans = {ans}")

# finally - When the program ends and we want to do after that. It runs in both case, if error happened or not.

finally:
    print("Program ends")