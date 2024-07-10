# PART 2


# retrive delete replace add
reclen = 10

with open("cities.bin", "wb") as file:
    n = int(input("enter a number of cities :"))
    for i in range(n):
        city_name = input("Enter a cities :")

        city_name_length = len(city_name)
        # Pad the city name with spaces to ensure it's 10 characters long
        # if city_name is 'Pune', it becomes 'Pune      '
        city_name = city_name + (reclen - city_name_length) * " "

        city_name_bytes = city_name.encode()

        file.write(city_name_bytes)

# record_length = 10
# with open("color.bin", "wb") as file:
#     n = int(input("enter a number of colors to write:"))  # 5
#
# for x in range(n):
#     colorName = input("Enter a colorNames : ")
#     colorLength = len(colorName)
#     colorName = colorName + (record_length - colorLength) * " "
#
#     colorNameByte = colorName.encode()
#
#     file.write(colorNameByte)


record_length =10

with open('color.bin','rb') as file:


