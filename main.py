
## **Reading and Displaying the Contents of an HP3 or HP4 File**

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Import the hp3_read function from the hp3 module
from hp import *

# Specify the URL or path to the HP3 or HP4 file
url = "file.hp3"
#url = "file.hp4"

# Read the HP3 file and extract the data
data, extension = hp_read(url)

# Display the data
print(data)

# **Splitting Data into Left and Right Sides**

# For example, splitting data into left and right sides
left_data = data[data['side'] == "L"]
right_data = data[data['side'] == "R"]

# **Draw the Acceleration Signal, PPG, and ECG of the Left and Right Sides**

# Draw the acceleration signal of the left and right sides
left_data.plot(x="index", y=["acc_x", "acc_y", "acc_z"], figsize=(22, 3))
right_data.plot(x="index", y=["acc_x", "acc_y", "acc_z"], figsize=(22, 3))

# Draw the ECG of the left and right sides
left_data.plot(x="index", y=["ecg"], figsize=(22, 3))
right_data.plot(x="index", y=["ecg"], figsize=(22, 3))

# Draw the PPG of the left and right sides in case of hp3
if extension == "hp3":
  left_data.plot(x="index", y=["ppg"], figsize=(22, 3))
  right_data.plot(x="index", y=["ppg"], figsize=(22, 3))

# **Remove the Drift in the Acceleration Signal of the Left Side and Draw the Signal Before and After**

# Acceleration Signal on the Left side

# Remove the drift in the acceleration signal of the left side
left_data_no_drift = hp_remove_drift(left_data, extension, base=100) #base is number of data points used in each rolling window to compute the mean.

# Display the data after removing the drift
print(left_data_no_drift)

# Draw the signal before and after removing the drift for the left side
draw_drift(left_data_no_drift)

# Acceleration Signal on the Right side
# Remove the drift in the acceleration signal of the right side
right_data_no_drift = hp_remove_drift(right_data, extension, base=100) #base is number of data points used in each rolling window to compute the mean.

# Display the data after removing the drift
print(right_data_no_drift)

# Draw the signal before and after removing the drift for the right side
draw_drift(right_data_no_drift)