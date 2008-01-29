#!/usr/bin/env python
#daemon.py

import os
import sys
import time
import datetime
import create_daemon

PIDFILE = '/var/run/start-stop.pid'

def logit():
    fp = open('test.log','a')
    current_time = datetime.datetime.now()
    #fp.write('Hello\n')
    fp.write(str(current_time) + '\n')
    fp.close()

class Daemon(object):
    interval = 5
    pidfile = PIDFILE

    def __init__(self):
        self.main()

    def get_running_pid(self):
        try:
            fp = open(self.pidfile, 'r')
        except IOError:
            return None
        self.pid = fp.read()
        fp.close()
        return self.pid

    def write_pid(self):
        fp = open(self.pidfile, 'w')
        fp.write(str(os.getpid()))
        fp.close()
        return True

    def get_status(self):
        if self.get_running_pid() is not None:
            return True

    def run(self):
        logit()

    def status(self):
        if self.get_status():
            print 'Daemon running'
        else:
            print 'Daemon not running'
        return True

    def start(self):
        print 'Starting Daemon ...'
        if self.get_status():
            print 'Daemon already started.'
            return False
        create_daemon.createDaemon()
        self.write_pid()
        while True:
            time.sleep(self.interval)
            self.run()
        return True

    def stop(self):
        print 'Stopping Daemon ...'
        pid = self.get_running_pid()
        if pid is None:
            print 'Daemon not started.'
            return False
        try:
            os.kill(int(pid), 15)
        except OSError:
            pass
        os.unlink(self.pidfile)
        return True

    def restart(self):
        self.stop()
        return self.start()

    def print_usage(self):
        print 'WRONG'

    def main(self):
        self.filename = sys.argv[0]
        try:
            command = sys.argv[1]
        except IndexError:
            command = 'help'
        if command == 'start':
            self.start()
        elif command == 'stop':
            self.stop()
        elif command == 'restart':
            self.restart()
        elif command == 'status':
            self.status()
        else:
            self.print_usage()


if __name__ == '__main__':
    Daemon()

