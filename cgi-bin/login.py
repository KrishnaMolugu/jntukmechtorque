import cgi,sqlite3
print("content-type:text/html \n")
conn=sqlite3.connect("artisolfest.db")
cur=conn.cursor()
sql="select  *  from register"
c=cur.execute(sql)
rs=c.fetchall()
print(rs)
