
from DAL.MUSICSTUDIODAL import Employee, Client, Booking

class EmployeeDAL:
    def __init__(self):
        self.EmployeeDAL = Employee()

    def add(self,first_name,last_name,email):
        query = self.EmployeeDAL.addEmp(first_name,last_name,email)

        return query
    
    def displayEmp(self):
        query = self.EmployeeDAL.displayEmployees()
        return query
    
#     def displayStudentGPA(self):
#         query3 = self.studentDAL.displayStudentgpa()
#         return query3

class ClientDAL:
    def __init__(self):
        self.clientDAL = Client()

        
    def addClient(self, fname, lname, email, address, phone_number):
        query = self.clientDAL.addClient(fname, lname, email, address, phone_number)
        return query

    def displayClients(self):
        query = self.clientDAL.displayallClients()
        return query
    
    def clientSessions(self,cemail):
        query = self.clientDAL.clientSession(cemail)
        return query


class BookingDAL:
    def __init__(self):
        self.bookingDAL = Booking()
  
    def bookSession(self, cemail, service, emp_id, date):
        query = self.bookingDAL.bookSession(cemail, service, emp_id, date)
        return query
    
    def addServices(self,sname, sdescription, price):
        query = self.bookingDAL.addService(sname, sdescription, price)
        return query

    def viewServices(self):
        query = self.bookingDAL.viewServices()
        return query

    def allSessions(self):
        query = self.bookingDAL.allSessions()
        return query
