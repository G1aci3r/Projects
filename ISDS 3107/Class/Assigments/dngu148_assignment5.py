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
from dateutil.relativedelta import relativedelta as rd
import csv

def full_name(first,last):
        return first + ' ' + last

def age(dob):
        dob_format = dt.strptime(dob, "%Y-%m-%d")
        today = dt.today()
        age = rd(today, dob_format)
        return age.years

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



    file = open('dngu148_assignment5.csv','w')
    headers = ['Customer ID', 'Name', 'Age']
    file.write(str(headers) + '\n')
    for row in results:
        x = id(row[0])
        n = full_name(row[1],row[2])
        a = age(row[3])
        file.write(str(x)+'  ' +n +'  '+ str(a) + '\n')

    file.close()

    connection.close()

main()
