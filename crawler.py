import requests
from bs4 import BeautifulSoup
import mysql.connector

# MySQL 연결 설정
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rlacksdn)7!",
    database="school_db"
)

cursor = db.cursor()

# 학교 웹사이트 URL
url = "https://www.kisy.or.kr/862707002"

def crawl_school_info():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 학교 행사 정보 크롤링
    events = soup.find_all('div', class_='event')

    # 데이터베이스에 저장
    cursor.execute("DELETE FROM school_info")
    for event in events:
        event_name = event.find('div', class_='title title-block').text.strip()
        event_date = event.find('small', class_='date')['title'].strip()
        cursor.execute("INSERT INTO school_info (event_name, event_date) VALUES (%s, %s)", (event_name, event_date))
    db.commit()

if __name__ == "__main__":
    crawl_school_info()
