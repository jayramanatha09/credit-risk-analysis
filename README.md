# Credit Risk Analysis & Approval Strategy

This project demonstrates an end-to-end credit risk analytics workflow, focused on
understanding default risk and evaluating loan approval strategies.

## Project Overview
- Exploratory Data Analysis (EDA) and data quality validation
- Statistical trend analysis using quantile- and rule-based bucketing
- Interpretable ML modeling (logistic regression) for Probability of Default (PD)
- Approval policy simulation (conservative, balanced, aggressive)
- Power BI dashboards for portfolio-level decision support

## Tech Stack
Python (Pandas, NumPy, Scikit-learn), Power BI

## Repository Structure
- `notebooks/` – Phase-wise analysis and validation
- `src/` – Modular preprocessing and pipeline code
- `data/` – Raw and processed datasets
- `powerbi/` – Power BI report and dashboard assets

## Power BI Dashboard
The Power BI report (`powerbi/credit_risk_dashboard.pbix`) contains:
- Risk bucket distribution
- Approval policy comparison
- Expected loss proxy analysis
- Segment-level default risk insights

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run preprocessing pipeline: `python src/pipeline.py`
3. Open notebooks in order for analysis and results
4. Open Power BI report using Power BI Desktop

## Outputs
- PD scores and risk buckets (`pd_scoring_output.csv`)
- Approval strategy comparison via Power BI dashboard
