from paramiko import SSHClient, AutoAddPolicy, client
from rich import print, pretty, inspect
from hosts import hosts_map

def exec_commands():
    # stdin, stdout, stderr = client.exec_command('cat /etc/os-release')
    # stdin, stdout, stderr = client.exec_command('uname -r')
    stdin, stdout, stderr = client.exec_command('sudo yum update -y')
    print(f'STDOUT: {stdout.read().decode("utf8")}')

    
# pretty.install()
client = SSHClient()

if __name__ == "__main__":
    client.load_host_keys('c:/Users/abhishek.singh/.ssh/known_hosts')
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())

    for user,iplist in hosts_map.items():
        for ip in iplist:

            print("Establishing connection to {}".format(ip))
            client.connect(ip, username=user)
            exec_commands()
            # print('*'*100)
            print("Concluding the reports/output of : {} \n\n".format(ip))
            print('*'*100)
            client.close()