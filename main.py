from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# ================================
# 1️⃣ Lookup tables
# ================================

BOUNCE_CHEQUES_SCORE = {
    1: 600,
    2: 400,
    3: 200,
    4: 0
}

ONGOING_RELATIONSHIP_SCORE = {
    1: 600,
    2: 400,
    3: 200,
    4: 0
}

DELAY_INSTALLMENTS_SCORE = {
    1: 600,
    2: 400,
    3: 200,
    4: 0
}

DELINQUENCY_HISTORY_SCORE = {
    1: 600,
    2: 400,
    3: 200,
    4: 0
}

WRITE_OFF_SCORE = {
    1: 600,
    2: 0
}

FRAUD_LITIGATION_SCORE = {
    1: 600,
    2: 0
}


# ================================
# 2️⃣ Weights
# ================================

WEIGHTS = {
    "bounce_cheques": 0.20,
    "ongoing_relationship": 0.15,
    "delay_installments": 0.20,
    "delinquency_history": 0.20,
    "write_off": 0.10,
    "fraud_litigation": 0.15
}


# ================================
# 3️⃣ COA calculation engine
# ================================

def calculate_coa_score(inputs):
    total = 0

    total += BOUNCE_CHEQUES_SCORE[inputs.bounce_cheques] * WEIGHTS["bounce_cheques"]
    total += ONGOING_RELATIONSHIP_SCORE[inputs.ongoing_relationship] * WEIGHTS["ongoing_relationship"]
    total += DELAY_INSTALLMENTS_SCORE[inputs.delay_installments] * WEIGHTS["delay_installments"]
    total += DELINQUENCY_HISTORY_SCORE[inputs.delinquency_history] * WEIGHTS["delinquency_history"]
    total += WRITE_OFF_SCORE[inputs.write_off] * WEIGHTS["write_off"]
    total += FRAUD_LITIGATION_SCORE[inputs.fraud_litigation] * WEIGHTS["fraud_litigation"]

    return round(total)


# ================================
# 4️⃣ FastAPI input schema
# ================================

class COAInput(BaseModel):
    bounce_cheques: int = Field(..., ge=1, le=4)
    ongoing_relationship: int = Field(..., ge=1, le=4)
    delay_installments: int = Field(..., ge=1, le=4)
    delinquency_history: int = Field(..., ge=1, le=4)
    write_off: int = Field(..., ge=1, le=2)
    fraud_litigation: int = Field(..., ge=1, le=2)


class COAOutput(BaseModel):
    coa_score: int


# ================================
# 5️⃣ FastAPI app
# ================================

app = FastAPI(
    title="COA Scoring API",
    description="Conduct of Account scoring engine",
    version="1.0.0"
)


@app.post("/calculate-coa", response_model=COAOutput)
def calculate_coa(data: COAInput):
    try:
        score = calculate_coa_score(data)
        return {"coa_score": score}
    except KeyError:
        raise HTTPException(status_code=400, detail="Invalid input value")
