from flask import Flask, request
app = Flask(__name__)


callback = []


@app.route('/view')
def hello_world():
    return callback[-1]


@app.route('/add', methods=["POST", "GET"])
def add():
   data = request.json if request.is_json else request.data
   callback.append(data)

   return {"status": "200 OK"}


if __name__ == '__main__':
    app.run()