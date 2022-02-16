#!/bin/env python
import random
import time

from os.path import join

from ganga.ganga import ganga
from ganga import Job, Executable, ArgSplitter


def get_status(jmain):
    """A simplified model of the monitoring for jobs on the Local backend"""

    def get_exit_code(f):
        import re
        with open(f) as statusfile:
            stat = statusfile.read()
        m = re.compile(
            r'^EXITCODE: (?P<exitcode>-?\d*)', re.M).search(stat)
        if m is None:
            return None
        else:
            return int(m.group('exitcode'))


    def get_pids(f):
        import re
        with open(f) as statusfile:
            stat = statusfile.read()
        m_pid = re.compile(r'^PID: (?P<pid>\d*)', re.M).search(stat)
        m_wrapper = re.compile(r'^WRAPPER: (?P<pid>\d*)', re.M).search(stat)
        pid = None
        wrapper = None
        if m_pid:
            pid = int(m_pid.group('pid'))
        if m_wrapper:
            wrapper = int(m_wrapper.group('pid'))
        return pid, wrapper

    
    statuses = {}
    for j in jmain.subjobs:
        id = j.id
        statuses[id] = 'submitted'
        try:
            statusfile = join(j.outputdir, '__jobstatus__')
            pid, wrapper_pid = get_pids(statusfile)
            if pid:
                statuses[id] = 'running'
            exitcode = get_exit_code(statusfile)
        except IOError as x:
            exitcode = None
        except Exception as x:
            print(f'Problem while monitoring job {id}')
            raise x

        if not exitcode is None:
            if exitcode == 0:
                statuses[id] = 'completed'
            else:
                statuses[id] = 'failed'
    return statuses

def main():
    """Simple demonstration of creating a job with a large number of subjobs 
    and then after a short period checking the status of them"""

    jmain = Job(application=Executable(exe='sleep'))
    jmain.splitter = ArgSplitter(args=
                                 [ [random.randint(1,4)] for _ in range(1000)])
    jmain.submit()

    time.sleep(60)

    try:
        t0 = time.monotonic()
        statuses = get_status(jmain)
        t1 = time.monotonic()
    except Exception as x:
        jmain.kill()
        raise x


    print(f'Evaluated status in {t1-t0:.4f} seconds')

    l = list(statuses.values())
    print(f'Job summary:')
    print(f'Submitted : {l.count("submitted")}')
    print(f'Running   : {l.count("running")}')
    print(f'Completed : {l.count("completed")}')
    print(f'Failed    : {l.count("failed")}')
    
    jmain.kill()


if __name__ == '__main__':
    main()
