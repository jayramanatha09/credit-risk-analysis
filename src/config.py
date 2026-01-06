RANDOM_STATE = 42

# Data percentages going to be used for training, validation and real time analysis

TRAIN_SIZE = 0.70 #training
VAL_SIZE = 0.15 #validation
TEST_SIZE = 0.15 # real time analysis

#Minimum legal age to work
EMP_AGE_MIN = 18 

#Target column 
TARGET_COL = "loan_status"

#Numberic Columns
NUMERIC_COLS = [
    "person_age",
    "person_income",
    "loan_amnt",
    "person_emp_length",
    "cb_person_cred_hist_length"
]

#String columns 
CATEGORICAL_COLS = [
    "person_home_ownership",
    "loan_intent",
    "cb_person_default_on_file"
]
