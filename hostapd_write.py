import time
import os
import colorama
from colorama import Fore, init
init(autoreset=True)



#----------------------------------------------------------------------- CONFIG HANDELING


# set variables
interface = ""                  # Wireless interface (e.g., wlan0)
driver = "nl80211"              # Common Linux driver
ssid = ""                       # Network name (SSID)
bssid = ""                      # Set AP MAC address
hw_mode = "g"                   # Band: a = 5GHz, g = 2.4GHz
channel = ""                    # Wi-Fi channel (1–14 for 2.4GHz, 36+ for 5GHz)
auth_algs = "1"                 # Auth: 1=open, 2=shared, 3=both
wep_default_key = "0"           # Default WEP key index (0–3)
wep_key0 = "SuperSecretPassword"  # WEP key (ASCII or hex)






# open hostpad as READ
with open('hostapd.conf', 'r') as file:
    content = file.read()



# setting variables to later be changed in handle_set_command def
color_handle1 = Fore.RED
color_handle2 = Fore.RED
color_handle3 = Fore.RED
color_handle4 = Fore.RED




# Help / Options Menu
def Options_Menu_hostapd():
    print(Fore.MAGENTA + "use ' SET [ Option ] [ New Value ] ' to change")
    print(Fore.RED + "RED = CHANGE")
    print(Fore.GREEN + "help menu = HELP")
    print("")
    print(Fore.BLUE + "NOTE: Channels 1-14 → hw_mode = g | Channels 36-165 → hw_mode = a")
    print("----------------------------------------------")
    print("")
    print(f"{color_handle2}[+] interface : ", interface)
    print("")
    print(Fore.GREEN + "[+] driver : ", driver)
    print("")
    print(f"{color_handle3}[+] ssid : ", ssid)
    print("")
    print(f"{color_handle1}[+] bssid : ", bssid)
    print("")
    print(Fore.GREEN + "[+] hw_mode : ", hw_mode)
    print("")
    print(f"{color_handle4}[+] channel : ", channel)
    print("")
    print(Fore.GREEN + "[+] auth_algs : ", auth_algs)
    print("")
    print(Fore.GREEN + "[+] wep_default_key : ", wep_default_key)
    print("")
    print(Fore.GREEN + "[+] wep_key0 : ", wep_key0)
    print("")




# js to make clearing a prompting menu easy
def clear():
    os.system("clear")
    Options_Menu_hostapd()




# the def bellow handles the ' SET [Option] [Value] ' command.
# it also changes the handle color once its been given a input

# N0TE  -   even tho only a few options are RED, others can be changed if needed


def handle_set_command(command):
    # Split the command into parts
    parts = command.split()
    
    global color_handle1,color_handle2, color_handle3, color_handle4

    if len(parts) == 3:  # Ensure the command is in the format "SET [Option] [New Value]"
        if parts[0].lower() == "set":  # Ensure it's a 'SET' command
            option = parts[1].lower() # sets user given option to variable ' option '
            new_value = parts[2] # sets user given value to ' new_value ' 
            
            
            if option == "interface":
                global interface # sets as global, lets it be used / chnaged outside of this function
                interface = new_value # sets the user given ' new value ' to interface variable. this comes into play during ' write_to_conf() '
                print(Fore.GREEN + f"Updated interface to {interface}") 
                color_handle2 = Fore.GREEN # changes handle color to green ( this variable is previously set to RED higher up)
                time.sleep(2)
                clear()

            elif option == "bssid":
                global bssid
                bssid = new_value
                print(Fore.GREEN + f"Updated bssid to {bssid}")
                color_handle1 = Fore.GREEN
                time.sleep(2)
                clear()
            
            elif option == "driver":
                global driver
                driver = new_value
                print(Fore.GREEN + f"Updated driver to {driver}")
                time.sleep(2)
                clear()

            elif option == "ssid":
                global ssid
                ssid = new_value
                print(Fore.GREEN + f"Updated SSID to {ssid}")
                color_handle3 = Fore.GREEN
                time.sleep(2)
                clear()

            elif option == "hw_mode":
                global hw_mode
                hw_mode = new_value
                print(Fore.GREEN + f"Updated hw_mode to {hw_mode}")
                time.sleep(2)
                clear()

            elif option == "channel":
                global channel
                channel = new_value
                print(Fore.GREEN + f"Updated channel to {channel}")
                color_handle4 = Fore.GREEN
                time.sleep(2)
                clear()

            elif option == "auth_algs":
                global auth_algs
                auth_algs = new_value
                print(Fore.GREEN + f"Updated auth_algs to {auth_algs}")
                time.sleep(2)
                clear()

            elif option == "wep_default_key":
                global wep_default_key
                wep_default_key = new_value
                print(Fore.GREEN + f"Updated wep_default_key to {wep_default_key}")
                time.sleep(2)
                clear()

            elif option == "wep_key0":
                global wep_key0
                wep_key0 = new_value
                print(Fore.GREEN + f"Updated wep_key0 to {wep_key0}")
                time.sleep(2)
                clear()

            else:
                print(Fore.RED + "Invalid option.")
        else:
            print(Fore.RED + "Invalid command format. Use: SET [Option] [New Value]")
    else:
        print(Fore.RED + "Invalid command format. Use: SET [Option] [New Value]")



#----------------------------------------------------------------------- LOAD PRESETS MENU

folder_path = "hostapd_presets/"

def show_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    files = os.listdir(folder_path)
    if not files:
        print(Fore.BLUE + f"The folder '{folder_path}' is empty.")
        print(Fore.RED + "Please ensure you have previously saved a preset using Option 1. of the ' hostapd_setup.py ' script")
        return
    

    print(Fore.GREEN +  "Type ", "' help '", Fore.GREEN + " for help menu")
    print("")
    print(Fore.MAGENTA + "to load preset: ", "load [ preset ]")
    print(Fore.CYAN + "to show preset contents: ", "show [ preset ]")
    print("")
    print(Fore.LIGHTRED_EX + "----", Fore.BLUE + f"Presets" , Fore.LIGHTRED_EX +  "----")
    
    for file in files:
        x = file.replace(".conf", "")
        print("- ", Fore.MAGENTA + x)


    




#----------------------------------------------------------------------- DISPLAY CONFIG

#Display Current Hostapd.conf file
def hostapt_config_display(content):
    a = input("Display Current Hostapd Config? y/n  >  ")
    if a == "y":
        print(f''' 

              Current Hostapd Config 
              -----------------------

        ''')
        print(content)
    
    elif a == "n":
        pass
    
    else:
        print("Please Enter A Valid Option")
    
    print("")




    

#----------------------------------------------------------------------- WRITE TO FILE

# write to file
def write_to_conf():

    #open file as write
    a = open("hostapd.conf", "w")
    a.write(f'''
interface={interface}                  
driver={driver}
ssid={ssid}                             
bssid={bssid}                      
hw_mode={hw_mode}
channel={channel}                       
auth_algs={auth_algs}
wep_default_key={wep_default_key}
wep_key0={wep_key0}
''')
    


#----------------------------------------------------------------------- HELP MENU

# option 1 help menu
def help_menu1():
    os.system("clear")
    print(''' 
        OVERVIEW
------------------------

this section of the tool is used to configure the hostapd.conf file

        HELP MENU
-------------------------

[ COMMANDS ]

clear                  - Clears the screen and refreshes the options menu
exit                   - Exits the script safely
HELP                   - Displays the help menu with command and option info

          
set <option> <value>   - Sets a configuration value
                         Example: SET ssid MyNetwork

PRESET <name>          - Saves the current hostapd setup as a preset file
                         Example: PRESET OfficeAP

back                   - goes back to previous menu


Type ' clear ' to go back to initial menu
''')


# option 2 help menu
def help_menu2():
    os.system("clear")
    print(''' 
        OVERVIEW
------------------------

this section is used to load previously saved hostapd configurations
          
        HELP MENU
-------------------------

[ COMMANDS ]

clear                  - Clears the screen and refreshes the options menu
exit                   - Exits the script safely
HELP                   - Displays the help menu with command and option info

          
load < option >        - Loads a pre-saved preset from the list
show < option >
          
back                   - goes back to previous menu


Type ' clear ' to go back to initial menu
''')


#----------------------------------------------------------------------- USER INTERACTION PART



def hostapd_setup_input():
    os.system("clear")
    print("")
    print("Hostapd : 1.SETUP  or  2.PRESET")

    a = input("$> ") # the little input symbol thingie

    if a == "exit":
        print(Fore.MAGENTA + "Thank You For Using!")
        time.sleep(2)
        exit()
    

    # option 1.
    elif a == "1":

        os.system("clear") # clear current screen
        Options_Menu_hostapd() # calls option menu

        while True:
            command = input("$> ")
            
            if command == "clear":
                os.system("clear")
                Options_Menu_hostapd()


            elif command == "back":
                break
                
            # code bellow also changes menu [+] color when it is given a input
            elif command.lower().startswith("set "):
                handle_set_command(command)  # Handle the SET command
            
            elif command == "WRITE":
                write_to_conf()

            elif command == "exit":
                print(Fore.MAGENTA + "Thank You For Using!")
                time.sleep(2)
                exit()

            elif command == "HELP":
                help_menu1()

            elif command == "help":
                help_menu1()
                
                

            elif command == "PRESET":
                os.system("clear")
                preset_name = input("Preset Name: ").lower()
                with open(f'hostapd_presets/{preset_name}.conf', 'w') as file:
                    file.write(f'''
interface={interface}                  
driver={driver}
ssid={ssid}                             
bssid={bssid}                      
hw_mode={hw_mode}
channel={channel}                       
auth_algs={auth_algs}
wep_default_key={wep_default_key}
wep_key0={wep_key0}
''')
                


            else:
                print("Please Enter Valid Input")

            ready_colors = [color_handle1, color_handle2, color_handle3, color_handle4]

            # Check if all items in ready_colors are equal to Fore.GREEN
            if all(item == Fore.GREEN for item in ready_colors):
                print(Fore.GREEN + "READY TO WRITE  -  ' WRITE ' in all caps to write .conf file")
                print(Fore.MAGENTA + "Type ' PRESET ' to save as preset")
            
            





    # option 2.
    elif a == "2":

        os.system("clear") # clear current screen

        show_files_in_folder(folder_path)

        while True:
            command = input("$> ")

            if command == "clear":
                os.system("clear")
                show_files_in_folder(folder_path)
            
            elif command == "back":
                break

            elif command == "help":
                help_menu2()

            elif command == "HELP":
                help_menu2()

            elif command == "exit":
                print("Thanks For Using!")
                exit()


            



            # load preset command
            # just a FYI. when using split in python via the os library, it starts at 0 not 1. eg, load a (load = 0 , a = 1)
            elif command.lower().startswith("load "):
                bb = command.split() # split the user input into 2 sections. makes it easier to read different parts of input
                if len(bb) == 2: # if user input length (how many words) == 2
                    load_value = bb[1] # set the load_value variable to the second word in the user input
                    try:
                        with open(f'hostapd_presets/{load_value}.conf', 'r') as file:
                            preset_read = file.read()
                            time.sleep(.5)
                            print(Fore.GREEN + f"Loaded {load_value}")
                            with open("hostapd.conf", "w") as b:
                                b.write(preset_read)
                    except FileNotFoundError:
                        print(Fore.RED + f"Preset '{load_value}' not found.")
                        
                else:
                    print(Fore.RED + "Usage: load <preset_name>")
            
            elif command.lower().startswith("show "):
                os.system("clear")
                show_files_in_folder(folder_path)
                cc = command.split() # split the user input into 2 sections. makes it easier to read different parts of input
                if len(cc) == 2:
                    read = cc[1]
                    with open(f"hostapd_presets/{read}.conf", "r") as read_file:
                        aaaaaa = read_file.read()
                        print(aaaaaa)
            else:
                print("Please Enter Valid Input")
                time.sleep(2)
    else:
        print("Please Enter Valid Input")
        time.sleep(2)




#----------------------------------------------------------------



# use this function to run the script
while True:
    hostapd_setup_input()
