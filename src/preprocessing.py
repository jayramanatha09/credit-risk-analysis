import pandas as pd
from config import NUMERIC_COLS, CATEGORICAL_COLS, EMP_AGE_MIN

# This ensures numeric columns are numeric and invalid values are coerced to NaN.
# Categorical columns are left untouched and handled later.
def enforce_types(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in NUMERIC_COLS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

# Apply logical constraints on data to ensure data integrity 
def apply_validity_rules(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Legal working age
    df = df[df["person_age"] >= EMP_AGE_MIN]

    # Employment length cannot exceed working age years
    df = df[df["person_emp_length"] <= df["person_age"] - EMP_AGE_MIN]

    # Income must be positive
    df = df[df["person_income"] > 0]

    return df

# Handling missing values based off of plots seen in phase 1
def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
   
    df = df.copy()

    # Numeric columns to median
    df[NUMERIC_COLS] = df[NUMERIC_COLS].fillna(
        df[NUMERIC_COLS].median()
    )

    # Categorical columns to explicit 'Unknown'
    for col in CATEGORICAL_COLS:
        df[col] = df[col].fillna("Unknown")

    return df


