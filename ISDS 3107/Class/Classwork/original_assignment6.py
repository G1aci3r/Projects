from datetime import datetime
from dateutil.relativedelta import relativedelta

class Customer:

    def __int__(self,id,name,lname, dob): # you will need to add the attributes
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.dob = dob

        # need full name method

    #def age(self):  can use the same one as ass5, but add self, need to calculate the age. take from ass5 but put self and self.dob
        #self.dob <--- this will have the string of the date of birth
        #return  needs an interger
    def age(self):
            dob_format = dt.strptime(dob.self, "%Y-%m-%d")
            today = dt.today()
            age = rd(today, dob_format)
            return age.years

    def adult(self):
        return self.age() >= 18

    def to_json(self):
        j = self.__dict__
        j['age'] = self.age()
        j['adult'] = self.adult()

        return j
