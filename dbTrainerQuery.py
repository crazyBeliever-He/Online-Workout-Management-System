# dbTrainerQuery.py
# 执行query代码，还会检查数据的合法性

from dbCustomerQuery import connect_db


def trainer_list():
    query = 'SELECT * FROM trainer ORDER BY trainerid '
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data


def add_trainer(trainer_id, first_name, last_name, address, phone, email):
    if not address:
        address = None
    query = '''INSERT INTO trainer (trainerid, firstname, lastname, address, phone, email)
                VALUES (%s, %s, %s, %s, %s, %s)'''
    values = [trainer_id, first_name, last_name, address, phone, email]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()


def delete_trainer(trainer_id):
    query = 'DELETE FROM trainer WHERE trainerid = %s'
    values = [str(trainer_id)]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()


def update_trainer(trainer_id, updated_data):
    # 构建 SET 部分
    set_values = ', '.join([f"{key}=%s" for key in updated_data.keys()])
    # 构建 SQL 查询语句
    query = f"UPDATE trainer SET {set_values} WHERE trainerid=%s"
    # 提取数据，注意将空字符串转换为 None
    values = [value if value != '' else None for value in updated_data.values()] + [str(trainer_id)]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()


def search_trainer(trainer_id, first_name, last_name, phone, email):
    # 构建查询语句
    query = 'SELECT * FROM trainer WHERE 1=1'
    conditions = []
    values = []
    if trainer_id:
        conditions.append("trainerid = %s")
        values.append(trainer_id)
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
    if conditions:
        query += ' AND ' + ' AND '.join(conditions)
    query += ' ORDER BY trainerid ASC'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        trainer_data = cursor.fetchall()
    return trainer_data
