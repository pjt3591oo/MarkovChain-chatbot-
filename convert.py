import pandas as pd

kakao_file = 'kakao_text'

df = pd.read_csv(kakao_file+'.csv', encoding="utf-8")

Date = 'Date'
User = 'User'
Message = 'Message'

df = df[df[Message] != '(이모티콘) ']

pre_user = ''

messages = []
user_message = ''

for index, user in enumerate(df[User]):

    try:
        if pre_user !=user:
            pre_user = user
            messages.append(user_message)
            user_message = ''
        user_message += df[Message][index]
    except:
        pass

fp = open('converted.txt', 'a', encoding="utf-8")

for message in messages:
    if message:
        fp.write(message.replace(':', '').replace(',', '') + '\n')