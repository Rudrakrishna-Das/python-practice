from storage.storage import Storage
class Helper:
    def find_employee(user_email):
        employees = Storage.read_from_file()

        for i,emp in enumerate(employees):
            if emp['email'] == user_email:
                return {"data":emp,"index":i}

    def convert_to_dict(employee):        
        return employee.__dict__    
    