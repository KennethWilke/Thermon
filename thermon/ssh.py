import paramiko

class SSHConnection(object):
    ''' SSH-based interface to systems '''
    def __init__(self, address, username, password, sshtimeout=10):
        self.address = address
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(address, username=username, password=password,
                         timeout=sshtimeout)

    def command(self, command):
        ''' Runs a shell command, returns (stdin, stdout, stderr) handles '''
        return self.ssh.exec_command(command)

    def call(self, command):
        stdin, stdout, stderr = self.command(command)
        return stdout.read(), stderr.read()

