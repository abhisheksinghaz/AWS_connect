from paramiko import SSHClient, AutoAddPolicy, client
from rich import print, pretty, inspect

pretty.install()

client = SSHClient()

hosts = ['10.0.2.148','10.0.2.248']

for host in hosts:
    # loading host keys
    client.load_host_keys('c:/Users/abhishek.singh/.ssh/known_hosts')
    client.load_system_host_keys()

    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(host, username='magicqa')

    stdin, stdout, stderr = client.exec_command('cat /etc/os-release')
    print(f'STDOUT: {stdout.read().decode("utf8")}')
    print(f'STDERR: {stderr.read().decode("utf8")}')