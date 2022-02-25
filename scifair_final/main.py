import pandas as pd
from sklearn import linear_model
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

Best_Renewable_Resource = {
    'low_temp_(f)': [35, 28, 39, 44, 50, 45, 56, 38, 37, 50, 40, 66, 63, 44, 60, 35, 36, 42, 39, 35, 43, 60, 36, 42, 48,
                     44, 52, 44, 32],
    'high_temp_(f)': [53, 56, 58, 59, 67, 58, 75, 55, 56, 64, 60, 36, 80, 64, 78, 60, 50, 64, 60, 57, 66, 78, 59, 62,
                      71, 64, 76, 62, 54],
    'precipitation_(in)': [44.85, 24.93, 39.35, 43.56, 39.74, 34.1, 49.76, 9.3, 36.82, 23.64, 42.94, 9.67, 54.69, 47,
                           52.71, 12.52, 29.13, 53.4, 37.77, 13.3, 44.75, 45.28, 34.66, 2.15, 54.37, 42.64, 53, 41.5,
                           24.31],
    'wind_speed_(mph)': [9.28, 5.21, 4.84, 6.94, 7.78, 3.83, 10.75, 9.6, 5.85, 7.85, 10.43, 6.24, 9.38, 3.69, 8.95,
                         11.63, 8.75, 6.8, 10.45, 4.3, 6.83, 8.11, 11.21, 10.96, 6.58, 8.45, 4.31, 5.83, 11.82],
    'humidity_(d)': [0.11, 0, 2.25, 2.37, 2.33, 0, 11.75, 1.94, 1.42, 0.02, 3.23, 0, 19.4, 0.008, 17.37, 0, 0.45, 0,
                     2.91, 0, 5.65, 14.78, 3.57, 3.91, 8.32, 5.34, 10.09, 3.65, 1.45],
    'cloudy_(percentage)': [50.75, 39.33, 49, 47.58, 44.75, 52.83, 44.42, 47.25, 49.75, 33.75, 46.67, 34.58, 46.75,
                            55.16, 46.83, 41.25, 54.92, 43.16, 48.67, 50.33, 42.33, 40.58, 42.92, 40.91, 42.42, 43.5,
                            43.58, 46.5, 44.58],
    'snowy_(in)': [38.4, 14.91, 59, 38.5, 15, 0.24, 0.1, 4.58, 81, 0, 37, 1.73, 0, 3, 0, 75, 119, 0.62, 16.4, 1.69, 14,
                   0, 23, 0.99, 2, 1, 0.1, 2.04, 33],
    'best_renewable_resource': [1, 2, 1, 3, 2, 1, 2, 1, 2, 2, 1, 2, 3, 1, 3, 2, 4, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1],
}

df = pd.DataFrame(Best_Renewable_Resource,
                  columns=['low_temp_(f)', 'high_temp_(f)', 'precipitation_(in)', 'wind_speed_(mph)', 'humidity_(d)',
                           'cloudy_(percentage)', 'snowy_(in)', 'best_renewable_resource'])

X = df[['high_temp_(f)', 'low_temp_(f)', 'precipitation_(in)',  'wind_speed_(mph)', 'humidity_(d)','cloudy_(percentage)'
    , 'snowy_(in)']].astype(
    float)
Y = df['best_renewable_resource'].astype(float)

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X.values, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# tkinter GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width=500, height=300)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify='center')
canvas1.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients_result = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify='center')
canvas1.create_window(260, 240, window=label_Coefficients)

# New_High_Temp label and input box
label1 = tk.Label(root, text='Type high_temp_(f): ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry(root)  # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

# New_Precipitation label and input box
label2 = tk.Label(root, text=' Type precipitation_(in): ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry(root)  # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)


def values():
    global New_High_Temp  # our 1st input variable
    New_High_Temp = float(entry1.get())

    global New_Precipitation  # our 2nd input variable
    New_Precipitation = float(entry2.get())

    prediction_result = ('Predicted Best Renewable Resource: ', regr.predict([[New_High_Temp, 28, New_Precipitation, 5.21, 0, 39.33, 14.91]]))
    label_Prediction = tk.Label(root, text=prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)


button1 = tk.Button(root, text='Predict Best Renewable Resource', command=values,
                    bg='orange')  # button to call the 'values' command above
canvas1.create_window(270, 150, window=button1)

# plot 1st scatter
figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['high_temp_(f)'].astype(float), df['best_renewable_resource'].astype(float), color='r')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['best_renewable_resource'])
ax3.set_xlabel('high_temp_(f)')
ax3.set_title('high_temp vs. best_renewable_resource')

# plot 2nd scatter
figure4 = plt.Figure(figsize=(5, 4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['precipitation_(in)'].astype(float), df['best_renewable_resource'].astype(float), color='g')
scatter4 = FigureCanvasTkAgg(figure4, root)
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend(['best_renewable_resource'])
ax4.set_xlabel('precipitation_(in)')
ax4.set_title('precipitation vs. best_renewable_resource')

root.mainloop()
