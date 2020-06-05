import sys
import numpy as np
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QInputDialog
from PyQt5.QtGui import QIcon, QPalette, QWindow
from PyQt5.QtCore import pyqtSlot
from functools import partial
from PyQt5.Qt import QVBoxLayout



class App(QWidget):


    def checkSolvable(self, arr, black):
        count = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (arr[i] > arr[j] and arr[i] != black and arr[j] != black):
                    count = count + 1
        if (black > 3 and black < 8 and count%2 == 0):
            print("Inversions: ", count)
            print("Black: ", black)
            return True
        elif (black > 11 and count%2 == 0):
            print("Inversions: ", count)
            print("Black: ", black)
            return True
        elif (black < 4 and count%2 != 0):
            print("Inversions: ", count)
            print("Black: ", black)
            return True
        elif (black > 7 and black < 12 and count%2 != 0):
            print("Inversions: ", count)
            print("Black: ", black)
            return True
        else: 
            return False
     

    
    
    def __init__(self):
        super().__init__()
        self.title = 'Puzzle'
        self.left = 500
        self.top = 200
        self.width = 250
        self.height = 280
        self.blackBox = random.randint(0,15)
        self.button = list()
        self.coordinateArrX = []
        self.coordinateArrY = []
        self.moves = 0
        self.label = QLabel("Moves: " + str(self.moves),self)
        self.ranks = []
        self.leaderLabels = []
        self.table = 0
        #self.label2 = QLabel(str(self.moves))
        self.arr = random.sample(range(1,16),15)
        random.shuffle(self.arr)
        
        while(self.checkSolvable(self.arr,self.blackBox) == False):
            self.blackBox = random.randint(0,15)
            random.shuffle(self.arr)
        
        self.textArr = []
        idx = 0
        
        for i in range(16):
            if (i == self.blackBox):
                self.button.append(QPushButton(self))
                self.textArr.append(str("0"))
            else:
                self.button.append(QPushButton(str(self.arr[idx]),self))
                self.textArr.append(str(self.arr[idx]))
                idx = idx + 1
        
        for i in range(4):
            for j in range(4):
                self.coordinateArrX.append(j*62)
                self.coordinateArrY.append(i*62)
        
        temp = []
        for i in range(len(self.arr)):
            if (i == self.blackBox):
                temp.append(0)
            temp.append(self.arr[i])
        self.arr = temp
        self.initUI()
    
    
        
   
       
        
                
                
    def callPuzzle(self):
        
        value = str(self.moves)
        self.label.setText("Moves: " + value)
        self.label.adjustSize()
        self.label.move(100,260)
        font = self.button[0].font()
        font.setPointSize(12)
        
       
        for i in range(16):
            self.button[i].setText(self.textArr[i])
            self.button[i].setFont(font)  
            self.button[i].move(self.coordinateArrX[i],self.coordinateArrY[i])
            self.button[i].resize(60,60)
            self.button[i].clicked.connect(self.swapButton)
            self.button[i].setAutoFillBackground(True)
            self.button[i].setStyleSheet("background-color:rgb(100,100,100); color:rgb(0,0,0)")
        self.button[self.blackBox].setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(0, 0, 0)")
        self.button[self.blackBox].clicked.disconnect()        
        self.show()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.callPuzzle()

   

    
    def isSwappable(self,x,y):
        a = self.coordinateArrX[self.blackBox]
        b = self.coordinateArrY[self.blackBox]
        if (x - a == 0 and abs(y - b) == 62):
            return True
        elif (y - b == 0 and abs(x - a) == 62):
            return True
        else:
            return False
    
    @pyqtSlot()
    def swapButton(self):
        
        buttonIndex = self.button.index(self.sender())
        x = self.coordinateArrX[buttonIndex]
        y = self.coordinateArrY[buttonIndex]
        if (self.isSwappable(x,y) == True):
            self.button[buttonIndex], self.button[self.blackBox] = self.button[self.blackBox], self.button[buttonIndex]
            self.coordinateArrX[buttonIndex], self.coordinateArrX[self.blackBox] = self.coordinateArrX[self.blackBox], self.coordinateArrX[buttonIndex]
            self.coordinateArrY[buttonIndex], self.coordinateArrY[self.blackBox] = self.coordinateArrY[self.blackBox], self.coordinateArrY[buttonIndex]
            self.arr[buttonIndex], self.arr[self.blackBox] = self.arr[self.blackBox], self.arr[buttonIndex]
            self.moves = self.moves + 1

        
        self.callPuzzle()
        
if __name__ == '__main__':
    
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    