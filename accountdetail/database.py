import pymysql as pm
import pandas.io.sql as sql
import openpyexcel
from django.http import HttpResponse
class Connection:
    def __init__(self):
        self.con = pm.connect(host='localhost', user='root',password='123456', database='djangocrud')
        self.cursor = self.con.cursor()

    def storeUser(self,code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount):
        sql="insert into accountdetail(code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount) values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount)
        self.cursor.execute(sql)
        try:
            self.con.commit()
            self.status=True
        except:
            self.con.rollback()
            self.status=False
        y="select * from accountdetail"
        self.cursor.execute(y)
        m=self.cursor.fetchall()
        self.status=True
        return self.status,m

    def checkUser(self):
        sql="select * from accountdetail" 
        self.cursor.execute(sql)
        p=self.cursor.fetchall()
        if self.cursor.rowcount > 0:
            self.status=True
        else:
            self.status=False
        return self.status,p

    def deleteUser(self,code):
        sql = "select * from accountdetail where code = '%d' " % (code)
        self.cursor.execute(sql)  
        m=0  
        if self.cursor.rowcount > 0:
            sql = "delete from accountdetail where code = '%d' " % (code)
            self.cursor.execute(sql)
            try:
                self.con.commit()
                y="select * from accountdetail"
                self.cursor.execute(y)
                m=self.cursor.fetchall()
                self.status=True
            except:
                self.con.rollback()
                self.status=False
        else:
             self.status=False   
        return self.status,m
    
    def updateUser(self,code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount):
        sql = "select * from accountdetail where code = '%d' " % (code)
        self.cursor.execute(sql) 
        m=0   
        if self.cursor.rowcount > 0:
            sqlb = "delete from accountdetail where code = '%d' " % (code)
            self.cursor.execute(sqlb)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            sqla="insert into accountdetail(code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount) values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount)
            self.cursor.execute(sqla)
            try:
                self.con.commit()
            except:
                self.con.rollback()
            y="select * from accountdetail"
            self.cursor.execute(y)
            self.status=True
            m=self.cursor.fetchall()
            return self.status,m
        else:
            return HttpResponse("User Not Found")

    def printData(self):
        # read the data
        df=sql.read_sql('select * from accountdetail',self.con)
        df.to_excel('accdetail.xlsx')