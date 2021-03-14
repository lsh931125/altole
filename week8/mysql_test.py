import pymysql

conn = pymysql.connect(
    host = '15.164.102.130', # host name
    user = 'root', # user name
    password = 'Penta12./', # password
    db = 'study', # db name
    charset = 'utf8'
)
curs = conn.cursor()

# sql = "insert into member(u_id,u_pw,u_name) values('test2','1234','sungho2');"
# curs.execute(sql)
# sql = "insert into member(u_id,u_pw,u_name) values('test3','1234','sungho3');"
# curs.execute(sql)
# sql = "insert into member(u_id,u_pw,u_name) values('test4','1234','sungho4');"
# curs.execute(sql)
# conn.commit()

# sql = "SELECT * FROM member;"
# curs.execute(sql)
# result = curs.fetchall()
# print(result[0][1])

# sql = '''update member set u_name = 'lim' where no = 5;'''
# curs.execute(sql)
# conn.commit()

sql = '''delete from member where no = 6;'''
curs.execute(sql)
conn.commit()