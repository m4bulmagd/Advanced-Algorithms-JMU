import math

def editDistanceDP(str1, str2, booli):
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

    # for i in range(m+1):
    #    print(matrix[i])
    if booli:
        firststr, bibing, secondstr = alignmentD(matrix, str1, str2)
        return matrix[m][n], firststr, bibing, secondstr
    else:
        return matrix[m][n]

def alignmentD(matrix, str1, str2):
    i = len(str1)
    j = len(str2)
    str1 = list(str1)
    str2 = list(str2)
    alig = []
    infrow = []
    infcol = []

    while True:
        if i - 1 < 0:
            matrix[i - 1][j - 1] = math.inf
            matrix[i - 1][j] = math.inf
        if j - 1 < 0:
            matrix[i - 1][j - 1] = math.inf
            matrix[i][j - 1] = math.inf

        operitions = [matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]]
        choosen = operitions.index(min(operitions))
        if choosen == 0:
            if matrix[i][j] > matrix[i - 1][j - 1]:
                alig.insert(0, "_")
                if i != 0:
                    i = i - 1
                if j != 0:
                    j = j - 1
            else:
                alig.insert(0, "|")
                if i != 0:
                    i = i - 1
                if j != 0:
                    j = j - 1



        elif choosen == 1:
            alig.insert(0, "_")
            str1.insert(i, "*")
            if j != 0:
                j = j - 1

        elif choosen == 2:
            alig.insert(0, "_")
            str2.insert(j, "*")
            if i != 0:
                i = i - 1

        if i == 0 and j == 0:
            break

    align = ""
    string1 = ""
    string2 = ""

    for i in range(len(alig)):
        align = align + alig[i]
        string1 = string1 + str1[i]
        string2 = string2 + str2[i]

    return string1, align, string2

def editDistanceR(str1, str2, m, n, _alignment=""):
    # if 1st String is empty ED will be the length of 2nd string ( insert all chars )
    if m == 0:
        _alignment = "I" * n
        return n, _alignment

    # if 2nd String is empty ED will be the length of 1nd string ( remove all chars )
    if n == 0:
        _alignment = "R" * m
        return m, _alignment

    # If last characters of two strings are same, move to the next chars .
    if str1[m - 1] == str2[n - 1]:
        edit, _alignment = editDistanceR(str1, str2, m - 1, n - 1, _alignment)
        _alignment = _alignment + "M"
        return edit, _alignment

    insert, _alignment1 = editDistanceR(str1, str2, m, n - 1, _alignment)
    remove, _alignment2 = editDistanceR(str1, str2, m - 1, n, _alignment)
    replace, _alignment3 = editDistanceR(str1, str2, m - 1, n - 1, _alignment)

    operitions = [insert, remove, replace]
    # if the two chars are not equal to each other then do the three Opreation and return the minimum cost for all three operations recursivly
    choosen = operitions.index(min(operitions))

    result = 0
    if choosen == 0:
        result = insert + 1
        _alignment1 = _alignment1 + "I"
        return result, _alignment1

    elif choosen == 1:
        result = remove + 1
        _alignment2 = _alignment2 + "R"
        return result, _alignment2

    elif choosen == 2:
        result = replace + 1
        _alignment3 = _alignment3 + "S"
        return result, _alignment3

def alignmentR(str1, str2, alignment):
    bibing = ""
    for i in range(len(alignment)):
        if alignment[i] == "S":
            bibing = bibing + "_"
        elif alignment[i] == "I":
            bibing = bibing + "_"
            str1 = str1[:i] + "*" + str1[i:]
        elif alignment[i] == "R":
            bibing = bibing + "_"
            str2 = str2[:i] + "*" + str2[i:]
        elif alignment[i] == "M":
            bibing = bibing + "|"
        else:
            bibing = "SOMETHING WENT WRONG"
    return str1, str2, bibing

def editDistancekDP(str1, str2, k, booli):
    if len(str2) > len(str1):
        str1, str2 = str2, str1

    m = len(str1)
    n = len(str2)

    if m == 0: return n
    if n == 0: return m

    start = (0, 0)
    end = (m, n - 1)
    diag = get_line(start, end)

    # we will use just 2 rows -- that is all what we need ,,
    # the first itiration we can fill the row without need any additional info from previous rows
    # first we wirte on the second row then we will overwrite it on first row ,, this will be our for loop
    # then we will use the first row to generate the second (next) row and after finish it we will overwrite it on first row

    matrix = [[math.inf for x in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # we will not fill all the cells ,, just few of them K around the diagonal
            # choose which cell we will fill
            if j >= max(0, (diag[i][1] - k)) and j <= diag[i][1] + k:
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
    if booli:
        firststr, bibing, secondstr = alignmentD(matrix, str1, str2)
        return matrix[m][n], firststr, bibing, secondstr
    else:
        return matrix[m][n]

def editDistanceBB(str1, str2, m, n, cost=0, _alignment=""):
    best = max(len(str1), len(str2))
    # if 1st String is empty ED will be the length of 2nd string ( insert all chars )
    if m == 0:
        best = n
        _alignment = "I" * n
        return n, _alignment
    # if 2nd String is empty ED will be the length of 1nd string ( remove all chars )
    if n == 0:
        best = m
        _alignment = "R" * m
        return m, _alignment

    # If last characters of two strings are same, move to the next chars .
    if str1[m - 1] == str2[n - 1]:
        edit, _alignment = editDistanceBB(str1, str2, m - 1, n - 1, cost=cost, _alignment=_alignment)
        _alignment = _alignment + "M"
        return edit, _alignment

    if cost <= best:
        cost = cost + 1
        insert, _alignment1 = editDistanceBB(str1, str2, m, n - 1, cost=cost, _alignment=_alignment)
        remove, _alignment2 = editDistanceBB(str1, str2, m - 1, n, cost=cost, _alignment=_alignment)
        replace, _alignment3 = editDistanceBB(str1, str2, m - 1, n - 1, cost=cost, _alignment=_alignment)

        operitions = [insert, remove, replace]
        # if the two chars are not equal to each other then do the three Opreation and return the minimum cost for all three operations recursivly
        choosen = operitions.index(min(operitions))

        result = 0
        if choosen == 0:
            result = insert + 1
            _alignment1 = _alignment1 + "I"
            return result, _alignment1

        elif choosen == 1:
            result = remove + 1
            _alignment2 = _alignment2 + "R"
            return result, _alignment2

        elif choosen == 2:
            result = replace + 1
            _alignment3 = _alignment3 + "S"
            return result, _alignment3
    return math.inf ,_alignment

'''
def editDistancekDP(str1,str2 ):
    k=2
    if len(str2) > len(str1):
        str1, str2 = str2, str1

    m = len(str1)
    n = len(str2)

    if m == 0: return n
    if n == 0: return m

    start = (0, 0)
    end = (m, n - 1)
    diag = get_line(start, end)

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
'''

####### get The Diagonal - this function to generate the diagonal path ( Points ) which will be used for choose the cells around it  #################
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
####### get The Diagonal #################

