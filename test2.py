# import sys
# from subprocess import PIPE, Popen
#
EXTERNAL_PROG = 'build -p ios --profile preview'
#
# p = Popen(['eas', EXTERNAL_PROG], stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
#
# print(p.stdout.readline())
# print(p.stdout.readline())
# p.stdin.write(b'greysonlalonde13\n')
# p.stdin.write(b'2\n')
# p.stdin.flush()
# print(p.stdout.readline())
# print(p.stdout.readline())
# from subprocess import Popen, PIPE
from sweetpotato.config import settings
#
# p = Popen([f'eas build', 'build', '-p', 'ios'], cwd=settings.REACT_NATIVE_PATH, stdout=PIPE, stdin=PIPE, stderr=PIPE,
#           shell=True)
# p.stdin.write(b'\ngreysonlalonde13\n')
# # p.stdin.write(b'2\n')
# p.communicate(input=b'greysonlalonde13\n')
# print(p.__dict__)
import subprocess
import os
import pty
import time

# Allocate the pty to talk to su with.
# master, slave = pty.openpty()
# process = subprocess.Popen([f'eas', 'build', '-p', 'ios'], stderr=subprocess.PIPE, stdout=subprocess.PIPE,
#                            bufsize=0)
#
# for out in iter(process.stdout.readline, b""):
#     print(out)
import os
import pty

command = 'id'

scmd = "sudo -S %s" % (command)


def reader(fd):
    return os.read(fd, 50)


def writer(fd):
    return os.write(fd, b'password')


# pty.spawn([f'eas', 'build', '-p', 'ios'], reader, writer)
import os
import pty


def inpty(argv):
    output = []

    # def reader(fd):
    #     c = os.read(fd, 1024)
    #     while c:
    #         output.append(c)
    #         c = os.read(fd, 1024)

    os.chdir(settings.REACT_NATIVE_PATH)
    pty.spawn(argv, reader, writer, )
    pin = os.fdopen(master, "w")
    pin.write("password_to_enter\n")
    pin.flush()
    return b''.join(output).decode('utf-8')


print("Command output: " + inpty([f'eas', 'build', '-p', 'ios']))
# Open the process, pass in the slave pty as stdin.
# process = subprocess.Popen([f'eas build', 'build', '-p', 'ios'],
#                            cwd=settings.REACT_NATIVE_PATH,
#                            stdin=slave,
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE,
#                            shell=True)
# print(process)
# # Make sure we wait for the "Password:" prompt.
# # The correct way to do this is to read from stdout and wait until the message is printed.
# time.sleep(2)
# print("sleep")
#
# # Open a write handle to the master end of the pty to write to.
# pin = os.fdopen(master, "w")
# print(pin)
# pin.write("greysonlalonde13\n")
# print(pin)
# pin.write("password_to_enter\n")
# print(pin)
# pin.flush()
# print(pin)
# # Clean up
# # print(process.communicate()[0], "pppp")
# pin.close()
# os.close(slave)
