from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    name_give = request.form['name_give']
    count_give = request.form['count_give']
    address_give = request.form['address_give']
    phone_give = request.form['phone_give']
    item_give = request.form['item_give']

    doc = {'name': name_give,
           'count': count_give,
           'address': address_give,
           'phone': phone_give,
           'item': item_give}

    db.item.insert_one(doc)

    return jsonify({'result': 'success'})


@app.route('/order', methods=['GET'])
def listing():
    item_give = request.args.get('item_give')
    item_info = list(db.item.find({'item': item_give}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': item_info})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
