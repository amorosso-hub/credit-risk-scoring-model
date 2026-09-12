
# HCIS | Explainable Credit Risk Demo

Home Credit 공개 데이터를 활용하여 신용위험을 추정하고,
점수·등급·추가검토 대상을 설명 가능한 형태로 제시하는 Streamlit 포트폴리오 프로젝트입니다.

> 이 프로젝트는 교육 및 포트폴리오 목적의 데모입니다.
> 실제 대출 승인·거절 또는 금융 의사결정에 사용하지 않습니다.

## 주요 기능

- 고객별 부도확률(PD) 추정
- PD 기반 신용점수 및 등급 산출
- SHAP 기반 주요 리스크 요인 설명
- 추가검토 대상 분류
- 리스크 유형별 승인 전환 시뮬레이션
- 선택 기능: 생성형 AI 기반 심사 검토 설명 초안

## 프로젝트 구조

```text
.
├── app.py
├── config.py
├── pages/
├── modules/
├── utils/
├── assets/
├── artifacts/model/
│   └── v1.0.2_XGB_artifact.joblib
└── data/
    ├── demo_input.parquet
    └── reason_code_mapping.parquet
```
