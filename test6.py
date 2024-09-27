
def products_test():
    products = [
        {
            "title": "Smartphone",
            "image": "smartphone.jpg",
            "price": 299.99,
            "category": "Electronics",
        },
        {
            "title": "Running Shoes",
            "image": "running_shoes.jpg",
            "price": 89.99,
            "category": "Footwear",
        },
        {
            "title": "Backpack",
            "image": "backpack.jpg",
            "price": 49.99,
            "category": "Accessories",
        },
        {
            "title": "Coffee Maker",
            "image": "coffee_maker.jpg",
            "price": 119.99,
            "category": "Home Appliances",
        },
{
            "title": "Wireless Headphones",
            "image": "wireless_headphones.jpg",
            "price": 159.99,
            "category": "Electronics",
        },
        {
            "title": "Fitness Tracker",
            "image": "fitness_tracker.jpg",
            "price": 59.99,
            "category": "Wearables",
        },
        {
            "title": "Digital Camera",
            "image": "digital_camera.jpg",
            "price": 349.99,
            "category": "Electronics",
        },
        {
            "title": "Yoga Mat",
            "image": "yoga_mat.jpg",
            "price": 25.99,
            "category": "Fitness",
        },
{
            "title": "Novel - 'Mystery of the Old Manor'",
            "image": "novel.jpg",
            "price": 14.99,
            "category": "Books",
        },
        {
            "title": "Portable Charger",
            "image": "portable_charger.jpg",
            "price": 39.99,
            "category": "Electronics",
        },
    ]

    # A) Print the Title and Prices of Electronics
    for product in products:
        title = product ["title"]
        price = product ["price"]   

        if product["category"] == "Electronics":
            print(f"{title} {price}")


    # B) What it the total of Electronics
        if category == "Electronics":
                print(f"{title} {price}")
                total += price

    print(f"The total for Electronics is: {total}")

# A) Print the Title and Price of Electronics
    # B) What is the total of Electronics?
    # C) How many Electronics products exist in the list?
    total = 0
    for product in products:
        title = product["title"]
        price = product["price"]
        category = product["category"]

        if category == "Electronics":
            print(f"{title} {price}")
            total += price


#C) How mane Electornics products are in the list
    total = 0
    count = 0
    for product in products:
        title = product["title"]
        price = product["price"]
        category = product["category"]

        if category == "Electronics":
            print(f"{title} {price}")
            total += price

    print(f"The total for Electronics is: {total}")





products_test()