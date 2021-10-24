from paramiko import SSHClient, AutoAddPolicy, client
from rich import print, pretty, inspect
from hosts import host_list

pretty.install()

client = SSHClient()

# def exec_commands():

if __name__ == "__main__":
    for host in host_list:
        # loading host keys
        client.load_host_keys('c:/Users/abhishek.singh/.ssh/known_hosts')
        client.load_system_host_keys()

        client.set_missing_host_key_policy(AutoAddPolicy())

        client.connect(host, username='ubuntu')
        print("Following is the info for instance {}".format(host))
        stdin, stdout, stderr = client.exec_command('cat /etc/os-release')
        # stdin2, stdout2, stderr2 = client.exec_command('wget https://inspector-agent.amazonaws.com/linux/latest/install')
        # stdin3, stdout3, stderr3 = client.exec_command('sudo bash install')
        print(f'STDOUT: {stdout.read().decode("utf8")}')
        print(f'STDERR: {stderr.read().decode("utf8")}')
        client.close()