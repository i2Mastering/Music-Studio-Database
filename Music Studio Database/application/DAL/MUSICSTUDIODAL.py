import mysql.connector

from mysql.connector import errorcode

import time

 class Employee:
    def __init__(self):
        # self.admin_cnx = admin_cnx
        self.admin_cnx = mysql.connector.connect(user = 'admin_user', password = 'admin1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
        self.modify_cnx = mysql.connector.connect(user = 'modify_user', password = 'modify1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
        self.read_cnx = mysql.connector.connect(user = 'read_only', password = 'read1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
   
    def displayEmployees(self):
        cursor = self.read_cnx.cursor(dictionary=True)
        cursor.callproc('displayEmployees')
        self.read_cnx.commit()
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['EMP_ID'], item['EMP_FIRST_NAME'], item['EMP_LAST_NAME'], item['EMP_EMAIL']))
        cursor.close()       
        return list
    
    def addEmp(self, fname, lname, email):
        cursor = self.modify_cnx.cursor(dictionary = True)
        arguments = (fname, lname, email)       
        cursor.callproc('addEmp',arguments)
        self.modify_cnx.commit()
        cursor.callproc('displayEmployees')
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['EMP_ID'], item['EMP_FIRST_NAME'], item['EMP_LAST_NAME'], item['EMP_EMAIL']))
        cursor.close()       
        return list


        
class Client:
    def __init__(self):
        self.admin_cnx = mysql.connector.connect(user = 'admin_user', password = 'admin1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
        self.modify_cnx = mysql.connector.connect(user = 'modify_user', password = 'modify1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
        self.read_cnx = mysql.connector.connect(user = 'read_only', password = 'read1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
    
    def addClient(self, fname, lname, email, address, phone_number):
        cursor = self.modify_cnx.cursor(dictionary = True)
        arguments = (fname, lname, email, address, phone_number)       
        cursor.callproc('addClient',arguments)
        self.modify_cnx.commit()
        cursor.callproc('displayClients')
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['CLIENT_FIRST_NAME'], item['CLIENT_LAST_NAME'], item['CLIENT_EMAIL'], item['ADDRESS'], item['PHONE_NUMBER']))
        cursor.close()       
        return list
    
    
    def clientSession(self,cemail):
        cursor = self.read_cnx.cursor(dictionary = True)   
        arguments = (cemail,)
        cursor.callproc('client_sessions',arguments)
        self.read_cnx.commit()
        list = []
        for result in cursor.stored_results():
            for item in result.fetchall():
                list.append((item['BOOKING_NUMBER'], item['CLIENT_EMAIL'], item['SERVICE_NAME'], item['EMP_ID'], item['BOOKING_DATE']))
        cursor.close()       
        return list
    
    def displayallClients(self):
        cursor = self.read_cnx.cursor(dictionary = True)   
        cursor.callproc('displayClients')
        self.read_cnx.commit()
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['CLIENT_FIRST_NAME'], item['CLIENT_LAST_NAME'], item['CLIENT_EMAIL'], item['ADDRESS'], item['PHONE_NUMBER']))
        cursor.close()       
        return list

class Booking:
    def __init__(self):
        self.admin_cnx = mysql.connector.connect(user = 'admin_user', password = 'admin1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
        self.modify_cnx = mysql.connector.connect(user = 'modify_user', password = 'modify1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')
        self.read_cnx = mysql.connector.connect(user = 'read_only', password = 'read1234',
                                    host = '127.0.0.1',
                                    database = 'MUSIC_STUDIO')

    #THIS FUNCTION IS ONLY FOR EXISTING CLIENTS

    def bookSession(self, cemail, service, emp_id, date):
        cursor = self.modify_cnx.cursor(dictionary = True)
        arguments = (cemail, service, emp_id, date) 
        cursor.callproc('book_session',arguments)
        self.modify_cnx.commit()
        cursor.callproc('all_session')
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
                   list.append((item['BOOKING_NUMBER'], item['CLIENT_EMAIL'], item['SERVICE_NAME'], item['EMP_ID'], item['BOOKING_DATE']))
        cursor.close()  
        return list
    
    def allSessions(self):
        cursor = self.read_cnx.cursor(dictionary = True)
        cursor.callproc('all_session')
        self.read_cnx.commit()
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
                   list.append((item['BOOKING_NUMBER'], item['CLIENT_EMAIL'], item['SERVICE_NAME'], item['EMP_ID'], item['BOOKING_DATE']))
        cursor.close()  
        return list
     
             
    def addService(self,sname, sdescription, price):
        cursor = self.modify_cnx.cursor(dictionary = True)
        arguments = (sname, sdescription, price)       
        cursor.callproc('addService',arguments)
        self.modify_cnx.commit()
        cursor.callproc('viewService')
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['SERVICE_NAME'], item['SERVICE_DESCRIPTION'], item['ADDRESS'], item['PHONE_NUMBER']))
        cursor.close()       
        return list
        
    def viewServices(self):
        cursor = self.read_cnx.cursor(dictionary = True)   
        cursor.callproc('viewServices')
        self.read_cnx.commit()
        list = []
        for result in cursor.stored_results():
           for item in result.fetchall():
               list.append((item['SERVICE_NAME'], item['SERVICE_DESCRIPTION'], item['ADDRESS'], item['PHONE_NUMBER']))
        cursor.close()       
        return list
        

