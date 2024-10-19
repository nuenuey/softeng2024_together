from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dodo")
def dodo():
    return render_template('dodo.html')

@app.route("/soonday")
def soonday():
    return render_template('soonday.html')

@app.route("/so_ba")
def so_ba():
    return render_template('so_ba.html')

@app.route("/flower")
def flower():
    return render_template('flower.html')

@app.route("/king")
def king():
    return render_template('king.html')

@app.route("/onedanggo")
def onedanggo():
    return render_template('onedanggo.html')

# posts = [
#     {
#         'title': '통집',
#         'content': '소개 내용이 아직 없습니다.'
#     },
#     {
#         'title': '덕천식당',
#         'content': '소개 내용이 아직 없습니다.'
#     }
# ]




@app.route("/posts")
def post():
    df = pd.read_csv("./data.csv")

    posts = []
    for i, row in df.iterrows():
        posts.append({
            "title": row['title'],
            "content": row['content']
        })

        print(posts)
    return render_template('posts.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)