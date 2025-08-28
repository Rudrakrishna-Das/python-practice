from models.employe import Employe
from storage.storage import Storage
from helper.helper import Helper

class FullTimeEmployee(Employe):
    def __init__(self, name, role,email,annual_salary,id = None,bonus = None,net_salary = None,leave= None,type=None,save=True):        
        super().__init__(name,role,email,id)
        self.annual_salary = annual_salary
        self.type = type or self.__class__.__name__
        self.bonus = bonus or {}
        self.net_salary = net_salary or {}
        self.leave = leave or {}
        if save:
            converted_to_dict = Helper.convert_to_dict(self)
            Storage.save_to_json(converted_to_dict)

    @classmethod
    def convert_from_dict(cls,data):
       
        return cls(
            name=data["name"],
            role=data["role"],
            email=data["email"],
            annual_salary=data["annual_salary"],
            id=data.get("id"),
            type=data.get("type"),
            bonus=data.get("bonus",{}),
            leave=data.get("leave",{}),
            net_salary=data.get("net_salary",{}),
            save = False
        )

   

    def calculate_monthly_salay(self,month,year,utilities):
        monthly_salary = int(self.annual_salary) / 12
        unpaid_leaves = utilities['leave'].get_unpaid_leaves(year,month,self)
        working_days = utilities['leave'].total_working_days(int(year),int(month))

        if unpaid_leaves is None or unpaid_leaves == 0:
            key = str((year,month))
            unpaid_leaves = self.leave.get(key,0)
        per_day = monthly_salary/working_days
    
        gross_salary = int(per_day * (working_days - unpaid_leaves))
        bonus = int(utilities['bonus'].get_bonus(year,month,self))
        if bonus is None or bonus == 0:
            key = str((year,month))
            bonus = self.bonus.get(key,0)
        tax = int(utilities['tax'].calculate_tax(gross_salary+bonus,self))        
        data = Helper.find_employee(self.email)
        if data is not None:
            data['data']['net_salary'][str((year,month))] = gross_salary - tax
            Storage.save_to_json(data['data'],data['index'])
            return gross_salary - tax


    
        