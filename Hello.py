import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Lenovo\Downloads\Data.csv")

# Data Cleaning
df.dropna(inplace = True)
print(df.to_string())

# Data Analysis

# First
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

# Second
df.plot(kind = 'scatter', x = 'Duration', y = 'Pulse')
plt.show()

# Third
df.plot(kind = "scatter", x = "Pulse", y = "Calories")
plt.show()