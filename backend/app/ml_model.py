import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "backend/data/trained_model.pkl"
DATA_DIR = "backend/data"

def load_data():
    try:
        cases_df = pd.read_csv(os.path.join(DATA_DIR, "sample_hospital_data.csv"))
        env_df = pd.read_csv(os.path.join(DATA_DIR, "sample_environment_data.csv"))
        cases_df['date'] = pd.to_datetime(cases_df['date'])
        env_df['date'] = pd.to_datetime(env_df['date'])
        df = pd.merge(cases_df, env_df, on=['date', 'area_code'], how='inner')
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def train_model():
    df = load_data()
    if df.empty: return {"status": "error"}
    df['target'] = (df['cases'] > 5).astype(int)
    X = df[['temperature', 'rainfall', 'humidity', 'population_density']]
    y = df['target']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return {"status": "success"}

def predict_risk(temp, rain, hum, pop_density):
    if not os.path.exists(MODEL_PATH): train_model()
    model = joblib.load(MODEL_PATH)
    input_data = np.array([[temp, rain, hum, pop_density]])
    return model.predict_proba(input_data)[0][1]