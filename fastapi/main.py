from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import base64

plt.rcParams['font.family'] = 'AppleGothic'

app = FastAPI()

def data():
    # 학부모가 선호하는 자녀가 가장 잘하면 좋겠는 과목과 자녀의 과목 선호도
    subjects = ["국어", "수학", "영어", "미술", "체육"]
    parents_like = [36.6, 36.6, 23.3, 1.6, 0.3]
    children_like = [14.0, 31.4, 4.4, 31.6, 13.8]

    df = pd.DataFrame({
        "과목": subjects,
        "학부모 선호도 (%)": parents_like,
        "자녀 선호도 (%)": children_like
    })
    return df

# 그래프 생성
def create_plot():
    df = data()

    # x축 위치 생성
    x = np.arange(len(df["과목"]))
    width = 0.35  # 막대 폭
    fig, ax = plt.subplots(figsize=(10, 6))

    # 막대 그래프
    ax.bar(x - width/2, df["학부모 선호도 (%)"], width, label="학부모 선호도")
    ax.bar(x + width/2, df["자녀 선호도 (%)"], width, label="자녀 선호도")

    ax.set_xlabel("과목")
    ax.set_ylabel("선호도 (%)")
    ax.set_title("학부모와 자녀의 과목 선호도 비교")
    ax.set_xticks(x)
    ax.set_xticklabels(df["과목"])
    ax.legend()

    # 그래프 이미지 저장
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=100, bbox_inches="tight")
    buf.seek(0)
    encoded_img = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    return encoded_img

@app.get("/", response_class=HTMLResponse)
async def read_root():
        # 그래프 생성
        img_data = create_plot()

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>선호도 그래프</title>
        </head>
        <body>
            <h1>학부모와 자녀의 과목 선호도</h1>
            <img src="data:image/png;base64,{img_data}" alt="그래프">
        </body>
        </html>
        """
        return html_content
