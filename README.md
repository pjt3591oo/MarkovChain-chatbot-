# 심플 챗봇

해당 프로젝트는 마르코프 체인을 이용한 간단한 챗봇입니다.

# 프로젝트 구조

* botengine.py
* convert.py
* chatbot-data.json
* slack.py

---

* `convert.py`
 
 해당 파일은 카카오톡 대화내용을 이용하여 챗팅 훈련에 필요한 데이터로 만들어 줍니다.
 한 유저가 끊어서 채팅 한 경우 하나의 문장으로 만들어 줍니다.
 
 ```python
 kakao_file = 카카오톡 대화내용
```

파일명을 적을 땐 확장자 csv는 붇이지 않아도 됨. 파일명만 적어줄 것.

해당 파일을 실행하면 **`converted.txt`** 파일 생성

* `botengine.py`

메세지 생성 메인 프로그램

해당 파일을 직접 실행할 경우 convert.py로 생성한 converted.txt를 학습한다. 학습 된 경과는 chatbot-data.json에 저장된다.

`make_reply()`를 호출하면 새로운 문장을 만들어 낸다.

```python
from botengine import make_reply as mr

new_sentence = mr('안녕하세요')
```

문장을 생성하기 위해 넘긴 문장을 다시 chatbot-data.json에 적용한다. 지속적으로 학습을 한다.

* `chatbot-data.json`

학습된 결과를 저장한다.

botengine.py를 직접 실행, botengine을 import 하고 make_reply()를 호출할 때 chatbot-data.json을 업데이트.


* ` slack.py`

슬랙 봇 메인 프로그램

```python
slack_token = '슬랙토큰'
channel = '#채널명'
```

해당 슬랙 팀에 맞는 토큰과 채널을 넣어주면 됩니다.

> 디렉토리 정리하기 귀찮아서 그냥 다 때려밖음.