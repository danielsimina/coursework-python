import pandas as pd

# U.S. Median Household Income by Race and Ethnicity
data = {
    'Race_Ethnicity': ['Asian', 'White (Non-Hispanic)', 'All Races Average', 'Hispanic', 'Black'],
    'Median_Household_Income': [105000, 81000, 75000, 60000, 53000]
}
df_income = pd.DataFrame(data)
print(df_income.to_string(index=False))