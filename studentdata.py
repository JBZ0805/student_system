import pymysql

# 连接数据库，此前在数据库中创建数据库yuketang
db = pymysql.connect(host="localhost", user="root", password="123456", db="student")
# 使用cursor()方法获取操作游标
cursor = db.cursor()


# 学生类
class Student:
    def __init__(self, snum, name, gender, age, native_place, department, classid):
        self.snum = snum
        self.name = name
        self.gender = gender
        self.age = age
        self.native_place = native_place
        self.department = department
        self.classid = classid

    # 查询各个学院的学生姓名
    def search_department(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT name FROM students WHERE department='" + self.department + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 查询男生和女生
    def search_gender(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT name FROM students WHERE gender='" + self.gender + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 查询学生的年龄
    def search_age(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT name FROM students WHERE age='" + self.age + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 按学号查询全部学生的个人信息
    def search_datas(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT * FROM students WHERE snum='" + self.snum + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchone()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 查询students的所有信息
    def search_students(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT * FROM students"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(list(item))
        # 关闭数据库a
        db.close()
        # 返回结果
        return results

    # 添加学生的个人信息
    def add_datas(self):
        # ping()使用该方法 ping(reconnect=True)
        db.ping(reconnect=True)
        # 编写sql语句
        sql_0 = "INSERT INTO students(snum,name,gender,age,native,department,classid) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        sql = sql_0 % (repr(self.snum), repr(self.name), repr(self.gender), repr(self.age), repr(self.native_place),
                       repr(self.department), repr(self.classid))
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库
        db.close()

    # 修改学生信息
    def update_datas(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "UPDATE students SET name='" + self.name + "',gender='" + self.gender + "',age='" + self.age + "', \
                                                                                                            native='" + self.native_place + "',department='" + self.department + "',classid='" + self.classid + "' WHERE snum='" + self.snum + "'"
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()

    # 删除学生的信息
    def delete_data(self):
        # ping()使用该方法 ping(reconnect=True)
        db.ping(reconnect=True)
        sql = "DELETE FROM students WHERE snum='" + self.snum + "' "
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库
        db.close()


class Graduation:
    def __init__(self, snum, graddirect):
        self.snum = snum
        self.graddirect = graddirect

    def search_direct(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT snum  FROM direction WHERE grddirect='" + self.graddirect + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results


class Course:
    def __init__(self, snum, course1, course2, course3, course4):
        self.snum = snum
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4

    def search_course(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT *  FROM course WHERE snum='" + self.snum + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchone()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 修改学生选课
    def update_course(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "UPDATE course  SET course1='" + self.course1 + "',course2='" + self.course2 + "',course3='" + self.course3 + "',course4='" + self.course4 + "'WHERE snum='" + self.snum + "'"
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()


class Grade:
    def __init__(self, snum, course1, course2, course3, course4):
        self.snum = snum
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4

    # 按学号查询学生的成绩
    def search_snum_grade(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT *  FROM grades WHERE snum='" + self.snum + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchone()
        results = []
        for item in results1:
            results.append(item)
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 查询学生的成绩
    def search_grade(self):
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT * FROM grades"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(list(item))
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 修改学生成绩
    def update_grade(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "UPDATE grades SET course1='" + self.course1 + "',course2='" + self.course2 + "',course3='" + self.course3 + "', course4='" + self.course4 + "' WHERE snum='" + self.snum + "'"
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        db.close()

    # 删除学生成绩
    def delete_grade(self):
        # ping()使用该方法 ping(reconnect=True)
        db.ping(reconnect=True)
        sql = "DELETE FROM grades WHERE snum='" + self.snum + "' "
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库
        db.close()

    # 录入成绩
    def add_grade(self):
        # ping()使用该方法 ping(reconnect=True)
        db.ping(reconnect=True)
        # 编写sql语句
        sql_0 = "INSERT INTO grades(snum,course1,course2,course3,course4) VALUES(%s,%s,%s,%s,%s)"
        sql = sql_0 % (repr(self.snum), repr(self.course1),
                       repr(self.course2), repr(self.course3), repr(self.course4))
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库
        db.close()


class Reward(Student):
    def __init__(self, snum, name, gender, age, native_place, department, classid, reward):
        super().__init__(snum, name, gender, age, native_place, department, classid)
        self.reward = reward

    # 查询奖项的学号
    def search_reward(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT snum FROM rewards where reward='" + self.reward + "'"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(list(item))
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 查询得到奖项的学号以及部门
    def search_reward_snum(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT r.snum FROM rewards r,students s where r.reward !='记过处分' AND r.reward!='未获奖' AND r.snum=s.snum   AND s.department='" + self.department + "' "
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(list(item))
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 查询全部的奖项信息以及姓名，二级学院,年龄
    def search_all_reward(self):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        db.ping(reconnect=True)
        # 插入sql语句
        sql = "SELECT r.snum,s.name,s.department,reward FROM rewards r,students s where r.snum=s.snum"
        # 执行sql语句
        cursor.execute(sql)
        results1 = cursor.fetchall()
        results = []
        for item in results1:
            results.append(list(item))
        # 关闭数据库
        db.close()
        # 返回结果
        return results

    # 删除奖惩情况
    def delete_reward(self):
        # ping()使用该方法 ping(reconnect=True)
        db.ping(reconnect=True)
        sql = "DELETE FROM rewards WHERE snum='" + self.snum + "' "
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库
        db.close()
