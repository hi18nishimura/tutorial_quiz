import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="クイズアプリ", page_icon="❓")
st.title("🎉 クイズアプリ 🎉")

# 初期化
if "quiz" not in st.session_state:
    st.session_state.quiz = requests.get(f"{API_URL}/quiz").json()
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answers = []
    st.session_state.finished = False

# 回答送信処理
def submit_answer():
    idx = st.session_state.current
    q = st.session_state.quiz[idx]
    selected = st.session_state.sel
    resp = requests.post(
        f"{API_URL}/answer", json={"question_id": q["id"], "selected_index": selected}
    )
    res = resp.json()
    st.session_state.answers.append({
        "question": q["question"],
        "correct": res["correct"],
        "correct_option": res["correct_option"],
    })
    if res["correct"]:
        st.session_state.score += 1
    # 次へ or 終了判定
    if st.session_state.current + 1 < len(st.session_state.quiz):
        st.session_state.current += 1
    else:
        st.session_state.finished = True

# メインロジック
if not st.session_state.finished:
    idx = st.session_state.current
    q = st.session_state.quiz[idx]
    st.progress((idx + 1) / len(st.session_state.quiz))
    st.markdown(f"**問題 {idx+1} / {len(st.session_state.quiz)}**")
    st.write(q["question"])
    st.radio(
        "回答を選択してください",
        options=list(range(len(q["options"]))),
        format_func=lambda i: q["options"][i],
        key="sel",
    )
    st.button("次へ", on_click=submit_answer)
else:
    st.header("📊 結果発表")
    st.write(f"あなたのスコア: {st.session_state.score} / {len(st.session_state.quiz)}")
    for a in st.session_state.answers:
        symbol = "✅" if a["correct"] else "❌"
        st.write(f"{symbol} {a['question']}  正解: {a['correct_option']}")
    if st.button("リセット"):
        for key in ["quiz", "current", "score", "answers", "finished"]:
            st.session_state.pop(key, None)
        st.write("リセットしました。ページをリロードしてください。")