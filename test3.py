
def say_hello (name, age):
    print("Hi " + name + ", so you are" +str(age) + " years old")
    # F string
    print(f"Hi {name}, so you are {age} years old")




def format_address(street, number, city, zip):
    print(f"Please return to street: {street} {number} {city} {zip}")


def list_1():
    names = ["Dave", "Taiga", "Mike", "Conner"]
    print(names)

    #count the elements
    print(len(names)) # len =lenght of the list or sting

    #add element to list
    names.append("Taiga")
    print(names)

    #remove element from list
    names.remove("Taiga")
    print(names)

    # foor loop
    for name in names:
        print(name)


def get_total():
    price = [123, 234, 45, 12, 84, 123, 672, 787, 173, 51, 687, 146, 613, 6, 135]

    #A) print each price on a line
    #B) sum of all prices
    total = 0
    for price in prices:
        print(price)
        total = total + price

        print(f"The total is: {total}")

def test_list3():
    student_ages = [20, 29, 53, 65, 27, 35, 51, 45, 74, 46, 27, 20, 32, 47, 33, 27]
    #A) how many students are there?
    print(len(student_ages))
    #B): print ages greater than 30 years old
    for age in student_ages:
        if age > 30:
            print (age)


# solve this:
say_hello("john", 25) #Hi John, so you are 25 years old
say_hello("jane", 31) #Hi John, so you are 25 years old



# solve for this:
format_address("evergreen", 25, "Springfield", 92484)


print("------------")
list_1()

print("------------")
get_total()

print("------------")
test_list3()