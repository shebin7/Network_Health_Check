![alt text](https://github.com/shebin7/Network_Health_Check/blob/master/Advance_Ping_Dev.gif)

* Excell Output
![alt text](https://github.com/shebin7/Network_Health_Check/blob/master/Snapshots/Excell_Status.png)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Libraries](#libraries)
* [Setup](#setup)

## General info
This project allows the users to see which branch device is Live,it does this by a Ping test,the user first access the centralized server from where it has 
connectivity to all the Branch's Device,and then it runs a Ping to each and every device, The Programme looks for certain patterns form the Device response 
If the pattern matches the programmes value it will be either considered as UP or DOWN based ont the pattern,and a summary table is presented to the user on console
Also the output is saved in excell with color coding based on the Ping result.

## Technologies
Project is created with:
* Python 3.6.9

Network Devices 
* GNS3 IOU and IOS Devices


## Libraries
 * [Rich](https://rich.readthedocs.io/en/latest/)

 * [Nornir](https://nornir.readthedocs.io/en/latest/)


	
## Setup
To run this project, clone this to your local Folder using 'git clone'

```
$ git clone https://github.com/shebin7/Network_Health_Check
```
Then run it from IDE or from Terminal 
```
$ python3 Network_Health_Check.py
```

