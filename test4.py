import asyncio
import signal
import os
import sys
import time

from sweetpotato.config import settings
import subprocess


# async def run_async(loop=''):
#     cmd1 = f'eas build -p ios'
#
#     print("[INFO] Starting script...")
#     process = await asyncio.create_subprocess_shell(
#         cmd1, stdin=asyncio.subprocess.PIPE,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.STDOUT
#     )
#     await process.wait()
#     print("[INFO] Script is complete.")
#
#
# loop = asyncio.get_event_loop()
#
# tasks = [loop.create_task(run_async())]
# wait_tasks = asyncio.wait(tasks)
# loop.run_until_complete(wait_tasks)
#
# loop.close()
def run():
    command = [f'eas build', '-p', "ios"]
    # command = "eas build -p ios"
    # command = "eas login"
    os.chdir(settings.REACT_NATIVE_PATH)
    # lazy use of universal_newlines to prevent the need for encoding/decoding
    # p = await asyncio.create_subprocess_shell(command, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, )
    p = subprocess.Popen("", text=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    # os.system("eas login ")
    user = input("User: ")
    sys.stdin.write(f"{user}\n")
    # pswd = input("Password: ")
    # sys.stdin.write(f"{pswd}\n")
    try:
        outs, errs = p.communicate(input="{}\n{}\n".format('greysonlalonde13', "encarta1996"))
        # outs, errs = p.communicate(
        #     input="{}\n{}\n".format('greysonlalonde13', "encarta1996"))
        print(outs, errs)
        ...
    except subprocess.TimeoutExpired:
        p.kill()
        outs, errs = p.communicate()

    # stdout, stderr = p.communicate(timeout=10,
    #                                input="{}\n{}\n".format('greysonlalonde13', "encarta1996"))
    # print(stdout, stderr)
    # stderr is not connected to a pipe, so err is None


async def get(p):
    output, err = await p.communicate(input="{}\n{}\n".format('greysonlalonde13', "encarta1996"))
    print(output, err)


# asyncio.run(run())
run()
# we just want the result of the command
