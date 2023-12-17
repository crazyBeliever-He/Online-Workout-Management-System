# app.py
import random

from flask import Flask, render_template, request, redirect, url_for, jsonify

from dbCustomerQuery import *
from dbTrainerQuery import *
from dbTransactionQuery import *
from procedureOrFunction import *

app = Flask(__name__)
app.config['DATABASE_URI'] = 'postgresql://believer:728683007@192.168.56.101:5432/exp3and4'


# 根路由
@app.route('/')
def basic():
    customers = customer_list()
    trainers = customer_list()
    return render_template('basic.html', customer_data=customers, trainer_data=trainers)


# 展示customer关系表的所有数据
@app.route('/customer', methods=['POST', 'GET'])
def customer():
    customer_data = customer_list()
    return render_template('basic.html', func="customer", customer_data=customer_data)


# 添加customer元组
@app.route('/addCustomer', methods=['POST'])
def addCustomer():
    # 赋予一个不重复的id
    existing_ids = get_ids('customer')
    while True:
        customer_id = str(random.randint(1, 1000000))
        if customer_id not in existing_ids:
            break
    print(customer_id)
    print(existing_ids[0])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    birthdate = request.form['birthdate']
    fitness_level = request.form['fitness_level']
    exercise_history = request.form['exercise_history']
    medical_history = request.form['medical_history']
    result = add_customer(customer_id, first_name, last_name, address, phone, email, birthdate,
                          fitness_level, exercise_history, medical_history)
    # 添加完customer，展示所有数据
    if result != "Successfully":
        return render_template('basic.html', func=result)
    return redirect(url_for('customer'))


# 通过id删除customer元组
@app.route('/deleteCustomer/<int:customer_id>', methods=['POST'])
def deleteCustomer(customer_id):
    delete_customer(customer_id)
    # 删除后，展示所有数据
    return redirect(url_for('customer'))


# 更新customer的某一元组
@app.route('/updateCustomer/<int:customer_id>', methods=['POST'])
def updateCustomer(customer_id):
    # 从前端获取更新的数据,前端通过JSON发送更新数据
    updated_data = request.json
    update_customer(customer_id, updated_data)
    return jsonify('app.py: successfully!')


# 查询符合要求的customer元组
@app.route('/searchCustomer', methods=['POST'])
def searchCustomer():
    customer_id = request.form['customer_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    email = request.form['email']
    birthdate = request.form['birthdate']
    fitness_level = request.form['fitness_level']
    customer_data = search_customer(customer_id, first_name, last_name,
                                    phone, email, birthdate, fitness_level)
    if customer_data == "Invalid Fitness Level":
        return render_template('basic.html', func=customer_data)
    return render_template('basic.html', func="search_customer", customer_data=customer_data)


# 展示trainer关系表的所有数据
@app.route('/trainer', methods=['POST', 'GET'])
def trainer():
    trainer_data = trainer_list()
    return render_template('basic.html', func="trainer", trainer_data=trainer_data)


# 添加trainer元组
@app.route('/addTrainer', methods=['POST'])
def addTrainer():
    # 赋予一个不重复的id
    existing_ids = get_ids('trainer')
    while True:
        trainer_id = str(random.randint(1, 1000000))
        if trainer_id not in existing_ids:
            break
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    add_trainer(trainer_id, first_name, last_name, address, phone, email)
    # 添加完trainer，展示所有数据
    return redirect(url_for('trainer'))


# 通过id删除trainer元组
@app.route('/deleteTrainer/<int:trainer_id>', methods=['POST'])
def deleteTrainer(trainer_id):
    delete_trainer(trainer_id)
    # 删除后，展示所有数据
    return redirect(url_for('trainer'))


# 更新trainer的某一元组
@app.route('/updateTrainer/<int:trainer_id>', methods=['POST'])
def updateTrainer(trainer_id):
    # 从前端获取更新的数据,前端通过JSON发送更新数据
    updated_data = request.json
    update_trainer(trainer_id, updated_data)
    return jsonify('app.py: successfully!')


# 查询符合要求的trainer元组
@app.route('/searchTrainer', methods=['POST'])
def searchTrainer():
    trainer_id = request.form['trainer_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    email = request.form['email']
    trainer_data = search_trainer(trainer_id, first_name, last_name, phone, email)
    return render_template('basic.html', func="search_trainer", trainer_data=trainer_data)


# 展示trainer关系表的所有数据
@app.route('/transaction', methods=['POST', 'GET'])
def transaction():
    transaction_data = transaction_list()
    return render_template('basic.html', func="transaction", transaction_data=transaction_data)


# 添加transaction元组
@app.route('/addTransaction', methods=['POST'])
def addTTransaction():
    customer_id = request.form['customer_id']
    trainer_id = request.form['trainer_id']
    program_level = request.form['program_level']
    monthly_fee = request.form['monthly_fee']
    assignment_date = request.form['assignment_date']
    result = add_transaction(customer_id, trainer_id, program_level, monthly_fee, assignment_date)
    # 添加完transaction，展示所有数据
    if result != "Successfully":
        return render_template('basic.html', func=result)
    return redirect(url_for('transaction'))


# 通过id删除transaction元组
@app.route('/deleteTransaction/<int:customer_id>/<int:trainer_id>', methods=['POST'])
def deleteTransaction(customer_id, trainer_id):
    delete_transaction(customer_id, trainer_id)
    # 删除后，展示所有数据
    return redirect(url_for('transaction'))


# 查询符合要求的transaction元组
@app.route('/searchTransaction', methods=['POST'])
def searchTransaction():
    customer_id = request.form['customer_id']
    trainer_id = request.form['trainer_id']
    program_level = request.form['program_level']
    assignment_date = request.form['assignment_date']
    transaction_data = search_transaction(customer_id, trainer_id, program_level, assignment_date)
    if transaction_data == "Invalid Program Level":
        print("Invalid Program Level")
        return render_template('basic.html', func=transaction_data)
    return render_template('basic.html', func="search_transaction", transaction_data=transaction_data)


# 调用一个名为 over an age 的过程
@app.route('/overAge', methods=['POST'])
def overAge():
    age = int(request.form['over_an_age'])
    over_age_data = over_an_age(age)
    # 返回结果
    if over_age_data == "Wrong Age":
        return render_template('basic.html', func=over_age_data)
    return render_template('basic.html', func="over_an_age", over_age_data=over_age_data, age_data=age)


# 调用一个名为 fit and gold 的函数
@app.route('/fitGold', methods=['POST'])
def fitGold():
    fit_gold_data = fit_and_gold()
    # 返回结果
    return render_template('basic.html', func="fit_and_gold", fit_gold_data=fit_gold_data)


# 调用一个名为 clients per trainer 的函数
@app.route('/clientNumber', methods=['POST'])
def clientNumber():
    clients_per_trainer_data = clients_per_trainer()
    # 返回结果
    return render_template('basic.html', func="clients_per_trainer", clients_per_trainer_data=clients_per_trainer_data)


# 调用一个名为delete_young_members 的过程
@app.route('/deleteYoung', methods=['POST'])
def deleteYoung():
    result = delete_young_members()
    # 返回结果
    if result != "Successfully":
        return render_template('basic.html', func=result)
    return redirect(url_for('customer'))


# 调用一个名为 monthly money report 的函数
@app.route('/moneyReport', methods=['POST'])
def moneyReport():
    trainer_money_report_data = monthly_money_bring_in_by_rainer()
    # 返回结果
    return render_template('basic.html', func="trainer_money_report",
                           trainer_money_report_data=trainer_money_report_data)


if __name__ == '__main__':
    app.run()
