from collections import defaultdict
from storage.storage import Storage
from helper.helper import Helper

class Bonus:
    def __init__(self):
        self.bonus = defaultdict(int)

    def set_bonus(self,year,month,amount,emp):
        self.bonus[(emp.id,year,month)] = amount

        data = Helper.find_employee(emp.email)
        key = str((year,month))
        
        if data is not None:
            if key in data['data']['bonus']:
                data['data']['bonus'][key] += amount
            else:
                data['data']['bonus'][key] = amount

            Storage.save_to_json(data['data'],data['index'])
            return
        

    
    def get_bonus(self,year,month,emp):
        return self.bonus[(emp.id,year,month)] or 0