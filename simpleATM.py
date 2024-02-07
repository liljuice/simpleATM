class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

class Card:
    def __init__(self, cardNumber, PIN):
        self.cardNumber = cardNumber
        self.pin = PIN
        self.accounts = []
    
    # 카드에 계좌 연결 (테스트용)
    def addAccount(self, accountNumber):
        self.accounts.append(accountNumber)
    
    # 카드에 연결된 계좌
    def getAccount(self):
        return self.accounts

class Bank:
    def __init__(self):
        self.accounts = {}
        self.cards = {}
    
    # (테스트용) 계좌 정보 등록
    def registerAccount(self, accountNumber, balance):
        account = Account(accountNumber, balance)
        self.accounts[accountNumber] = account
        
    # (테스트용) 카드 정보 등록
    def registerCard(self, cardNumber, PIN):
        card = Card(cardNumber, PIN)
        self.cards[cardNumber] = card
        
    # (테스트용) 카드에 계좌 연결
    def addAccToCard(self, cardNumber, accountNumber):
        card = self.cards.get(cardNumber)
        if card:
            card.addAccount(accountNumber)
        else:
            print("no card")
        
    # 카드 넘버에 대한 PIN 번호가 일치하는지 확인
    def checkPIN(self, cardNumber, inputPIN):
        card = self.cards.get(cardNumber)
        if card:
            return card.pin == inputPIN
        else:
            return False

    # 카드에 연결된 계좌 확인
    def getAccount(self, cardNumber):
        card = self.cards.get(cardNumber)
        if card:
            return card.getAccount()
        else:
            return None
        
    # 잔고
    def balance(self, accountNumber):
        account = self.accounts.get(accountNumber)
        if account:
            return account.balance
        else:
            print("해당 계좌가 존재하지 않습니다.")
            return None
    
    # 예금(잔고 추가)
    def deposit(self, accountNumber, amount):
        account = self.accounts.get(accountNumber)
        if account:
            account.balance += amount
            print("예금이 성공적으로 처리되었습니다.")
        else:
            print("해당 계좌가 존재하지 않습니다.")
    
    # 출금(잔고 감소)
    def withdraw(self, accountNumber, amount):
        account = self.accounts.get(accountNumber)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                print("출금이 성공적으로 처리되었습니다.")
                return True
            else:
                print("잔고가 부족합니다.")
                return False
        else:
            print("해당 계좌가 존재하지 않습니다.")
            return False
    
class Controller:
    def __init__(self, bank):
        self.bank = bank
        self.accountNumber = None
        self.cardNumber = None
        self.certified = False
    
    # 고객의 카드 번호를 저장
    def insertCard(self, cardNumber):
        self.cardNumber = cardNumber
        
    def selectAccount(self, accountNumber):
        self.accountNumber = accountNumber
        
    # 고객의 PIN 번호를 입력받아 올바른지 확인
    def enterPIN(self, PIN):
        if self.bank.checkPIN(self.cardNumber, PIN):
            self.certified = True
            return True
        else:
            self.certified = False
            return False

    
    def checkBalance(self):
        balance = self.bank.balance(self.accountNumber)
        return balance
    
    def deposit(self, amount):
        self.bank.deposit(self.accountNumber, amount)
    
    def withdraw(self, amount):
        isWork = self.bank.withdraw(self.accountNumber, amount)
        return isWork
        
    
class Main:
    def run(self):
        bank = Bank()
        controller = Controller(bank)
        
        # 테스트를 위함
        bank.registerAccount('12345678', 50000)
        bank.registerAccount('20240207', 0)
        bank.registerAccount('11111111', 300000)
        bank.registerCard('1234', '5678')
        bank.registerCard('2024', '0207')
        bank.addAccToCard('1234', '12345678')
        bank.addAccToCard('2024', '20240207')
        bank.addAccToCard('2024', '11111111')

        while True:
            print("======= Simple ATM Controller =======")
            print("카드를 넣어주세요. (카드 번호를 입력하세요.)")
            print("종료하시려면, 0을 입력해주세요.")
            cmdFirst = input()
            if cmdFirst == '0':
                break
            controller.insertCard(cmdFirst)
            print("PIN 번호를 입력하세요.")
            
            if controller.enterPIN(input().rstrip()):
                print("확인되었습니다.")
                
                print("다음은 연결되어 있는 계좌입니다.")
                acc = bank.getAccount(cmdFirst)

                for i in range(len(acc)):
                    print("계좌", i+1, "번 : ", acc[i])
                    
                n = int(input("이용하실 계좌의 순번을 입력하세요: "))
                if n < 1 or n > len(acc) + 1:
                    print("올바르지 않은 입력입니다.")
                    break
                else:
                    controller.selectAccount(acc[n-1])
                    
                while True:
                    print("원하시는 기능의 번호를 입력하세요.")
                    print("1. 예금")
                    print("2. 출금")
                    print("3. 잔고 확인")
                    print("0. 종료")
                    command = input("입력: ")
                    
                    if command == '1':
                        amt = int(input("입금할 금액: "))
                        controller.deposit(amt)
                        print("입금되었습니다.\n")
                    elif command == '2':
                        amt = int(input("출금할 금액: "))
                        isWork = controller.withdraw(amt)
                        if isWork:
                            print("출금되었습니다.\n")
                        else:
                            print("출금에 실패했습니다.\n")
                    elif command == '3':
                        b = controller.checkBalance()
                        print("고객님의 계좌 잔고는", b, "달러입니다.\n")
                    elif command == '0':
                        break
            else:
                print("카드와 PIN 번호가 일치하지 않습니다. 다시 시도해주세요.\n")
        

if __name__ == "__main__":
    main = Main()
    main.run()
