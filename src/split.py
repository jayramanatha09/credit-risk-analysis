from sklearn. model_selection import train_test_split
from config import (
    TARGET_COL,
    TRAIN_SIZE,
    VAL_SIZE,
    TEST_SIZE,
    RANDOM_STATE
)

def split_data(df):
    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    # Step 1: Hold-out test set
    X_temp, X_test, y_temp, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        stratify=y,
        random_state=RANDOM_STATE
    )

    # Step 2: Train / Validation split
    val_relative_size = VAL_SIZE / (TRAIN_SIZE + VAL_SIZE)

    X_train, X_val, y_train, y_val = train_test_split(
        X_temp,
        y_temp,
        test_size=val_relative_size,
        stratify=y_temp,
        random_state=RANDOM_STATE
    )

    return X_train, X_val, X_test, y_train, y_val, y_test
