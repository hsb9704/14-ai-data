from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/user/<userId>")
def profile(userId):
    return f"<h1>{userId}님의 프로필</h1><p>이곳은 유저 상세 페이지입니다.</p>"


if __name__ == "__main__":
    app.run(debug=True)







