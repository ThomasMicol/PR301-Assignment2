import re
from datetime import *
import math

class DataValidator:
    
    def __init__(self):
        self.data_array = []

    # validate input for date type
    # KATE
    def valid_date(self, birthday):
        minyear = 1000
        maxyear = date.today().year

        mydate = birthday.split('-')
        if len(mydate) == 3:
            birthdate = mydate[0]
            birthmonth = mydate[1]
            birthyear = mydate[2]
            print(birthyear)

            if int(birthyear) > maxyear or int(birthyear) < minyear:
                print(mydate)
                birthdayobj = date(birthdate, birthmonth, birthyear)
                return True
            else:
                print('Year is out of range')

    def check_person_id(self, person_id):
            if re.match(r'[a-z][0-9]{3}', (person_id).lower()):
                if len(str(person_id)) >= 5:
                    return False
                else:
                    return True
            else:
                return False

    def check_person_sex(self, person_sex):
        if person_sex.upper() == "M" or (person_sex).upper() == "F":
            return True
        else:
            return False

    def check_person_age(self, person_dob):
        try:
            datetime.strptime(person_dob, "%d-%m-%Y")
        except ValueError:
            return False

    def check_person_sales(self, person_sales):
        if re.match(r'[0-9]{3}', person_sales):
            return True
        else:
            return False

    def check_person_bmi(self, person_bmi):
        if re.match(r'\b(NORMAL|OVERWEIGHT|OBESITY|UNDERWEIGHT)\b', (person_bmi).upper()):
            return True
        else:
            return False

    def check_person_salary_is_int(self, person_salary):
        if(isinstance(person_salary, int)):
            return True
        else:
            return False

    def check_person_salary_length(self, person_salary):
        try:
            if len(str(int(person_salary))) > 3:
                return False
            else:
                return True
        except ValueError:
            return False
    # Validate date match year
    # KATE

    def valid_age(self, birthday):
        today = date.today()
        mydate = birthday
        try:
            born = datetime.strptime(mydate, '%d%m%Y')
        except ValueError:
            pass
        else:
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return age

    # Validate file data

    def validate(self, data):
        """ TestCase for validate
        >>> aFileHandler = FileHandler()
        >>> aFileHandler.validate([("e01","m","20","20","Normal","200","12-06-1998")])
        invalidate data: e01
        invalidate data: m
        invalidate data: 20
        invalidate data: 20
        invalidate data: Normal
        invalidate data: 200
        invalidate data: 12-06-1998

        """
        self.data_array = data
        clean_array = []

        feedback = ""
        for person in data:
            feedback += "Feedback for data at: " + str(data.index(person) + 1) + "\n"

            self.valid = True

            if not self.check_person_id(person['id']):
                feedback += "ID is incorrect; must contain a letter and 3 digits e.g. a001.\n"
                self.valid = False;

            if not self.check_person_sex(person['sex']):
                feedback += "Incorect Gender; must be M or F.\n"
                self.valid = False;

            if not self.check_person_age(person['dob']):
                feedback += "Date is not corrent format! " + str(person['dob'])
                self.valid = False
            else:  
                the_date = datetime.strptime(person['dob'], "%d-%m-%Y")
                test_age = math.floor(((datetime.today() - the_date).days/365))
                if test_age == int(person['age']):
                    pass
                else:
                    self.valid = False
                    feedback += "Age and birthday does not match. " + str(test_age) + ":" + str(int(person['age']))


            if not self.check_person_sales(person['sales']):
                feedback += "Incorrect sales number; must be a 3 digit whole number. \n"
                self.valid = False

            if not self.check_person_bmi(person['bmi']):
                feedback += "Incorrect BMI value; Choose from Normal, Overweight, Obesity or Underweight. \n"
                self.valid = False

            if not self.check_person_salary_is_int(person['salary']):
                feedback += "Incorrect income; must be an integer number. \n" + str(person['salary'])
                self.valid = False

            if not self.check_person_salary_length(person['salary']):
                feedback += "Income is too large."
                self.valid = False

            if self.valid:
                clean_array.append(person)
                feedback += "Passed and added to database.\n"
            else:
                feedback += '\n\n'

        print(feedback)
        return clean_array