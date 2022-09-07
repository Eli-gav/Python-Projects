



import sqlite3
conn=sqlite3.connect('test.db')
with conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_list(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    col_flist TEXT)")
    conn.commit()


conn=sqlite3.connect('test.db')


#list
fileList=('information.docx','Hello.txt','myImage.png',\
         'myMovie.mpg','World.txt','data.pdf','myPhoto.png')

#loop
for x in fileList:
    if x.endswith('txt'):
        with conn:
            curr=conn.cursor()
            cur.execute("INSERT INTO tbl_list (col_flist) VALUES(?)",(x,))
            print(x)

conn.close()













