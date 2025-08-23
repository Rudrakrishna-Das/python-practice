from models.employe import Employe
from storage.storage import Storage

class FullTimeEmployee(Employe):
    def __init__(self, name, role,annual_salary):
        find_employee = Storage.find_employee(name=name)
        if find_employee is not None:
            super().__init__(find_employee['data']['name'],find_employee['data']['role'],find_employee['data']['id'])
            self.annual_salary = find_employee['data']['annual_salary']
        else:
            super().__init__(name,role)
            self.annual_salary = annual_salary
            self.save()

    def calculate_monthly_salay(self,month,year,utilities):
        monthly_salary = self.annual_salary / 12
        unpaid_leaves = utilities['leave'].get_unpaid_leaves(self.id,year,month)
        working_days = utilities['leave'].total_working_days(year,month)
        per_day = monthly_salary/working_days

        gross_salary = round(per_day * (working_days - unpaid_leaves), 2)
        bonus = round(utilities['bonus'].get_bonus(self.id,year,month), 2)
        tax = round(utilities['tax'].calculate_tax(gross_salary+bonus,self), 2)        
        data = Storage.find_employee(self.id)
        if data is not None:
            data['data']['gross_salary'][str((year,month))] =gross_salary
            data['data']['tax'][str((year,month))] = tax
            data['data']['net_monthly_salary'][str((year,month))] = gross_salary - tax
            Storage.save_to_json(data['data'],data['index'])
            return gross_salary - tax
    def save(self):
        data = Storage.convert_to_dict(self)
        Storage.save_to_json(data)