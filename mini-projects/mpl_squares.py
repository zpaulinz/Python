# python3 -m pip install --user matplotlib
# plt.style.available
# Simple Line Plot
import matplotlib.pyplot as plt
print(plt.style.available)
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# [
#  '_classic_test_patch', 
#  'classic', 
#  'dark_background', 
#  'fast', 
#  'ggplot', 
#  'grayscale', 
#  'petroff10', 
#  'seaborn-v0_8', 
#  'seaborn-v0_8-bright', 
#  'seaborn-v0_8-colorblind', 
#  'seaborn-v0_8-dark', 
#  'seaborn-v0_8-dark-palette', 
#  'seaborn-v0_8-darkgrid', 
#  'seaborn-v0_8-deep', 
#  'seaborn-v0_8-muted', 
#  'seaborn-v0_8-notebook', 
#  'seaborn-v0_8-paper', 
#  'seaborn-v0_8-pastel', 
#  'seaborn-v0_8-poster', 
#  'seaborn-v0_8-talk', 
#  'seaborn-v0_8-ticks', 
#  'seaborn-v0_8-white', 
# ]
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Defining the title of the chart and axis labels
ax.set_title("Squares of Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Squares of Values", fontsize=14)

# Defining the size of the labels
ax.tick_params(labelsize=14)

# Display the plot
plt.show()

