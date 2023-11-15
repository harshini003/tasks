#Task 2: Create a Data Visualization Tool
#level 3
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("h:\cognifyz\level-3\data_visualization\datasettask2 - Sheet1.csv")
plt.scatter(data['day'], data['tip'])
plt.title("Scatter Plot")
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()
