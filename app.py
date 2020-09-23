

class Hospital():
    auth_level= {
        4: [1,2,3,4,5,6,7,8,9,10,0],
        3: [1,2,3,4,5,6,7,0],
        2: [1,2,3,5,6,0],
        1: [0],
        0: [0]
    }
    options = {
        11: 'View your records',
        1: 'View Patient Records',
        2: 'View All Patients',
        3: 'Add New Patient',
        4: 'Delete Patient',
        5: 'View All Patients Records',
        6: 'Add Patient Records',
        7: 'Delete Record',
        8: 'View All Employees',
        9: 'Add Employee',
        10: 'Delete Employee',
        0: 'Logout'
    }
    def __init__(self,hospital_name):
        self.name=hospital_name
        self.patients={'madarchod':Patient('madarchod','madarchod')}
        self.access=0
        self.current_user=None
        self.employees={hospital_name:Employee(hospital_name,'adminpass','superadmin')}
        self.loggedin = False
    def add_employee(self,name,password,role):
        self.employees[name]=Employee(name,password,role)
    def add_patient(self,name,password,records={}):
        self.patients[name]=Patient(name,password,records)
    def del_employee(self,name):
        del self.employees[name]
    def del_patient(self,name):
        del self.patients[name]
    def list_patients(self):
        for patient in self.patients.values():
            print(patient.name)
    def list_employees(self):
        for employee in self.employees.values():
            print(employee.name)
    def view_records(self,name):
        print('Name: ', name)
        for record_id,record in self.patients[name].records.items(): 
            print(record_id, record)
    def add_records(self,name,employee_name,key,value):
        self.patients[name].records[key]=f"{employee_name}\n{value}"
    def remove_record(self,name,key):
        del self.patients[name].records[key]
    def print_menu(self, user):
        menu_options = self.auth_level[self.access]
        for key in menu_options:
            print(f" > {key}. {self.options[key]}")
    def login(self):
        name = input('Please key in username: ')
        password = input('Please key in password: ')
        if self.patients.get(name):
            if self.patients[name].password==password:
                self.current_user= self.patients[name]
                self.access = self.current_user.access_level
                self.loggedin = True
                print('Login Successful')
            else:
                print('User exists but password is incorrect')
        elif self.employees.get(name):
            if self.employees[name].password==password:
                self.current_user=self.employees[name]
                self.access = self.current_user.access_level
                self.loggedin = True
                print('Login Successful')
            else:
                print('User exists but password is incorrect')
        else:
            print('User not found')
    def logout(self):
        self.loggedin = False
        print('Logged out')


    

class Patient():
    def __init__(self,name,password,records={}):
        self.name=name
        self.password=password
        self.records=records
        self.access_level=0
    def view_records(self):
        print('Name: ', self.name)
        for record_id,record in self.records.items(): 
            print(record_id, record)

class Employee():
    def __init__(self,name,password,role):
        self.name=name
        self.password=password
        self.role=role
        self.access_level=self.provide_access()
    def provide_access(self):
        if self.role=='superadmin':
            return 4
        elif self.role == 'doctor':
            return 3
        elif self.role == 'receptionist':
            return 2
        elif self.role == 'janitor':
            return 1



metro = Hospital('metro')
# print(metro.employees)
while metro.loggedin == False:
    metro.login()

while metro.loggedin == True:
    metro.print_menu(metro.current_user)
    response = input('What would you like to do ?\n')
    if response == '11':
        metro.current_user.view_records()
    elif response == '1':
        metro.view_records(input('Patients name ?\n'))
    elif response == '2':
        metro.list_patients()
    elif response == '3':
        patient_name = input('Patient name ?\n')
        patient_password = input('Patient password ?\n')
        metro.add_patient(patient_name,patient_password)
    elif response == '4':
        metro.del_patient(input('Patient name ?\n'))
    elif response == '5':
        print('This function is invalid for the time being')
    elif response == '6':
        patient_name = input('Patient name ?\n')
        patient_record = input('Patients record ?\n')
        record_date = input('Record Date ?\n')
        metro.add_records(patient_name,metro.current_user.name,record_date,patient_record)
    elif response == "7":
        patient_name = input('Patient name ?\n')
        record_date = input('Record Date ?\n')
        metro.remove_record(patient_name,record_date)
    elif response == '8':
        metro.list_employees()
    elif response == '9':
        employee_name = input('Employee name ?\n')
        employee_password = input('Employee password ?\n')
        employee_role = input('Employee role ?\n')
        metro.add_employee(employee_name,employee_password,employee_role)
    elif response == '10':
        metro.del_employee(input('Employee name ?\n'))
    elif response == '0':
        metro.logout()