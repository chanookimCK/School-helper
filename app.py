from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# MySQL 연결 설정
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rlacksdn)7!",
    database="school_db"
)

# DialoGPT 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)

# 데이터베이스에서 정보 검색 함수
def get_school_info():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT event_name, event_date FROM school_info")
    results = cursor.fetchall()
    return results

# 챗봇 응답 생성 함수
def get_chatbot_response(user_input, school_info):
    context = "Here is some recent information about school events:\n"
    for info in school_info:
        context += f"- {info['event_name']} on {info['event_date']}\n"
    
    prompt = context + "\nUser: " + user_input + "\nAI:"
    response = pipe(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']

# API 엔드포인트: 사용자의 질문에 대한 응답 생성
@app.route('/query', methods=['POST'])
def query():
    user_input = request.json.get('input')
    school_info = get_school_info()
    bot_response = get_chatbot_response(user_input, school_info)
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
