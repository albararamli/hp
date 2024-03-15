# Import the hp3_read function from the hp3 module
from hp3 import *

# Specify the URL or path to the HP3 file
url = "hp3_file.hp3"

# Read the HP3 file and extract the data
data = hp3_read(url)

# Perform further analysis or visualization tasks as needed

# For example, splitting data into left and right sides
left_data = data[data['side'] == "L"]
right_data = data[data['side'] == "R"]

# Draw the acceleration signal, PPG, and ECG of the left and right sides
left_data.plot(x="index", y=["acc_x", "acc_y", "acc_z"], figsize=(22, 3))
right_data.plot(x="index", y=["acc_x", "acc_y", "acc_z"], figsize=(22, 3))

left_data.plot(x="index", y=["ppg"], figsize=(22, 3))
right_data.plot(x="index", y=["ppg"], figsize=(22, 3))

left_data.plot(x="index", y=["ecg"], figsize=(22, 3))
right_data.plot(x="index", y=["ecg"], figsize=(22, 3))

# Acceleration Signal on the Left side
# Remove the drift in the acceleration signal of the left side
left_data_no_drift = hp3_remove_drift(left_data, base=50)

# Display the data after removing the drift
print(left_data_no_drift)

# Draw the signal before and after removing the drift for the left side
draw_drift(left_data_no_drift)

# Acceleration Signal on the Right side
# Remove the drift in the acceleration signal of the right side
right_data_no_drift = hp3_remove_drift(right_data, base=50)

# Display the data after removing the drift
print(right_data_no_drift)

# Draw the signal before and after removing the drift for the right side
draw_drift(right_data_no_drift)