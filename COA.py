
# 1️ Lookup tables 


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


# 2️ Weights (exactly as Excel)


WEIGHTS = {
    "bounce_cheques": 0.20,
    "ongoing_relationship": 0.15,
    "delay_installments": 0.20,
    "delinquency_history": 0.20,
    "write_off": 0.10,
    "fraud_litigation": 0.15
}


# 3️ COA calculation engine 


def calculate_coa_score(inputs):
    total = 0

    total += BOUNCE_CHEQUES_SCORE[inputs["bounce_cheques"]] * WEIGHTS["bounce_cheques"]
    total += ONGOING_RELATIONSHIP_SCORE[inputs["ongoing_relationship"]] * WEIGHTS["ongoing_relationship"]
    total += DELAY_INSTALLMENTS_SCORE[inputs["delay_installments"]] * WEIGHTS["delay_installments"]
    total += DELINQUENCY_HISTORY_SCORE[inputs["delinquency_history"]] * WEIGHTS["delinquency_history"]
    total += WRITE_OFF_SCORE[inputs["write_off"]] * WEIGHTS["write_off"]
    total += FRAUD_LITIGATION_SCORE[inputs["fraud_litigation"]] * WEIGHTS["fraud_litigation"]

    return round(total)


# 4️ Qualitative Input (EXCEL DROPDOWN 1-5)


if __name__ == "__main__":

    excel_like_inputs = {
        "bounce_cheques": 2,
        "ongoing_relationship": 1,
        "delay_installments": 2,
        "delinquency_history": 1,
        "write_off": 2,
        "fraud_litigation": 1
    }

    coa_score = calculate_coa_score(excel_like_inputs)
    print("CONDUCT OF ACCOUNT SCORE:", coa_score)
