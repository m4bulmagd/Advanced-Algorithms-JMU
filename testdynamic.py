import csv
from datetime import datetime


csvfile = open("C:\\_____\\___\\export_1512164163.csv")
data=csv.reader(csvfile)
for row in data:
    x=list(data)
    k=0
    current_time = datetime.now()
    num_sample=int(input("enter the total of samples to test  :"))

    for k in range(0,num_sample):
         target1=x[k]
         target2=x[k+1]
         _1st=target1[3]
         _2nd=target2[3]


         def editdistanceDP(str1, str2):
             m = len(str1)
             n = len(str2)

             if m == 0: return n
             if n == 0: return m

             matrix = [[0 for x in range(n + 1)] for y in range(m + 1)]

             for i in range(m + 1):
                 for j in range(n + 1):
                     if i == 0:
                         matrix[i][j] = j

                     elif j == 0:
                         matrix[i][j] = i

                     elif str1[i - 1] == str2[j - 1]:
                         matrix[i][j] = matrix[i - 1][j - 1]

                     else:
                         matrix[i][j] = 1 + min(matrix[i][j - 1],  # Insert
                                                matrix[i - 1][j],  # Remove
                                                matrix[i - 1][j - 1])  # Replace
             return matrix[m][n]


         print(editdistanceDP(_1st, _2nd))
    time_finish=datetime.now()
    print("processing time for first ",num_sample," samples =",time_finish-current_time)
