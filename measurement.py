def get_productmeasurements(connection):
    cursor = connection.cursor()
    query = ("select * from product_measurements")
    cursor.execute(query)
    response = []
    for (idproduct_measurments_id, product_measurement_name) in cursor:
        response.append({
            'idproduct_measurement_id': idproduct_measurments_id,
            'product_measurement_name': product_measurement_name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_productmeasurements(connection))