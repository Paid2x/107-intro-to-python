

def products_test():
    catalog = [ 
        {"title": "Keyboard", "price": 45.33},
        {"title": "Mouse", "price": 20.00},
        {"title": "4K Monitor", "price": 195.93},
        {"title": "Ultrawide Monitor", "price": 425.16},
        {"title": "Webcam", "price": 42.50},
    ]

# A) print the title of each product
# B) print the price of each product
    total = 0
    for product in catalog:
        title = product["title"]
        price = product["price"]
        print(f"{title} ${price}")
        total = total + price
    
    print(f"The total is: {total}")


def students_test():
    students = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 34,
            "grade": "A",
            "due_balance": 325.00,
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "age": 56,
            "grade": "B",
            "due_balance": 30.00,
        },
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "age": 37,
            "grade": "B",
            "due_balance": 0.00,
        },
        {
            "first_name": "Carlos",
            "last_name": "Rodriguez",
            "age": 56,
            "grade": "B",
            "due_balance": 30.00,
        },
{
            "first_name": "Emma",
            "last_name": "Smith",
            "age": 22,
            "grade": "B",
            "due_balance": 150.00,
        },
        {
            "first_name": "Liam",
            "last_name": "Johnson",
            "age": 20,
            "grade": "A",
            "due_balance": 200.00,
        },
        {
            "first_name": "Olivia",
            "last_name": "Williams",
            "age": 23,
            "grade": "C",
            "due_balance": 220.00,
        },
        {
            "first_name": "Noah",
            "last_name": "Brown",
            "age": 21,
            "grade": "B",
            "due_balance": 180.00,
        },
        {
            "first_name": "Ava",
            "last_name": "Jones",
            "age": 24,
            "grade": "A",
            "due_balance": 300.00,
        },
{
            "first_name": "Ethan",
            "last_name": "Garcia",
            "age": 25,
            "grade": "C",
            "due_balance": 100.00,
        },
        {
            "first_name": "Sophia",
            "last_name": "Miller",
            "age": 26,
            "grade": "B",
            "due_balance": 250.00,
        },
    ]


    #A) print: LastName FirstName Grade  
    #A) print: Grade - firstName LasatName  
    for student in students:
        last = student["last_name"]
        first = student["first_name"]
        grade = student["grade"]

        print(f"{grade} - {first} {last}")

    print("-------------")

    #B) print total due

    for student in students:
        last = student["last_name"]
        first = student["first_name"]
        grade = student["grade"]
        due = student["due_balance"]

        print(f"{grade} - {first} {last}")
        total = total + due

    print(f"Total due: {total}")

    print("-------------")
# C) print the fist name of students with a A or B
    for student in students:
        first = student["first_name"]
        grade = student["grade"]

        if (grade == "A" or grade == "B"):
            print(first)

# D) print the fist name of students with a A or B
    for student in students:
        first = student["first_name"]
        grade = student["grade"]

        if (grade == "A" or grade == "B"):
            print(first)

# C) print the fist name of students with a A or B
    # D) count how may students are 25 yo or older
    count = 0
    for student in students:
        first = student["first_name"]
        grade = student["grade"]
        age = student["age"]

        if (grade == "A" or grade == "B"):
            print(first)

        if age >= 25:
            count = count + 1

    print(f"There are {count} students 25 yo or older")



    classA = 0
    for student in students:
        first = student["first_name"]
        grade = student["grade"]
        age = student["age"]

        if (grade == "A"):
            classA += 1


products_test()
students_test()

