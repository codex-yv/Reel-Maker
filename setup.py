
import subprocess
import socket

setup_design = """
  ________  _______  _______  _______  _______  _______  _______ 
 /  __   _||       ||       ||       ||       ||       ||       |
|  /  |  ||  _____||    ___||   _   ||  _____||_     _||_     _|
|  |  |  || |_____ |   |___ |  | |  || |_____   |   |    |   |  
|  |  |  ||_____  ||    ___||  |_|  ||_____  |  |   |    |   |  
|  |  |  ||_____  ||   |___ |       ||_____  |  |   |    |   |  
|  |  |  ||  _____||    ___||  _____||  _____|  |   |    |   |  
|  |__|  || |_____ |   |___ || |     | |_____  |   |    |   |  
|______| ||_______||_______||_|     ||_______|  |___|    |___|  
                                                              
       Setup Program - Installer for Your Application       
      =======================================================
"""

print(setup_design)


def is_connected():
    try:
        # Try connecting to Google's DNS (8.8.8.8) on port 53
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False

if is_connected():
    con=1
else:
    con=0

cres=is_connected()
if cres==1:
    def install_modules(module_list):
        not_found_modules = []
        
        for module in module_list:
            try:
                subprocess.run(['pip', 'install', module], check=True)
            except subprocess.CalledProcessError:
                not_found_modules.append(module)
        
        if not_found_modules:
            print("Modules not found and not installed:")
            for module in not_found_modules:
                print(module)
        else:
            print("All modules installed successfully!")

    # List of modules to install
    modules_to_install = ['tk-tools','requests','pillow',
                          'tkcalendar','customtkinter','moviepy']
    install_modules(modules_to_install)
    print("\n\n________SETUP PART--1--Done________")
else:
    print("++==++==++==++Connect to the internet first! ++==++==++==++")