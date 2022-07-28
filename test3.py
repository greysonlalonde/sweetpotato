# import subprocess
# import os
# import pty
# import time
import os
import pty
import subprocess
import time

from sweetpotato.config import settings
#
# os.chdir(settings.REACT_NATIVE_PATH)
# # Allocate the pty to talk to su with.
# master, slave = pty.openpty()
#
# # Open the process, pass in the slave pty as stdin.
# process = subprocess.Popen([f'eas', 'build', '-p', 'ios'], stdin=slave, stdout=subprocess.PIPE, shell=True)
#
# # Make sure we wait for the "Password:" prompt.
# # The correct way to do this is to read from stdout and wait until the message is printed.
# time.sleep(2)
#
# # Open a write handle to the master end of the pty to write to.
# pin = os.fdopen(master, "w")
# pin.write("password_to_enter\n")
# pin.flush()
#
# # Clean up
# print(process.communicate()[0])
# pin.close()
# os.close(slave)
import asyncio


#

async def run(cmd):
    master, slave = pty.openpty()
    os.chdir(settings.REACT_NATIVE_PATH)
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    # await asyncio.sleep(3)
    # pin = os.fdopen(master, "w")
    # pin.write("password_to_enter\n")
    # pin.flush()

    # Clean up
    stdout, stderr = await proc.communicate(b"password_to_enter\n")
    # pin.close()
    os.close(slave)

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')


#
#
asyncio.run(run(f'eas build -p ios'))
import asyncio
import sys


async def get_date():
    os.chdir(settings.REACT_NATIVE_PATH)
    code = f'eas build -p ios'
    #
    # Create the subprocess; redirect the standard output
    # into a pipe.
    print(sys.executable)
    proc = await asyncio.create_subprocess_shell(
        code,
        cwd=settings.REACT_NATIVE_PATH,
        stderr=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE)
    await asyncio.sleep(5)
    stdout_data, stderr_data = await proc.communicate(input=b'greysonlalonde13\n')
    # proc.stdin.write(b'greysonlalonde13\n')
    print(stderr_data, stdout_data)
    # communicate(input=b'greysonlalonde13\n')
    # Read one line of output.
    # data = await proc.stdout.readline()

    # Wait for the subprocess exit.
    await proc.wait()

# date = asyncio.run(get_date())
# print(f"Current date: {date}")
