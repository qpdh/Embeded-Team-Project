# 자판기

- 클라우드 DB 사용 (AWS 프리티어 RDS)
- 터치스크린 -> 스케치 할 때

## python/VendingMachine
```
main.py - 메인으로 실행
manager_mode.py - 메인에서 매니저모드 선택 시 다이얼로그 실행
dialog_deposit.py - 메인에서 입금모드 선택 시 다이얼로그 실행
```

## python/VendingMachine/IO_Modules
```
dot_write.py - dot matrix 쓰기 모듈
push_switch_read.py - push switch 읽기 모듈
fnt_write.py - fnd 쓰기 모듈
led_write.py - led 쓰기 모듈
dip_switch_read.py - dip switch 읽기 모듈
step_motor_write.py - step_motor 쓰기 모듈
text_lcd_write.py - text lcd 쓰기 모듈
all.py - 위의 모든 모듈을 불러오는 모듈
```

## python/VendingMachine/capture
```
매니저 모드 선택 시 사진 촬영을 하며, 촬영된 사진이 보관됨
```

## python/VendingMachine/ui
```
각 main, dialoG_deposit, manager_mod 의 ui파일이 존재
디자인 작업은 ui로 하며 이 ui를 불러와 이벤트 맵핑을 하여 동작을 함
```

## python/VendingMachine/drink_images
```
음료 이미지 저장
```

## 김동현
임베디드 시스템을 처음 배워보면서 Low level IO를 공부할 수 있는 계기가 되었다. 
캐릭터 디바이스 입출력을 함으로써 바이트 단위로 데이터를 인코딩하고 전송하고 디코딩하여 사용자에게 제공하는 것을 공부하면서
추후 소켓 프로그래밍에서의 인코딩, 디코딩 등 다른곳에 데이터 송수신에서 자주 쓸 수 있다고 생각했다.
또한 쓰레드를 이용함으로써 프로그램의 동작 구조를 이해하고, 좀 더 원활하게 단일 쓰레드, 단일 프로세스가 아닌 멀티 쓰레드, 멀티 프로세스로 확장하여 프로그래밍 할 수 있는 계기가 되었다.
또한 클라우드 DB를 사용하여 데이터를 송수신하는 작업에 대한 이해가 증가했다.
Qt GUI 프로그래밍을 하면서 내가 디자인한 GUI가 실제로 응용프로그램에 보여지는 것을 보고 추후에는 이를 이용하여 좀 더 견고한 프로그램을 만들고 싶다는 생각이 들었다.

- MQTT : 구매 시  
-> 임베디드 강의실 우분투에 전달  
(ex: 00제품이 00개 판매되었습니다. 남은 재고 : 00개)

- Qt + LED
  - 제품의 종류 8개 2*4
  - 선택된 제품
- Qt + FND
  - 재고 출력
- Qt + Dot 
  - 구매할 수량
- Qt + Text LCD
  - 제품, 가격 출력
- Qt + DIP SW
  - Passwd : 관리자모드 -> 재고 추가기능
- Qt + PUSH SW
  - 상하좌우 (1,3,5,7) 
    - 제품 선택
  - 구매 버튼 (4)
  - 구매할 수량(0,2)
    - 0 : 감소
    - 2 : 증가
  - 잔돈 반환 (6)
  - 금액 추가 (8)
- Qt + Step Motor
  - 관리자모드에서만 돌아감
