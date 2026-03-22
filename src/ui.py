def show_menu():
    while True:
        print("------  PRODUCTS  ------")
        print("1 - Create new product")
        print("2 - Read the procuts")
        print("3 - Update a product")
        print("4 - Delete a product")
        print("5 - Exit")

        try:
            answer = int(input("What operation will be performed? "))
            if answer < 1 or answer > 5:
                print("Invalid option. Please, choose between 1 and 5.")
                continue
            return answer
        except (ValueError, TypeError):
            print("Invalid option. Please, enter a number.")

def get_product_id():
    while True:
        try:
            product_id = int(input("Enter the product id: "))
            if product_id < 0:
                print("The id must be greater than 0.")
            return product_id
        except (ValueError, TypeError):
            print("The id must be an integer.")

def get_product_data():
    while True:
        name = str(input("Enter the product name: ").lower())
        if name.strip() == "":
            print("The name cannot be null.")
            continue
        break
    return name

def get_valid_price():
    while True:
        try:
            price = float(input("Enter the product price: "))
            if price <= 0:
                print("The price must be greater than 0.")
                continue
            break                
        except ValueError:
            print("Invalid price. Please enter a real one.")
    return price

def get_valid_stock():
    while True:
        try:
            stock = int(input("Enter the quantity of product in stock: "))
            if stock < 0:
                print("Stock cannot be negative.")
                continue
            break
        except ValueError:
            print("The stock must be an integer.")
            continue
    return stock