import random
import string
import timeit
from functools import reduce

from bokeh.embed import components
from bokeh.plotting import figure
from flask import render_template, request

from modules import editDistanceR, editDistanceBB, editDistanceDP, editDistancekDP, alignmentR
from run import app


@app.route('/', methods=['GET', 'POST'])
def index():
    first = ""
    second = ""
    kstripe = 4
    edit_distanceDP = [0]
    edit_distanceR = 0
    edit_distancebb = 0
    edit_distanceKDP = [0]
    edit_distanceR_Align = []
    edit_distanceBB_Align = []

    if request.method == 'POST':
        # user inputs
        first = request.form.get('first')
        second = request.form.get('second')
        kstripe = int(request.form.get('kstripe'))

        edit_distanceDP = editDistanceDP(first, second, True)
        edit_distanceR, _alignmentR = editDistanceR(first, second, len(first), len(second))
        edit_distanceR_Align = alignmentR(first, second, _alignmentR)

        edit_distancebb, _alignmentBB = editDistanceBB(first, second, len(first), len(second))
        edit_distanceBB_Align = alignmentR(first, second, _alignmentBB)

        edit_distanceKDP = editDistancekDP(first, second, kstripe, True)

    return render_template('home.html', val_edDP=edit_distanceDP, val_edR=edit_distanceR, AlignR=edit_distanceR_Align,
                           val_edbb=edit_distancebb, AlignBB=edit_distanceBB_Align, val_edkDP=edit_distanceKDP,
                           kstripe=kstripe, first=first,
                           second=second)

@app.route('/recursice', methods=['GET', 'POST'])
def recursice():
    maxchar = 5
    if request.method == 'POST':
        # user inputs
        maxchar = int(request.form.get('maxchar'))
    matrix = [[0 for x in range(11)] for y in range(maxchar)]
    recursice_av_time = []
    lenght_list = []
    for i in range(1, maxchar + 1):
        for j in range(10):
            str1 = generator(i, "qwertyuiopzxcvb")
            str2 = generator(i, "asdfghjklnbv123")
            starttime = timeit.default_timer()
            editDistanceR(str1, str2, len(str1), len(str2), "")
            endtime = timeit.default_timer()
            matrix[i - 1][j] = endtime - starttime
        matrix[i - 1][10] = reduce(lambda x, y: x + y, matrix[i - 1]) / 10.0
        lenght_list.append(i)

    for i in range(maxchar):
        recursice_av_time.append(matrix[i][10])

    for i in range(maxchar):
        for j in range(11):
            matrix[i][j] = float("{0:.5f}".format(matrix[i][j]))

    p = ploting(recursice_av_time, lenght_list, "Recursice", "red")
    script, div = components(p)
    return render_template('recursice.html', maxChar=maxchar, timeex=matrix, the_div=div, the_script=script)


@app.route('/branchbound', methods=['GET', 'POST'])
def branchbound():
    maxchar = 5
    if request.method == 'POST':
        # user inputs
        maxchar = int(request.form.get('maxchar'))
    matrix = [[0 for x in range(11)] for y in range(maxchar)]
    bb_av_time = []
    lenght_list = []
    for i in range(1, maxchar + 1):
        for j in range(10):
            str1 = generator(i, "qwertyuiopzxcvb")
            str2 = generator(i, "asdfghjklnbv123")
            starttime = timeit.default_timer()
            editDistanceBB(str1, str2, len(str1), len(str2))
            endtime = timeit.default_timer()
            matrix[i - 1][j] = endtime - starttime
        matrix[i - 1][10] = reduce(lambda x, y: x + y, matrix[i - 1]) / 10.0
        lenght_list.append(i)

    for i in range(maxchar):
        bb_av_time.append(matrix[i][10])

    for i in range(maxchar):
        for j in range(11):
            matrix[i][j] = float("{0:.5f}".format(matrix[i][j]))

    p = ploting(bb_av_time, lenght_list, "Branch&Bound", "green")
    script, div = components(p)
    return render_template('bb.html', maxChar=maxchar, timeex=matrix, the_div=div, the_script=script)


@app.route('/dynamic')
def dynamic():
    matrix = [[0 for x in range(11)] for y in range(10)]
    dynamic_av_time = []
    lenght_list = []
    for i in range(1, 11):
        for j in range(10):
            str1 = generator(i * 40, "qwertyuopzxcvb")
            str2 = generator(i * 40, "asdfghjklnbv123")
            starttime = timeit.default_timer()
            editDistanceDP(str1, str2, False)
            endtime = timeit.default_timer()
            matrix[i - 1][j] = endtime - starttime
        matrix[i - 1][10] = reduce(lambda x, y: x + y, matrix[i - 1]) / 10.0
        lenght_list.append(i * 40)
    for i in range(10):
        dynamic_av_time.append(matrix[i][10])

    for i in range(10):
        for j in range(10):
            matrix[i][j] = float("{0:.5f}".format(matrix[i][j]))

    p = ploting(dynamic_av_time, lenght_list, "Dynamic", "gold")
    script, div = components(p)
    return render_template('dynamic.html', timeex=matrix, the_div=div, the_script=script)


@app.route('/dynamick', methods=['GET', 'POST'])
def dynamick():
    kstrip = 20
    if request.method == 'POST':
        # user inputs
        kstrip = int(request.form.get('kstrip'))
    matrix = [[0 for x in range(11)] for y in range(10)]
    kdynamic_av_time = []
    lenght_list = []
    for i in range(1, 11):
        for j in range(10):
            str1 = generator(i * 40, "qwertyuiopzxcvb")
            str2 = generator(i * 40, "asdfghjklnbv123")
            starttime = timeit.default_timer()
            editDistancekDP(str1, str2, kstrip, False)
            endtime = timeit.default_timer()
            matrix[i - 1][j] = endtime - starttime
        matrix[i - 1][10] = reduce(lambda x, y: x + y, matrix[i - 1]) / 10.0
        lenght_list.append(i * 40)
    for i in range(10):
        kdynamic_av_time.append(matrix[i][10])

    for i in range(10):
        for j in range(10):
            matrix[i][j] = float("{0:.5f}".format(matrix[i][j]))

    p = ploting(kdynamic_av_time, lenght_list, "Dynamic K strip", "blue")
    script, div = components(p)
    return render_template('dynamick.html', kstrip=kstrip, timeex=matrix, the_div=div, the_script=script)



@app.route('/all', methods=['GET', 'POST'])
def all():
    ####Dynamic#######
    kstrip = 4
    if request.method == 'POST':
        # user inputs
        kstrip = int(request.form.get('kstrip'))

    matrixD = [[0 for x in range(11)] for y in range(10)]
    matrixK = [[0 for x in range(11)] for y in range(10)]
    kdynamic_av_time = []
    dynamic_av_time = []
    lenght_listD = []
    for i in range(1, 11):
        for j in range(10):
            str1 = generator(i * 10, "qwertyuopzxcvb")
            str2 = generator(i * 10, "asdfghjklnbv123")

            starttime = timeit.default_timer()
            editDistanceDP(str1, str2, False)
            endtime = timeit.default_timer()
            matrixD[i - 1][j] = endtime - starttime

            starttime = timeit.default_timer()
            editDistancekDP(str1, str2, kstrip, False)
            endtime = timeit.default_timer()
            matrixK[i - 1][j] = endtime - starttime

        matrixK[i - 1][10] = reduce(lambda x, y: x + y, matrixK[i - 1]) / 10.0
        matrixD[i - 1][10] = reduce(lambda x, y: x + y, matrixD[i - 1]) / 10.0
        lenght_listD.append(i * 10)

    for i in range(10):
        dynamic_av_time.append(matrixD[i][10])
        kdynamic_av_time.append(matrixK[i][10])

    ############################################
    ##########Branch&BOUND##############
    maxchar = 8
    if request.method == 'POST':
        # user inputs
        maxchar = int(request.form.get('maxchar'))
    matrixBB = [[0 for x in range(11)] for y in range(maxchar)]
    matrixR = [[0 for x in range(11)] for y in range(maxchar)]
    recursice_av_time = []
    bb_av_time = []
    lenght_listR = []
    for i in range(1, maxchar + 1):
        for j in range(10):
            str1 = generator(i, "qwertyuiopzxcvb")
            str2 = generator(i, "asdfghjklnbv123")

            starttime = timeit.default_timer()
            editDistanceBB(str1, str2, len(str1), len(str2))
            endtime = timeit.default_timer()
            matrixBB[i - 1][j] = endtime - starttime

            starttime = timeit.default_timer()
            editDistanceR(str1, str2, len(str1), len(str2), "")
            endtime = timeit.default_timer()
            matrixR[i - 1][j] = endtime - starttime

        matrixR[i - 1][10] = reduce(lambda x, y: x + y, matrixR[i - 1]) / 10.0
        matrixBB[i - 1][10] = reduce(lambda x, y: x + y, matrixBB[i - 1]) / 10.0
        lenght_listR.append(i)

    for i in range(maxchar):
        bb_av_time.append(matrixBB[i][10])
        recursice_av_time.append(matrixR[i][10])

    timelist = [dynamic_av_time, kdynamic_av_time, bb_av_time, recursice_av_time]
    lenght_list = [lenght_listD, lenght_listR]
    names = ["DYnamic", "K Stripe", "Branch&Bound", "Recursive"]
    colors = ["red", "gold", "blue", "green"]

    fig1 = plotingmulti(timelist, lenght_list, names, colors)
    script1, div1 = components(fig1)

    fig2 = plotingmulti(timelist, lenght_list, names, colors,1)
    script2, div2 = components(fig2)

    fig3 = plotingmulti(timelist, lenght_list, names, colors,2)
    script3, div3 = components(fig3)

    return render_template('all.html', the_div=div1, the_script=script1, div2=div2, script2=script2, div3=div3,
                           script3=script3 , kstripe=kstrip , maxcharR=maxchar)




def ploting(y, x, name, color):
    p = figure(title=name)
    p.line(x, y, legend=name, line_color=color, line_width=2)
    p.legend.location = "top_left"
    p.xaxis.axis_label = 'Length of the String '
    p.yaxis.axis_label = 'Time in Sec'

    return p


def plotingmulti(y, x, name, color, val=0):
    if val == 0:
        p = figure(title="ALL")
        p.line(x[0], y[0], legend=name[0], line_color=color[0], line_width=1)
        p.line(x[0], y[1], legend=name[1], line_color=color[1], line_width=1)
        p.line(x[1], y[2], legend=name[2], line_color=color[2], line_width=1)
        p.line(x[1], y[3], legend=name[3], line_color=color[3], line_width=1)
        p.legend.location = "top_left"
        p.xaxis.axis_label = 'Length of the String '
        p.yaxis.axis_label = 'Time in Sec'
        return p
    if val == 1:
        p = figure(title="Dynamic and Stripe")
        p.line(x[0], y[0], legend=name[0], line_color=color[0], line_width=1)
        p.line(x[0], y[1], legend=name[1], line_color=color[1], line_width=1)
        p.legend.location = "top_left"
        p.xaxis.axis_label = 'Length of the String '
        p.yaxis.axis_label = 'Time in Sec'
        return p
    if val == 2:
        p = figure(title="Ricursive & BB")
        p.line(x[1], y[2], legend=name[2], line_color=color[2], line_width=1)
        p.line(x[1], y[3], legend=name[3], line_color=color[3], line_width=1)
        p.legend.location = "top_left"
        p.xaxis.axis_label = 'Length of the String '
        p.yaxis.axis_label = 'Time in Sec'
        return p


def generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


'''
##################
import xlsxwriter

workbook = xlsxwriter.Workbook('Rec_time.xlsx')
worksheet = workbook.add_worksheet()
row = 2
for col, data in enumerate(matrix):
    worksheet.write_column(row, col, data)

workbook.close()

########################
'''
