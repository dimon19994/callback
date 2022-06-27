from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


callback = []


@app.route('/view')
def hello_world():
    print("show data", len(callback))

    try:
        show = callback[-1]
        row = ""
        if show != "":
            for i in show.items():
                row += f"{i[0]}  ->  {i[1]}<br><br>"
    except:
        row = "NO DATA"

    return row


@app.route('/add', methods=["POST", "GET"])
def add():


    data = {
        "headers": request.headers,
        "values": request.values,
        "method": request.method
    }
    if request.is_json:
        data["json"] = request.json
    else:
        data["data"]: request.data

    callback.append(data)

    print("get data")

    return {"status": "200 OK"}


if __name__ == '__main__':
    app.run()