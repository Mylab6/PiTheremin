import os
import subprocess
def append_sys_file(text_to_add, file_location):
    print('Wirting to ', file_location)
    file_object = open(file_location, 'a+')
    if text_to_add in file_object.read():
        print('No need to update ', file_location)
    else:
        file_object.write("\n")                   
        file_object.write(text_to_add)

    file_object.close()
  
try:
    subprocess.run('pip3 install pipenv', shell=True)
    uart_enable_str = 'enable_uart=1'
    boot_config_file_location = '/boot/config.txt'
    append_sys_file(uart_enable_str,boot_config_file_location)
    add_to_path_str = 'export PATH="$HOME/.local/bin:$PATH"'
    bash_rc_location = os.path.join( os.path.expanduser('~'), '.bashrc')
    append_sys_file(add_to_path_str,bash_rc_location)
    print(' Good to reboot now')
except Exception as e: 
    print(e)              
