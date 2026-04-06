# TrendPulse: Real-Time Trend Analysis Pipeline

TrendPulse is a Python-based data engineering pipeline that collects, processes, analyzes, and visualizes trending topics from the web. The project uses the HackerNews API to identify what topics are currently gaining attention.

This repository demonstrates the first phase of the pipeline: automated data collection, cleaning, analysis, and visualization.


## Project Overview

The goal of this project is to analyze trending stories from HackerNews and understand engagement patterns using data analysis and visualization.

The pipeline consists of four main stages:

1. Data Collection  
2. Data Cleaning  
3. Data Analysis  
4. Data Visualization


## Project Structure
trendpulse_sowmya/
│
├── data/
│ ├── trends_20260405.json
│ ├── trends_clean.csv
│ └── trends_analysed.csv
│
├── outputs/
│ ├── chart1_top_stories.png
│ ├── chart2_categories.png
│ ├── chart3_scatter.png
│ └── dashboard.png
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py


## Tasks

### Task 1 — Data Collection
Fetches trending stories from the HackerNews API and stores them as JSON.

File: `task1_data_collection.py`


### Task 2 — Data Processing
Cleans the raw JSON data and converts it into structured CSV format.

File: `task2_data_processing.py`


### Task 3 — Data Analysis
Uses NumPy and Pandas to analyze engagement metrics such as score and number of comments.

File: `task3_analysis.py`


### Task 4 — Data Visualization
Generates charts and a dashboard using Matplotlib to visualize trending patterns.

File: `task4_visualization.py`

Generated Visualizations:
- Top trending stories
- Category distribution
- Engagement scatter plot
- Combined dashboard


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- HackerNews API

##Install dependencies:

pip install pandas numpy matplotlib

##Run the pipeline:

python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py

##Output

The generated visualizations will be saved inside the outputs/ folder.
