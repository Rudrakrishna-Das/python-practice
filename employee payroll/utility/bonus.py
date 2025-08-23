from collections import defaultdict
from storage.storage import Storage

class Bonus:
    def __init__(self):
        self.bonus = defaultdict(int)

    def set_bonus(self,id,year,month,amount):
        self.bonus[(id,year,month)] = amount

        data = Storage.find_employee(id)
        key = str((year,month))
        
        if data is not None:
            if key in data['data']['bonus']:
                data['data']['bonus'][key] += amount
            else:
                data['data']['bonus'][key] = amount

            Storage.save_to_json(data['data'],data['index'])
            return
        

    
    def get_bonus(self,id,year,month):
        return self.bonus[(id,year,month)] or 0