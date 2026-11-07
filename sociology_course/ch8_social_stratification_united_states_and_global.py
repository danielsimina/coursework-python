import pandas as pd

# U.S. Wealth Distribution Data (Sociological/Economic benchmarks)
percentiles = ['Bottom 50%', '50th-90th Percentile', '90th-99th Percentile', 'Top 1%']
wealth_share = [2.5, 30.5, 37.0, 30.0]

df_wealth = pd.DataFrame({'Group': percentiles, 'Wealth_Share_Percent': wealth_share})
print(df_wealth.to_string(index=False))