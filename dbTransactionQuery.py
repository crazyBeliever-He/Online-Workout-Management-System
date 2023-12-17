# dbTransactionQuery.py
# 执行query代码，还会检查数据的合法性

from dbCustomerQuery import connect_db, get_ids


def transaction_list():
    query = 'SELECT * FROM transaction ORDER BY assignmentdate '
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data


def add_transaction(customer_id, trainer_id, program_level, monthly_fee, assignment_date):
    trainer_exit = get_ids('trainer')
    customer_exit = get_ids('customer')
    if customer_id not in customer_exit:
        print(customer_exit)
        print(customer_id)
        return "Customer does not exist"
    if trainer_id not in trainer_exit:
        return "Trainer does not exist"
    if program_level not in ['Gold', 'Silver', 'Bronze']:
        return "Invalid Program Level"
    query = '''INSERT INTO transaction (customerid, trainerid, programlevel, monthlyfee, assignmentdate)
                VALUES (%s, %s, %s, %s, %s)'''
    values = [customer_id, trainer_id, program_level, monthly_fee, assignment_date]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()
    return "Successfully"


def delete_transaction(customer_id, trainer_id):
    query = 'DELETE FROM transaction WHERE customerid = %s AND trainerid =%s'
    values = [str(customer_id), str(trainer_id)]
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        conn.commit()
    return "Successfully"


# noinspection SpellCheckingInspection
def search_transaction(customer_id, trainer_id, program_level, assignment_date):
    if program_level:
        if program_level not in ['Gold', 'Silver', 'Bronze']:
            return "Invalid Program Level"
    # 构建查询语句
    query = 'SELECT * FROM transaction WHERE 1=1'
    conditions = []
    values = []
    if customer_id:
        conditions.append("customerid = %s")
        values.append(customer_id)
    if trainer_id:
        conditions.append("trainerid = %s")
        values.append(trainer_id)
    if program_level:
        conditions.append("programlevel = %s")
        values.append(program_level)
    if assignment_date:
        conditions.append("assignmentdate = %s")
        values.append(assignment_date)
    if conditions:
        query += ' AND ' + ' AND '.join(conditions)
    query += ' ORDER BY assignmentdate'
    with connect_db() as conn, conn.cursor() as cursor:
        cursor.execute(query, values)
        transaction_data = cursor.fetchall()
    return transaction_data
