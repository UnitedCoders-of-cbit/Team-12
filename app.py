import string
from encryption import encrytpting
from flask import Flask, redirect, render_template, request
from comparison import compare

app = Flask(__name__)


@app.get('/')
def index_page():
    return render_template('index.html')


@app.post('/compare')
def comparingdocs():

    a = request.form.get('f1')
    completed = encrytpting(a, "TEMP.csv")

    pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10 = compare("TEMP.csv")

    print(pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10)

    p1 = round(pr1)
    p2 = round(pr2)
    p3 = round(pr3)
    p4 = round(pr4)
    p5 = round(pr5)
    p6 = round(pr6)
    p7 = round(pr7)
    p8 = round(pr8)
    p9 = round(pr9)
    p10 = round(pr10)

    return render_template('ONE.html', pr1=pr1, pr2=pr2, pr3=pr3, pr4=pr4, pr5=pr5, pr6=pr6, pr7=pr7, pr8=pr8, pr9=pr9, pr10=pr10, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)


@app.post('/stored')
def storing():
    fdata = request.form.get('ftext')
    nam = request.form.get('fname')+".csv"

    completed = encrytpting(fdata, nam)

    pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10 = compare(nam)

    print(pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10)

    p1 = round(pr1)
    p2 = round(pr2)
    p3 = round(pr3)
    p4 = round(pr4)
    p5 = round(pr5)
    p6 = round(pr6)
    p7 = round(pr7)
    p8 = round(pr8)
    p9 = round(pr9)
    p10 = round(pr10)

    return render_template('ONE.html', pr1=pr1, pr2=pr2, pr3=pr3, pr4=pr4, pr5=pr5, pr6=pr6, pr7=pr7, pr8=pr8, pr9=pr9, pr10=pr10, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)


@app.post('/cimg')
def compimg():
    y = request.form.get('iname')
    if y == "CBIT1.jpg" or "CBIT2.jpg" or "CBIT3.jpg" or "CBIT4.jpg" or "CBIT5.jpg" or "CBIT6.jpg" or "CBIT7.jpg" or "CBIT8.jpg" or "CBIT9.jpg" or "CBIT10.jpg" or "CHESS1.jpg" or "CHESS2.jpg" or "CHESS3.jpg" or "CHESS4.jpg" or "CHESS5.jpg" or "CHESS6.jpg" or "CHESS7.jpg" or "CHESS8.jpg" or "CHESS9.jpg" or "CHESS10.jpg" or "KOHLI1.jpg" or "KOHLI2.jpg" or "KOHLI3.jpg" or "KOHLI4.jpg" or "KOHLI5.jpg" or "KOHLI6.jpg" or "KOHLI7.jpg" or "KOHLI8.jpg" or "KOHLI9.jpg" or "KOHLI10.jpg" or "PHYSICS1.jpg" or "PHYSICS2.jpg" or "PHYSICS3.jpg" or "PHYSICS4.jpg" or "PHYSICS5.jpg" or "PHYSICS6.jpg" or "PHYSICS7.jpg" or "PHYSICS8.jpg" or "PHYSICS9.jpg" or "PHYSICS10.jpg" or "CHEMISTRY1.jpg" or "CHEMISTRY2.jpg" or "CHEMISTRY3.jpg" or "CHEMISTRY4.jpg" or "CHEMISTRY5.jpg" or "CHEMISTRY6.jpg" or "CHEMISTRY7.jpg" or "CHEMISTRY8.jpg" or "CHEMISTRY9.jpg" or "CHEMISTRY10.jpg" or "FIFAWORLDCUP1.jpg" or "FIFAWORLDCUP2.jpg" or "FIFAWORLDCUP3.jpg" or "FIFAWORLDCUP4.jpg" or "FIFAWORLDCUP5.jpg" or "FIFAWORLDCUP6.jpg" or "FIFAWORLDCUP7.jpg" or "FIFAWORLDCUP8.jpg" or "FIFAWORLDCUP9.jpg" or "FIFAWORLDCUP10.jpg":
        man = "THIS IS NOT ORIGINAL CONTENT AND HAS BEEN PIRATED, YOU ARE COMING WITH US"
    else:
        man = "THIS IS ORIGINAL CONTENT GOOD TO GO"
    return render_template('result.html', man=man)


if __name__ == "__main__":
    app.run(debug=True)
