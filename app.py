# ----------------------------
# 라이브러리 호출
# ----------------------------

import streamlit as st 
# 실행 방법: python -m streamlit run 홈.py

# ----------------------------
# 페이지 생성
# ----------------------------

st.set_page_config(
    page_title="HCIS 신용평가 시스템",
    layout="wide"
)

# ----------------------------
# 상단 여백 조정
# ----------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 2rem !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# 타이틀
# ----------------------------
with st.container():
    st.title("🏦 HCIS 신용평가 시스템")
    st.subheader("시스템 설명")
    st.caption("본 시스템은 Home Credit 데이터를 기반으로 대출 심사 프로세스를 운영 관점에서 재구성한 신용평가 데모입니다. \n (실제 대출 의사결정에 사용하지 않는 시뮬레이션)")

    st.markdown("### 🧭 대출 심사 프로세스")

    # 대출 심사 프로세스 5분할
    cols = st.columns(5)

    process_steps = [
        ("📥", "대출 심사 프로세스", "고객 정보 기반\n심사 흐름 시작"),
        ("📊", "PD 산출", "부도확률\n(PD) 계산"),
        ("🔢", "점수 변환", "PD → Score\n정규화"),
        ("🏷️", "등급 분류", "Score 기반\nRisk Grade"),
        ("🤖", "심사 검토 지원", "AI 기반 검토 설명 초안\n행동 추천")
    ]

    for col, (icon, title, desc) in zip(cols, process_steps):
        with col:
            st.markdown(
                f"""
                <div style="
                    border:1px solid #e6e6e6;
                    border-radius:12px;
                    padding:16px;
                    height:180px;
                    text-align:center;
                    background-color:#fafafa;
                    color:#111;
                ">
                    <div style="font-size:28px;">{icon}</div>
                    <div style="font-weight:600; margin-top:8px;">{title}</div>
                    <div style="font-size:12px; color:#666; margin-top:6px; white-space:pre-line;">
                        {desc}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

# ----------------------------
# 활용 가이드
# ----------------------------

with st.container():
    st.subheader("📌 활용 가이드")

    # 활용 가이드 3분할
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div style="
            padding:18px;
            border-radius:12px;
            background:#f4f6f8;
            height:240px;
            color:#111;
        ">
            <h4>📘 홈</h4>
            <p style="font-size:14px; line-height:1.6;">
                시스템 설명 및<br>
                대출 심사 프로세스 · 대시보드 활용가이드 설명
                • 운영 기준<br>
                • 점수–등급–결정 흐름
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="
            padding:18px;
            border-radius:12px;
            background:#f4f6f8;
            height:240px;
            color:#111;
        ">
            <h4>👤 개요</h4>
            <p style="font-size:14px; line-height:1.6;">
                시스템 구조 및<br>
                신용평가 심사 로직 설명
            </p>
            <hr>
            <p style="font-size:12px; color:#555;">
                • 고객 문의 응대<br>
                • 결과 설명용 출력
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div style="
            padding:18px;
            border-radius:12px;
            background:#f4f6f8;
            height:240px;
            color:#111;
        ">
            <h4>🧑‍💼 대출 심사</h4>
            <p style="font-size:14px; line-height:1.6;">
                심사 판단 및<br>
                내부 보고 활용 화면
            </p>
            <hr>
            <p style="font-size:12px; color:#555;">
                • 상세 Feature<br>
                • 내부 분석 · 리스크 판단
            </p>
        </div>
        """, unsafe_allow_html=True)