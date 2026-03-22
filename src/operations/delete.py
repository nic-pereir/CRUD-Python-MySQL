def delete_product(connection, product_id):
    """
    Deletar produto no BD

    Args:
        connection (_type_): Python connection with MySQL
        product_id (_int_): Product ID
    """
    cursor = None
    try:
        cursor = connection.cursor()

        query = """
        DELETE FROM products
        WHERE id = %s
        """

        values = (product_id,) # The comma deletes the entire row from the table

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount == 0:
            print("No products were found with that ID.")
        else:
            print("Product deleted successfully!")

    except Exception as e:
        print(f"Error deleting product: {e}")
    
    finally:
        if cursor:
            cursor.close()



    