https://www.acmicpc.net/problem/9935

#### 파이썬은 리스트와 리스트 비교시 내용물이 같은지 확인해줌
#### 예를 들어 list_a == list_b 내용물이 같은지
#### id(list_a) == id(list_b) 주소가 같은지

#### 자바의 경우 '==' 기호는 메모리 주소 비교이기 때문에 값 비교를 위해서 ArrayList 선언시 .equals() 동등성 확인
#### 자바는 특별하게 int[] 인경우 equals()도 주소비교를 하기 때문에 Arrays.equals() 함수 사용