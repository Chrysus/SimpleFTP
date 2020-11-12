import SimpleFTP

global ftp

def main():
    global ftp
    ftp = SimpleFTP.SimpleFTP()
    
    cli_loop()

# useage - connect [host] [username] [password]
def connect(args):
    global ftp

    host = args[0]
    username = None
    password = None
    if len(args) > 1:
        username = args[1]
        password = args[2]
    ftp.connect(host, username, password)

def disconnect():
    global ftp

    if ftp == None:
        return

    ftp.disconnect()

'''
REMOTE COMMANDS
'''
def change_dir(args):
    global ftp

    if ftp == None:
        return

    if len(args) <= 0:
        return

    # this handles autocomplete spaces in filenames
    # (example '/My\ Documents/')
    new_path = args[0].replace('\\', '')
    for a in args[1:]:
        a = a.replace('\\', '')
        new_path = new_path + ' ' + a

    ftp.change_dir(new_path)

def ls():
    # TODO - implement & hookup to CLI :)
    pass

def put_files(args):
    # TODO - implement
    pass

def put_file(args):
    global ftp

    if ftp == None:
        return

    filepath = args[0]
    ftp.put_file(filepath)

def get_files(args):
    pass

def get_file(filepath):
    # TODO - implement
    pass

def sync():
    global ftp

    if ftp == None:
        return

    ftp.sync()

'''
LOCAL COMMANDS
'''

def local_change_dir(args):
    global ftp

    if ftp == None:
        return
    if len(args) <= 0:
        return

    new_path = args[0].replace('\\', '')
    for a in args[1:]:
        a = a.replace('\\', '')
        new_path = new_path + ' ' + a
    
    ftp.local_change_dir(new_path)

    
def local_ls():
    global ftp
    
    if ftp == None:
        return

    ftp.local_ls();

def local_pwd():
    global ftp

    if ftp == None:
        return

    ftp.local_pwd()


'''
HELPER COMMANDS
'''

def diff():
    # TODO - implement...or remove ;)
    pass


'''
CLI COMMANDS
'''

def cli_loop():
    cmd = ''

    quit_commands = ['q', 'quit', 'exit']
    
    while (cmd.lower() not in quit_commands):
        cmd = input('ftp> ')
        process_command(cmd)

def process_command(command_line):
    global ftp
    
    if len(command_line) <= 0:
        return
    
    command_args = command_line.split(' ')
    cmd = command_args[0].lower()
    args = command_args[1:]

    quit_commands = ['q', 'quit', 'exit']

    print("Command: " + cmd)
    print("args: " + str(args))

    if cmd == 'connect':
        connect(args)
        return

    if cmd == 'disconnect':
        disconnect()
        return

    if cmd == 'ls':
        global ftp
        
        if ftp == None:
            return

        ftp.ls()
        return

    if cmd == 'cd':
        change_dir(args)
        return

    if cmd == 'put':
        put_file(args)
        return

    #HACK - Add *your* "quick connect' credentials here
    if cmd == 'qc':
        args = ["ftp.server.name.com", "username", "password"]
        connect(args)
        return

    # LOCAL COMMANDS

    if cmd == 'lls':
        local_ls();
        return

    if cmd == 'lcd':
        local_change_dir(args)
        return

    if cmd == 'sync':
        sync()
        return

    if cmd == 'lpwd':
        local_pwd()
        return

    if cmd in quit_commands:
        # TODO - verify connection status
        #        before attempting to disconnect
        disconnect()
        return
    
    print('NOT IMPLEMENTED')
    

if __name__ == '__main__':
    main()
