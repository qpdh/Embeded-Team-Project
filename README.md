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
