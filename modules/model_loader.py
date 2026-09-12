import joblib
from pathlib import Path
import streamlit as st

@st.cache_resource
def load_artifact():
    """
    모델 아티팩트 로드 (model, calibrator, model_type, feature_names)

    ✅ pickle 호환 패치 포함:
    과거에 __main__.IsotonicCalibrator 등으로 저장된 경우에도
    Streamlit 실행(__main__=홈.py)에서 로드 가능하도록 주입.
    """

    import __main__
    from .calibrators import IsotonicCalibrator, PlattCalibrator, NoneCalibrator

    # 과거 artifact가 __main__.ClassName 으로 저장된 경우를 대비
    __main__.IsotonicCalibrator = IsotonicCalibrator
    __main__.PlattCalibrator = PlattCalibrator
    __main__.NoneCalibrator = NoneCalibrator

    # -----------------------------
    # 아티팩트 로드
    # -----------------------------
    artifact = joblib.load(
        Path("artifacts/model/v1.0.2_XGB_artifact.joblib")  # 🔥 반드시 v1.0.2
    )

    return (
        artifact["model"],
        artifact["calibrator"],
        artifact["model_type"],
        artifact["feature_names"],
    )
