import toga
from toga.style.pack import COLUMN, Pack
import toga.widgets

from BLL.MUSICSTUDIOBLL import EmployeeDAL, ClientDAL, BookingDAL

emp_bll = EmployeeDAL()  
client_bll = ClientDAL() 
booking_bll = BookingDAL()

class addEMP(toga.App):

    def startup(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.data = emp_bll.displayEmp()

        self.left_container = toga.Table(headings=["Employee ID", "First Name","Last Name", "Email"], data=self.data)
        
        right_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
        input_box_fn = toga.Box(style=Pack(padding=10))
        input_box_ln = toga.Box(style=Pack(padding=10))
        input_box_email = toga.Box(style=Pack(padding=10))
    
        self.first_name = toga.TextInput(placeholder="First Name")
        self.last_name = toga.TextInput(placeholder="Last Name")
        self.email = toga.TextInput(placeholder="Email Address")
    
        input_box_fn.add(self.first_name)
        input_box_ln.add(self.last_name)
        input_box_email.add(self.email)

        right_content.add(
                input_box_fn,
                input_box_ln,
                input_box_email,

        )
        right_content.add(
                toga.Button("Add User",
                    on_press=self.button_handler,
                    style=Pack(width=200, padding=20),
                )
            )

        right_container = toga.ScrollContainer(horizontal=False)

        right_container.content = right_content

        split = toga.SplitContainer()

        split.content = [(self.left_container, 1), (right_container, 2)]

        self.main_window = toga.MainWindow()

        self.main_window.content = split

        self.main_window.show()

    def button_handler(self,widget):
        self.data = emp_bll.add(self.first_name.value, self.last_name.value, self.email.value)
        self.left_container.data = self.data
        self.first_name.value = ""
        self.last_name.value = ""
        self.email.value = ""


class vSessions(toga.App):
    
    def startup(self):

        self.data = booking_bll.all_sessions()

        self.left_container = toga.Table(headings=["Booking number", "Client Email", "Service", "Employee ID", "Date"], data=self.data)
        
    
        self.main_window = toga.MainWindow()

        self.main_window.content = self.left_container


        self.main_window.show()

class addClient(toga.App):
    
    def startup(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.address = ""
        self.phone_number = ""
        self.data = client_bll.displayClients()

        self.left_container = toga.Table(headings=["First Name","Last Name", "Email", "Address", "Phone Number"], data=self.data)
        
        right_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
        input_box_fn = toga.Box(style=Pack(padding=10))
        input_box_ln = toga.Box(style=Pack(padding=10))
        input_box_email = toga.Box(style=Pack(padding=10))
        input_box_address = toga.Box(style=Pack(padding=10))
        input_box_phone_number = toga.Box(style=Pack(padding=10))
    
        self.first_name = toga.TextInput(placeholder="First Name")
        self.last_name = toga.TextInput(placeholder="Last Name")
        self.email = toga.TextInput(placeholder="Email Address")
        self.address= toga.TextInput(placeholder="Address")
        self.phone_number= toga.TextInput(placeholder="Phone Number")
    
        input_box_fn.add(self.first_name)
        input_box_ln.add(self.last_name)
        input_box_email.add(self.email)
        input_box_address.add(self.address)
        input_box_phone_number.add(self.phone_number)

        right_content.add(
                input_box_fn,
                input_box_ln,
                input_box_email,
                input_box_address,
                input_box_phone_number,
        )
        right_content.add(
                toga.Button("Add client",
                    on_press=self.button_handler,
                    style=Pack(width=200, padding=20),
                )
            )

        right_container = toga.ScrollContainer(horizontal=False)

        right_container.content = right_content

        split = toga.SplitContainer()

        split.content = [(self.left_container, 1), (right_container, 2)]

        self.main_window = toga.MainWindow()

        self.main_window.content = split

        self.main_window.show()

    def button_handler(self,widget):
        self.data = client_bll.addClient(self.first_name.value, self.last_name.value, self.email.value, self.address.value, self.phone_number.value )
        self.left_container.data = self.data
        self.first_name.value = ""
        self.last_name.value = ""
        self.email.value = ""
        self.address = ""
        self.phone_number = ""


class book_session(toga.App):
    def startup(self):
        self.cemail = ""
        self.service = ""
        self.emp_id = ""
        self.date = ""
        self.data = booking_bll.allSessions()

        self.left_container = toga.Table(headings=["Booking Number", "Client Email", "Service","Employee ID", "Date"], data=self.data)
        
        right_content = toga.Box(style=Pack(direction=COLUMN, padding_top=50))
        input_box_email = toga.Box(style=Pack(padding=10))
        input_box_service = toga.Box(style=Pack(padding=10))
        input_box_emp_id = toga.Box(style=Pack(padding=10))
        input_box_date = toga.Box(style=Pack(padding=10))
    
        self.email = toga.TextInput(placeholder="Client Email")
        self.service = toga.TextInput(placeholder="Service")
        self.emp_id = toga.TextInput(placeholder="Employee ID")
        self.date= toga.TextInput(placeholder="date")
    
        input_box_service.add(self.service)
        input_box_emp_id.add(self.emp_id)
        input_box_email.add(self.email)
        input_box_date.add(self.date)

        right_content.add(
                input_box_service,
                input_box_emp_id,
                input_box_email,
                input_box_date,
        )
        right_content.add(
                toga.Button("Book Session",
                    on_press=self.button_handler,
                    style=Pack(width=200, padding=20),
                )
            )

        right_container = toga.ScrollContainer(horizontal=False)

        right_container.content = right_content

        split = toga.SplitContainer()

        split.content = [(self.left_container, 1), (right_container, 2)]

        self.main_window = toga.MainWindow()

        self.main_window.content = split

        self.main_window.show()

    def button_handler(self,widget):
        self.data = booking_bll.bookSession(self.email.value, self.service.value, self.emp_id.value, self.date.value)
        self.left_container.data = self.data
        self.service.value = ""
        self.emp_id.value = ""
        self.email.value = ""
        self.date.value = ""
    
    