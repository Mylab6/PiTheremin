from BasicScreenControl import BasicScreenControl
import readline
import shlex
import drums
import time

screen = BasicScreenControl()
print('Enter a command to do something, e.g. `create name price`.')
print('To get help, enter `help`.')
while True:
    cmd, *args = shlex.split(input('> '))

    if cmd == 'drums':
        screen.updateText("Playing Drums !")
        drums.main()
    if cmd == 'exit':
        # cant get this to work
        screen.updateText('Thanks for playing')
        time.sleep(3)
        screen.updateText("")

        break

    elif cmd == 'help':
        print('...')

    elif cmd == 'create':
        name, cost = args
        cost = int(cost)
        # ...
        print('Created "{}", cost ${}'.format(name, cost))

    # ...

    else:
        print('Unknown command: {}'.format(cmd))

# /home/pi/logs/cronlog 2>&1
