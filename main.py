from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

callback = []


@app.route('/view')
@app.route('/view/<int:id>')
def hello_world(id=1):
    print("show data", len(callback))

    row = ""
    try:
        show = callback[-id]
        if show != "":
            for i in show.items():
                row += f"--->{i[0].upper()}<---<br>{i[1]}<br>"
    except:
        row = "NO DATA"

    return row


@app.route('/add', methods=["POST", "GET"])
def add():
    row_data = ""
    if request.headers["content-type"] == 'application/x-www-form-urlencoded':
        for i in request.values.items():
            row_data += f"{i[0]}: {i[1]}<br>"
    elif request.headers["content-type"] == 'application/json':
        for i in request.json.items():
            row_data += f"{i[0]}: {i[1]}<br>"

    row_headers = ""
    for i in request.headers.items():
        row_headers += f"{i[0]}: {i[1]}<br>"

    data = {
        "method": request.method + "<br>",
        "data": row_data + "<br>",
        "headers": row_headers + "<br>",
    }

    callback.append(data)

    print("get data")

    return {"status": "OK"}


if __name__ == '__main__':
    app.run()