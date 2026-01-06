import os
import pandas as pd

from preprocessing import enforce_types, apply_validity_rules, handle_missing
from feature_engineering import create_ratio_features
from split import split_data


def run_pipeline(input_path: str, output_dir: str) -> None:
   
    df = pd.read_csv(input_path)

    # Preprocessing
    df = enforce_types(df)
    df = apply_validity_rules(df)
    df = handle_missing(df)

    # Feature engineering
    df = create_ratio_features(df)

    # Train / Val / Test split
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)

    # Save outputs
    os.makedirs(output_dir, exist_ok=True)

    X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
    X_val.to_csv(os.path.join(output_dir, "X_val.csv"), index=False)
    X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)

    y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    y_val.to_csv(os.path.join(output_dir, "y_val.csv"), index=False)
    y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)
