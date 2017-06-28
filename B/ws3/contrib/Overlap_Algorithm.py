import numpy as np
import itertools

lat40times = np.genfromtxt('40Lat100Lon5degFix.csv', dtype=None, delimiter=',')

#Creating an empty array to store binary arrays
over_array = []
'''
First I step through the data structured like:
(sthr, stmin, stsec, endhr, endmin, endsec, dur).
I generate an array of zeros equal in length to the
amount of seconds in a day and fill it with a 1 where the pass 
took place and store the result in the over_array. 
The last step is to check if there is any overlap between any of the arrays
with any of the others. The final lines of code just check to see if
overlap was found...in this case there wasn't any
'''
for i in lat40times:
    day_sec = np.zeros((1,24*3600))
    day_sec[i[0]*3600+i[1]*60+i[2]:i[3]*3600+i[4]*60+i[5]]=1
    over_array.append(day_sec)

for x,y in itertools.combinations(over_array, 2):
    test = np.logical_and(x==1, y==1)
    
for i in test:
    for j in i:
        if j==True:
            print ("True!")  
        




    

    