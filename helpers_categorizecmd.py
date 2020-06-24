


def starts_with_one_of(s, slist):
    for tests in slist:
        if s.startswith(tests):
            return True
    return False



def categorize_cmd(cmd):
    """ This is based on pragmatism
        - group lots of small kernel stuff

    """ 
    if starts_with_one_of(cmd, ('systemd-',)):
        return '(systemd)'
    
    # These are more useful when kept separate
    #if starts_with_one_of(cmd, ('postgres', 'mysql', )):  # useful to keep separate, though
    #    return '(database)'

    if starts_with_one_of(cmd, ('oom_reaper','rcuos', 'rcu_', 'kworker', 'ksoftirqd', 'kthreadd', 'migration', 'watchdog',
                                'khelper', 'kdevtmpfs', 'kworker', 'irq/', 'cpuhp/', 'khungtaskd',
                                'irqbalance',
                                'init','getty', 'upstart', 'rsyslog', 'syslog',
    )):
        # non-driver kernel stuff
        return '(kernel+system)'
    
    elif starts_with_one_of(cmd, ('z_', 'zvol', 'zfs_', 'arc_', 'l2arc_', 'txg_', 'zil_', 'ext4', 'ecryptfs','jbd2','jfscommit','xfsmalloc')):
        # filesystem-supporting processes
        return '(io+filesystem)'
    elif starts_with_one_of(cmd, ('scsi', 'ata_', 'kswap', 'fsnotify',  'writeback', )):
        # directly related to disk IO
        return '(io+filesystem)'


    elif starts_with_one_of(cmd, ('gnome-', 'gvfs-', 'gvfsd-', 'gsd-','gdm')):
        return '(gui)'
    
    if '/' in cmd:
        cmd = cmd.split('/')[-1]

    return cmd
