from flask import Flask , render_template

app = Flask(__name__)

# 1. 홈 화면
@app.route("/")
def hello_world():
    return render_template()

# 2. 유저 프로필 화면 (동적 라우팅)
@app.route("/user/<userId>")
def profile(userId):
    # userId를 받아서 화면에 출력합니다.
    return f"<h1>{userId}님의 프로필</h1><p>이곳은 유저 상세 페이지입니다.</p>"

# 서버 실행 로직은 파일의 '최하단'에 딱 한 번만!
if __name__ == "__main__":
    app.run(debug=True)


