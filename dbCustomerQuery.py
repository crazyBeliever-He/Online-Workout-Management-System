# dbCustomerQuery.py
# 执行query代码，还会检查数据的合法性!!!!!!!!!!!!!!!!!!数据合法性还没做，并且没有反馈
import psycopg2
from flask import current_app


def connect_db():
    return psycopg2.connect(current_app.config['DATABASE_URI'])


def get_ids(table):
    if table == 'customer':
        query = 'SELECT customerid FROM customer ORDER BY customerid '
        with connect_db() as conn, conn.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    elif table == 'trainer':
        query = 'SELECT trainerid FROM trainer ORDER BY trainerid '
        with connect_db() as conn, conn.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
    return data


def customer_list():
    query = 'SELECT * FROM customer ORDER BY customerid '
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data


def add_customer(customer_id, first_name, last_name, address, phone, email, birthdate,
                 fitness_level, exercise_history, medical_history):
    if not address:
        address = None
    if not birthdate:
        birthdate = None
    if not fitness_level:
        fitness_level = None
    if not exercise_history:
        exercise_history = None
    if not medical_history:
        medical_history = None
    query = '''INSERT INTO customer (customerid, firstname, lastname, address, phone, email, birthdate, 
                                            fitnesslevel, exercisehistory, medicalhistory)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    values = [customer_id, first_name, last_name, address, phone, email, birthdate,
              fitness_level, exercise_history, medical_history]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()


def delete_customer(customer_id):
    query = 'DELETE FROM customer WHERE customerid = %s'
    values = [str(customer_id)]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()


def update_customer(customer_id, updated_data):
    # ！！！！！！！首先检查数据合法性
    # 构建 SET 部分
    set_values = ', '.join([f"{key}=%s" for key in updated_data.keys()])
    # 构建 SQL 查询语句
    query = f"UPDATE customer SET {set_values} WHERE customerid=%s"
    # 提取数据，注意将空字符串转换为 None
    values = [value if value != '' else None for value in updated_data.values()] + [str(customer_id)]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()


def search_customer(customer_id, first_name, last_name, phone, email, birthdate, fitness_level):
    # 构建查询语句
    query = 'SELECT * FROM customer WHERE 1=1'
    conditions = []
    values = []
    if customer_id:
        conditions.append("customerid = %s")
        values.append(customer_id)
    if first_name:
        conditions.append("firstname = %s")
        values.append(first_name)
    if last_name:
        conditions.append("lastname = %s")
        values.append(last_name)
    if phone:
        conditions.append("phone = %s")
        values.append(phone)
    if email:
        conditions.append("email = %s")
        values.append(email)
    if birthdate:
        conditions.append("birthdate = %s")
        values.append(birthdate)
    if fitness_level:
        conditions.append("fitnesslevel = %s")
        values.append(fitness_level)
    if conditions:
        query += ' AND ' + ' AND '.join(conditions)
    query += ' ORDER BY customerid ASC'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        customer_data = cursor.fetchall()
    return customer_data
