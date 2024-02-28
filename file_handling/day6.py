#
# reclen = 10
#
# with open("cities.bin" ,"wb") as file :
#     n = int(input("enter a number of cities :"))
#     for i in range(n):
#         city_name = input("Enter a cities :")
#
#         city_name_length = len(city_name)
#         # Pad the city name with spaces to ensure it's 10 characters long
#         # if city_name is 'Pune', it becomes 'Pune      '
#         city_name = city_name + (reclen - city_name_length) * " "
#
#         city_name_bytes = city_name.encode()
#
#         file.write(city_name_bytes)


# reclen = 10
# with open('cities.bin','rb') as file:
#     n = int(input('Enter the record you wish to read'))  #3
#     file.seek(reclen *(n-1))
#     str = file.read(reclen)
#     str = str.decode()
#     print(str)


record_length = 10
with open("Fruits.bin", "wb") as file:
    n = int(input("Enter a number of fruits :"))
    for i in range(n):
        Fruits_names = input("Enter a fruits :")
        fruits_name_length = len(Fruits_names)
        Fruits_names = Fruits_names + (record_length - fruits_name_length) * " "
        Fruits_names_bytes = Fruits_names.encode()
        file.write(Fruits_names_bytes)

record_length = 10
with open("Fruits.bin", "rb") as file:
    n = int(input("enter a number which you want to read :"))  # 3
    file.seek(record_length * (n - 1))  # 10 * (3-1) ===>20
    str = file.read(record_length)
    str = str.decode()
    print(str)

# OUTPUT
# WRITE
# Enter a number of fruits :5
# Enter a fruits :apple
# Enter a fruits :banana
# Enter a fruits :papaya
# Enter a fruits :mango
# Enter a fruits :graphs

# READ
# enter a number which you want to read :3
# papaya
