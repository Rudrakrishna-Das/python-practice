from models.employe import Employe
from storage.storage import Storage
from helper.helper import Helper

class Contractor(Employe):
    def __init__(self, name, role,email,id = None,type=None,pay_per_hour=None,net_salary = None, monthly_worked=None,save=True):        
        super().__init__(name,role,email,id)
        self.type = type or self.__class__.__name__
        self.net_salary = net_salary or {}
        self.pay_per_hour = pay_per_hour or 60
        self.monthly_worked = monthly_worked or {}
        if save:
            converted_to_dict = Helper.convert_to_dict(self)
            Storage.save_to_json(converted_to_dict)

    @classmethod
    def convert_from_dict(cls,data):
        
        return cls(
            name=data["name"],
            role=data["role"],
            email=data["email"],
            id=data.get("id"),
            type=data.get("type"),
            pay_per_hour=data.get("pay_per_hour",0),
            net_salary=data.get("net_salary",{}),
            monthly_worked=data.get("monthly_worked",{}),
            save = False
        )    

    def calculate_monthly_salay(self,month,year,utilities):
        monthly_worked_time = utilities['work_hour'].get_working_hour(year,month,self)

        if monthly_worked_time is None or monthly_worked_time == 0:
            key = str((year,month))
            monthly_worked_time = self.monthly_worked.get(key,0)
        gross_salary = int(monthly_worked_time) * self.pay_per_hour
        
        tax = int(utilities['tax'].calculate_tax(gross_salary,self))        
        data = Helper.find_employee(self.email)
        
        if data is not None:
            data['data']['net_salary'][str((year,month))] = gross_salary - tax
            
            Storage.save_to_json(data['data'],data['index'])


    
        