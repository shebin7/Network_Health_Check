[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/shebin7/Network_Health_Check)



![alt text](https://github.com/shebin7/Network_Health_Check/blob/master/Advance_Ping_Dev.gif)

* Excell Output
![alt text](https://github.com/shebin7/Network_Health_Check/blob/master/Snapshots/Excell_Status.png)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Libraries](#libraries)
* [Usage](#usage)
* [Setup](#setup)
* [Other Informations](#other-informations)


## General info
This project allows the users to see which branch device is Live,it does this by a Ping test,the user first access the centralized server from where it has 
connectivity to all the Branch's Device,and then it runs a Ping to each and every device, The Programme looks for certain patterns form the Device response 
If the pattern matches the programmes value it will be either considered as UP or DOWN based ont the pattern,and a summary table is presented to the user on console
Also the output is saved in excell with color coding based on the Ping result.

## Technologies
Project is created with:
* Python 3.6.9

Network Devices and Platforms
* GNS3 IOU and IOS Devices
* EVE-NG IOU and IOS Devices
* CML2(VIRL 2) IOU and IOS Devices

## Usage

* When your Host/Laptop acts as a Centralized Server.

  * Host(System/Laptop)------Network_Devices

  When mirroring this in your'e System , you need to setup a topology on your Simulator of your choice having full connectivity with your Local System ip which is running this code , and save the ip address of Lan or Loopback ip of all the Devices running on Simulator in csv file and assign or copy-paste this csv file path as a value to variable 'branch_ip_address_for_pinging' then run the code.

  ![alt text](https://github.com/shebin7/Network_Health_Check/blob/master/Snapshots/snap_assign_branch_ip.png)


* When an Intermediate/Jump Server acts as Centralized Server.

  * Host(System/Laptop)----Intermediate/Jump Server(Linux)----Network_Devices  

  When mirroring this in your'e System , you need to setup a topology on your Simulator of your choice , you must have connectivity with the Jump Server and The Jump Server should have connectivity with the Network Device in Simulator,your Jump Server will act as an Intermediate Server and through it you will connect to Network Devices , but the code will run and excute in the Local System/Host itself. 



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

# Other Informations
Working on adding an Option for Intermediate-Server or Jump-Server.

