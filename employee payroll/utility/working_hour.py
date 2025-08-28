from collections import defaultdict
from helper.helper import Helper
from storage.storage import Storage
class WorkingHour:
    def __init__(self):
        self.monthly_working_hours =defaultdict(int)

    def add_working_hours(self,year,month,work_hour,emp):
        self.monthly_working_hours[(year,month)] = work_hour

        data = Helper.find_employee(emp.email)
        key = str((year,month))
        
        if data is not None:
            if key in data['data']['monthly_worked']:
                data['data']['monthly_worked'][key] += work_hour
            else:
                data['data']['monthly_worked'][key] = work_hour

            Storage.save_to_json(data['data'],data['index'])
            return
        
    def get_working_hour(self,year,month,emp):
        return self.monthly_working_hours[(year,month)] or 0