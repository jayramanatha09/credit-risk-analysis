import pandas as pd

#creating values used in Phase 2
def create_ratio_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["loan_burden"] = df["loan_amnt"] / df["person_income"]
    df["emp_stability"] = df["person_emp_length"] / df["person_age"]

    return df
