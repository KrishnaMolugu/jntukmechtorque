import cgi,sqlite3
print("content-type:text/html \n")
form=cgi.FieldStorage()
u=form.getvalue("name")
a=form.getvalue("number")
b=form.getvalue("email")
c=form.getvalue("college")
d=form.getvalue("branch")
e=form.getvalue("location")
conn=sqlite3.connect("artisolfest.db")
cur=conn.cursor()
sql="insert into register values('"+u+"','"+a+"','"+b+"','"+c+"','"+d+"','"+e+"')"
try:
	cur.execute(sql)
	conn.commit()
	print("successfully inserted")
	print("<meta http-equiv=\"refresh\"content=\"0; url=http://localhost:8000/index.html\"/>")
except Exception as e:
	print(e)
cur.close()
conn.close()
