largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        new_num = int(num)
        if largest is None or largest < new_num:
            largest = new_num
        elif smallest is None or smallest > new_num:
            smallest = new_num

    except:
        print("Invalid input")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
