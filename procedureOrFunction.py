# procedureOrFunction.py
# 执行query代码，还会检查数据的合法性

from dbCustomerQuery import connect_db


def over_an_age(age):
    if age >= 0:
        query = 'SELECT * FROM over_an_age(%s)'
        values = [age]
        with connect_db() as conn, conn.cursor() as cursor:
            cursor.execute(query, values)
            data = cursor.fetchall()
        return data
    return "Wrong Age"


def fit_and_gold():
    query = 'SELECT * FROM fit_and_gold()'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data


def clients_per_trainer():
    query = 'SELECT * FROM clients_per_trainer()'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data


def delete_young_members():
    query = 'CALL delete_young_members()'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    return "Successfully"


def monthly_money_bring_in_by_rainer():
    query = 'select * from monthly_money_report() order by trainerfirstname, trainerlastname, totalmonthlyfee DESC'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data
