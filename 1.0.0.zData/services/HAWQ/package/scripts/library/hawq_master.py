import os
import utilities

from resource_management.core.exceptions import ComponentIsNotRunning
from resource_management import *

def install(env):
    import params

    # Add Hawq User
    User(params.hawq_user, action="create", groups="hadoop", password=params.hawq_password, shell="/bin/bash")
    utilities.appendBashProfile(params.hawq_user, "source %s;" % params.hawq_environment_path, run=True)

    # Hostfile Segments
    TemplateConfig(
        params.hawq_hostfile_path,
        owner=params.hawq_user, mode=0644
    )

    Execute("gpssh-exkeys -f %s;" % params.hawq_hostfile_path, user=params.hawq_user, environment={})

    utilities.kernelParameters({
        'sysctl.kernel.shmmax': '500000000',
        'sysctl.kernel.shmmni': '4096',
        'sysctl.kernel.shmall': '4000000000',
        'sysctl.kernel.sem': '250 512000 100 2048',
        'sysctl.kernel.sysrq': '1',
        'sysctl.kernel.core_uses_pid': '1',
        'sysctl.kernel.msgmnb': '65536',
        'sysctl.kernel.msgmax': '65536',
        'sysctl.kernel.msgmni': '2048',
        'sysctl.net.ipv4.tcp_syncookies': '0',
        'sysctl.net.ipv4.ip_forward': '0',
        'sysctl.net.ipv4.conf.default.accept_source_route': '0',
        'sysctl.net.ipv4.tcp_tw_recycle': '1',
        'sysctl.net.ipv4.tcp_max_syn_backlog': '200000',
        'sysctl.net.ipv4.conf.all.arp_filter': '1',
        'sysctl.net.ipv4.ip_local_port_range': '1025 65535',
        'sysctl.net.core.netdev_max_backlog': '200000',
        'sysctl.vm.overcommit_memory': '2',
        'sysctl.fs.nr_open': '3000000',
        'sysctl.kernel.threads-max': '798720',
        'sysctl.kernel.pid_max': '798720',
        'sysctl.net.core.rmem_max': '2097152',
        'sysctl.net.core.wmen_max': '2097152'
    })


def configure():
    pass

def start():
    pass

def stop():
    pass

def is_running():
    pass