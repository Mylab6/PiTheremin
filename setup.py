file_object = open('/boot/config.txt, 'a')
# Append 'hello' at the end of file
file_object.write("\n")                   
file_object.write('enable_uart=1')
# Close the file
file_object.close()
print(' Good to reboot now')
                  
