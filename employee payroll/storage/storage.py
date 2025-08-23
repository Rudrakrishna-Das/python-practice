import json
class Storage:
    def save_to_json(employee_details,index =None):
        
        all_data = Storage.read_from_file()
        if index is not None:
            all_data[index] = employee_details
        else:
            find_employe = Storage.find_employee(name=employee_details['name'])
            if find_employe is None:            
                all_data.append(employee_details)

        with open("employee.json", "w") as es:
            try:
                json.dump(all_data,es,indent=4)
            except Exception as e:
                print(str(e))

    def read_from_file():
        try:
            with open("employee.json",'r') as es:
                data = json.load(es)
                return [emp for emp in data]
        except Exception as e:
            print(str(e))
            return []

    def convert_to_dict(employee):
        employee_details ={
            "id":employee.id,
            "name":employee.name,
            "role":employee.role,
            "annual_salary":employee.annual_salary,
            "type":employee.__class__.__name__,
            "bonus":{},
            "tax":{},
            "gross_salary":{},
            "taken_leave":{},
            "net_monthly_salary":{}
        }
        return employee_details
    @staticmethod    
    def find_employee(id=None,name=None):
        data = Storage.read_from_file()
        if data:
            for index,emp in enumerate(data):
                if id is not None:
                   if emp['id'] == id:
                        return {'index':index,'data':emp}
                else:
                   if emp['name'] == name:
                        return {'index':index,'data':emp}
                


