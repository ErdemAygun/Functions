def connect_and_execute_sql_query():
    data = [1, 2, 3]
    raise TimeoutError('Unable to connect to database.')

    return data


def fetch_last_year_data():
    query = 'select * from sales'
    return connect_and_execute_sql_query(query)


def generate_report():
    try:
        data = fetch_last_year_data()
        last_year_sales = sum(data)
        print(f'Last year sales = {last_year_sales}')
    except TimeoutError:
        print('We are not able to connect to database, please try to connect again')


generate_report()