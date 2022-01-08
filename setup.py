import subprocess
def write_to_config_file():
    uart_enable_str = 'enable_uart=1'
    file_object = open('/boot/config.txt', 'a+')
    if uart_enable_str in file_object.read():
        print('No need to update boot config')
    else:
        file_object.write("\n")                   
        file_object.write(uart_enable_str)

    file_object.close()
    print(' Good to reboot now')
try:
    subprocess.run('sudo apt install -y pipenv', shell=True, check=True)
    write_to_config_file()
except: 
    print('Could not open config.txt, are you root ?')              
