import readline
import shlex
import drums
print('Enter a command to do something, e.g. `create name price`.')
print('To get help, enter `help`.')

while True:
    cmd, *args = shlex.split(input('> '))

    if cmd == 'drums':
        drums.main()
    if cmd == 'exit':
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
