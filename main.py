from paramiko import SSHClient, AutoAddPolicy, client
from rich import print, pretty, inspect
from hosts import hosts_map

pretty.install()

client = SSHClient()

# def exec_commands():

if __name__ == "__main__":
    client.load_host_keys('c:/Users/abhishek.singh/.ssh/known_hosts')
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())

    for user,iplist in hosts_map.items():
        for ip in iplist:
            print(user,ip)

            client.connect(ip, username=user)
            print("Following is the info for instance {}".format(ip))
            stdin, stdout, stderr = client.exec_command('cat /etc/os-release')
            print(f'STDOUT: {stdout.read().decode("utf8")}')
            print(f'STDERR: {stderr.read().decode("utf8")}')
            client.close()