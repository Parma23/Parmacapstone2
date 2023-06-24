# Create scatter plot
ax = df.plot.scatter('TIME', 'VALUE')
# Calculate line of best fit
x = df['TIME']
y = df['VALUE']
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
# Add line of best fit to plot
xp = np.linspace(x.min(), x.max(), 100)
ax.plot(xp, polynomial(xp), '-', color='red')
plt.show()