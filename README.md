# HP3 and HP4 File Processing with Python

Welcome to our repository! Here, we present a Python script designed for processing HP3 and HP4 files, extracting data, and performing various analyses. This script facilitates the extraction of accelerometer, ECG, and PPG data from HP3 and HP4 files and provides functionalities such as drift removal and visualization.

## Introduction

The script provided in this repository offers a comprehensive solution for working with HP3 and HP4 files. It includes functions for reading HP3 and HP4 files, extracting sensor data, removing drift from accelerometer data, and visualizing the results.

## Features

- **HP3 and HP4 File Reading**: The script can parse HP3 and HP4 files and extract relevant sensor data, including accelerometer readings, ECG, (and PPG which is in and HP3 only) signals.
- **Data Processing**: Various data processing tasks are supported, such as drift removal from accelerometer data.
- **Visualization**: The script includes visualization functions to plot accelerometer, ECG, and PPG signals for both left and right sides.
- **Customization**: Users can customize parameters and settings to adapt the script to different datasets and analysis requirements.

## Getting Started

To begin using the script, follow these steps:

1. **Download the Script Files**: Download the `hp.py` and `main.py` files. Place `hp.py` in the same directory as `main.py`.

2. **Provide Target HP File**: Ensure you have the target HP file (`file.hp3`) or (`file.hp4`) in the same directory as `main.py`. This file contains the data you want to analyze.

3. **Install Dependencies**: Make sure you have Python installed on your system. Additionally, install the required libraries by running:

   ```
   pip3 install pandas matplotlib
   ```

4. **Execute the Script**: Run the `main.py` script using the following command:

   ```
   python3 main.py
   ```

   This will start processing the target HP3 or HP4 file and analyzing the data.
   
## Example Usage

```python
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
```

## Acknowledgments

If you find this script useful in your work, please consider citing our paper:

- **Walk4Me: Telehealth Community Mobility Assessment, An Automated System for Early Diagnosis and Disease Progression**  
  Authors: Albara Ah Ramli, Xin Liu, Erik K Henricson  
  [Read the paper](https://arxiv.org/abs/2305.05543)
