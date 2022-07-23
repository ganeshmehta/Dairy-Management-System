import pymysql as pm
import pandas.io.sql as sql
import openpyexcel

class Connection:
    def __init__(self):
        self.con = pm.connect(host='localhost', user='root',password='123456', database='djangocrud')
        self.cursor = self.con.cursor()

    def storeUser(self,code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp):
        sql="insert into ledgeracc(code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp) values ('%d','%s','%s','%s','%s','%s','%s','%s','%s')" % (code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp)
        self.cursor.execute(sql)
        y="select * from ledgeracc"
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
        sql="select * from ledgeracc" 
        self.cursor.execute(sql)
        p=self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status,p

    def deleteUser(self,code):
        sql = "select * from ledgeracc where code = '%d' " % (code)
        self.cursor.execute(sql)  
        m=0  
        if self.cursor.rowcount > 0:
            sql = "delete from ledgeracc where code = '%d' " % (code)
            self.cursor.execute(sql)
            try:
                self.con.commit()
                y="select * from ledgeracc"
                self.cursor.execute(y)
                m=self.cursor.fetchall()
                self.status=True
            except:
                self.con.rollback()
                self.status=False
        else:
             self.status=False   
        return self.status,m
    
    def updateUser(self,code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp):
        sql = "select * from ledgeracc where code = '%d' " % (code)
        self.cursor.execute(sql)    
        if self.cursor.rowcount > 0:
            sql = "delete from ledgeracc where code = '%d' " % (code)
            self.cursor.execute(sql)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            sql="insert into ledgeracc values ('%d','%s','%s','%s','%s','%s','%s','%s','%s')" % (code,accounttype,ledgertype,subtedger,party,dept,subdept,grp,subgrp)
            self.cursor.execute(sql)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            y="select * from ledgeracc"
            self.cursor.execute(y)
            m=self.cursor.fetchall()
        return m

    def printData(self):
        df=sql.read_sql('select * from ledgeracc',self.con)
        df.to_excel('dairyapp.xlsx')
    
    def displayData(self,m):
        n=len(m)
        m = set(m)
        a = ''
        sql = "select {} from ledgeracc".format(m)
        self.cursor.execute(sql)
        mt=self.cursor.fetchall()
        print(mt)