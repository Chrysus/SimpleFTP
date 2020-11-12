import os

from ftplib import FTP
from glob import glob
from os import path


class SimpleFTP():

    def __init__(self):
        self.ftp = None
        self.lpwd = os.getcwd()


    def connect(self, host, username, password):

        if self.ftp != None:
            #TODO - check connection state
            #     - disconnect if necessary
            self.ftp = None
    
        try:
            self.ftp = FTP(host)
        except:
            print("Connection error")
            return

        if (len(username) > 0):
            try:
                self.ftp.login(user=username, passwd=password)
            except:
                print("Login error")
                return

    def disconnect(self, force=False):
        if force:
            try:
                self.ftp.close()
            except:
                print("ERROR - could not force quit!")
            return
        
        try:
            self.ftp.quit()
        except:
            print("ERROR - could not disconnect!")
            return

        self.ftp = None

    '''
    REMOTE COMMANDS
    '''

    def change_dir(self, directory):
        try:
            self.ftp.cwd(directory)
        except:
            print("ERROR - did not change directory")
            return
        
        print("changed to: " + directory)

    def ls(self):
        if self.ftp == None:
            return
        
        self.ftp.dir()

    def put_files(self):
        # TODO - implement this :)
        pass

    def put_file(self, filepath):
        print(filepath)

        # try local file first
        fullpath = self.lpwd + '/' + filepath
        
        if path.isfile(fullpath) != True:
            # try abspath next
            fullpath = filepath
            if path.isfile(fullpath):
                print('ERROR - file not found')
                return
        
        filename = path.basename(fullpath)
        fd = open(fullpath, 'rb')

        if fd:
            try:
                self.ftp.storbinary('STOR ' + filename, fd)
            except:
                print('ERROR - put failed: ' + filename)

            fd.close()
            
        print("file put complete: " + filename)

    # sync finds all the regular files in the client's pwd
    #      that don't exist in the server's pwd, and puts
    #      them from the client to the server.
    def sync(self):
        # find local files
        dir_path = self.lpwd + '/*'
        local_files = glob(dir_path)

        # find remote files
        remote_files_gen = self.ftp.mlsd()
        remote_files = []
        for filename, filestats in remote_files_gen:
            remote_files.append(filename)
        
        # get diff
        delta = []
        for filepath in local_files:
            filename = path.basename(filepath)
            isfile = path.isfile(filepath)
            if isfile and filename not in remote_files:
                delta.append(filename)
                
        for f in delta:
            self.put_file(f)


    '''
    LOCAL COMMANDS
    '''

    def local_change_dir(self, new_path):
        new_dir = new_path
        if path.isabs(new_dir) != True:
            new_dir = self.lpwd + '/' + new_path
            new_dir = path.abspath(new_dir)
            
        if path.exists(new_dir):
            self.lpwd = new_dir

    def local_ls(self):
        dir_path = path.abspath(self.lpwd) + '/*'
        local_files = glob(dir_path)

        for f in local_files:
            print(path.basename(f))

    def local_pwd(self):
        print(self.lpwd)
