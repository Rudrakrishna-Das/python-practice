from models.employe import Employe
from storage.storage import Storage
from helper.helper import Helper

class Intern(Employe):
    def __init__(self, name, role,email,id = None,type=None,stipend=None,net_salary=None,save=True):        
        super().__init__(name,role,email,id)
        self.type = type or self.__class__.__name__
        self.net_salary = net_salary or {}
        self.stipend = stipend or 6000
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
            stipend=data.get("stipend",0),
            net_salary=data.get("net_salary",{}),
            save = False
        )  
    def update_stipend(self,amount):
        self.stipend = amount
        data = Helper.find_employee(self.email)
        if data is not None:
            data['data']['stipend'] = int(amount)
            Storage.save_to_json(data['data'],data['index'])


    def calculate_monthly_salay(self,month,year,utilities): 
        gross_salary = self.stipend
        tax =int(utilities['tax'].calculate_tax(gross_salary,self))      
        data = Helper.find_employee(self.email)
       
        if data is not None:
            data['data']['net_salary'][str((year,month))] = int(gross_salary) - int(tax)
            Storage.save_to_json(data['data'],data['index'])


    
        