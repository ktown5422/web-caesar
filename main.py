from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="" method="post">
            <label>
                <input type="text" name="rot" value="0">
                <textarea name="text">
                </textarea>
            </label>
            <input type="submit">
        </form>

    </body>
</html>

"""
@app.route("/", methods=['POST'])
def encrypt():
    val_1 = int(request.form['rot'])
    val_2 = request.form['text']

    return "<h1>" + rotate_string(val_2, val_1) + "</h1>"

@app.route("/")
def index():
    return form

app.run()