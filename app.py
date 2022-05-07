import calendar
from datetime import datetime
from flask import Flask, render_template, redirect, request
import studentdata as std
import functions as func

app = Flask(__name__, static_url_path="/")
app.secret_key = 'ahdbahibaiuhjonbawiuh'


# 设置默认界面
@app.route("/")
def default_page():
    return redirect('/login')


# 主界面接口
@app.route('/index')
def main_interface():
    return render_template("index.html")


# 图表统计页面接口
@app.route('/charts')
def charts():
    bar_options = func.char_department()
    pie_options = func.char_gender()
    bar_options1 = func.char_age()
    return render_template('charts.html', bar_options=bar_options, pie_options=pie_options, bar_options1=bar_options1)


# 学生个人信息页面接口(按学号查)
@app.route('/student-datas', methods=['GET', 'POST'])
def student_data():
    if request.method == 'GET':
        return render_template('student-datas.html')
    if request.method == 'POST':
        data_lst = func.search_snum_data(request.form.get('snum'))
        return render_template('student-datas.html', data_lst=data_lst)


# 添加学生信息
@app.route('/add-student-data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'GET':
        return render_template('add-student-data.html')
    if request.method == 'POST':
        func.add_data()
        return redirect('/student-datas')


# 查找全部学生信息接口
@app.route('/all-student-datas')
def all_student_data():
    data1_lst = func.search_data()
    return render_template('student-datas.html', data1_lst=data1_lst)


# 修改学生信息的接口
@app.route('/update-student-data/<data2_list>', methods=['GET', 'POST'])
def update_student_data(data2_list):
    snum = data2_list[2:6]
    data_list = func.search_snum_data(snum)
    if request.method == 'GET':
        return render_template('update-student-data.html', snum=snum, data_list=data_list)
    if request.method == 'POST':
        func.update_data(snum)
        return redirect('/student-datas')


# 删除学生信息的接口
@app.route('/delete-student-data/<data_list>')
def delete_student_data(data_list):
    num = data_list[2:6]
    std.Student(num, '', '', '', '', '', '').delete_data()
    return redirect('/student-datas')


# 毕业学生去向界面的接口
@app.route('/graduation')
def graduation():
    bar_options2 = func.char_direct()
    return render_template('graduation.html', bar_options2=bar_options2)


# 学生选课界面接口(按学号查询）
@app.route('/select-course', methods=['GET', 'POST'])
def select_course():
    if request.method == 'GET':
        return render_template('select-course.html')
    if request.method == 'POST':
        snum = request.form.get('snum')
        course_lst = func.show_snum_course(snum)
        return render_template('select-course.html', course_lst=course_lst)


# 修改学生选课接口
@app.route('/update-select-course/<course_lst>', methods=['GET', 'POST'])
def update_course(course_lst):
    snum = course_lst[1:5]
    course_lst1 = func.show_snum_course(snum)
    if request.method == 'GET':
        return render_template('update-select-course.html', snum=snum, course_lst1=course_lst1)
    if request.method == 'POST':
        func.update_select_course(snum)
        return redirect('/select-course')


# 学生选课界面(全部)
@app.route('/all-select-course')
def all_select_course():
    course_lst1 = func.show_course()
    return render_template('select-course.html', course_lst1=course_lst1)


# 学生成绩界面接口(按学号查)
@app.route('/grade', methods=['GET', 'POST'])
def grade():
    if request.method == 'GET':
        return render_template('grade.html')
    if request.method == 'POST':
        grade_lst = func.search_snum_grade(request.form.get('snum'))
        return render_template('grade.html', grade_lst=grade_lst)


# 全部学生成绩界面接口
@app.route('/all-grade')
def all_grade():
    grade_lst1 = func.search_grade()
    return render_template('grade.html', grade_lst1=grade_lst1)


# 修改学生成绩
@app.route('/update-grade/<grade_list>', methods=['GET', 'POST'])
def update_grade(grade_list):
    snum = grade_list[2:6]
    grade_list1 = func.search_snum_grade(snum)
    if request.method == 'GET':
        return render_template('update-grade.html', grade_list1=grade_list1, snum=snum)
    if request.method == 'POST':
        func.update_grade(snum)
        return redirect('/grade')


# 删除学生成绩的接口
@app.route('/delete-grade/<grade_list>')
def delete_grade(grade_list):
    num = grade_list[2:6]
    std.Grade(num, '', '', '', '').delete_grade()
    return redirect('/grade')


# 录入学生成绩的接口
@app.route('/add-grade', methods=['GET', 'POST'])
def add_grade():
    if request.method == 'GET':
        return render_template('add-grade.html')
    if request.method == 'POST':
        func.add_grade()
        return redirect('/grade')


# 奖惩情况界面接口
@app.route('/reward')
def reward():
    bar_options = func.chart_reward()
    bar_options1 = func.chart_reward_depart()
    reward_list = func.select_all_reward()
    return render_template('reward.html', bar_options=bar_options, bar_options1=bar_options1, reward_list=reward_list)


# 删除奖惩情况
@app.route('/delete-reward/<reward_list>')
def delete_reward(reward_list):
    snum = reward_list[2:6]
    std.Reward(snum, '', '', '', '', '', '', '').delete_reward()
    return redirect('/reward')


# 登录接口
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        res = func.login()
        if res == 1:
            return redirect('/index')
        else:
            return '账号不为admin,或密码错误！'


# 日历接口
@app.route('/calendar')
def show_calendar():
    date = datetime.today()
    this_month = calendar.month_abbr[date.month]
    return render_template('calendar.html', this_month=this_month, date=date, content=func.show_calender(date))


if __name__ == '__main__':
    app.run(port=8000)
