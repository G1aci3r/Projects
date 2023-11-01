student_name = "Don Nguyen"
# ID  fName      lName    dob           city                state  ZIP
# 1, 'Kristen', 'Klein', '2002-11-03', 'North Cynthiafurt', 'AZ', '50788'
# 3, 'Justin', 'Hanna', '1998-01-30', 'North Chadfurt', 'WA', '39505'
# 4, 'Pamela', 'Stephens', '1995-11-12', 'Margaretland', 'MN', '13967'
# 5, 'Annette', 'Murphy', '1996-08-09', 'Ronaldtown', 'WA', '98806'
# 7, 'Oscar', 'Doyle', '1995-02-02', 'South Cindy', 'VT', '04481'
# 8, 'Kelly', 'Ramos', '1997-09-12', 'South Paulmouth', 'MT', '01272'
# 9, 'James', 'Rollins', '1994-10-17', 'Lake Ricardoton', 'CA', '22420'
# 10, 'Lisa', 'Williams', '1997-10-23', 'Farmerborough', 'WY', '59675'




import sqlalchemy as db
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

class Customer:

    def __init__(self,id,fname,lname, dob,city,state,zip): # you will need to add the attributes
        self.id = id
        self.firstname = fName
        self.lastname = lName
        self.dob = dob
        self.city = city
        self.state = state
        self.zip = ZIP



        # need full name method
    def full_name(self,fName,lName):
        return self.firstname + " " + self.lastname

    #def age(self):  can use the same one as ass5, but add self, need to calculate the age. take from ass5 but put self and self.dob
        #self.dob <--- this will have the string of the date of birth
        #return  needs an interger
    def age(self,dob):
            dob_format = dt.strptime(self.dob, "%Y-%m-%d")
            today = dt.today()
            age = rd(today, dob_format)
            return age.years

    def adult(self):
        if self.age() >= 18:
            return True
        else:
            return False

    def to_json(self):
        j = {}  # create an empty dict
        j.update(self.__dict__)  # add the object's attributes as a dict
        j['id'] = self.id
        j['first_name'] = self.fName
        j['last_name'] = self.lName
        j['dob'] = self.dob
        j['city'] = self.city
        j['state'] = self.state
        j['zip'] = self.ZIP
        j['age'] = self.age
        j['full_name'] = self.full_name
        j['adult'] = self.adult
        # add the other key / value pairs per the assignment.
        return j

    def main():
        engine = db.create_engine('sqlite:///customer.sqlite')
        connection = engine.connect()
        metadata = db.MetaData()
        customer = db.Table('customer', metadata, autoload=True, autoload_with=engine)
        query = db.select([customer.columns.id,
                        customer.columns.first_name,
                        customer.columns.last_name,
                        customer.columns.dob])

        proxy = connection.execute(query)
        results = proxy.fetchall()


        with open('assignment6.txt','w') as out_file:
            from dngu148_cust_class import Customer
            import json
            j = self.__dict__
            json.dumps(j,outfile)
