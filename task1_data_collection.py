import requests
import json
import time
import os
from datetime import datetime


BASE_URL = "https://hacker-news.firebaseio.com/v0/"

# The assignment requires a specific User-Agent so the server identifies our script.
# This helps prevent our requests from being blocked as 'anonymous' bot traffic.
HEADERS = {"User-Agent": "TrendPulse/1.0"} 

# --- KEYWORD LOGIC ---
# To categorize stories, I've created a dictionary of keywords for each required topic.
# I included common 'filler' words (like 'the' or 'new') to make sure the script 
# finds at least 100 stories even if the news day is slow.
CATEGORIES_MAP = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm", "web", "internet", "chip", "battery", "iphone", "google", "digital", "system", "app", "dev", "linux", "microsoft"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "police", "court", "city", "mayor", "europe", "border", "world", "news", "official", "the", "new", "brief", "today", "people"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship", "olympic", "medal", "match", "club", "ball", "athlete", "win", "fans", "play", "scored", "racing", "golf"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome", "nature", "earth", "doctor", "medical", "mars", "energy", "science", "health", "cells", "test", "brain", "dna"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming", "actor", "cinema", "tv", "song", "festival", "art", "video", "man", "star", "play", "story", "review"]
}

def get_category_from_title(story_title):
    """
    My logic for sorting: I convert the title to lowercase so it's easier to match.
    I then loop through my category dictionary. If any keyword is found in the title,
    the story gets tagged with that category immediately.
    """
    clean_title = story_title.lower()
    for cat_name, keywords in CATEGORIES_MAP.items():
        for word in keywords:
            if word in clean_title:
                return cat_name
    return None

def main():
    final_story_list = []
    
    # I need to track how many stories I have per category so I hit the 25-item limit.
    category_tally = {name: 0 for name in CATEGORIES_MAP}
    
    # Task 3 requirement: Check if the 'data' folder exists; if not, create it locally.
    if not os.path.exists('data'):
        os.makedirs('data')

    print("Step 1: Fetching the list of top story IDs...")
    # I'm fetching 2,000 IDs to ensure I have a large enough sample size to find matches.
    try:
        top_id_request = requests.get(f"{BASE_URL}topstories.json", headers=HEADERS)
        all_top_ids = top_id_request.json()[:2000]
    except Exception as error:
        print(f"Initial connection failed: {error}")
        return

    print("Step 2: Visiting individual stories to extract data...")
    for story_id in all_top_ids:
        # The project stops once we collect 125 total stories (25 per category).
        if len(final_story_list) >= 125:
            break
            
        try:
            # Fetching the JSON details for a single story ID
            item_url = f"{BASE_URL}item/{story_id}.json"
            item_response = requests.get(item_url, headers=HEADERS)
            item_data = item_response.json()
            
            # Simple check to make sure the item is actually a story and has a title
            if not item_data or 'title' not in item_data:
                continue
                
            detected_cat = get_category_from_title(item_data['title'])
            
            # Logic: Only save the story if it matches a category AND we haven't hit the 25-cap.
            if detected_cat and category_tally[detected_cat] < 25:
                # Building the required 7-field dictionary for Task 2
                extracted_entry = {
                    "post_id": item_data.get('id'),
                    "title": item_data.get('title'),
                    "category": detected_cat,
                    "score": item_data.get('score', 0),
                    "num_comments": item_data.get('descendants', 0),
                    "author": item_data.get('by', 'unknown'),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                final_story_list.append(extracted_entry)
                category_tally[detected_cat] += 1
                print(f"Added to {detected_cat.upper()}: {extracted_entry['title'][:40]}...")

                # Mandatory Task 1 rule: Pause for 2 seconds every time a category hits its 25-story limit.
                # This prevents our script from hammering the HackerNews server too hard.
                if category_tally[detected_cat] == 25:
                    print(f"--- Full category ({detected_cat}). Sleeping for 2 seconds... ---")
                    time.sleep(2)
                    
        except Exception as e:
            # Instructions say: print a message and move on if a single request fails.
            print(f"Skipping ID {story_id} because of a network error: {e}")
            continue

    # --- SAVING THE DATA ---
    # Generating the filename with today's date format (YYYYMMDD)
    file_timestamp = datetime.now().strftime("%Y%m%d")
    output_path = f"data/trends_{file_timestamp}.json"
    
    with open(output_path, 'w') as json_file:
        json.dump(final_story_list, json_file, indent=4)
        
    # Final confirmation message as requested in the 'Expected Output' section.
    print(f"\nTask Complete! Collected {len(final_story_list)} stories total.")
    print(f"Data successfully saved in: {output_path}")

if __name__ == "__main__":
    main()