import pandas as pd
import numpy as np

def run_analysis():
    # --- STEP 1: LOAD AND EXPLORE ---
    try:
        df = pd.read_csv('data/trends_clean.csv')
    except FileNotFoundError:
        print("Error: trends_clean.csv not found. Run Task 2 first!")
        return

    print(f"Loaded data: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())

    # --- STEP 2: NUMPY STATISTICS ---
    # We convert the column to a NumPy array for fast math
    scores = df['score'].values
    
    print("\n--- NumPy Stats ---")
    print(f"Mean score      : {np.mean(scores):.2f}")
    print(f"Median score    : {np.median(scores)}")
    print(f"Std deviation   : {np.std(scores):.2f}")
    print(f"Max score       : {np.max(scores)}")
    print(f"Min score       : {np.min(scores)}")

    # Finding the most frequent category
    top_cat = df['category'].value_counts().idxmax()
    cat_count = df['category'].value_counts().max()
    print(f"\nMost stories in: {top_cat} ({cat_count} stories)")

    # Finding the story with the most comments
    top_story_idx = df['num_comments'].idxmax()
    top_story = df.loc[top_story_idx]
    print(f"Most commented story: \"{top_story['title']}\" - {top_story['num_comments']} comments")

    # --- STEP 3: ADD NEW COLUMNS ---
    # 1. Engagement Formula: how much talk per upvote
    df['engagement'] = df['num_comments'] / (df['score'] + 1)
    
    # 2. Popularity Check: is it above the average?
    avg_score = np.mean(scores)
    df['is_popular'] = df['score'] > avg_score

    # --- STEP 4: SAVE THE RESULT ---
    output_file = 'data/trends_analysed.csv'
    df.to_csv(output_file, index=False)
    print(f"\nSaved analysed data to {output_file}")

if __name__ == "__main__":
    run_analysis()
    