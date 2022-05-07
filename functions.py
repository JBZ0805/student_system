import studentdata as std
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from flask import request, session
import calendar

calendar.setfirstweekday(firstweekday=6)
week = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


# 登录功能
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username != 'admin':
        return '账号错误，请重新输入！'
    else:
        if password == '123456':
            session['username'] = username
            return 1
        else:
            return "密码错误，请重新登录"


# 图表展示各二级学院人数
def char_department():
    depart_lst = ['理学院', '计算机学院', '电子学院', '商学院', '海外教育学院', '地理学院']
    num_lst = []
    for item in depart_lst:
        student = std.Student('', '', '', '', '', f'{item}', '')
        num_lst.append(len(student.search_department()))
    bar = (Bar(init_opts=opts.InitOpts(bg_color='lightskyblue')).add_xaxis(depart_lst)
           .add_yaxis("人数", num_lst).set_global_opts(title_opts=opts.TitleOpts(title="各学院学生人数")))
    bar_options = bar.dump_options()
    return bar_options


# 图表展示男女比例
def char_gender():
    student1 = std.Student('', '', '男', '', '', '', '')
    student2 = std.Student('', '', '女', '', '', '', '')
    res1 = len(student1.search_gender())
    res2 = len(student2.search_gender())
    pie = (Pie(init_opts=opts.InitOpts(bg_color='lightgoldenrodyellow')).add('', [('男生', res1), ('女生', res2)])
           .set_global_opts(title_opts=opts.TitleOpts(title='男女学生比例'))
           .set_series_opts(label_opts=opts.LabelOpts(formatter='')))
    pie_options = pie.dump_options()
    return pie_options


def char_age():
    age_lst = [18, 19, 20, 21, 22, 23, 24, 25]
    num_lst = []
    for item in age_lst:
        student = std.Student('', '', '', f'{item}', '', '', '')
        num_lst.append(len(student.search_age()))
    bar = (Bar(init_opts=opts.InitOpts(bg_color='cornflowerblue')).add_xaxis(age_lst)
        .add_yaxis("人数", num_lst).set_global_opts(
        title_opts=opts.TitleOpts(title="各年龄学生人数")))
    bar_options = bar.dump_options()
    return bar_options


def char_direct():
    num_lst = []
    direct_lst = ['考研', '考公', '考编', '工作', '留学']
    for item in direct_lst:
        gradu = std.Graduation('', f'{item}')
        num_lst.append(len(gradu.search_direct()))
    bar = (Bar(init_opts=opts.InitOpts(bg_color='lightskyblue')).add_xaxis(direct_lst)
           .add_yaxis("人数", num_lst).set_global_opts(title_opts=opts.TitleOpts(title="毕业去向图")))
    bar_options = bar.dump_options()
    return bar_options


# 按学号查找单个学生的个人信息
def search_snum_data(snum):
    data_lst1 = []
    data_lst1.append(std.Student(snum, '', '', '', '', '', '').search_datas())
    return data_lst1


# 查找全部学生的个人信息
def search_data():
    data_lst = std.Student('', '', '', '', '', '', '').search_students()
    return data_lst


# 修改学生信息
def update_data(snum):
    st = []
    lst = ['name', 'gender', 'age', 'native-place', 'department', 'class-id']
    for item in lst:
        st.append(request.form.get(f'{item}'))
    std.Student(snum, st[0], st[1], st[2], st[3], st[4], st[5]).update_datas()


# 添加学生信息
def add_data():
    lst = ['snum1', 'name', 'gender', 'age', 'native-place', 'department', 'class-id']
    data_lst = []
    for item in lst:
        data_lst.append(request.form.get(f'{item}'))
    std.Student(data_lst[0], data_lst[1], data_lst[2], data_lst[3],
                data_lst[4], data_lst[5], data_lst[6]).add_datas()


# 按学号查找所有学生的选课信息
def show_course():
    course_lst = []
    for item in range(1006, 1106):
        course_lst.append(std.Course(f'{item}', '', '', '', '').search_course())
    return course_lst


# 按学号查找单个学生的选课信息
def show_snum_course(snum):
    course_lst = []
    course_lst.append(std.Course(snum, '', '', '', '').search_course())
    return course_lst


# 修改学生选课信息
def update_select_course(snum):
    course_lst = ['course1', 'course2', 'course3', 'course4']
    update_lst = []
    for item in course_lst:
        update_lst.append(request.form.get(f'{item}'))
    std.Course(snum, update_lst[0], update_lst[1], update_lst[2], update_lst[3]).update_course()


# 按学号查找单个学生的成绩
def search_snum_grade(snum):
    grade_lst = []
    grade_lst.append(std.Grade(snum, '', '', '', '').search_snum_grade())
    return grade_lst

# 查找全部学生的成绩
def search_grade():
    grade_lst = (std.Grade('', '', '', '', '').search_grade())
    return grade_lst


# 修改学生成绩
def update_grade(snum):
    st = []
    lst = ['course1', 'course2', 'course3', 'course4']
    for item in lst:
        st.append(request.form.get(f'{item}'))
    std.Grade(snum, st[0], st[1], st[2], st[3]).update_grade()


# 录入学生成绩
def add_grade():
    lst = ['snum', 'course1', 'course2', 'course3', 'course4']
    grade_lst = []
    for item in lst:
        grade_lst.append(request.form.get(f'{item}'))
    std.Grade(grade_lst[0], grade_lst[1], grade_lst[2], grade_lst[3], grade_lst[4]).add_grade()


# 图表展示各奖惩情况
def chart_reward():
    num_lst = []
    reward_lst = ['一等奖', '二等奖', '三等奖', '记过处分', '未获奖', '进步奖', '三好学生']
    for item in reward_lst:
        rew = std.Reward('', '', '', '', '', '', '', f'{item}')
        num_lst.append(len(rew.search_reward()))
    bar = (Bar().add_xaxis(reward_lst)
           .add_yaxis("人数", num_lst).set_global_opts(title_opts=opts.TitleOpts(title="奖惩情况统计图")))
    bar_options = bar.dump_options()
    return bar_options


# 图表展示各学院获得奖项人数
def chart_reward_depart():
    num_lst = []
    depart_lst = ['理学院', '计算机学院', '电子学院', '商学院', '海外教育学院', '地理学院']
    for item in depart_lst:
        rew = std.Reward('', '', '', '', '', f'{item}', ',', '').search_reward_snum()
        num_lst.append(len(rew))
    bar = (Bar(init_opts=opts.InitOpts(bg_color='lightskyblue')).add_xaxis(depart_lst)
           .add_yaxis("人数", num_lst).set_global_opts(title_opts=opts.TitleOpts(title="各二级学院获奖人数"), ))
    bar_options = bar.dump_options()
    return bar_options


# 查询所有奖惩的学号，姓名，二级学院，奖项
def select_all_reward():
    reward_list = std.Reward('', '', '', '', '', '', '', '').search_all_reward()
    return reward_list


# 展示日历
def show_calender(date):
    year = date.year
    yearInfo = dict()
    for month in range(1, 13):
        days = calendar.monthcalendar(year, month)
        if len(days) != 6:
            days.append([0 for _ in range(7)])
        month_addr = calendar.month_abbr[month]
        yearInfo[month_addr] = days
    return yearInfo
