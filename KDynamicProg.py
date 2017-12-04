str1 = input("str1 : ")
str2 = input("str2 : ")
k = int(input("# diagonal : "))  #the number of the cells around the diagonal


#not important :D i need the longest string to be the first one ( str1 )
if len(str2) > len(str1):
    print(len(str1)," ",len(str2))
    str1,str2 = str2,str1
    print(len(str1), " ", len(str2))

import math


####### get The Diagonal - this function to generate the diagonal path ( Points ) which will be used for choose the cells around it  #################
start = (0,0)
end = (len(str1),len(str2)-1)
def get_line(start, end):

    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    points = []
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    for x in range(x1, x2 + 1):
        coord = [y, x] if is_steep else [x, y]
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

diag = get_line(start,end)
####### get The Diagonal #################



def editdistanceKDP(str1,str2):
    m = len(str1)
    n = len(str2)

    if m == 0: return n
    if n == 0: return m

    # we will use just 2 rows -- that is all what we need ,,
    #the first itiration we can fill the row without need any additional info from previous rows
    # first we wirte on the second row then we will overwrite it on first row ,, this will be our for loop
    # then we will use the first row to generate the second (next) row and after finish it we will overwrite it on first row


    matrix = [[math.inf for x in range(n+1)] for y in range(2)] # generate 2 rows have infinity value

    for i in range(m+1):
        for j in range(n + 1):

            #overwrite on the first row
            matrix[0][j] = matrix[1][j]
            matrix[1][j]= math.inf

        for j in range(n+1):
            #we will not fill all the cells ,, just few of them K around the diagonal
            # choose which cell we will fill
            if j >= max(0,(diag[i][1] - k)) and j <= diag[i][1] + k :
                if i == 0:
                    matrix[1][j] = j

                elif j ==0 :
                    matrix[1][j] = i

                elif str1[i-1] == str2[j-1]:
                    matrix[1][j]= matrix[0][j-1]

                else:
                    matrix[1][j] = 1 + min( matrix[1][j-1],       # Insert
                                            matrix[0][j],       # Remove
                                            matrix[0][j-1])       # Replace
        print(matrix[1])

    return matrix[1][n]


print(editdistanceKDP(str1,str2),"  :D ")