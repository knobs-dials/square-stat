


def starts_with_one_of(s, stringlist):
    for test in stringlist:
        if s.startswith(test):
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
                                'khelper', 'kdevtmpfs', 'kworker', 'irq/', 'cpuhp/', 'khungtaskd', 'khugepaged',
                                'kcompactd',
                                'irqbalance', 'devfreq', 'mm_percpu_wq',
                                'kstrp',
                                'edac-', 'acpid', 'acpi_',
                                #'nv_queue',
                                'init','getty', 'upstart', 'rsyslog', 'syslog',
    )):
        # non-driver kernel stuff
        return '(kernel+system)'

    elif starts_with_one_of(cmd, (
        # filesystem-supporting processes
        'z_', 'zvol', 'zfs_', 'arc_', 'l2arc_', 'txg_', 'zil_', 'dp_zil_', 'dp_sync_', 'dbu_evict','dbuf_evict',
        'spl_',
        'ext4', 'ecryptfs', 'lvmetad',
        'jbd2', 'xfsmalloc','xfsalloc','xfs_', 'jfsIO','jfsSync','jfsCommit','jfscommit',
        # more directly related to disk IO
        'scsi', 'ata_', 'kswap', 'fsnotify',  'writeback', 'kblockd', 'kthrotld', 'kintegrityd', 'raid5wq',
        )):
        return '(io+filesystem)'

    # security stuff 
    #   'kauditd', 'polkitd'

    # higher level system stuff
    #   'journalctl', 'networkd-'

    elif starts_with_one_of(cmd, ('UVM ', 'docker', 'iprt-', 'containerd')):
        return '(vm+container)'

    elif starts_with_one_of(cmd, ('gnome-', 'gvfs-', 'gvfsd-', 'gsd-','gdm', 'at-spi',
                                 #'gvfs' # maybe include GUI-supporting stuff in this too?     also e.g. dbuf?
                                 )):
        return '(gui)'
    
    if '/' in cmd:
        cmd = cmd.split('/')[-1]

    return cmd

if __name__ == '__main__':
    # testing the above 
    import subprocess
    p = subprocess.Popen("ps --no-header -eo comm",shell=True, stdout=subprocess.PIPE)        # rss is non-swapped physical
    out,_ = p.communicate()
    for name in sorted(set(out.splitlines())):
        cat = categorize_cmd(name)
        if len(cat)==0 or cat[0]!='(':
            print( '%20s %s'%(name, cat ) )
    