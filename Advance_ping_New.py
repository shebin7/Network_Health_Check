from rich.console import Console
from rich.panel import Panel
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_config,netmiko_send_command
from nornir.plugins.functions.text import print_result,print_title
from genie.testbed import load
from rich.table import Table
from rich.progress import Progress
from openpyxl.styles import *
from netmiko import ConnectHandler
import csv
import openpyxl
from threading import Thread
import time
from alive_progress import alive_bar

### File path for config.yaml ###
config_file_yaml ="/home/shebin/NETDEVOPS/Net_automation_Project/Network_Heath_Check/config.yaml"

### File path for all the Branch Ip Address which we will ping from central server to check connectivity ###
ip_address_loopup_for_pinging = "/home/shebin/NETDEVOPS/Net_automation_Project/csv_files/branch_ipaddress.csv"

### Final result Device Up or Down result will be stored here
final_reault_of_Health_Check =  "/home/shebin/NETDEVOPS/Net_automation_Project/Network_Heath_check/csv_files/finale_result_health.csv"



### Initilizing nornir object ###
nr = InitNornir(config_file=config_file_yaml)



### Reading Total number of Rows in CSV files ###
file = open(ip_address_loopup_for_pinging)
num_rows = len(file.readlines())




### Rich Variable for styles&tabels ###
status_up  = '[bold] :white_heavy_check_mark: '
status_down = '[bold] :cross_mark:'

style_down = '[red][bold] '
style_up = '[green] [bold] '


### Creating a Table for the result on CLI ###
console = Console()
cli_table = Table(title='[bold]Network Health Check Table [/bold]')
cli_table.add_column("SOL_ID", justify="right", style="cyan", no_wrap=True)
cli_table.add_column("BRANCH_NAME", justify="right", style="cyan", no_wrap=True)
cli_table.add_column("IP_ADDRESS", justify="right", style="cyan", no_wrap=True)
cli_table.add_column("HEALTH_STATUS", justify="right", style="cyan", no_wrap=True)



### Header fields for csv file where ping result will be stored ###
report_fields = ['SOL_ID','IP_ADDRESS','BRANCH_NAME','HEALTH_STATUS','TIME']


### Opening and writing Results to Csv File ###
with open(final_reault_of_Health_Check,'a+')as wr:
    csv_dictwrite = csv.DictWriter(wr,report_fields)
    csv_dictwrite.writeheader()



console.print(Panel("[bold]  :smiley:   ~WELCOME TO NETWORK HEALTH CHECKUP~   :smiley: ",style='white on blue'),justify='center')
console.print()
console.print()
#console.print(':computer: [green][bold] `~`~`~`~`~`~`~`~`~`~`~`~`[/bold][/green]:satellite: ~`~`~`~`~`~`~`~`~`~`~`~` :computer:   ',justify='center')  
console.print()
console.print(' :satellite:','[blink]:sparkles:'*4,                       ':satellite:',justify='center')
console.print(' :vertical_traffic_light:'+'          '+':vertical_traffic_light:',' '*14,justify='center')   
console.print(':bank:',':traffic_light:'*10,':cloud:'+'           '+':cloud:',':traffic_light:'*10,':office:',justify='center' )  
console.print()
console.print()
console.print()
console.print("[bold][red][blink]Warning![/blink][/red][/bold] [red][italic]PLEASE DONOT INTERUPT THE EXECUTION",justify='center')
console.print()
console.print()
console.print('Working...',style='green')

def Network_Health_Check(task):
   with alive_bar(num_rows-1)as bar:
        with open(ip_address_loopup_for_pinging,'r')as re:
            csv_d_reader = csv.DictReader(re)
            for row in csv_d_reader:

                row_values={'ip' : row['IP_ADDRESS'],'solid' :  row['Sol_ID'],'branch' : row['Branch_Name']}
                res = task.run(netmiko_send_command,command_string='ping '+row_values['ip'])
                ping_search = res.result
                if not '!!!' in ping_search:
                    
                    sol_id_down = style_down+row_values['solid']
                    branch_down = style_down+row_values['branch']
                    ip_down = style_down+row_values['ip']
                    cli_table.add_row(sol_id_down,branch_down,ip_down,status_down)

                                        
                else:
                    
                    sol_id_up = style_up+row_values['solid']
                    branch_up = style_up+row_values['branch']
                    ip_up = style_up+row_values['ip']
                    cli_table.add_row(sol_id_up,branch_up,ip_up,status_up)

### Bar tracks/shows  ETA/Time needed to complete the execution ###    
                bar()
         
                continue


result_of_ping = nr.run(Network_Health_Check)

result_of_ping
console.print()
console.print()
console.print(cli_table)
