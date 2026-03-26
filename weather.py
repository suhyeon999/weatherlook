import requests
import os

# --- [API 키 입력] ---
# 날씨 키
WEATHER_API_KEY = '20e3de27ebbee9029f5db2f226929823' 

def get_weather_total_look(city):
    print(f"--- ⛅ '{city}' 실시간 날씨 기반 '오늘의 룩' 큐레이션 ---")
    
    try:
        # 1. 실시간 날씨 가져오기 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},kr&appid={WEATHER_API_KEY}&units=metric&lang=kr"
        res = requests.get(url, timeout=10)
        data = res.json()

        if res.status_code != 200:
            print(f"❌ 날씨 데이터 수집 실패")
            return

        temp = data['main']['temp']           
        feels_like = data['main']['feels_like'] 
        weather_desc = data['weather'][0]['description'] 

        print(f"✅ 날씨 데이터 수집 성공!")
        print(f"📍 현재 {city} 기온: {temp}°C (체감 {feels_like}°C)")
        print(f"☁️ 날씨 상태: {weather_desc}")
        print("-" * 65)

        # 2. 지능형 코디 추천 로직 (AI 에러 방지를 위한 자체 로직)
        print(f"🤖 AI가 현재 기온을 분석하여 최적의 코디를 선정합니다...")
        
        # 기온별 추천 데이터 
        if temp <= 4:
            look = "🧥 아우터: 롱패딩이나 두꺼운 코트\n👕 상의: 기모 맨투맨 + 히트텍\n👖 하의: 기모 슬랙스\n👟 신발: 따뜻한 운동화나 부츠\n🧣 소품: 목도리, 장갑 필수!"
        elif 5 <= temp <= 9:
            look = "🧥 아우터: 코트나 가죽 자켓\n👕 상의: 니트 또는 셔츠+조끼\n👖 하의: 청바지나 면바지\n👟 신발: 스니커즈\n🧣 소품: 얇은 머플러"
        elif 10 <= temp <= 16:
            look = "🧥 아우터: 자켓, 가디건 또는 야상\n👕 상의: 셔츠나 긴팔 티셔츠\n👖 하의: 슬랙스나 데님\n👟 신발: 로퍼나 스니커즈\n☂️ 소품: 일교차 대비용 가벼운 스카프"
        elif 17 <= temp <= 22:
            look = "👕 상의: 맨투맨이나 얇은 니트\n👖 하의: 면바지나 청바지\n👟 신발: 단화나 운동화"
        else:
            look = "👕 상의: 반팔 티셔츠나 얇은 셔츠\n👖 하의: 반바지나 얇은 면바지\n👟 신발: 샌들이나 슬립온"

        print("="*65)
        print(f"👗 [AI's Daily Total Look Recommendation] 👗\n")
        print(f"현재 기온은 {temp}도이며 '{weather_desc}' 상태이므로,\n다음과 같이 입는 것이 가장 적절합니다:\n")
        print(look)
        
        # 비가 올 경우 추가 멘트
        if '비' in weather_desc or '강수' in weather_desc:
            print("\n☔ 추가 알림: 현재 비 소식이 있으니 우산을 꼭 챙기세요!")
        
        print("="*65)

    except Exception as e:
        print(f"⚠️ 시스템 오류 발생: {e}")

if __name__ == "__main__":
    get_weather_total_look("Busan")

