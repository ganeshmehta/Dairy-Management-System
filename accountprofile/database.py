from django.http import HttpResponse
import pymysql as pm
import pandas.io.sql as sql
import openpyexcel

class Connection:
    def __init__(self):
        self.con = pm.connect(host='localhost', user='root',password='123456', database='djangocrud')
        self.cursor = self.con.cursor()

    def storeUser(self,code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone):
        sql="insert into account(code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone) values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone)
        self.cursor.execute(sql)
        y="select * from account"
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
        sql="select * from account" 
        self.cursor.execute(sql)
        p=self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status,p

    def deleteUser(self,code):
        sql = "select * from account where code = '%d' " % (code)
        self.cursor.execute(sql)  
        m=0  
        if self.cursor.rowcount > 0:
            sql = "delete from account where code = '%d' " % (code)
            self.cursor.execute(sql)
            try:
                self.con.commit()
                y="select * from account"
                self.cursor.execute(y)
                m=self.cursor.fetchall()
                self.status=True
            except:
                self.con.rollback()
                self.status=False
        else:
             self.status=False   
        return self.status,m
    
    def updateUser(self,code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone):
        sql = "select * from account where code = '%d' " % (code)
        self.cursor.execute(sql) 
        m=0   
        if self.cursor.rowcount > 0:
            sqlb = "delete from account where code = '%d' " % (code)
            self.cursor.execute(sqlb)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            sqla="insert into account(code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone) values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone)
            self.cursor.execute(sqla)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            y="select * from account"
            self.cursor.execute(y)
            self.status=True
            m=self.cursor.fetchall()
            return self.status,m
        else:
            return HttpResponse("User Not Found")


    def printData(self):
        # read the data
        df=sql.read_sql('select * from account',self.con)
        df.to_excel('ds.xlsx')