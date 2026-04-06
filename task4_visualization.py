import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os

def create_visuals():
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    
    try:
        df = pd.read_csv('data/trends_analysed.csv')
    except:
        print("Error: trends_analysed.csv missing!")
        return

    # --- CHART 1: TOP 10 STORIES ---
    plt.figure(figsize=(10, 6))
    # We sort by score and take the top 10
    top_10 = df.sort_values('score', ascending=False).head(10)
    # Shorten titles if they are too long
    display_titles = [t[:47] + "..." if len(t) > 50 else t for t in top_10['title']]
    
    plt.barh(display_titles, top_10['score'], color='skyblue')
    plt.gca().invert_yaxis() # Highest score at the top
    plt.title('Top 10 Stories by Score')
    plt.xlabel('Upvote Score')
    plt.tight_layout()
    plt.savefig('outputs/chart1_top_stories.png')
    plt.close()

    # --- CHART 2: STORIES PER CATEGORY---
    plt.figure(figsize=(8, 6))
    cat_counts = df['category'].value_counts()
    # Using a different color for each bar
    cat_counts.plot(kind='bar', color=['red', 'blue', 'green', 'orange', 'purple'])
    plt.title('Distribution of Stories per Category')
    plt.ylabel('Number of Stories')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/chart2_categories.png')
    plt.close()

    # --- CHART 3: SCORE VS COMMENTS ---
    plt.figure(figsize=(8, 6))
    # Colour dots based on the 'is_popular' column from Task 3
    for popular_status, color in [(True, 'orange'), (False, 'gray')]:
        mask = df['is_popular'] == popular_status
        plt.scatter(df[mask]['score'], df[mask]['num_comments'], 
                    c=color, label='Popular' if popular_status else 'Standard', alpha=0.6)
    
    plt.title('Engagement: Score vs Comments')
    plt.xlabel('Score')
    plt.ylabel('Comments')
    plt.legend()
    plt.tight_layout()
    plt.savefig('outputs/chart3_scatter.png')
    plt.close()

    # --- BONUS: DASHBOARD ---
    # Combine everything into one figure
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('TrendPulse Data Dashboard', fontsize=20)
    
    # Re-drawing them into the subplots
    # (Simplified for the dashboard)
    axs[0, 0].barh(display_titles[:5], top_10['score'][:5], color='skyblue')
    axs[0, 0].set_title('Top 5 Stories')
    
    cat_counts.plot(kind='pie', ax=axs[0, 1], autopct='%1.1f%%')
    axs[0, 1].set_title('Category Share')
    
    axs[1, 0].scatter(df['score'], df['num_comments'], alpha=0.5)
    axs[1, 0].set_title('Overall Engagement')
    
    axs[1, 1].axis('off') # Hide the 4th empty spot
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('outputs/dashboard.png')
    print("Success! 4 images saved in 'outputs/' folder.")

if __name__ == "__main__":
    create_visuals()
