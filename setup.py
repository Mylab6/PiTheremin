import os
import subprocess
def append_sys_file(text_to_add, file_location):
    print('Wirting to ', file_location)
    file_object = open(file_location, 'a+')
    text_location = file_object.read().find(text_to_add)
    if text_location:
        print('No need to update ', file_location)
    else:
        file_object.write("\n")                   
        file_object.write(text_to_add)

    file_object.close()
  
try:
    subprocess.run('pip3 install pipenv', shell=True)
    subprocess.run(' sudo apt-get install -y python3-numpy', shell=True)
    subprocess.run('sudo apt-get install -y libjpeg-dev zlib1g-dev', shell=True)
    subprocess.run('sudo apt-get -y install python3-rpi.gpio', shell=True)
    subprocess.run('sudo apt-get install -y gcc libffi-dev libssl-dev python3-dev',shell=True)
    subprocess.run('sudo apt-get install -y  libjack0', shell=True)
    subprocess.run('sudo apt-get install -y libatlas-base-dev', shell=True)
    subprocess.run('sudo raspi-config nonint do_i2c 0', shell=True)

    uart_enable_str = 'enable_uart=1'
    boot_config_file_location = '/boot/config.txt'
    append_sys_file(uart_enable_str,boot_config_file_location)
    add_to_path_str = 'export PATH="$HOME/.local/bin:$PATH"'
    bash_rc_location = os.path.join( os.path.expanduser('~'), '.bashrc')
    append_sys_file(add_to_path_str,bash_rc_location)
    subprocess.run('pipenv install')
    # you might need to do this manually latter, 

    subprocess.run('export CFLAGS=-fcommon')
    subprocess.run('pip3 install RPI.GPIO')
    print(' Good to reboot now')
except Exception as e: 
    print(e)              
