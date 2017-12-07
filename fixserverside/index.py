from flask import Flask, jsonify, request
from simplefix import FixMessage

from fixserverside.models.user import User, UserSchema
from fixserverside.models.order import Order, OrderSchema

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [
  User(1, 'mohamed', 'med@gmail.com', 'azerty'),
  User(2, 'omar', 'omar@gmail.com', 'omar'),
  User(3, 'tahar', 'tahar@gmail.com', 'tahar'),
]

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/logon")
def simplefix_init():
    msg = FixMessage()
    msg.append_string("8=FIX.4.2")
    msg.append_string("35=O")
    mohamed = users[0]
    schema = UserSchema()
    print(msg.get("35"))
    return jsonify(schema.dump(mohamed))

# @app.route('/incomes')
# def get_incomes():
#   schema = IncomeSchema(many=True)
#   incomes = schema.dump(
#     filter(lambda t: t.type == TransactionType.INCOME, transactions)
#   )
#   return jsonify(incomes.data)
#
#
@app.route('/api/new-single-order', methods=['POST'])
def add_income():
  new_order = request.get_json()
  print(new_order)
  schema = UserSchema()
  user = schema.dump(
    filter(lambda o: o.email == new_order.email and o.password == new_order.password, users)
  )
  print(user)
  #logon(user[0].id)
  return "", 204

def logon(id):
    msg = FixMessage()
    msg.append_string("8=FIX.4.2")
    msg.append_string("35=A")
    msg.append_string("34=1")
    msg.append_string("49="+id)
    print("ok"+id)

def standard_header():
    msg = FixMessage()
    msg.append_string("8=FIX.4.2")
    msg.append_string("35=A")
    msg.append_string("34=1")
    msg.append_string("")
#
#
# @app.route('/expenses')
# def get_expenses():
#   schema = ExpenseSchema(many=True)
#   expenses = schema.dump(
#       filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
#   )
#   return jsonify(expenses.data)
#
#
# @app.route('/expenses', methods=['POST'])
# def add_expense():
#   expense = ExpenseSchema().load(request.get_json())
#   transactions.append(expense.data)
#   return "", 204


if __name__ == "__main__":
    app.run()