from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import os


workingDirectory = os.path.dirname(os.path.abspath(__file__))
settingWindow = uic.loadUiType(os.path.join(workingDirectory, 'vendingsetting.ui'))[0]
mainUi = uic.loadUiType(os.path.join(workingDirectory, 'vending.ui'))[0]

drinkList = ['아이시스A', '아이시스B', '아이시스C', '레몬워터A', '레몬워터B', '옥수수수염차A', '옥수수수염차B', '콘트라베이스', '트레비A', '트레비B',
             '밀키스', '펩시', '핫식스', '칠성사이다', '코코리치A', '코코리치B', '립톤복숭아', '트로피카나사과맛A', '트로피카나사과맛B', '트로피카나포도맛',
             '가나초코A', '가나초코B', '레쓰비A', '레쓰비B', '칸타타', '레쓰비카페타임', '게토레이A', '게토레이B', '코코포도', '잔치집식혜']

moneyList = [700, 700, 700, 1600, 1600, 1400, 1400, 2100, 1100, 1100,
             900, 900, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100,
             700, 700, 700, 700, 1100, 1100, 900, 900, 900, 900]

drinks = dict()
money = 0
sellingDrink = False



class second(QDialog, QWidget, settingWindow):
    def __init__(self):
        super(second, self).__init__()
        self.setupUi(self)

        self.editButton.clicked.connect(self.editDrink)
        self.showDrink()
        self.show()
    
    def showDrink(self):
        self.currentDrink.setText("")
        for i in range(len(drinkList)):
            self.currentDrink.append('id : ' + str(i) + '||' + drinkList[i] + ' : ' + str(drinks[drinkList[i]]) + '잔')

    def editDrink(self):
        global drinks, drinkList
        try:
            selectedDrink = int(self.idEdit.toPlainText())
            if self.adminCode.toPlainText() == "admin":
                drinks[drinkList[selectedDrink]] = int(self.amountEdit.toPlainText())
                QMessageBox.about(self,'정보',f'{drinkList[selectedDrink]}의 잔 수가 수정되었습니다.')
            else: 
                QMessageBox.about(self,'정보','관리자 코드가 올바르지 않습니다.')
        except ValueError:
            QMessageBox.about(self, '오류', '잔 수나 아이디에는 오직 정수만 들어갈 수 있습니다.')
        except IndexError:
            QMessageBox.about(self, '오류', 'id의 값이 벗어났습니다.')
        self.showDrink()
    

class mainWindow(QMainWindow, mainUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for i in range(len(drinkList)):
            drinks[drinkList[i]] = 20
        
        self.adminButton.clicked.connect(self.admin_window)
        self.smallMoney.clicked.connect(lambda : self.inputMoney(100))
        self.medMoney.clicked.connect(lambda : self.inputMoney(500))
        self.bigMoney.clicked.connect(lambda : self.inputMoney(1000))
        self.releaseButton.clicked.connect(lambda : self.releaseMoney())

        
        self.drinkButton0.clicked.connect(lambda : self.buyDrink(0))
        self.drinkButton1.clicked.connect(lambda : self.buyDrink(1))
        self.drinkButton2.clicked.connect(lambda : self.buyDrink(2))
        self.drinkButton3.clicked.connect(lambda : self.buyDrink(3))
        self.drinkButton4.clicked.connect(lambda : self.buyDrink(4))
        self.drinkButton5.clicked.connect(lambda : self.buyDrink(5))
        self.drinkButton6.clicked.connect(lambda : self.buyDrink(6))
        self.drinkButton7.clicked.connect(lambda : self.buyDrink(7))
        self.drinkButton8.clicked.connect(lambda : self.buyDrink(8))
        self.drinkButton9.clicked.connect(lambda : self.buyDrink(9))
        self.drinkButton10.clicked.connect(lambda : self.buyDrink(10))
        self.drinkButton11.clicked.connect(lambda : self.buyDrink(11))
        self.drinkButton12.clicked.connect(lambda : self.buyDrink(12))
        self.drinkButton13.clicked.connect(lambda : self.buyDrink(13))
        self.drinkButton14.clicked.connect(lambda : self.buyDrink(14))
        self.drinkButton15.clicked.connect(lambda : self.buyDrink(15))
        self.drinkButton16.clicked.connect(lambda : self.buyDrink(16))
        self.drinkButton17.clicked.connect(lambda : self.buyDrink(17))
        self.drinkButton18.clicked.connect(lambda : self.buyDrink(18))
        self.drinkButton19.clicked.connect(lambda : self.buyDrink(19))
        self.drinkButton20.clicked.connect(lambda : self.buyDrink(20))
        self.drinkButton21.clicked.connect(lambda : self.buyDrink(21))
        self.drinkButton22.clicked.connect(lambda : self.buyDrink(22))
        self.drinkButton23.clicked.connect(lambda : self.buyDrink(23))
        self.drinkButton24.clicked.connect(lambda : self.buyDrink(24))
        self.drinkButton25.clicked.connect(lambda : self.buyDrink(25))
        self.drinkButton26.clicked.connect(lambda : self.buyDrink(26))
        self.drinkButton27.clicked.connect(lambda : self.buyDrink(27))
        self.drinkButton28.clicked.connect(lambda : self.buyDrink(28))
        self.drinkButton29.clicked.connect(lambda : self.buyDrink(29))

            
        self.initialize()
        self.show()

    def initialize(self):
        self.moneyDisplay.display(12345)
        for i in range(30):
            drinkLabel = drinkList[i] + "\n" + str(moneyList[i]) + "원" # 리스트의 값을 자판기 창의 각 라벨에 대입
            exec(f"self.drinkLabel{i}.setText(drinkLabel)")
            exec(f"self.drinkButton{i}.setText('----')")

        self.textEdit.setText("판매중") # 판매중 글자 띄우기
        self.releaseButton.setEnabled(False)

    def inputMoney(self, insert):
        global money
        money += insert
        self.textEdit.append(str(insert) + "원 넣었습니다.")
        self.gotMoney()
        self.releaseButton.setEnabled(True)

    def gotMoney(self):
        global money
        self.moneyDisplay.display(money)  
        self.compareMoney()

    def compareMoney(self):
        global sellingDrink
        global money
        sellingDrink = True
        for i in range(30):
            if drinks[drinkList[i]] == 0:
                exec(f"self.drinkButton{i}.setText('품절됨')")
            elif money >= moneyList[i]:
                exec(f"self.drinkButton{i}.setText('구매 (◉)')")
            elif money < moneyList[i]:
                exec(f"self.drinkButton{i}.setText('구매 (불가)')")
            
    

    def buyDrink(self, drink):
        global money
        global sellingDrink
        print(drinks)
        if sellingDrink == False:
            pass
        else:
            if money >= moneyList[drink]:
                if drinks[drinkList[drink]] >= 1:
                    money -= moneyList[drink]
                    self.moneyDisplay.display(money)
                    drinks[drinkList[drink]] -= 1

                    self.textEdit.append(f"{drinkList[drink]}를 구매하였습니다.")
                    self.textEdit.append(f"남은 {drinkList[drink]} 수 : {drinks[drinkList[drink]]}잔")
                    self.compareMoney()
                else:
                    self.textEdit.append("품절되었습니다.")
            else:
                self.textEdit.append("잔액이 부족합니다.")
            if money == 0:
                self.getBack()
    

    def getBack(self):
        global sellingDrink
        self.textEdit.append("이용해 주셔서 감사합니다.")
        self.moneyDisplay.display(12345)
        self.releaseButton.setEnabled(False)
        for i in range(30):
            exec(f"self.drinkButton{i}.setText('----')")
        sellingDrink = False
        
    
    def releaseMoney(self):
        global money
        a = money // 1000
        b = (money - a * 1000) // 500
        c = (money - a * 1000 - b * 500) // 100
        self.textEdit.append(f"1000원 {a}장, 500원 {b}개, 100원 {c}개 반환되었습니다.")
        money = 0
        self.getBack()


    def admin_window(self):
        self.settings = second()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = mainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
