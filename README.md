TrendPulse: Real-Time Trend Analysis Pipeline
TrendPulse is a multi-stage data engineering pipeline designed to fetch, clean, and visualize trending topics from the web. This repository contains the first phase of the project: Automated Data Collection.

Project Overview
The goal of this project is to identify what's actually trending right now by analyzing data from the HackerNews API. The pipeline is broken down into four key tasks:

Task 1: Fetch JSON Data (Current) — Automated scraping and categorization.
Task 2: Clean CSV — Data restructuring and noise removal.
Task 3: NumPy/Pandas — Statistical analysis of the trends.
Task 4: Visualize — Creating a dashboard of the findings.

Task 1: Data Collection Logic
For this initial phase, I developed a Python script (task1_data_collection.py) that performs the following:
API Integration: Connects to the HackerNews Firebase API to retrieve the top 500-2000 story IDs.
Dynamic Categorization: Uses a keyword-matching algorithm to sort stories into five domains: Technology, WorldNews, Sports, Science, and Entertainment.
Data Extraction: Captures 7 specific data points for each story, including upvotes (score), comment counts (descendants), and timestamps.
Rate Limiting: Implements a mandatory 2-second delay between category fetches to ensure ethical scraping and API stability.
Storage: Outputs the final dataset into a structured JSON file within the /data directory.

Tech Stack
Language: Python 3.x

Libraries: requests (HTTP calls), json (data storage), time (rate limiting)

📂 Repository Structure
Plaintext
├── data/
│   └── trends_YYYYMMDD.json  # The collected trend data
├── .venv/                    # Python virtual environment
├── task1_data_collection.py  # Main execution script
└── README.md                 # Project documentation

⚙️ Setup & Usage
Activate the virtual environment:

PowerShell
.\.venv\Scripts\Activate.ps1
Install dependencies:

Bash
pip install requests
Run the collector:

Bash
python task1_data_collection.py
Next Steps

I am currently moving into Task 2, where I will load the generated JSON file and convert it into a clean CSV format for easier analysis.
