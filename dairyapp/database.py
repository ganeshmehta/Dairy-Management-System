# database connectivity file
import pymysql as pm
import pandas.io.sql as sql
import openpyexcel

class Connection:
    def __init__(self):
        self.con = pm.connect(host='localhost', user='root',password='123456', database='djangocrud')
        self.cursor = self.con.cursor()

    def storeUser(self,email,inv,vehicle,invno,deliveryemail,invby,refno,vatac):
        sql="insert into sample(email,inv,vehicle,invno,deliveryemail,invby,refno,vatac) values ('%s','%s','%s','%d','%s','%s','%s','%s')" % (email,inv,vehicle,invno,deliveryemail,invby,refno,vatac)
        self.cursor.execute(sql)
        y="select * from sample"
        self.cursor.execute(y)
        m=self.cursor.fetchall()
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        return self.status,m

    def checkUser(self):
        sql="select * from sample" 
        self.cursor.execute(sql)
        p=self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status,p

    def deleteUser(self,email):
        sql = "select * from sample where email = '%s' " % (email)
        self.cursor.execute(sql)  
        m=0  
        if self.cursor.rowcount > 0:
            sql = "delete from sample where email = '%s' " % (email)
            self.cursor.execute(sql)
            try:
                self.con.commit()
                y="select * from sample"
                self.cursor.execute(y)
                m=self.cursor.fetchall()
                self.status=True
            except:
                self.con.rollback()
                self.status=False
        else:
             self.status=False   
        return self.status,m
    
    def updateUser(self,email,inv,vehicle,invno,deliveryemail,invby,refno,vatac):
        sql = "select * from sample where email = '%s' " % (email)
        self.cursor.execute(sql)    
        if self.cursor.rowcount > 0:
            sql = "delete from sample where email = '%s' " % (email)
            self.cursor.execute(sql)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            sql="insert into sample values ('%s','%s','%s','%d','%s','%s','%s','%s')" % (email,inv,vehicle,invno,deliveryemail,invby,refno,vatac)
            self.cursor.execute(sql)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            y="select * from sample"
            self.cursor.execute(y)
            m=self.cursor.fetchall()
        return m

    def printData(self):
        # read the data
        df=sql.read_sql('select * from sample',self.con)
        df.to_excel('dairyapp.xlsx')
    
    def displayData(self,m):
        n=len(m)
        stringcolumn=''
        for i in m:
            stringcolumn+=i+' '
        s = stringcolumn.split()
        print(m)
        l = []
        m = set(m)
        a = ''
        # for i in range(len(m)):
        #     a += '%s'
        # sql = "select {} from sample".format(m)
        # self.cursor.execute(sql)
        # mt=self.cursor.fetchall()
        # print(mt)
        for i in m:
            sql = "select '%s' from sample"%(i)
            self.cursor.execute(sql)
            mt=self.cursor.fetchall()
            l.append(mt)
        print(l)
# database connectivity file