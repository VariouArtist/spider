import pymysql

while True:
    db = pymysql.connect("localhost","root","root","novel")
    cursor = db.cursor()
    print("--------------------查询名字 输入:name--------------------")
    print("--------------------查询作者 输入:author------------------")
    print("--------------------查询类型 输入:classify----------------")
    print("--------------------退出系统 输入:exit--------------------")
    
    chose = input("请输入你的操作:")
    if chose == 'name':
        name = input("请输入查询的书名:")
        sql = "SELECT novelName FROM novelInfo  \
                WHERE novelName = '%s' " % (name)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print("名字:",result)
                break
        except:
            print("查询无果!")
            break
    elif chose == 'author':
        author = input("请输入查询的作者:")
        sql = "SELECT novelName FROM novelInfo  \
              WHERE novelAuthor = '%s' " % (author)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print("书名:",result)   
        except:
            print("查询无果!")
            break
    elif chose == 'classify':
        classify = input("请输入查询的类型:")
        sql = "SELECT novelName FROM novelInfo  \
                WHERE novelClassify = '%s' " % (classify)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print("书名:",result)   
        except:
            print("查询无果!")
            break
    elif chose == 'exit':
        db.close()
        break
    else:
        print("输入有误，请重新输入！")
    