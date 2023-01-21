from flask import Flask, request, render_template
import bback.main as main

app = Flask(__name__)


@app.route('/') #나중에 URL coinback으로 수정
def main_site():
    st_name = request.args.get("stock_name") #종목명
    rt_value = request.args.get("ratio_value") #비율입력
    start_cal = request.args.get("start_day") #시작,끝 일
    end_cal = request.args.get("end_day") # request.args.get html url 파라미터를 가져옴 문자열로 넣기
    first_money = request.args.get("money") #초기값
    print(end_cal)

    return render_template("coinbacktest.html")