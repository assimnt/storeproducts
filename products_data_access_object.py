import mysql.connector
from sql_connection import get_sql_connection


def access_all_products(connection):
    cnx = mysql.connector.connect(user='root',password='SI03152398058',
                              host='127.0.0.1',
                               database='projectstore')
    cursor = connection.cursor()
    query = ("SELECT storeproducts.store_product_id , storeproducts.store_product_name, store_product_name.measurement_of_products_id ,"
             "storeproducts.price_of_products , storeproducts.category_of_products, product_measurements.product_measurements_name"
             "FROM storeproducts inner join product_measurements on product_measurements.idproduct_measurements_id =storeproducts.measurement_of_products-id")
    cursor . execute(query)
    response = []
    for ( store_product_id, store_product_name ,measurement_of_products_id,price_of_products,category_of_products,product_measurements_name) in cursor:
        response.append({
    'store_product_id' : store_product_id ,
    'store_product_name': store_product_name,
    'measurement_of_products_id':measurement_of_products_id,
    'price_of_products':price_of_products,
    'category_of_products': category_of_products,
            'product_measurements_name':product_measurements_name
        })

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO storeproducts "
             "(store_product_name, store_product_id,price_of_products)"
             "VALUES (%s, %s, %s)")
    data = (product['store_product_name'], product['store_product_id'], product['price_of_products'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid
    def delete_product(connection, store_product_id):
        cursor = connection.cursor()
        query = ("DELETE FROM storeproducts where store_product_id=" + str(store_product_id))
        cursor.execute(query)
        connection.commit()
        return cursor.lastrowid
        if __name__ == '__main__':
            connection = get_sql_connection()
            print(insert_new_product(connection, {
        'store_product_name': 'noodles',
        'store_product_id': '1',
        'price_of_products': 90
    }))


