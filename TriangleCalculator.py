import pdb
import time
import math
from appJar import gui


def Theta(theta):
    Q = 0
    V1 = 0
    tHeta = theta
    while Q == 0:
        try:
            theta = float(theta);
        except ValueError:
            theta = tHeta;
            V1 = 1;
        if theta == "x" or V1 == 0 or theta == "":
            Q = 1;
            return ""
            break
        if theta != "x" and V1 == 1 and theta != "":
            tError = "Please input the angle or input x to find the angle or hit enter"
            return tError
            break


def Hypotenuse(hypotenuse, theta):
    W = 0
    V2 = 0
    hYpot = hypotenuse
    while W == 0:
        try:
            hypotenuse = float(hypotenuse);
        except ValueError:
            hypotenuse = hYpot;
            V2 = 1;
        if hypotenuse == "x" and theta == "x":
            hError = "You have already inputed x for theta. Please change theta or change hypotenuse"
            return hError
        elif hypotenuse == "" and theta == "":
            hError = "Please input the hypotenuse or input x to find the hypotenuse"
            return hError
        elif hypotenuse != "x" and V2 == 1 and hypotenuse != "":
            hError = "Please input the hypotenuse or input x to find the hypotenuse"
            return hError
        elif hypotenuse == "x" or V2 == 0 or hypotenuse == "":
            W = 1;
            return ""
            break


def Adjacent():
    E = 0
    V3 = 0
    while E == 0:
        print("What Is The adjacent Of The Triangle");
        adjacent = input();
        try:
            A = float(adjacent);
        except ValueError:
            A = 0;
            V3 = 1;
        if adjacent == "x" or V3 == 0 or adjacent == "":
            E = 1;
            return adjacent
            break
        if adjacent != "x" and V3 == 1 and adjacent != "":
            print("Please Type A Real adjacent, Type x Or Hit Enter");


def Opposite():
    R = 0
    V4 = 0
    while R == 0:
        print("What Is The opposite Of The Triangle");
        opposite = input();
        try:
            O = float(opposite);
        except ValueError:
            O = 0;
            V4 = 1;
        if opposite == "x" or V4 == 0 or opposite == "":
            R = 1;
            return opposite
            break
        if opposite != "x" and V4 == 1 and opposite != "":
            print("Please Type A Real opposite, Type x Or Hit Enter");


def Thetax(theta, hypotenuse, adjacent, opposite):
    if theta == "x":
        if hypotenuse == "":
            ans = math.atan(float(opposite) / float(adjacent));
            return ans

        elif adjacent == "":
            ans = math.asin(float(opposite) / float(hypotenuse))
            return ans

        else:
            ans = math.acos(float(adjacent) / float(hypotenuse));
            return ans
    else:
        return "False"
        pass


def Hypotenusex(theta, hypotenuse, adjacent, opposite):
    if hypotenuse == "x":
        if theta == "":  # H, O, A
            ans = math.sqrt(math.pow(float(opposite), 2) + math.pow(float(adjacent), 2));
            return ans

        elif adjacent == "":  # H, O, T Sin
            ans = float(opposite) * math.sin(math.radians(float(theta)));
            return ans

        else:  # H, A, T Cos
            ans = float(adjacent) * math.cos(math.radians(float(theta)));
            return ans
    else:
        return "False"
        pass


def Adjacentx(theta, hypotenuse, adjacent, opposite):
    if adjacent == "x":
        if theta == "":  # A, H, O
            ans = math.sqrt(math.pow(float(hypotenuse), 2) + math.pow(float(opposite), 2));
            return ans

        elif hypotenuse == "":  # A, O, T Tan
            ans = float(opposite) * math.tan(math.radians(float(theta)));
            return ans

        else:  # A, H, T Cos
            ans = float(hypotenuse) * math.cos(math.radians(float(theta)));
            return ans
    else:
        return "False"
        pass


def Oppositex(theta, hypotenuse, adjacent, opposite):
    if opposite == "x":
        if theta == "":  # O, H,A
            ans = math.sqrt(math.pow(float(hypotenuse), 2) + math.pow(float(adjacent), 2));
            return ans

        elif hypotenuse == "":  # O, A, T Tan
            ans = float(adjacent) * math.tan(math.radians(float(theta)));
            return ans

        else:  # O, H, T Cos
            ans = float(hypotenuse) * math.cos(math.radians(float(theta)));
            return ans
    else:
        return "False"
        pass


def D(ansT, ansH, ansA, ansO):
    d = "False"
    try:
        ansT = float(ansT)
    except ValueError:
        d = "True"
    try:
        ansH = float(ansH)
    except ValueError:
        d = "False"
    try:
        ansA = float(ansA)
    except ValueError:
        d = "False"
    try:
        ansO = float(ansO)
    except ValueError:
        d = "False"
    return d


def Ans(ansT, ansH, ansA, ansO):
    try:
        ans = float(ansT)
    except ValueError:
        pass
    try:
        ans = float(ansH)
    except ValueError:
        pass
    try:
        ans = float(ansA)
    except ValueError:
        pass
    try:
        ans = float(ansO)
    except ValueError:
        pass
    return ans


def Answer(ans, m, d):
    if d == "True":
        print("%r Degrees" % ans);

    elif d == "False":
        print("{0}{1}".format(ans, m));


"""Intro()

m = Units()

theta = Theta()

hypotenuse = Hypotenuse()

adjacent = Adjacent()

opposite = Opposite()

ansT = Thetax(theta, hypotenuse, adjacent, opposite)

ansH = Hypotenusex(theta, hypotenuse, adjacent, opposite)

ansA = Adjacentx(theta, hypotenuse, adjacent, opposite)

ansO = Oppositex(theta, hypotenuse, adjacent, opposite)

d = D(ansT, ansH, ansA, ansO)

ans = Ans(ansT, ansH, ansA, ansO)

Answer(ans, m, d)"""

def press(button):
    if button == "Cancel":
        app.stop()
        exit(0)
    else:
        global m
        m = app.getRadioButton("Units")
        global theta
        theta = app.getEntry("Theta")
        global hypotenuse
        hypotenuse = app.getEntry("Hypotenuse")
        global adjacent
        adjacent = app.getEntry("Adjacent")
        global opposite
        opposite = app.getEntry("Opposite")


app = gui("Calc Window", "700x500")
app.setBg("white")
app.setFont(18)

app.infoBox("Info", "This is a triangle calculator you need to input the infomation about the triangle the side or angle that you are finding input an x and hit enter and for the infomation that you dont know about the triangle just hit enter", parent=None)

app.addLabel("title", "Triangle Calculator")
app.setLabelBg("title", "white")
app.setLabelFg("title", "black")

app.addRadioButton("Units", "km")
app.addRadioButton("Units", "m")
app.addRadioButton("Units", "cm")
app.addRadioButton("Units", "mm")
app.addValidationEntry("Theta")
app.addValidationEntry("Hypotenuse")
app.addValidationEntry("Adjacent")
app.addValidationEntry("Opposite")

app.setEntryDefault("Theta", "Theta")
app.setEntryDefault("Hypotenuse", "Hypotenuse")
app.setEntryDefault("Adjacent", "Adjacent")
app.setEntryDefault("Opposite", "Opposite")

app.addButtons(["Calculate", "Cancel"], press)

app.go()