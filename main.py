from sympy import derive_by_array,symbols,integrate,parse_expr
from PyQt5 import QtGui,QtWidgets
from sys import argv

class ID(QtWidgets.QWidget):
    def __init__(self):
        super(ID, self).__init__()
        self.setFixedSize(600, 400)
        self.setWindowTitle("Integration And Differentiate")
        self.setWindowIcon(QtGui.QIcon("1.jpg"))
        self.setStyleSheet("""background-color:rgba(255,100,150,0.1);""")
        self.setToolTip("Welcome ")
        self.setToolTipDuration(3000)

        self.inputt = QtWidgets.QLineEdit(self)
        self.inputt.setStyleSheet("""
        border-radius:25px;
        border:3px groove green;
        background-color: transparent;
        color:crimson;
        width:574;
        height:50;
        font-size:30px;
        font-family: 'Brush Script MT', cursive;
        padding: 10px;
        """)
        self.inputt.setToolTip("Enter Your Equation")
        self.setToolTipDuration(3000)
    
        self.label_hint = QtWidgets.QLabel("'X' Is The Variable Here !!", self)
        self.label_hint.setStyleSheet("""
        color: yellow;
        background-color: transparent;
        font-size:20px;
        font-family: 'Comic Sans MS', sans-serif;
        """)
        self.label_hint.move(180, 130)
        self.label_hint.setToolTip("Note")
        self.label_hint.setToolTipDuration(3000)
    
        self.integrate = QtWidgets.QPushButton("Integrate", self)
        self.integrate.setStyleSheet("""
        background-color: #F7CAC9;
        color: violet;
        font-size:20px;
        font-family: 'Comic Sans MS', sans-serif;
        border-radius: 30px;
        border: 4px groove black;
        """)
        self.integrate.resize(150, 60)
        self.integrate.move(50, 180)
        self.integrate.setToolTip("Integration")
        self.integrate.setToolTipDuration(3000)

        self.clear = QtWidgets.QPushButton("Clear", self)
        self.clear.setStyleSheet("""
                background-color: #F7CAC9;
                color: violet;
                font-size:20px;
                font-family: 'Comic Sans MS', sans-serif;
                border-radius: 30px;
                border: 4px groove black;
                """)
        self.clear.resize(150, 60)
        self.clear.move(215, 180)
        self.clear.setToolTip("Clear Screen")
        self.clear.setToolTipDuration(3000)

    
        self.derive = QtWidgets.QPushButton("Differentiate", self)
        self.derive.setStyleSheet("""
        background-color: #F7CAC9;
        color: violet;
        font-size:20px;
        font-family: 'Comic Sans MS', sans-serif;
        border-radius: 30px;
        border: 4px groove black;
        """)
        self.derive.resize(150, 60)
        self.derive.move(400, 180)
        self.derive.setToolTip("Differentiation")
        self.derive.setToolTipDuration(3000)
    
        self.result = QtWidgets.QLineEdit(self)
        self.result.setStyleSheet("""
        border-radius:25px;
        border:3px groove orange;
        background-color: transparent;
        color:crimson;
        width:574;
        height:50;
        font-size:30px;
        font-family: 'Brush Script MT', cursive;
        padding: 10px;
        """)
        self.result.move(0, 300)
        self.result.setToolTip("Result Of Integration Or Differentiate")
        self.result.setToolTipDuration(3000)
        self.result.setReadOnly(True)
        self._1()
        self._2()
        self._3()

    def _1(self):
        self.derive.clicked.connect(self.clicked1)

    def clicked1(self):
        inputt_string = self.inputt.text()
        if '^' in inputt_string:
            inputt_string = inputt_string.replace("^","**")
        x = symbols("x")
        self.result.setText(str(derive_by_array(parse_expr(inputt_string),x)))

    def _2(self):
        self.integrate.clicked.connect(self.clicked2)

    def clicked2(self):
        inputt_string = self.inputt.text()
        if '^' in inputt_string:
            inputt_string = inputt_string.replace("^","**")
        x = symbols("x")
        if(str(integrate(parse_expr(inputt_string),x)) != f"Integral({inputt_string}, x)"):
            self.result.setText(str(integrate(parse_expr(inputt_string),x)) + " + C")
        else:
            self.result.setText("Cannot Solve")

    def _3(self):
        self.clear.clicked.connect(self.clicked3)

    def clicked3(self):
        self.inputt.setText("")
        self.result.setText("")

if __name__ == '__main__':
    application = QtWidgets.QApplication(argv)
    win = ID()
    win.show()
    application.exec_()
