import pandas as pd
import os
from datetime import datetime

def process_and_clean_data():
    # --- STEP 1: LOADING THE DATA  ---
    # We need to find the JSON file we created in Task 1.
    today_date = datetime.now().strftime("%Y%m%d")
    json_path = f"data/trends_{today_date}.json"
    
    if not os.path.exists(json_path):
        print(f"Error: Could not find {json_path}. Did you run Task 1 first?")
        return

    # Loading the JSON file into a Pandas DataFrame (basically a Python spreadsheet)
    df = pd.read_json(json_path)
    print(f"Initial Load: Found {len(df)} stories in the raw JSON file.")

    # --- STEP 2: CLEANING THE DATA  ---
    
    # 1. Removing Duplicates: Sometimes the API returns the same story twice.
    # We use 'post_id' as the unique key to identify duplicates.
    df = df.drop_duplicates(subset=['post_id'])
    print(f"After removing duplicates: {len(df)}")

    # 2. Handling Missing Values: A story is useless if it doesn't have a title or score.
    # We drop any rows where critical columns are empty (NaN).
    df = df.dropna(subset=['post_id', 'title', 'score'])
    print(f"After removing nulls: {len(df)}")

    # 3. Fixing Data Types: We need to ensure numbers are treated as integers, 
    # not text, so we can do math or comparisons later.
    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)

    # 4. Low Quality Filter: Per the instructions, we only want popular trends.
    # Any story with a score (upvotes) less than 5 is removed.
    df = df[df['score'] >= 5]
    print(f"After removing low scores: {len(df)}")

    # 5. Cleaning Text: Titles often have accidental spaces at the start or end.
    # '.str.strip()' removes that invisible whitespace.
    df['title'] = df['title'].str.strip()

    # --- STEP 3: SAVING AS CSV  ---
    
    # We save the results as a CSV for the next stage of the pipeline.
    # 'index=False' prevents Pandas from adding an extra column of numbers.
    output_csv = "data/trends_clean.csv"
    df.to_csv(output_csv, index=False)
    
    print(f"\nSaved {len(df)} clean rows to {output_csv}")

    # Final requirement: Print a summary of stories per category
    print("\nStories per category:")
    print(df['category'].value_counts().to_string())
    

if __name__ == "__main__":
    process_and_clean_data()