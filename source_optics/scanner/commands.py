#  Copyright 2018-2019, Michael DeHaan
#  License: Apache License Version 2.0
#  -------------------------------------------------------------------------
#  commands.py - wrappers around executing shell commands, in the future,
#  no classes should be using subprocess directly (FIXME) so we can
#  centralize logging and timeouts/etc.
#  --------------------------------------------------------------------------

import io
import subprocess
import tempfile
import re
import shutil
import os

TIMEOUT = -1  # name of timeout command

ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')

#LOG = Logger()

def get_timeout():
    global TIMEOUT
    if TIMEOUT != -1:
        return TIMEOUT
    if shutil.which("timeout"):
        # normal coreutils
        TIMEOUT = "timeout"
    elif shutil.which("gtimeout"):
        # homebrew coreutils
        TIMEOUT = "gtimeout"
    else:
        TIMEOUT = None
    return TIMEOUT


def execute_command(repo, command, input_text=None, env=None, log_command=True, output_log=True, message_log=False,
                    timeout=None):
    """
    Execute a command (a list or string) with input_text as input, appending
    the output of all commands to the build log.
    """

    timeout_cmd = get_timeout()

    shell = True
    if type(command) == list:
        if timeout and timeout_cmd:
            command.insert(0, timeout)
            command.insert(0, timeout_cmd)
        shell = False
    else:
        if timeout and timeout_cmd:
            command = "%s %s %s" % (timeout_cmd, timeout, command)

    sock = os.environ.get('SSH_AUTH_SOCK', None)
    if env and sock:
        env['SSH_AUTH_SOCK'] = sock

    if log_command:
        LOG.debug("executing: %s" % command)
        if build:
            build.append_message(command)

    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               shell=shell, env=env)

    if input_text is None:
        input_text = ""

    stdin = io.TextIOWrapper(
        process.stdin,
        encoding='utf-8',
        line_buffering=True,
    )
    stdout = io.TextIOWrapper(
        process.stdout,
        encoding='utf-8',
    )
    stdin.write(input_text)
    stdin.close()

    out = ""
    for line in stdout:

        line = ansi_escape.sub('', line)

    if output_log or message_log:
        # FIXME: standardize logging
        print(line)

        out = "" + line


    process.wait()

    return out


def answer_file(answer):
    (_, fname) = tempfile.mkstemp()
    fh = open(fname, "w")
    fh.write("#!/bin/bash\n")
    fh.write("echo %s" % answer);
    fh.close()
    return fname