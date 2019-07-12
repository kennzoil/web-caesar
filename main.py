from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = '''<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            Encrypt a message!
            <br>
            <input type="text" name="rot" placeholder="Enter a number">
            <br><br>
            <textarea rows="4" cols="50" name="text" placeholder="Enter your message">{0}</textarea>
            <br>
            <button type="submit">submit</button>
        </form>
    </body>
</html>'''



@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    encrypted = rotate_string(text, int(rot))
    return form.format(encrypted)


# hey! lol

app.run()