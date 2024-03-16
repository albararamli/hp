# Copyright (c) https://albara.ramli.net
# This code is authored by Albara Ah Ramli
# All rights reserved.

# If you use this code, please cite the following paper:
# @misc{ramli2023walk4me,
#     title={Walk4Me: Telehealth Community Mobility Assessment, An Automated System for Early Diagnosis and Disease Progression}, 
#     author={Albara Ah Ramli and Xin Liu and Erik K. Henricson},
#     year={2023},
#     eprint={2305.05543},
#     archivePrefix={arXiv},
#     primaryClass={eess.SP}
# }



# Importing necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# Suppressing warnings
warnings.filterwarnings("ignore")

# Function to flip a binary bit
def flip(bit):
    return '1' if bit == '0' else '0'

# Function to compute the two's complement of a binary number
def scom(binary_str):
    # Compute the one's complement
    ones = ''.join(flip(bit) for bit in binary_str)
    twos = list(ones)
    
    # Compute the two's complement
    for i in range(len(binary_str) - 1, -1, -1):
        if ones[i] == '1':
            twos[i] = '0'
        else:
            twos[i] = '1'
            break
    
    # If all bits were '1', insert an additional '1' at the beginning
    if i == -1:
        twos.insert(0, '1')
    
    return ''.join(twos)

def hp3_read(url):
  results=[]
  print_out=0
  f = open(url, "r")
  i=0
  for x in f:
    x=x.replace("\n","")
    i=i+1
    if i==19:
      x=x.replace("<calibration_order>","")
      if print_out==1:
        print("***************************************")
      calibration_order=x.split(",")
      if print_out==1:
        print(calibration_order)
    if i==20:
      x=x.replace("<calibration_data>","")
      #print(x)
      calibration_data=x.split(",")
      if print_out==1:
        print(calibration_data)
        print("***************************************")
    if i==21:
      calibration={}
      n=0
      for calibration_i in calibration_order:
        calibration[calibration_i]=int(calibration_data[n])
        n=n+1
    ################################################################################
    ################################################################################
    ################################################################################
    TTT=23
    if (i==TTT) or (i>TTT and (i%3)==2):
      x=x.replace("\n","").replace("N:","").split("_")
      index=x[0]
      #print("",index)
      millesecond=int(x[1][0:2], 16)
      seconds=int(x[1][2:5], 16)
      timex=str(seconds)+"."+str(millesecond)
      #print(timex)
    ################################################################################
    ################################################################################
    ################################################################################
    if i>=TTT+1 and (i>TTT+1 and (i%3)!=2):
      #x="R1094F90C73A30E75A703FFAB"
      #x="L1181AD039DDA0F5846"
      #x="R6BA577563257574EBE57F15DFFFD4857260800B7A0"
      side=x[0:1]
      if print_out==1:
        print("===========================")
        print(x)
        print("===========================")
      l=6
      a=1
      b=a+l
      for x_i in range(1,7+1):
        ori="*"
        if print_out==1:
          print("Hexa=",x[a:b])
        out=""
        out=out+"{0:04b}".format(int(x[a+0:a+1], 16))
        out=out+"{0:04b}".format(int(x[a+1:a+2], 16))
        out=out+"{0:04b}".format(int(x[a+2:a+3], 16))
        out=out+"{0:04b}".format(int(x[a+3:a+4], 16))
        out=out+"{0:04b}".format(int(x[a+4:a+5], 16))
        out=out+"{0:04b}".format(int(x[a+5:a+6], 16))
        #print("Binary=",out)
        value=int(out, 2)
        if print_out==1:
          print("Int=",value)
        outx=scom(out.strip(""))
        outx=''.join(outx)
        #print("2nd complements = ",outx)
        #print("20 bit acc=",outx[0:20])
        #print("4bit remains=",outx[20:24])
        a=b
        b=a+l
        if x_i==1:
          if print_out==1:
            print("(x-axis) Vertical acceleration")
          ori="X"
          value_x=value
        if x_i==2:
          if print_out==1:
            print("(y-axis) Anterior-Posterior acceleration")
          ori="Y"
          value_y=value
        if x_i==3:
          if print_out==1:
            print("(z-axis) Lateral acceleration")
          ori="Z"
          value_z=value
        if ori!="*":
          if side=="R" and ori=="X":
            vmax_name=side+ori+"_MAX"
          else:
            vmax_name=side+ori+"_max"
          vmax_value=calibration[vmax_name]
          if print_out==1:
            print(vmax_name,vmax_value)
        if x_i==4:
          if print_out==1:
            print("ECG")
          ecg=value
        if x_i==5:
          if print_out==1:
            print("PPG")
          ppg=value
        if x_i==6:
          if print_out==1:
            print("Vref from left ADC")
          vref=value
          if side=="L":
            acc_x=(value_x-vref)/calibration[side+'X_max']
          else:
            acc_x=(value_x-vref)/calibration[side+'X_MAX']
          acc_y=(value_y-vref)/calibration[side+'Y_max']
          acc_z=(value_z-vref)/calibration[side+'Z_max']
          ecg_value=(ecg-vref)
          if print_out==1:
            print("Vref=",value)
          if print_out==1:
            print("INDEX=",index," Time=",timex," Side=",side," Acc_X=",acc_x," Acc_Y=",acc_y," Acc_Z=",acc_z," PPG=",ppg," ECG=",ecg)
          results.append([index,timex,side,acc_x,acc_y,acc_z,ppg,ecg_value])
        if x_i==7:
          if x[0:1]=="L":
            if print_out==1:
              print("Battery level")
          if x[0:1]=="R":
            if print_out==1:
              print("Square wave for time calibration")
        if print_out==1:
          print("====================================")
  #######################
  df=pd.DataFrame(results,columns=["index","time","side","acc_x","acc_y","acc_z","ppg","ecg"])
  #df['index2']=df['index']
  #df=df.set_index('index')
  #df=df.set_index('index')
  #df=df.sort_values(by=['timex'])
  iii=0
  ########################
  df["time"]=df["time"].astype(float)
  df["acc_x"]=df["acc_x"].astype(float)
  df["acc_y"]=df["acc_y"].astype(float)
  df["acc_z"]=df["acc_z"].astype(float)
  df["ppg"]=df["ppg"].astype(float)
  df["ecg"]=df["ecg"].astype(float)
  df["index"]=df["index"].astype(int)
  df=df.sort_values(by=['index'], ascending=True)
  df.reset_index(drop=True, inplace=True)
  ############
  # Calculate the time range
  time_diff_sec = 1 / 200
  # Calculate the total number of samples
  total_samples = len(df)
  # Create the time column
  df['time'] = pd.date_range(start='2024-01-01', periods=total_samples, freq=f'{time_diff_sec}S').time
  ###########
  return df

def hp4_read(url):
  results=[]
  print_out=0
  f = open(url, "r")
  i=0
  for x in f:
    x=x.replace("\n","")
    i=i+1
    ################################################################################
    ################################################################################
    ################################################################################
    TTT=20
    if (i==TTT) or (i>TTT and (i%3)==2):
      x=x.replace("\n","").replace("N:","")
      index=x
      timex=x
      if print_out==1:
        print("",index)
    ################################################################################
    ################################################################################
    ################################################################################
    if i>=TTT+1 and (i>TTT+1 and (i%3)!=2):
      #x="R1094F90C73A30E75A703FFAB"
      #x="L1181AD039DDA0F5846"
      #x="R6BA577563257574EBE57F15DFFFD4857260800B7A0"
      side=x[0:1]
      if print_out==1:
        print("===========================")
        print(x)
        print("===========================")
      l=6
      a=1
      b=a+l
      if side=="R":
        sec=4
      else:
        sec=3
        ecg=0
      for x_i in range(1,sec+1):
        ori="*"
        if print_out==1:
          print("Hexa=",x[a:b])
        out=""
        out=out+"{0:04b}".format(int(x[a+0:a+1], 16))
        out=out+"{0:04b}".format(int(x[a+1:a+2], 16))
        out=out+"{0:04b}".format(int(x[a+2:a+3], 16))
        out=out+"{0:04b}".format(int(x[a+3:a+4], 16))
        out=out+"{0:04b}".format(int(x[a+4:a+5], 16))
        out=out+"{0:04b}".format(int(x[a+5:a+6], 16))
        #print("Binary=",out)
        value=int(out, 2)
        if print_out==1:
          print("Int=",value)
        outx=scom(out.strip(""))
        outx=''.join(outx)
        #print("2nd complements = ",outx)
        #print("20 bit acc=",outx[0:20])
        #print("4bit remains=",outx[20:24])
        a=b
        b=a+l
        if x_i==1:
          if print_out==1:
            print("(x-axis) Vertical acceleration")
          ori="X"
          acc_x=value
        if x_i==2:
          if print_out==1:
            print("(y-axis) Anterior-Posterior acceleration")
          ori="Y"
          acc_y=value
        if x_i==3:
          if print_out==1:
            print("(z-axis) Lateral acceleration")
          ori="Z"
          acc_z=value
        if x_i==4:
          if print_out==1:
            print("ECG")
          ecg=value
      if print_out==1:
        print("INDEX=",index," Time=",timex," Side=",side," Acc_X=",acc_x," Acc_Y=",acc_y," Acc_Z=",acc_z," ECG=",ecg)
      results.append([index,timex,side,acc_x,acc_y,acc_z,ecg])
  #######################
  df=pd.DataFrame(results,columns=["index","time","side","acc_x","acc_y","acc_z","ecg"])
  #df['index2']=df['index']
  #df=df.set_index('index')
  #df=df.set_index('index')
  #df=df.sort_values(by=['timex'])
  iii=0
  ########################
  df["time"]=df["time"].astype(float)
  df["acc_x"]=df["acc_x"].astype(float)
  df["acc_y"]=df["acc_y"].astype(float)
  df["acc_z"]=df["acc_z"].astype(float)
  df["ecg"]=df["ecg"].astype(float)
  df["index"]=df["index"].astype(int)
  df=df.sort_values(by=['index'], ascending=True)
  df.reset_index(drop=True, inplace=True)
  ############
  # Calculate the time range
  time_diff_sec = 1 / 250
  # Calculate the total number of samples
  total_samples = len(df)
  # Create the time column
  df['time'] = pd.date_range(start='2024-01-01', periods=total_samples, freq=f'{time_diff_sec}S').time
  ###########
  return df

def hp_read(url):
  # Split the filename and extension
  filename, extension = os.path.splitext(url)
  extension=extension.lower()[1:]
  # Check if the extension matches hp4
  if extension == "hp4":
    # Call hp4_read function
    return hp4_read(url), extension
    # Check if the extension matches hp3
  elif extension == "hp3":
    # Call hp3_read function
    return hp3_read(url), extension
  else:
    # Print error message for unsupported file extensions
    print(f"Error: '{extension}' is not supported! The file extension should be either '.hp3' or '.hp4'")
    return None, extension

# Function to remove drift in the data for a single axis
def hp_remove_drift_single(zzz, letx, extension, base):
    # Create a copy of the DataFrame
    xxx = zzz.copy()
    
    # Calculate the rolling mean (trend) of acceleration data for the specified axis
    trend = zzz["acc_" + letx].rolling(base).mean().to_frame()
    trend.columns = ["trend_" + letx]  # Rename the column to indicate it's the trend
    trend.reset_index(drop=True, inplace=True)  # Reset index for alignment
    
    # Reset index of the original DataFrame for alignment
    xxx.reset_index(drop=True, inplace=True)
    
    # Add trend and new acceleration data columns to the DataFrame
    xxx["trend_" + letx] = trend["trend_" + letx]
    xxx["new_acc_" + letx] = xxx["acc_" + letx] - trend["trend_" + letx]

    if extension == "hp4":
        xxx["new_acc_" + letx] /= 2**18
    
    return xxx


# Function to remove drift in the data for all three axes
# base is the number of data points used in each rolling window to compute the mean.
def hp_remove_drift(zzz, extension, base):
    # Iterate over each axis (x, y, z)
    for axis in ["x", "y", "z"]:
        # Call hp_remove_drift_single to remove drift for the current axis
        zzz = hp_remove_drift_single(zzz, axis, extension, base)
    return zzz


# Function to draw the original, trend, and new acceleration data before and after removing drift
def draw_drift(out):
    # Define colors for each axis
    colors = {"x": "blue", "y": "orange", "z": "green"}
    
    # Iterate over each axis (x, y, z)
    for axis in ["x", "y", "z"]:
        # Print axis information
        print(f"{axis}-axis before and after")
        
        # Create subplots for original, trend, and new acceleration data
        fig, ax = plt.subplots(nrows=2, figsize=(22, 6))
        
        # Plot original and trend data
        out.plot(x="index", y=[f"acc_{axis}", f"trend_{axis}"], ax=ax[0], color=[colors[axis], 'red'])
        ax[0].set_title("Original and Trend Data")
        ax[0].legend([f"acc_{axis}", f"trend_{axis}"])
        
        # Plot new acceleration data
        out.plot(x="index", y=f"new_acc_{axis}", ax=ax[1], color=colors[axis])
        ax[1].set_title("New Acceleration Data")
        ax[1].legend([f"new_acc_{axis}"])
        
        # Add vertical space between subplots
        plt.subplots_adjust(hspace=0.5)
        
        # Display the plots
        plt.show()
