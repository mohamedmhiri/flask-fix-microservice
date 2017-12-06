from flask import Flask, jsonify, request
from simplefix import FixMessage

from fixserverside.models.user import User, UserSchema

app = Flask(__name__)

users = [
  User('mohamed', 'med@gmail.com', 'azerty'),
  User('omar', 'omar@gmail.com', 'omar'),
  User('tahar', 'tahar@gmail.com', 'tahar'),
]

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/logon")
def simplefix_init():
    msg = FixMessage()
    msg.append_string("8=FIX.4.2")
    msg.append_pair("9", "")
    mohamed = users[0]
    print(mohamed)
    return jsonify(mohamed)

# @app.route('/incomes')
# def get_incomes():
#   schema = IncomeSchema(many=True)
#   incomes = schema.dump(
#     filter(lambda t: t.type == TransactionType.INCOME, transactions)
#   )
#   return jsonify(incomes.data)
#
#
# @app.route('/incomes', methods=['POST'])
# def add_income():
#   income = IncomeSchema().load(request.get_json())
#   transactions.append(income.data)
#   return "", 204
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