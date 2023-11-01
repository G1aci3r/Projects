student_name = "Don Nguyen"
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

    csv.reader(file)
    mpg_reader = csv.reader(file)
    next(mpg_reader)

    for row in mpg_reader:
        num_auto += 1
        sum_city += int(row[8])
        sum_high += int(row[9])

        if row[1] == 'ford':
                sum_ford += int(row[9])
                num_ford += 1

        if row[11] == 'suv':
                sum_suv += int(row[8])
                num_suv += 1


    avg_hwy = sum_high / num_auto
    avg_city = sum_city / num_auto
    ford_hwy = sum_ford / num_ford
    suv_city = sum_suv / num_suv

    city = round(avg_city,2)
    hwy = round(avg_hwy,2)
    ford = round(ford_hwy,2)
    suv = round(suv_city,2)





file = open("dngu148_assignment4.txt",'w')
file.write( 'The average city mileage of all vehicles is '+ str(city) + '.\n')
file.write('The average highway mileage of all vehicles is '+ str(hwy)+ '.\n')
file.write('The average highway mileage for all Ford is '+ str(ford)+ '.\n')
file.write('The average city mileage of all SUV is '+ str(suv)+ '.\n')
file.close()
