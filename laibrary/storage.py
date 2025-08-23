import json
class Storage:
    """
    This is a storage specific class
    Methods
    1. Write to a json file.
    2. Read from a json file.
    """
    def write_to_file(data):
        try:
            with open('data.json','w') as f:
                json.dump(data,f,indent=4)
            return {'success':True,'message':'File Written successfully'}
        except Exception as e:
            return {'sucess':False,'message':str(e)}
        
    def read_from_file():
        try:
            with open('data.json','r') as f:
                data = json.load(f)
                return {'success':True,'result':data}
        except Exception as e:
            return{'success':False,'message':str(e)}

