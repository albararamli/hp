# HP3 File Processing with Python

Welcome to our repository! Here, we present a Python script designed for processing HP3 files, extracting data, and performing various analyses. This script facilitates the extraction of accelerometer, ECG, and PPG data from HP3 files and provides functionalities such as drift removal and visualization.

## Introduction

The script provided in this repository offers a comprehensive solution for working with HP3 files. It includes functions for reading HP3 files, extracting sensor data, removing drift from accelerometer data, and visualizing the results.

## Features

- **HP3 File Reading**: The script can parse HP3 files and extract relevant sensor data, including accelerometer readings, ECG, and PPG signals.
- **Data Processing**: Various data processing tasks are supported, such as drift removal from accelerometer data.
- **Visualization**: The script includes visualization functions to plot accelerometer, ECG, and PPG signals for both left and right sides.
- **Customization**: Users can customize parameters and settings to adapt the script to different datasets and analysis requirements.

## Getting Started

To begin using the script, follow these steps:

1. **Download the Script Files**: Download the `hp3.py` and `main.py` files. Place `hp3.py` in the same directory as `main.py`.

2. **Provide Target HP3 File**: Ensure you have the target HP3 file (`hp3_file.hp3`) in the same directory as `main.py`. This file contains the data you want to analyze.

3. **Install Dependencies**: Make sure you have Python installed on your system. Additionally, install the required libraries by running:

   ```
   pip3 install pandas matplotlib
   ```

4. **Execute the Script**: Run the `main.py` script using the following command:

   ```
   python3 main.py
   ```

   This will start processing the target HP3 file and analyzing the data.
   
## Example Usage

```python
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

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

# Draw the acceleration signal of the left and right sides
left_data.plot(x="index", y=["acc_x", "acc_y", "acc_z"], figsize=(22, 3))
right_data.plot(x="index", y=["acc_x", "acc_y", "acc_z"], figsize=(22, 3))

# Draw the PPG of the left and right sides
left_data.plot(x="index", y=["ppg"], figsize=(22, 3))
right_data.plot(x="index", y=["ppg"], figsize=(22, 3))

# Draw the ECG of the left and right sides
left_data.plot(x="index", y=["ecg"], figsize=(22, 3))
right_data.plot(x="index", y=["ecg"], figsize=(22, 3))

# Acceleration Signal on the Left side

# Remove the drift in the acceleration signal of the left side
left_data_no_drift = hp3_remove_drift(left_data, base=50)

# Display the data after removing the drift
display(left_data_no_drift)

# Draw the signal before and after removing the drift for the left side
draw_drift(left_data_no_drift)

# Acceleration Signal on the Right side

# Remove the drift in the acceleration signal of the right side
right_data_no_drift = hp3_remove_drift(right_data, base=50)

# Display the data after removing the drift
display(right_data_no_drift)

# Draw the signal before and after removing the drift for the right side
draw_drift(right_data_no_drift)
```

## Acknowledgments

If you find this script useful in your work, please consider citing our paper:

- **Walk4Me: Telehealth Community Mobility Assessment, An Automated System for Early Diagnosis and Disease Progression**  
  Authors: Albara Ah Ramli, Xin Liu, Erik K Henricson  
  [Read the paper](https://arxiv.org/abs/2305.05543)
