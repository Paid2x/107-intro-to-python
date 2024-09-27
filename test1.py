
# comment
name = "Dave"
last_name = "Burke"
age = 39
price = 12.99
found = True

print(name)
print(last_name)

# math
total = 21 / 21
print(total)


# if
if age < 100:
    print("Dont worry you are young!")
    print("inside the if")
    print("me too")


    print("I'm outside")


    # exc 1:
    # create an if, if the age is lower than 21,
    # show a message like "you can not drink alcohol"
    if age < 21:
        print ("you can not drink alcohol")

        #exc 2:
        # if you are is 21 and up, print "Do you fancy a beer?"
    if (age>=21):
        print("Do you fancy a  beer?")
        print("Do you fancy a  beer?")
        print("Do you fancy a  beer?")
        

    
def say_hello():
    print("hello there!")


# call function
say_hello()
say_hello()
say_hello()

def salute(name):
    print("HI " + name) 


    salute("john")
    salute("Jane")
    salute(name)

    def sum(num1, num2):
        total = num1 + num2
        print(total)


        sum(21,21)
        sum(9234, 13393)