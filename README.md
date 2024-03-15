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

1. **Clone the Repository**: Clone this repository to your local machine using Git.

2. **Install Dependencies**: Ensure that you have Python installed on your system along with the necessary libraries specified in the `requirements.txt` file.

3. **Execute the Script**: Run the main Python script to start processing HP3 files and analyzing the data.

## Example Usage

```python
# Import the hp3_read function from the hp3 module
from hp3 import hp3_read

# Specify the URL or path to the HP3 file
url = "path/to/your/hp3_file.hp3"

# Read the HP3 file and extract the data
data = hp3_read(url)

# Perform further analysis or visualization tasks as needed
```

## Acknowledgments

If you find this script useful in your work, please consider citing our paper:

- **Walk4Me: Telehealth Community Mobility Assessment, An Automated System for Early Diagnosis and Disease Progression**  
  Authors: Albara Ah Ramli, Xin Liu, Erik K Henricson  
  [Read the paper](https://arxiv.org/abs/2305.05543)

## Feedback and Contributions

We welcome feedback, suggestions, and contributions from the community. Feel free to open an issue or submit a pull request if you have any improvements or ideas to share.

We hope you find our HP3 file processing script valuable and insightful for your data analysis tasks!
