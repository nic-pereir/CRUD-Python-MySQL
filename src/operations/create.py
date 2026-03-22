def create_product(connection, name, price, stock):
    """
    Create product in the database.

    Args:
        connection (_type_): Python connection with MySQL
        name (_str_): Product name
        price (_float_): Product price
        stock (_int_): Quantity of product in stock
    """
    cursor = None
    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO products (name, price, stock)
        VALUES (%s, %s, %s)
        """

        values = (name, price, stock)

        cursor.execute(query, values)
        connection.commit()

    except Exception as e:
        print(f"Error registering product: {e}")

    finally:
        if cursor:
            cursor.close()