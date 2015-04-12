# daemon #

## Usage ##

Usage in python code:
```
#run-daemon.py

from emantools.daemon import Daemon

class DaemonClass(Daemon)
    interval = 5
    pid_file = '/var/run/daemon-class.pid'

    def __init__(self):
        self.main()

    def run(self):
        <code to run>

if __name__ == '__main__':
    DaemonClass()

```

Options for running:
```
# ./run-daemon.py start
# ./run-daemon.py stop
# ./run-daemon.py status
```

## Details ##

These are the methods you can override:
  * **run** specifies the actual process done by the daemon
  * **start** run when starting up the daemon
  * **stop** run when stopping the daemon
  * **status** run when stopping the code