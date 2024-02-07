# Simple ATM Controller

### Introduction
- Account Class   
: 계좌 번호와 잔고

- Card Class   
: 카드 번호와 PIN 번호, 연결된 계좌 번호   

- Bank Class   
: 계좌와 카드를 등록하고(테스트를 위해) 관리하는 기능   
카드의 PIN 번호를 확인하여 인증하고, 카드에 연결된 계좌를 보여주는 기능   

- Controller Class   
: 고객이 카드를 삽입하고, PIN 번호를 입력하여 인증하고, 계좌를 선택하고, 예금 및 출금 기능을 수행   
카드의 PIN 번호를 알아야 계좌 정보를 알 수 있으며, 그 계좌의 순번을 입력해서 계좌에 접근하므로 계좌 번호만 안다고 예금,출금을 수행할 수 없음   

- Main Class   
: 은행과 컨트롤러를 생성, 테스트용 계좌와 카드를 등록   
사용자가 정보를 입력하는 객체로, Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw 의 Flow를 CLI로 사용자가 파악할 수 있도록 함.


### Instructions
---
Requirements : Python 3

1) 리포지토리 복사하기
```
git clone https://github.com/liljuice/simpleATM.git
```
2) Clone된 로컬 디렉토리로 이동 및 실행하기
```
cd simpleATM
simpleATM.py
```
### Test Cases
---
다음 테스트 케이스가 입력되어 있습니다.

|Account Number|Balance|
|------|---|
|12345678|$50000|
|20240207|$0|
|11111111|$300000|

|Card Number|PIN Number|Linked Accounts List|
|------|---|-----|
|1234|5678|12345678|
|2024|0207|20240207, 11111111|

### ETC
---
ATM 컨트롤러의 Cash bin의 잔고와 같은 부분은 고려하지 않았습니다.   


