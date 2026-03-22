def update_product(connection, product_id, name, price, stock):
    """
    Atualizar produto no BD

    Args:
        connection (_type_): Python connection with MySQL
        product_id (_int_): Product ID
        name (_str_): Product name
        price (_float_): Product price
        stock (_int_): Quantity of product in stock
    """
    cursor = None
    try:
        cursor = connection.cursor()

        query = """
        UPDATE products
        SET name = %s, price = %s, stock = %s
        WHERE id = %s
        """

        values = (name, price, stock, product_id)

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount == 0: # Quantas linhas foram afetadas
            print("No products were found with that ID.")
        else:
            print("Product updated successfully!")

    except Exception as e:
        print(f"Error when updating product: {e}")

    finally:
        if cursor:
            cursor.close()
