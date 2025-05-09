import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from datetime import datetime
# import os # No longer needed as we save in the current directory

# --- Step 1: Data Preparation ---
# Using sample data. If you have a CSV, use: pd.read_csv('your_file.csv')
data = {
    'company_name': [
        'Fawry', 'Swvl', 'Instabug', 'Vezeeta', 'Paymob',
        'MaxAB', 'Trella', 'Breadfast', 'Halan', 'Bosta',
        'RabbitMart', 'MoneyFellows', 'Capiter', 'ExpandCart', 'Homzmart'
        # Reduced sample size for brevity in this example
    ],
    'sector': [
        'FinTech', 'Transportation', 'Developer Tools', 'HealthTech', 'FinTech',
        'B2B E-commerce', 'Logistics', 'FoodTech', 'FinTech', 'Logistics',
        'Q-Commerce', 'FinTech', 'B2B E-commerce', 'E-commerce Platform', 'E-commerce'
    ],
    'num_employees': [
        1500, 600, 150, 300, 700,
        400, 250, 200, 800, 180,
        350, 220, 320, 120, 280
    ],
    'founding_year': [
        2008, 2017, 2014, 2012, 2015,
        2018, 2018, 2017, 2017, 2016,
        2021, 2016, 2020, 2013, 2019
    ]
}
df = pd.DataFrame(data)

# Basic data type conversion
df['founding_year'] = df['founding_year'].astype(int)
df['num_employees'] = df['num_employees'].astype(int)

# Calculate company age (optional, but good for context)
current_year = datetime.now().year
df['company_age_years'] = current_year - df['founding_year']

print("--- Prepared Data Sample ---")
print(df.head())
print("\n")

# --- Step 2: Basic Analysis ---

# Companies with the most employees (as a proxy for growth/size)
top_companies = df.sort_values(by='num_employees', ascending=False).head(5)
print("--- Top 5 Companies by Number of Employees ---")
print(top_companies[['company_name', 'sector', 'num_employees']])
print("\n")

# Sectors with most companies
print("--- Sectors with the Most Companies ---")
popular_sectors = df['sector'].value_counts()
print(popular_sectors.head())
print("\n")

# Average number of employees per sector
avg_employees_per_sector = df.groupby('sector')['num_employees'].mean().sort_values(ascending=False)
print("--- Average Number of Employees per Sector ---")
print(avg_employees_per_sector.head())
print("\n")

# Correlation between number of employees and founding year
correlation = df['num_employees'].corr(df['founding_year'])
print(f"--- Correlation between Employees and Founding Year: {correlation:.2f} ---")
# A negative correlation suggests newer companies might have fewer employees, or older ones have more.
print("\n")


# --- Step 3: Visualizations ---
plt.style.use('seaborn-v0_8-whitegrid')

# Bar Plot: Number of companies in each sector
plt.figure(figsize=(10, 6))
sector_counts = df['sector'].value_counts()
sns.barplot(x=sector_counts.index, y=sector_counts.values, palette="coolwarm", hue=sector_counts.index, legend=False)
plt.title('Number of Companies per Sector (Sample Data)')
plt.xlabel('Sector')
plt.ylabel('Number of Companies')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('companies_per_sector.png') # Save in current directory
plt.show()

# Scatter Plot: Company size (employees) vs. Founding Year
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='founding_year', y='num_employees', hue='sector', size='num_employees', sizes=(30, 300), palette="viridis")
plt.title('Company Size vs. Founding Year (Sample Data)')
plt.xlabel('Founding Year')
plt.ylabel('Number of Employees')
plt.legend(title='Sector', bbox_to_anchor=(1.05, 1), loc='upper left') # Move legend out
plt.tight_layout()
plt.savefig('size_vs_year.png') # Save in current directory
plt.show()

# WordCloud: Most frequent sectors
sector_text = ' '.join(df['sector'])
wordcloud = WordCloud(width=700, height=350, background_color='white').generate(sector_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Frequent Sectors - Word Cloud (Sample Data)')
plt.tight_layout()
plt.savefig('sector_wordcloud.png') # Save in current directory
plt.show()

# --- Step 4: Recommendations ---
recommendation_text = "--- Simple Recommendations (Based on Sample Data) ---\n"

# Recommend based on sectors with high average employees
if not avg_employees_per_sector.empty:
    recommended_sector = avg_employees_per_sector.index[0]
    avg_emp = avg_employees_per_sector.iloc[0]
    recommendation_text += (
        f"Consider exploring the '{recommended_sector}' sector. "
        f"On average, companies in this sector (in our sample) have around {avg_emp:.0f} employees, "
        f"which might indicate a good potential for scaling.\n"
    )
else:
    recommendation_text += "Could not generate a specific sector recommendation from the sample data.\n"

# Recommend based on most numerous sectors
if not popular_sectors.empty:
    popular_rec_sector = popular_sectors.index[0]
    recommendation_text += (
        f"The '{popular_rec_sector}' sector has the highest number of startups in our sample, "
        f"suggesting high activity or lower barriers to entry.\n"
    )

recommendation_text += (
    "\nIMPORTANT: These recommendations are based on a very small, sample dataset. "
    "For real-world decisions, conduct thorough market research."
)

print("--- Recommendations ---")
print(recommendation_text)

# Save recommendations to a text file
with open('recommendations.txt', 'w', encoding='utf-8') as f:
    f.write(recommendation_text)

print("\n--- Analysis Complete. Check for saved plots and recommendations.txt ---")
