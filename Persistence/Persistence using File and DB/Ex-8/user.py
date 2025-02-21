import json

class User:
    def __init__(self, name, email, password, ssn):
        self.name = name
        self.email = email
        self.password = password  
        self.ssn = ssn  

    def to_json(self):
        user_data = {
            "name": self.name,
            "email": self.email
        } 
        return json.dumps(user_data, indent=4)

    @classmethod
    def from_json(cls, json_str, password, ssn):
        data = json.loads(json_str)
        return cls(data["name"], data["email"], password, ssn)

    def __repr__(self):
        return f"User(name={self.name}, email={self.email}, password=****, ssn=****)"
