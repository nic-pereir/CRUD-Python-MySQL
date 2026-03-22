import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database="crud_python"
)

cursor = connection.cursor() # Object that executes SQL commands

import src

while True:
    answer = src.show_menu()

    if answer == 1:
        name = src.get_product_data()
        price = src.get_valid_price()
        stock = src.get_valid_stock()
            
        src.create_product(connection, name, price, stock)
        print()

    elif answer == 2:
        products = src.read_products(connection)
        
        print()
        print("ID | Nome        | Preço   | Estoque")
        print("-" * 40)

        for product in products:
            print(f"{product['id']:<2} | {product['name']:<10} | R$ {product['price']:<6.2f} | {product['stock']}")

        print()

    elif answer == 3:
        product_id = src.get_product_id()
        name = src.get_product_data()
        price = src.get_valid_price()
        stock = src.get_valid_stock()

        src.update_product(connection, product_id, name, price, stock)
        print()

    elif answer == 4:
        product_id = src.get_product_id()
        src.delete_product(connection, product_id)
        print()

    elif answer == 5:
        print("Program finished. Thanks!")
        break

    else:
        print("Invalid option. Please, try again.")