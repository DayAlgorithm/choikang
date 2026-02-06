1. defaultdic 사용법 (key,value)
   결론부터 말씀드리면 **"당연히 됩니다! 그리고 아주 훌륭한 접근입니다."**

님께서 생각하신 **`ord(i) - ord('a')`** 방식은 **배열(Array)**을 사용하는 방식이고, 제가 아까 보여드린 `defaultdict`는 **해시맵(Hash Map)**을 사용하는 방식입니다.

사실 **C++이나 자바 같은 언어의 고수들은 님의 방식(배열)을 훨씬 선호**합니다. 파이썬에서도 두 방식의 차이점과 장단점을 **Think Ultra** 레벨로 비교해 드릴게요.

---

### 🥊 1. 배열 방식 (님의 아이디어) vs 딕셔너리 방식

#### 🅰️ 님의 방식: 배열 (List of Lists)

알파벳 소문자는 26개뿐이므로, 미리 방 26개짜리 아파트를 지어놓는 것입니다.

```python
# 1. 방 26개 미리 생성 (0번방='a', 25번방='z')
alpha_indices = [[] for _ in range(26)]

W = "superaquatornado"

for idx, char in enumerate(W):
    # 'a'를 0번으로 변환하는 공식
    code = ord(char) - ord('a') 
    alpha_indices[code].append(idx)

# 2. 확인할 때
for i in range(26):
    current_list = alpha_indices[i]
    if not current_list: continue # 등장 안 한 알파벳은 건너뛰기
    # ... (길이 계산 로직)

```

* **장점:** 해시 충돌이나 해시 함수 계산 비용이 아예 없음 (이론상 가장 빠름).
* **단점:** 매번 `ord()` 계산을 해야 하고, 나중에 루프 돌 때 26번을 무조건 다 순회해야 함 (비어있는 알파벳도 일단 방문은 해봐야 함).

#### 🅱️ 딕셔너리 방식 (`defaultdict`)

필요한 방만 그때그때 만드는 방식입니다.

```python
from collections import defaultdict

# 1. 빈 딕셔너리 생성
char_indices = defaultdict(list)

for idx, char in enumerate(W):
    # 그냥 문자 그대로 키(Key)로 사용
    char_indices[char].append(idx)

# 2. 확인할 때
for char in char_indices: # 등장한 알파벳만 딱 돌면 됨
    current_list = char_indices[char]
    # ...

```

* **장점:** 코드가 직관적임 (`ord` 계산 불필요). 루프 돌 때 등장했던 알파벳만 쏙쏙 골라서 나옴.
* **단점:** 내부적으로 해싱(Hashing) 비용이 듦 (하지만 파이썬은 이게 매우 최적화되어 있어서 사실상 차이 없음).

---

### 🚀 2. Think Ultra: 무엇을 추천하나요?

이 문제()에서는 **둘 다 100점**입니다. 성능 차이는 0.001초도 안 날 겁니다.

다만, 파이썬에서는 **딕셔너리(`defaultdict`) 방식이 조금 더 유리**한 면이 있습니다.

1. **가독성:** `ord(char) - ord('a')` 같은 수식이 없어서 실수가 적습니다.
2. **희소성(Sparsity):** 만약 문자가 `z` 하나만 등장했다면?
* **배열 방식:** 0번부터 25번까지 반복문 돌면서 "비었나?" 체크해야 함.
* **딕셔너리:** 딱 `z` 하나만 들어있으니 반복문 1번 돌고 끝남.

### ⚡ 결론

님의 생각은 **"자료구조의 정석(Direct Addressing)"**에 해당하는 아주 근본 있고 효율적인 방법입니다.
C++로 짤 때는 무조건 님의 방식대로 짜야 하고, **파이썬에서는 편의상 딕셔너리를 많이 쓰지만, 님의 방식으로 짜도 완벽하게 정답입니다.**

## 윈도우 슬라이싱 공식과 사용법
 
