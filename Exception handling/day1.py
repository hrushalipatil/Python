# program 1
# run time error
# print('hello')
# e=int(input("Enter the numberA")) #1
# f=int(input("Enter the numberB")) #2
# print(e/f)   # 0.5
# print("bye") # bye


# program 2
# number=[11,22,33,44,55]
# print(number[6])

# program 3
# logical error
# def calculateBonusSalary(amount):
#     return amount * 0.1
# print(calculateBonusSalary(10000))

# ==================================================
# program 4

# try except


# print("welcome")
# try:
#     e = int(input("Enter the number A : ")) # 10
#     f = int(input("Enter the number B : " )) # 0
#     print(e / f) # 10/0
#
# except Exception:
#     print("Please enter number ")
#
# print("bye")

# output:Please enter number
# bye

# 0
# 10
# 0.0
# bye


# try  except  else  finally
# print("welcome")
# names=["aboli","kabir","sanjeet","sayali"]
#
# try:
#     A=int(input("enter a numberA :"))
#     B=int(input("enter a  numberB : "))
#     print(A/B)
#     print(names[9])
#
# except ArithmeticError:
#     print("enter the number")
# except IndexError:
#     print("enter the correct index")
# except Exception:
#     print("Please correct the values")
#
# finally:
#     print(" will always execute")
#
# print("bye")
#
#

# A single try block can be follwed by several except block
# Multiple except blocks can be used to handle multiple excpetions
# We cannot write except block with try block
# We cannot write try block with except block
# Else block and finally block are not compulsory
# When there is no exception raised else block is executed after try block
# Finally block is always executed

# program 1
# try:
#     names = ["vrushali","kabir","sayali"]
#     a = int(input('Enter a numberA'))
#     b = int(input('Enter the number B'))
#     print(a/b)
#     print(names[4])
# except ArithmeticError:
#     print("please enter correct input")
# except IndexError:
#     print('please add more values to list')



# program2

# print("hello")
# try:
#     print(34/0)
# finally:
#     print("i will always execute")
# print("bye")

# output:
# ZeroDivisionError: division by zero

#Program 3
# print("hello")
# try:
#     print(34/0)
# except ZeroDivisionError:
#     print("output is not correct ")
# finally:
#     print("i will always execute")
# print("bye")

# output:
# hello
# output is not correct
# i will always execute
# bye

# program 4


def calculateAvg(list):
    [11, 22, 33][4]
    # [11,22,33][1]# enter the correct input{type error}

    total=0

    for i in list:
        total=total+i

    avg =total/len(list)

    return avg

try:
    a,b=calculateAvg([1,2,3,4,"a"])

    print(a)
    print(b)

except TypeError:
    print('enter the correct input{type error}')
except ZeroDivisionError:
    print('Arithmetic exception , enter correct value')
except Exception:
    print("exception")
finally:
    print("Always Executed ")










