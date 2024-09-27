
def about_me():
    # dictionary
    me = {
        "first": "Dave",
        "last": "Burke",
        "age": 43
}

    print(me)


    # read values
    print(me["first"])
    print(me["age"])

    # add new elements
    me["email"] = "Burke@example"
    print(me)

    #update existing 
    me["age"] = 43

    #check if key exist, before reading
    if"preferred_color" in me:
        me["preferred_color"] 


def test_address():
    location = {
        "street": "Evergreen",
        "number": 27,
        "city": "Springfield",
        "state": "CA",
        "zip": "92101"
    }

    print("street", "number", "city")
    

about_me()
test_address()


