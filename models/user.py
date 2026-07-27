class User:
    def __init__(self,user_id,first_name,last_name,email,password,phone,address):
        self.user_id=user_id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.__password=password
        self.phone=phone
        self.address=address
        self.notifications=[]

    def login(self,password):
        if self.__password==password:
            return "Login Successful"
        else:
            return "Incorrect password"
        
    def logout(self):
        return f"{self.first_name} {self.last_name} has logged out "
    
    def get_details(self):
        return f"ID : {self.user_id} Name : {self.first_name} {self.last_name} Email : {self.email}"
    
    def update_email(self,new_email):
        if "@" in new_email:
            self.email=new_email
            print(f"{self.email} updated successfully")
        else:
            print("invalid email")

    def update_password(self,old_password,new_password,confirm_new_password):
        if self.__password==old_password:
            if new_password==confirm_new_password:
                self.__password=new_password
                print("password updated successfully")
            else:
                print("Passwords do not match")
        else:
            print("incorrect password")

    def update_phone_number(self,phone_number):
        if phone_number.isdigit()==True and len(phone_number)==10:
            self.phone=phone_number
            print(f"{phone_number} Updated Successfully")
        else:
            print("invalid phone number")

    def update_address(self,new_address):
        self.address=new_address
        print("Address updated successfully")
