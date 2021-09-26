from email_validator import validate_email, EmailNotValidError

class Authentication(object):

    def __init__(self, username='', email='', mobile=''):
        self.username = username
        self.email = email
        self.mobile = mobile
    def __lower(self):  
        lower = any(c.islower() for c in self.username)
        if lower:
            error_string = ''
        else:
            error_string = "username should have at least 1 lower character \n \n"
        return lower, str(error_string)

    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        if upper:
            error_string = ''
        else:
            error_string = "username should have at least 1 upper character \n \n"
        return upper, str(error_string)

    def __digit(self):
        digit = any(c.isdigit() for c in self.username)
        if digit:
            error_string = ''
        else:
            error_string = "username should have at least 1 numeric character \n"
        return digit, str(error_string)

    def __space(self):
        space = any(c.isspace() for c in self.username)
        if not space:
            error_string = ''
        else:
            error_string = "username should not have space \n"
        return not space, str(error_string)

    def __length(self):
        length = len(self.username)
        if length >= 6:
            error_string = ''
        else:
            error_string = "username length is less than 6 \n"
        return length, str(error_string)

    def __specialcharacter(self):
        special_characters = '"!@#$%^&*()-+?_=,<>/"'
        special_exist = any(c in special_characters for c in self.username)
        if special_exist :
            error_string = ''
        else:
            error_string = "username should have at least 1 special character \n"
        return special_exist, str(error_string)

    def validate(self):
        lower, error1 = self.__lower()
        upper, error2 = self.__upper()
        digit, error3 = self.__digit()
        space, error4 = self.__space()
        length, error5 = self.__length()
        special_exist, error6 = self.__specialcharacter()
        report = lower and upper and digit and space and length >= 6 and special_exist

        if report:
            print("Username passed all checks ")
            return True
        else:
            print(error1,error2,error3,error4,error5,error6)
            return False


    def email_authentication(self):
        try:
            # Validate.
            email = self.email
            valid = validate_email(email)
            # Update with the normalized form.
            email = valid.email
            print("this is valid email " + email)
            return True
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e))
            return False,str(e)

    def mobile_authentication(self):
        mobile = self.mobile
        mobile_flag = all(c.isdigit() for c in mobile)
        mobile_length = len(mobile)
        if mobile_flag and mobile_length == 10:
            return True
        else:
            return str("Please check your mobile number")



C = Authentication("ram1@Q", "analyst.rohitk@gcom", "880040999079")
print(C.validate())
print(C.email_authentication())
print(C.mobile_authentication())

