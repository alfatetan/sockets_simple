#!/usr/bin/python3.7
# The module for managing the sample_server

import sys


def man_help():
    print('Attention! The sample_server must be work before to use next '
          'commands.\nFor start work the sample_server you need load the '
          'sample_server into memory with command:\n'
          'python3.7 sample_server.py &\n'
          'or, you can use command --start this server_manager:\n'
          'python3 server_manager --start')
    print('--help\tthis help page')
    print('--start\tload the sample_server into memory and start standby mode')
    print('--run\tstart work the ')
    return


def server_run():
    print('server_run')
    return


def server_stop():
    print('server_stop')
    return


def server_status():
    print('server_status')
    return


if __name__ == '__main__':
    commands = {
                   '--help': man_help,
                   '--start': server_run,
                   '--stop': server_stop,
                   '--status': server_status,
                    '--run': server_run,
               }

    for arg in sys.argv:
        if commands.get(arg, False):
            commands[arg]()

