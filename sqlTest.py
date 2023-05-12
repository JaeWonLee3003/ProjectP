import pymysql

db = pymysql.connect(host='localhost',port=3306,
                     user='root',password='manager')

cursor = db.cursor()

# cursor.execute("select * from Croller.danawacrawler")
# result = cursor.fetchall()
# result = cursor.fetchone()
# print(result)

# Insert 문법
# sql = "insert into Croller.danawacrawler (name,price,`option`) values (%s,%s,%s);"
# cursor.execute(sql,("테스트키보드",50000,"적축"))
# db.commit()

# Update 문법
# updateSQL = "UPDATE Croller.danawacrawler SET name='테스트3', price='50000', `option`='옵션3' WHERE idx=1;"
# cursor.execute(updateSQL)
# db.commit()

# Delete 문법
# deleteSQL = 'DELETE FROM Croller.danawacrawler WHERE idx=2;'
# cursor.execute(deleteSQL)
# db.commit()
