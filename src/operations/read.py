def read_products(connection):
    """
    Ler produtos no BD

    Args:
        connection (_type_): Python connection with MySQL
    """
    cursor = None
    try:
        cursor = connection.cursor(dictionary = True)

        query = "SELECT * FROM products"
        cursor.execute(query) # Send command to the database

        products = cursor.fetchall() # Returns the data from the database
        return products

    except Exception as e:
        print(f"Error when searching for product: {e}")
        return []

    finally:
        if cursor:
            cursor.close()
