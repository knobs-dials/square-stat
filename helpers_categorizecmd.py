#!/usr/bin/python3


def starts_with_one_of(s, stringlist): # TODO: change to regexp so I can more easily express  whole name ,startswith, word-boundary, and such
    for test in stringlist:
        if s.startswith(test):
            return True
    return False



def categorize_cmd(cmd:str, merge_databases=False, merge_services=False):
    """ This is based on pragmatism
        - group lots of small kernel stuff

        Takes str, or bytes (if bytes, assumes we can decode as utf8)
    """ 
    if type(cmd) is bytes:
        cmd = cmd.decode('utf8')

    if starts_with_one_of(cmd, (
        'systemd-',
        '(sd-pam)',
        'journalctl',
        )):
        return '(systemd)'
    
    # These are more useful when kept separate
    if merge_databases and starts_with_one_of(cmd, (
        'postgres', 
        'mysql',
        'rabbitmq', 'beam.smp',
        'mosquitto',
        'memcached',
        )):  # useful to keep separate, though
        return '(database)'

    if starts_with_one_of(cmd, (# drivery stuff
                                'oom_reaper','rcuos', 'rcu_', 'kworker', 'ksoftirqd', 'kthreadd', 'migration', 'watchdog',
                                'khelper', 'kdevtmpfs', 'kworker', 'irq/', 'cpuhp/', 'khungtaskd', 'khugepaged',
                                'kcompactd',
                                'irqbalance', 'devfreq', 'mm_percpu_wq',
                                'kstrp',
                                'edac-', 'acpid', 'acpi_',
                                'nv_queue',
                                'ttm_swap',
                                'ksmd',
                                #'nvidia-',

                                # support stuff
                                'init','getty', 'upstart', 'rsyslog', 'syslog',
                                'kauditd', 'polkitd', # security stuff 
                                'packagekitd', 'unattended-','cleanupd', #update stuff
                                'runsv', 'runsvdir', 'my_init', # inside containers, probably

                                'accounts-daemon', # look up properly
                                'xprtiod', # look up properly
                                'unattended-',

    )):
        return '(kernel+system)'

    if starts_with_one_of(cmd, (
        # filesystem-supporting processes
        'z_', 'zvol', 'zfs_', 'arc_', 'l2arc_', 'txg_', 'zil_', 'dp_zil_', 'dp_sync_', 'dbu_evict','dbuf_evict', 'metaslab_group',
        'zed',
        'spl_',
        'ext4', 'ecryptfs', 'lvmetad',
        'jbd2', 'xfsmalloc','xfsalloc','xfs_', 'jfsIO','jfsSync','jfsCommit','jfscommit',
        # more directly related to disk IO
        'scsi', 'ata_', 'kswap', 'fsnotify',  'writeback', 'kblockd', 'kthrotld', 'kintegrityd', 'raid5wq',

        'smartd',
        'udisksd',
        'loop0', 'loop1',

        'crypto', #practically
        )):
        return '(io+filesystem)'

    if starts_with_one_of(cmd, (
        'agetty',
        'atd', 'cron', #'anacron',
        'runsv','runsvdir',
        'nvidia-',
        'fancontrol',

        'dbus-', # arguable

        'charger_manager',

        )):
        return '(local-services)'

    if merge_services and starts_with_one_of(cmd, (
        'ipv6_addrconf',
        'wpa_supplicant', 'cfg80211',

        'networkd-',

        'inetutils-inetd',
        'rpc.', 'rpcbind', 'rpciod'
        'ntpd',

        'smbd',
        'cups', 'lpqd',
        'nfsd', 'xprtiod', 'blkmapd',
        'lockd',
        'rpc.', 'rpcbind', 'rpciod',

        'tmux', 'screen',
        'avahi-d',

        #'sshd', # commented, this is something I want to know separately

        'seaf',
        'apache', 'htcacheclean',
        'nginx',

        'networkd-',
        'winbindd',
        'rpc.idmapd',
        'rpc.mountd',
        'rpciod',
        'rpcbind',
        'cupsd',
        'cups-',
        'epmd',
        'lpqd',
        'nfsd', 'blkmapd',
        'smbd',

        'pickup',

        'munin-node',
        )):
        return '(network-services)'

    elif starts_with_one_of(cmd, ('UVM ', 'docker', 'iprt-', 'containerd', 'VBox')):
        return '(vm+container)'

    elif starts_with_one_of(cmd, ('gnome-', 'gvfs-', 'gvfsd-', 'gsd-','gdm', 'at-spi', 'colord', 'gdostep',
                                 #'gvfs' # maybe include GUI-supporting stuff in this too?     also e.g. dbuf?
                                 )):
        return '(gui)'



    
    if '/' in cmd:
        cmd = cmd.split('/')[-1]

    return cmd

if __name__ == '__main__':
    # testing the above 
    import subprocess
    p = subprocess.Popen("ps --no-header -eo comm",shell=True, stdout=subprocess.PIPE, encoding='u8')        # rss is non-swapped physical
    out,_ = p.communicate()
    for name in sorted(set(out.splitlines())):
        #name = name.encode('u8')
        cat = categorize_cmd(name,True,True)
        
        extra=''
        if len(cat)==0 or cat[0]!='(':
            extra = 'UNCAT'
        print( '%20s %10s   %s'%(name, extra, cat ) )
    
