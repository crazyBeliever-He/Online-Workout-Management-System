# app.py
import random

from flask import Flask, render_template, request, redirect, url_for, jsonify

from dbCustomerQuery import *
from dbTrainerQuery import *

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
    customers = customer_list()
    return render_template('basic.html', func="customer", customer_data=customers)


# noinspection SpellCheckingInspection 添加customer元组
@app.route('/addCustomer', methods=['POST'])
def addCustomer():
    # 赋予一个不重复的id
    existing_ids = get_ids('customer')
    while True:
        customer_id = str(random.randint(1, 1000000))
        if customer_id not in existing_ids:
            break
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    address = request.form['address']
    phone = request.form['phone']
    email = request.form['email']
    birthdate = request.form['birthdate']
    fitness_level = request.form['fitness_level']
    exercise_history = request.form['exercise_history']
    medical_history = request.form['medical_history']
    add_customer(customer_id, first_name, last_name, address, phone, email, birthdate,
                 fitness_level, exercise_history, medical_history)
    # 添加完customer，展示所有数据
    return redirect(url_for('customer'))


# noinspection SpellCheckingInspection 通过id删除customer元组
@app.route('/deleteCustomer/<int:customer_id>', methods=['POST'])
def deleteCustomer(customer_id):
    delete_customer(customer_id)
    # 删除后，展示所有数据
    return redirect(url_for('customer'))


# noinspection SpellCheckingInspection  更新customer的某一元组
@app.route('/updateCustomer/<int:customer_id>', methods=['POST'])
def updateCustomer(customer_id):
    # 从前端获取更新的数据,前端通过JSON发送更新数据
    updated_data = request.json
    update_customer(customer_id, updated_data)
    return jsonify('app.py: successfully!')


# noinspection SpellCheckingInspection 查询符合要求的customer元组
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
    return render_template('basic.html', func="search_customer", customer_data=customer_data)


if __name__ == '__main__':
    app.run()
