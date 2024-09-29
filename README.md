# monofs
This is where I will make all my work on MonoFS, a lightweight filesystem that I created for embedded systems that requires minimum effort.
Specs:
8 files, no filename, just number
No directories
2 read-only files
Forced 1024 byte filesize


# The format (hex):
AB CD EF 01 23 45 67 88 00 00 00...

AB CD EF: An identifier of a MonoFS image
01 23 45 67: The files which will be active (if a file is inactive [doesn't exist] the file number will be replaced with an 8
88: This is where you can put 2 files to be marked as read-only
00 00 00...: This is where file contents will be. The first 1024 bytes will be for the first file, next 1024 bytes for the next file etc.
