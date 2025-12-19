import pandas as pd
from app.database import SessionLocal, engine
from app import models
import os
import sys

# Add the current directory to path so we can import 'app'
sys.path.append(os.getcwd())

# Create tables
models.Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    # Path to your CSV
    csv_path = "data/sample_hospital_data.csv"
    
    if os.path.exists(csv_path):
        print(f"Found file: {csv_path}")
        df = pd.read_csv(csv_path)
        
        count = 0
        for _, row in df.iterrows():
            # Convert string date to object
            date_obj = pd.to_datetime(row['date']).date()
            
            # Check if exists
            exists = db.query(models.HospitalCase).filter_by(
                date=date_obj,
                area_code=row['area_code'],
                disease=row['disease']
            ).first()
            
            if not exists:
                db_record = models.HospitalCase(
                    date=date_obj,
                    area_code=row['area_code'],
                    disease=row['disease'],
                    cases=row['cases']
                )
                db.add(db_record)
                count += 1
        
        db.commit()
        print(f"SUCCESS! Added {count} records to database.")
    else:
        print(f"ERROR: Could not find {csv_path}. Make sure you are running this from the backend folder.")
    
    db.close()

if __name__ == "__main__":
    seed_data()