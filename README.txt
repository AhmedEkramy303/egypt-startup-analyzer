# Simple Egypt Startup Analysis (Sample Data)

## About This Project
This project provides a basic analysis of startup data, using a sample dataset themed around the Egyptian market for demonstration. The primary goal is to identify prominent sectors and observe some general characteristics of startups, such as size (by employee count) and founding year.

This is a beginner-friendly project, ideal for those new to data analysis with Python.

## How it Works
The Python script (`analyze_startups.py`) performs the following steps:

1.  **Data Preparation:**
    * It uses a built-in sample dataset containing fictional company names, their sectors, number of employees, and founding years.
    * Basic data type conversions are applied.

2.  **Basic Analysis:**
    * Identifies the top companies by the number of employees.
    * Determines the most common sectors within the sample data.
    * Calculates the average number of employees per sector.
    * Computes the correlation between the number of employees and the company's founding year.

3.  **Data Visualizations:**
    * **Bar Plot:** Shows the number of companies in each sector.
    * **Scatter Plot:** Illustrates the relationship between company size (number of employees) and its founding year, with sectors differentiated by color.
    * **Word Cloud:** Highlights the most frequently appearing sectors in the dataset.

4.  **Recommendations:**
    * Generates simple, data-driven suggestions for potentially promising sectors based on the analysis of the sample data (e.g., sectors with high average employee counts or high frequency).

## Getting Started

### Prerequisites
* Python 3.7+

### Setup and Execution

1.  **Clone the repository (or download the files):**
    If this project were on GitHub, you would clone it. For now, ensure you have `analyze_startups.py` and `requirements.txt` in the same directory.

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Open your terminal or command prompt in the project directory and run:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the analysis script:**
    ```bash
    python analyze_startups.py
    ```

## Expected Outputs
The script will print analysis results to the console and save the following files in the same directory as the script:

* `companies_per_sector.png`: A bar plot visualizing the number of companies per sector.
* `size_vs_year.png`: A scatter plot showing company size versus founding year.
* `sector_wordcloud.png`: A word cloud of the most common sectors.
* `recommendations.txt`: A text file containing simple, data-driven recommendations.

## Using Your Own Data
The current script uses hardcoded sample data. To analyze your own dataset:

1.  **Prepare your data:** Ensure your data is in a CSV file with columns like `company_name`, `sector`, `num_employees`, and `founding_year`.
2.  **Modify the script:** In `analyze_startups.py`, find the "Data Preparation" section.
    * Comment out or delete the existing sample `data` dictionary and `df = pd.DataFrame(data)` line.
    * Uncomment and adapt the following line to load your CSV file:
        ```python
        # df = pd.read_csv('your_file_name.csv') # Replace 'your_file_name.csv'
        ```
    * Ensure the column names in your CSV match those used in the script, or update the script's column references accordingly.

## Note on `cryptonews.csv`
The `cryptonews.csv` file that was initially mentioned or uploaded is not used in this project because its content is assumed not to match the required startup data structure (company names, sectors, employee counts, founding years). The project uses a self-contained sample dataset for demonstration purposes.

## Disclaimer
The analysis and recommendations provided by this script are based on a small, illustrative sample dataset. They are intended for educational and demonstrative purposes only and should not be used for making real-world business or investment decisions. Always conduct thorough and comprehensive research using extensive, real-world data before making any such decisions.