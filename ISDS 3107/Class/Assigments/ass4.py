student_name = 'Don Nguyen'
# id	manufacturer	model	displ	year	cyl	trans	    drv	cty	hwy	 fl	  class
# 1	    audi            a4	    1.8	    1999	4	auto(l5)    f	18	29   p    compact
# 2	    audi	        a4	    1.8	    1999	4	manual(m5)	f	21	29	 p    compact
# 3	    audi	        a4	    2	    2008	4	manual(m6)	f	20	31 	 p    compact
# 4	    audi	        a4	    2	    2008	4	auto(av)	f	21	30	 p    compact
# 5	    audi	        a4	    2.8	    1999	6	auto(l5)	f	16	26	 p    compact

import csv

with open('mpg.csv') as file:

    num_auto = 0
    sum_city = 0
    sum_high = 0
    num_ford = 0
    sum_ford = 0
    num_suv = 0
    sum_suv = 0

    cvs.reader(file)
    mpg_reader = csv.reader(file)
    next(mpg_reader)

    for row in mpg_reader:
        #print(row)
        num_auto += 1
        sum_city += int(row[8])
        sum_high += int(row[9])

        if row[1] == 'ford':
                sum_ford += int(row[8])
                num_ford += 1

        elif row[11] == 'suv':
                sum_suv += int(row[9])
                num_suv += 1


    avg_city = sum_city / num_auto
    avg_high = sum_high / num_auto
    avg_ford = sum_ford / num_ford
    avg_suv = sum_suv / num_suv

    print('The avg city milage is '+str(avg_city))
    print('The average highway milage of all vechiles is '+ str(avg_high))
    print('The average highway milage for all Ford is '+ str(avg_ford))
    print('The average city milage of all SUV is '+ str(avg_suv))


with open ('pawsid_assignment4.txt') as out_file:
    out_file.write("Ive created a new file. \n")
    out_file.write ('There are '+str(num_auto)+ 'vehicles in the file.')
# print("There are" + str(num_auto)+ " vehicles in the file.")
