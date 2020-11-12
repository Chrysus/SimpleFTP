# SimpleFTP

This is a quick and dirty ftp command line client written in Python (it requires Python 3).

I wrote this just to transfer a bunch of files to a specific ftp server, so it doesn't support a lot of standard ftp commands...yet...  But it's a decent starting point for anyone who wants to write their own ftp client or automate some ftp process.

----

To use:
```
$ python simple_ftp.py
ftp>
```
Then type your commands.  At the moment it supports the following commands:

```
connect       (server_address) (optional username) (optional password)
disconnect
ls
lls
pwd
lpwd
cd            (dir_path)
lcd           (dir_path)
put           (file_path)
sync
```

The sync command will find all the files in the local working directory (lpwd) that don't exist in the server's working directory (pwd), and it will put them from the client to the server.

That's about it!  Feel free to branch and extend the funcionality as much as you like!  Enjoy!
