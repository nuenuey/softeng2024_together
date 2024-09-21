from flask import Flask, request

app = Flask(__name__)


@app.route("/")  # 기본 페이지
def index():
    return """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
    <style>
    body {
  background-color: lightgray;}

    h1 {
  color: blue;
  text-align: center;}

    p {
  font-family: verdana;}

    table {
  width: 50%;
  margin: 0 auto;
  border-collapse: collapse;
  text-align: center;
  font-family: verdana;
  }

    th, td {
  padding: 10px;
  border: 1px solid black;
    }

    </style>

    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <title> 세계 시간 계산기 </title>
    </head>
    <body>
        <h1><세계 시간 계산기></h1>
        <form id="form_id" action="javascript:post_query()">
            <label> 시각 입력 예시 (HHMM) :
                <input type="text" name="time" required>
            </label>
            <button type="submit">결과 보기</button>
        </form>
        <div id="results"></div>
         <script>
        function post_query() {
        $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/time",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
        });
        }
        function update_result(data) {
        $("#results").html(data);
        }
         </script>

    </body>
    </html>
    """


@app.route("/time")
def time():
    inputTime = request.args.get("time")

    hour = int(inputTime[:2])
    minute = int(inputTime[2:])

    tokyo = f"{hour}시 {minute}분"
    shanghai = f"{(hour - 1) % 24}시 {minute}분"
    newyork = f"{(hour - 14) % 24}시 {minute}분"
    london = f"{(hour - 9) % 24}시 {minute}분"
    paris = f"{(hour - 8) % 24}시 {minute}분"
    berlin = f"{(hour - 8) % 24}시 {minute}분"

    return f"""
    <br><br>
    <table>
        <tr>
            <th>도시</th>
            <th>시간</th>
        </tr>
        <tr>
            <td>서울 (현재 시각)</td>
            <td>{hour}시 {minute}분</td>
        </tr>
        <tr>
            <td>일본, 도쿄 (+0시간)</td>
            <td>{tokyo}</td>
        </tr>
        <tr>
            <td>중국, 상하이 (-1시간)</td>
            <td>{shanghai}</td>
        </tr>
        <tr>
            <td>미국, 뉴욕 (-14시간)</td>
            <td>{newyork}</td>
        </tr>
        <tr>
            <td>영국, 런던 (-9시간)</td>
            <td>{london}</td>
        </tr>
        <tr>
            <td>프랑스, 파리 (-8시간)</td>
            <td>{paris}</td>
        </tr>
        <tr>
            <td>독일, 베를린 (-8시간)</td>
            <td>{berlin}</td>
        </tr>
    </table>
    """


if __name__ == "__main__":
    app.run(debug=True)
