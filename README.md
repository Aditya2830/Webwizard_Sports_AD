# Webwizard_Sports_Analytic_Dashboard

## Group Name:
  Web Wizards

## Project Title: 
  Sports Analytics Dashboard

## Description:
  Build a dashboard to visualize player/team performance metrics over a season.

## Group Members:
- Aditya Gajjar (KU2407U392)
- Henish Prajapati (KU2407U404)
- Krish Dhairav (KU2407U416)
- Tishya Sajnani (KU2407U444)

## Objective of the Project:
To create an interactive dashboard that visualizes player and team performance metrics over a sports season. This dashboard will leverage data analysis and visualization techniques to present  key performance indicators (KPIs) such as scores, rankings, and individual contributions, enabling stakeholders to gain actionable insights and enhance decision-making processes in sports management.

## Tools and Libraries Used:
- Numpy
- Pandas
- MatplotLib
- Tabulate

## Execution Steps (How to run the project):

### Step 1: Import Required Libraries
- **Purpose**: Import `numpy`, `pandas`, `matplotlib.pyplot`, and `tabulate` libraries.
- These libraries are used for numerical computations, data manipulation, visualization, and tabular representation.

### **Step 2: Load the CSV Data**
- **Action**: Load the CSV file into a Pandas DataFrame.
- **Purpose**: The CSV contains cricket player statistics.

### **Step 3: Display Data in Tabular Format**
- **Action**: Use the `tabulate` library to convert the DataFrame into a grid-style table.
- **Output**: Displays the dataset in a visually structured table format.

### **Step 4: Calculate the Highest Score**
- **Action**: Remove any '*' from the `Highest Score` column, convert it to numeric, and find the maximum value using NumPy.
- **Purpose**: Identifies the highest individual score among all players.
- **Output**: Prints the highest score.

### **Step 5: Calculate the Highest Number of Fifties**
- **Action**: Convert the `Fifties` column to numeric and find the maximum value using NumPy.
- **Purpose**: Identifies the player with the most fifties.
- **Output**: Prints the highest number of fifties.

### **Step 6: Calculate the Highest Number of Sixes**
- **Action**: Convert the `Sixes` column to numeric and find the maximum value using NumPy.
- **Purpose**: Identifies the player with the most sixes.
- **Output**: Prints the highest number of sixes.

### **Step 7: Calculate the Highest Number of Fours**
- **Action**: Convert the `Fours` column to numeric and find the maximum value using NumPy.
- **Purpose**: Identifies the player with the most fours.
- **Output**: Prints the highest number of fours.

### **Step 8: Calculate the Highest Strike Rate**
- **Action**: Convert the `Strike Rate` column to numeric and find the maximum value using NumPy.
- **Purpose**: Identifies the player with the highest strike rate.
- **Output**: Prints the highest strike rate.

### **Step 9: Calculate Average Score Per Match and Filter High Performers**
- **Action**: Add a new column `Average Score Per Match` and filter players with averages greater than 40.
- **Purpose**: Highlights consistent high-scoring players.
- **Output**: Displays players with an average score per match above 40.

### **Step 10: Sort Data by Total Runs**
- **Action**: Sort the dataset by the `Total Runs` column in descending order.
- **Purpose**: Identifies the top run-scorers.
- **Output**: Displays the sorted dataset.

### **Step 11: Visualizations**
#### **Visualization 1: Total Runs by Players**
- **Action**: Plot a bar chart of `Total Runs` against `Player`.
- **Purpose**: Compares total runs among players.
- **Output**: Displays a bar chart.

#### **Visualization 2: Strike Rate Comparison**
- **Action**: Plot a line graph of `Strike Rate` against `Player`.
- **Purpose**: Shows strike rate trends among players.
- **Output**: Displays a line plot.

#### **Visualization 3: Fours vs Sixes**
- **Action**: Plot a scatter plot of `Fours` vs. `Sixes`.
- **Purpose**: Highlights the relationship between fours and sixes hit by players.
- **Output**: Displays a scatter plot.

#### **Visualization 4: Centuries and Fifties**
- **Action**: Plot a grouped bar chart for `Centuries` and `Fifties` against `Player`.
- **Purpose**: Compares century and fifty counts for each player.
- **Output**: Displays a grouped bar chart.

## Challenges Faced

- Difficulty in sourcing consistent and comprehensive data from multiple platforms.
- Integration of diverse data formats into a unified structure suitable for analysis and visualization.
- Ensuring data accuracy while dealing with missing or inconsistent records.
- Implementing robust data cleaning processes to maintain the integrity of the metrics.

## Summary of Results:

This dashboard serves as a powerful tool for cricket enthusiasts, analysts, and team management to delve into detailed performance metrics and make informed decisions.
