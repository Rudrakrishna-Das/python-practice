import json
class Storage:
    def save_to_json(employee_details,index =None):
        
        all_data = Storage.read_from_file()
        if index is not None:
            all_data[index] = employee_details
        else:
            all_data.append(employee_details)

        with open("storage/employee.json", "w") as es:
            try:
                json.dump(all_data,es,indent=4)
            except Exception as e:
                print(str(e))
                return

    def read_from_file():
        try:
            with open("storage/employee.json",'r') as es:
                data = json.load(es)
                return [emp for emp in data]
        except Exception as e:
            print(str(e))
            return []

    
   
                


