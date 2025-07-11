from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Streamlit からのアクセスを許可
    allow_methods=["*"],
    allow_headers=["*"],
)

# クイズデータ
quiz_data: List[Dict] = [
    {"id": 1, "question": "日本の首都はどこですか？", "options": ["大阪", "東京", "京都", "名古屋"], "correct_index": 1},
    {"id": 2, "question": "地球上で最も大きな海洋はどれですか？", "options": ["大西洋", "インド洋", "太平洋", "北極海"], "correct_index": 2},
    {"id": 3, "question": "1年は何日ですか？", "options": ["364日", "365日", "366日", "367日"], "correct_index": 1},
    {"id": 4, "question": "富士山の標高は約何メートルですか？", "options": ["3,776m", "3,500m", "4,000m", "3,200m"], "correct_index": 0},
    {"id": 5, "question": "日本で最も長い川はどれですか？", "options": ["利根川", "信濃川", "石狩川", "北上川"], "correct_index": 1},
]

class QuizQuestion(BaseModel):
    id: int
    question: str
    options: List[str]

class AnswerIn(BaseModel):
    question_id: int
    selected_index: int

class AnswerOut(BaseModel):
    correct: bool
    correct_index: int
    correct_option: str

@app.get("/quiz", response_model=List[QuizQuestion])
def get_quiz():
    return [QuizQuestion(**q) for q in quiz_data]

@app.post("/answer", response_model=AnswerOut)
def post_answer(ans: AnswerIn):
    q = next((q for q in quiz_data if q["id"] == ans.question_id), None)
    if not q:
        return AnswerOut(correct=False, correct_index=-1, correct_option="")
    is_correct = ans.selected_index == q["correct_index"]
    return AnswerOut(
        correct=is_correct,
        correct_index=q["correct_index"],
        correct_option=q["options"][q["correct_index"]],
    )