import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file using pandas
data = pd.read_csv('Salaries.csv')

# 1. Basic Data Exploration
# We can get of the size of the dataset using the shape attribute.
# The shape is printed like this (number of lines, number of columns)
number_rows, number_columns = data.shape
# we also can use the len() function to get the number of rows 
# and len() combined with data.columns to get the number of columns.
# number_rows = len(data)
# number_columns = len(data.columns)

# We can check the data type of all columns at once using pandas.DataFrame.dtypes
data_types = data.dtypes
# We can check for missing values in each column using pandas.DataFrame.isnull().sum()
missing_values = data.isnull().sum()

# 2. Descriptive Statistics
# Calculate basic statistics
salary_statistics = data['TotalPay'].describe()

# Select specific values
mean_salary = salary_statistics['mean']
median_salary = salary_statistics['50%'] # Equivalent to the median
mode_salary = data['TotalPay'].mode()[0]
minimum_salary = salary_statistics['min']
maximum_salary = salary_statistics['max']
salary_range = maximum_salary - minimum_salary
standard_deviation_salary = salary_statistics['std']

# 3. Data Cleaning
# One way to deal with empty cells is to remove rows that contain empty cells. 
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
# Handling missing data by dropping rows with missing values in any column
cleaned_data = data.dropna()
missing_values_after_cleaning = cleaned_data.isnull().sum()
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value
# cleaned_data = data.fillna(10, inplace = True)


# 4. Basic Data Visualization
plt.figure(figsize=(10, 5)) # Set the size of the first figure
plt.hist(data['TotalPay'], bins=25, color='orange', edgecolor='black') # Create a histogram of 'TotalPay' column with 25 bins
plt.title('Distribution of Salaries') # Set the title of the histogram
plt.xlabel('Salary') # Set label for x-axis
plt.ylabel('Frequency') # Set label for y-axis
plt.show() # Display the histogram

plt.figure(figsize=(8, 6)) # Set the size of the second figure
department_counts = data['JobTitle'].value_counts() # Count the occurrences of each unique 'JobTitle' and store it in department_counts
top_12_departments = department_counts.head(12) # Select the top 12 departments based on the counts
''' Selecting only the top 12 departments for visualization helps to focus on the most prevalent job titles, 
maintaining clarity and relevance. Including all departments could clutter the visualization, 
especially with numerous unique job titles of low frequencies. Limiting to the top 12 ensures a clear 
presentation of employee distribution across departments.'''
plt.pie(top_12_departments, labels=top_12_departments.index, autopct='%1.1f%%') # Create a pie chart showing the proportion of employees in the top 12 departments
plt.title('Proportion of Employees in Different Departments')
plt.show() # Display the pie chart

# 5. Grouped Analysis
# The groupby() function is used to split the data into groups based on unique job titles.
# For each group, the mean() function calculates the average salary (TotalPay) for employees holding that job title.
avg_salary_by_dept = data.groupby('JobTitle')['TotalPay'].mean()

# 6. Simple Correlation Analysis
# This analysis aims to investigate the correlation between two numerical columns: 'TotalPay' and 'Year'.
# The correlation coefficient, which quantifies the strength and direction of the linear relationship between two variables,
# is calculated using the corr() function. Here, we are interested in understanding how the total pay (TotalPay) relates 
# to the Year of employees.
correlation = data['TotalPay'].corr(data['Year'])
plt.figure(figsize=(10, 6))
plt.scatter(data['TotalPay'], data['Year'], alpha=0.5) # Create the scatter plot
plt.title('Scatter Plot of Year vs Salary')
plt.xlabel('Salary')
plt.ylabel('Year')
plt.show()

print("Number of rows:", number_rows)
print("Number of columns:", number_columns,end="\n\n")
print("Data Types of Columns:\n", data_types, end="\n\n")
print("Missing Values:\n", missing_values, end="\n\n")
print("Mean Salary:", mean_salary)
print("Median Salary:", median_salary)
print("Mode Salary:", mode_salary)
print("Minimum Salary:", minimum_salary)
print("Maximum Salary:", maximum_salary)
print("Salary Range:", salary_range)
print("Standard Deviation of Salary:", standard_deviation_salary, end="\n\n")
print("Missing Values after cleaning:\n", missing_values_after_cleaning, end="\n\n")
print("Average Salary by Department:\n", avg_salary_by_dept, end="\n\n")
print("Correlation between Year and Salary:", correlation)

# 7. Summary of Insights: 
'''
After conducting various analyses on the provided salary dataset, several key insights have been uncovered:

- Basic Data Exploration:
  - The dataset contains 148,654 rows and 13 columns, representing various attributes of employee salaries.
  - Data types range from integers to floating-point numbers, indicating a mix of numerical data.
  - Missing values are present in certain columns, such as 'BasePay', 'OvertimePay', and 'Benefits'.

- Descriptive Statistics:
  - The average salary across all employees is approximately $74,768.32, with a median salary of $71,426.61.
  - The most common salary value (mode) is $0.0, suggesting a significant number of records with no reported pay.
  - The salary range spans from -$618.13 to $567,595.43, indicating considerable variability in pay.
  - The standard deviation of salaries is approximately $50,517.01, highlighting the dispersion of salary values around the mean.

- Data Cleaning:
  - Rows with missing values have been removed to ensure data integrity and analysis accuracy.

- Basic Data Visualization:
  - A histogram reveals the distribution of salaries, showing a right-skewed distribution with most salaries clustered around the lower end.
  - A pie chart illustrates the proportion of employees in different departments, focusing on the top 12 departments based on frequency.

- Grouped Analysis:
  - The average salary for each job title has been calculated, providing insights into salary discrepancies across different roles.

- Simple Correlation Analysis:
  - A scatter plot demonstrates the relationship between employee salary and the year of employment, indicating a general trend of increasing salaries over the years.

Overall, these analyses shed light on the salary landscape within the dataset, uncovering patterns, trends, and potential areas for further exploration or action.
'''
