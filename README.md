Name: Geetha N
Company:CODETECH IT SOLUTIONS
ID:CT0806EK
Domain: DATA SCIENCE
Duration:December 12th,2024 to january 12th,2025
Mentor: Neha

OVERVIEW OF  THE PROJECT

Exploratory Data Analysis (EDA) on a Custom Dataset

Objective:
To create a dataset, perform exploratory data analysis (EDA), and derive insights about the data using Python and libraries such as pandas, matplotlib, and seaborn.

Key Steps:

1. Dataset Creation
A custom dataset was created using Python dictionaries, containing four columns:
 Name: Names of individuals (categorical).
 Age: Ages of individuals (numeric).
 City: Cities where individuals live (categorical).
 Salary: Monthly salary of individuals (numeric).
 Saved the dataset as `my_dataset.csv` using `pandas.DataFrame` and `to_csv()`.

 2. Loading the Dataset
 The dataset was loaded into a `pandas` DataFrame using `pd.read_csv()`.

 3. Exploratory Data Analysis (EDA)
Performed various EDA steps to understand the dataset:
Basic Inspection:
- Displayed the first few rows using `df.head()`.
  - Checked for missing values with `df.isnull().sum()`.
  - Obtained summary statistics using `df.describe()`.

 Data Visualization:
  - Histograms: Analyzed the distribution of numerical columns (e.g., Age).
  - Scatter Plots: Explored relationships between numerical columns (e.g., Age vs. Salary).
  - Heatmaps: Visualized correlations between numerical columns

4. Insights Derived
Age Distribution: The histogram shows how ages are distributed.
  Relationship Between Age and Salary: The scatter plot identifies trends between these variables.
  Correlations:
  - Identified correlations between numeric columns using a heatmap.
  - Filtered only numeric columns for meaningful correlation analysis.


 Tools and Technologies Used
Python
  Libraries:
  - `pandas`: For data manipulation and analysis.
  - `matplotlib` & `seaborn`: For data visualization.

Challenges Faced
1. Correlation Errors: Fixed errors by filtering only numeric columns for correlation.
2. File Path Issues: Resolved by ensuring the dataset file was in the correct directory or using absolute paths.

Future Extensions
1. Handle Missing Data:
   - Impute missing values (if any) using mean, median, or mode.
2. Advanced Visualizations:
   - Add boxplots, violin plots, or pair plots for deeper analysis.
3. Feature Engineering:
   - Encode categorical variables (e.g., City) for analysis.
4. Modeling:
   - Use this dataset to build a simple prediction model (e.g., predicting Salary based on Age and City).

Outcome
This project demonstrated the ability to:
- Create and work with custom datasets.
- Perform a structured exploratory analysis.
- Visualize data and derive insights effectively.

