from models.full_time_employe import FullTimeEmployee as FTE
from models.contractor import Contractor as C
from models.intern import Intern as I
from utility import bonus,leave,tax,working_hour
from helper.helper import Helper

b = bonus.Bonus()
l = leave.Leave()
t = tax.Tax()
wh = working_hour.WorkingHour()


utilities={
    "leave":l,
    "tax":t,
    'bonus':b,
    "work_hour": wh
}

greet = """
WELCOM To our Employee Payroll System(EPS) 
Choose Your Employee type
1. Full Time Employee(FTE)
2. Contractor
3. Intern
"""

option_for_user = """
Chosse your options number to use.
1. Add Bonus,
2. Take leaves,
3. Calculate Monthly Salary
4. Choose Employee Type again
"""

option_for_contractor = """
Chosse your options number to use.
1. Add Working Hour
2. Calculate Monthly Salary
3. Choose Employee Type again
"""
option_for_intern = """
Chosse your options number to use.
1. Update Stipend
2. Calculate Monthly Salary
3. Choose Employee Type again
"""


running = True

while running:
    select_user_type = input(greet)
    match select_user_type:
        case "1":                        
            user_email = input("Please enter user email to search for Employee:- ")

            found_employee = Helper.find_employee(user_email)
            if found_employee is not None and found_employee["data"]["type"] != "FullTimeEmployee":
                print(f"You alredy have this user with the type {found_employee["data"]['type']}. Edit that")
                continue
            if found_employee is None:
                user_role = input("Please enter user role:- ")
                user_name = input("Please enter user name:- ")
                user_annual_salary = input("Please enter user annual salary:- ")
                emp = FTE(user_name,user_role,user_email,user_annual_salary)
            else:
                emp = FTE.convert_from_dict(found_employee['data'])
                

            selcting_options = True        
            while selcting_options:
                user_selection = input(option_for_user)
                match user_selection:
                    case "1":
                        year=input("Enter Year")
                        month=input("Enter Month")
                        amount=input("Enter Amount")
                        utilities['bonus'].set_bonus(year,month,int(amount),emp)
                    case "2":
                        year=input("Enter Year")
                        month=input("Enter Month")
                        days=input("Enter Days")
                        utilities['leave'].add_leave(year,month,int(days),emp)
                    case "3":
                        year=input("Enter Year")
                        month=input("Enter Month")
                        emp.calculate_monthly_salay(month,year,utilities)

                    case "4":
                        selcting_options = False
                    case _:
                        selcting_options = False
                        print('Wrong Selection')
        case "2":                        
            user_email = input("Please enter user email to search for Employee:- ")

            found_employee = Helper.find_employee(user_email)
            if found_employee is not None and found_employee["data"]["type"] != "Contractor":
                print(f"You alredy have this user with the type {found_employee["data"]['type']}. Edit that")
                continue
            if found_employee is None:
                user_role = input("Please enter user role:- ")
                user_name = input("Please enter user name:- ")
                emp = C(user_name,user_role,user_email)
            else:
                emp = C.convert_from_dict(found_employee['data'])
                

            selcting_options = True        
            while selcting_options:
                user_selection = input(option_for_contractor)
                match user_selection:
                    case "1":
                        year=input("Enter Year ")
                        month=input("Enter Month ")
                        hours=input("Enter Hour Worked ")
                        utilities['work_hour'].add_working_hours(year,month,int(hours),emp)
                    case "2":
                        year=input("Enter Year")
                        month=input("Enter Month")
                        emp.calculate_monthly_salay(month,year,utilities)

                    case "3":
                        selcting_options = False
                    case _:
                        selcting_options = False
                        print('Wrong Selection')
        case "3":                        
            user_email = input("Please enter user email to search for Employee:- ")

            found_employee = Helper.find_employee(user_email)
            if found_employee is not None and found_employee["data"]["type"] != "Intern":
                print(f"You alredy have this user with the type {found_employee["data"]['type']}. Edit that")
                continue
            if found_employee is None:
                user_role = input("Please enter user role:- ")
                user_name = input("Please enter user name:- ")
                emp = I(user_name,user_role,user_email)
            else:
                emp = I.convert_from_dict(found_employee['data'])
                

            selcting_options = True        
            while selcting_options:
                user_selection = input(option_for_intern)
                match user_selection:
                    case "1":
                        amount=input("Enter new Stipend ")
                        emp.update_stipend(amount)
                    case "2":
                        year=input("Enter Year")
                        month=input("Enter Month")
                        emp.calculate_monthly_salay(month,year,utilities)

                    case "3":
                        selcting_options = False
                    case _:
                        selcting_options = False
                        print('Wrong Selection')
            


