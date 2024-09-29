from textblob import TextBlob
from googletrans import Translator

# Google 번역 API 초기화
translator = Translator()

# 감정 분석 함수
def analyze_sentiment(text):
    
    # 한국어 문장을 영어로 번역
    translation = translator.translate(text, src='ko', dest='en')
    translated_text = translation.text

    # 번역된 문장으로 감정 분석 수행
    blob = TextBlob(translated_text)
    sentiment = blob.sentiment.polarity

    # 감정 점수에 따라 결과 판단
    if sentiment > 0:
        return "긍정적"
    elif sentiment == 0:
        return "중립적"
    else:
        return "부정적"

# 사용자 문장 입력
text = input("분석할 한국어 문장을 입력하세요: ")

# 감정 분석 결과 출력
result = analyze_sentiment(text)
print(f"감정 분석 결과: {result}")