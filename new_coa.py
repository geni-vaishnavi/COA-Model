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
# 2️⃣ Weights (same as Excel)
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

    total += BOUNCE_CHEQUES_SCORE[inputs["bounce_cheques"]] * WEIGHTS["bounce_cheques"]
    total += ONGOING_RELATIONSHIP_SCORE[inputs["ongoing_relationship"]] * WEIGHTS["ongoing_relationship"]
    total += DELAY_INSTALLMENTS_SCORE[inputs["delay_installments"]] * WEIGHTS["delay_installments"]
    total += DELINQUENCY_HISTORY_SCORE[inputs["delinquency_history"]] * WEIGHTS["delinquency_history"]
    total += WRITE_OFF_SCORE[inputs["write_off"]] * WEIGHTS["write_off"]
    total += FRAUD_LITIGATION_SCORE[inputs["fraud_litigation"]] * WEIGHTS["fraud_litigation"]

    return round(total)


# ================================
# 4️⃣ Terminal input helper
# ================================

def get_int_input(prompt, allowed_values):
    while True:
        try:
            value = int(input(prompt))
            if value in allowed_values:
                return value
            else:
                print(f"❌ Invalid input. Allowed values: {allowed_values}")
        except ValueError:
            print("❌ Please enter a valid integer.")


# ================================
# 5️⃣ Main program (Terminal-based)
# ================================

if __name__ == "__main__":

    print("\n==============================")
    print(" CONDUCT OF ACCOUNT (COA) SCORE ")
    print("==============================\n")

    user_inputs = {
        "bounce_cheques": get_int_input(
            "Enter bounce_cheques (1-4): ", [1, 2, 3, 4]
        ),
        "ongoing_relationship": get_int_input(
            "Enter ongoing_relationship (1-4): ", [1, 2, 3, 4]
        ),
        "delay_installments": get_int_input(
            "Enter delay_installments (1-4): ", [1, 2, 3, 4]
        ),
        "delinquency_history": get_int_input(
            "Enter delinquency_history (1-4): ", [1, 2, 3, 4]
        ),
        "write_off": get_int_input(
            "Enter write_off (1 = No, 2 = Yes): ", [1, 2]
        ),
        "fraud_litigation": get_int_input(
            "Enter fraud_litigation (1 = No, 2 = Yes): ", [1, 2]
        )
    }

    coa_score = calculate_coa_score(user_inputs)

    print("\n==============================")
    print(" CONDUCT OF ACCOUNT SCORE ")
    print("==============================")
    print("Score:", coa_score)
