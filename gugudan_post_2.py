from markupsafe import escape
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello():
    html_str = """


    <!DOCTYPE html>
    <html lang = "kr">
    <head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    </head>
    <body>
    <form id="form_id" action="javascript:post_query()">
    <input type="text" name="dan" value="7">
    <button type="submit">Go</button>
    </form>
    <div id="results"></div>

    <script>
    function post_query() {
    $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/gugudan/",
    data: $("#form_id").serialize(),
    success: update_result,
    dataType: "html"
    });
    }
    function update_result(data) {
    $("#results").html(data);
    }
    </script>
        
    </body >
    </html >

    """

    return html_str


@app.route("/hello/<name>") #인사 바로 url
def say_hello(name):
    return f"안녕하세요! {escape(name)}님."


@app.route("/dan/<dan>") #구구단 바로 url
def gugudan_html(dan):
    html_str = ""
    for j in range(1, 10):
        html_str += f"{dan} X {j}= {int(dan) * j}<br>"
    return html_str


@app.route("/gugudan/") #바로 2단 url
def gugudan_arg_html():
    dan = request.args.get("dan", "2")
    html_str = ""
    for j in range(1, 10):
        html_str += f"{dan} X {j}= <strong>{int(dan) * j}</strong><br>"
    return html_str


app.run(debug=True,port=5001)