import paramiko
import argparse
from tqdm import tqdm

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('hostname', help='SSH server hostname')
parser.add_argument('username', help='SSH username')
parser.add_argument('remote_path', help='Path to remote binary file')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-k', '--key', help='Path to SSH private key file')
group.add_argument('-p', '--password', help='SSH password')
args = parser.parse_args()

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if args.key:
    # Load private key and connect using SSH key authentication
    private_key = paramiko.RSAKey.from_private_key_file(args.key)
    client.connect(args.hostname, username=args.username, pkey=private_key)
else:
    # Connect using password authentication
    client.connect(args.hostname, username=args.username, password=args.password)

# Get size of remote binary file
with client.open_sftp() as sftp:
    remote_file_size = sftp.stat(args.remote_path).st_size

# Load binary file into memory with progress bar
with client.open_sftp() as sftp:
    with sftp.open(args.remote_path, 'rb') as remote_file:
        binary_data = bytearray()
        with tqdm(total=remote_file_size, unit='B', unit_scale=True, desc='Loading') as progress_bar:
            for chunk in iter(lambda: remote_file.read(1024), b''):
                binary_data += chunk
                progress_bar.update(len(chunk))

# Close SSH connection
client.close()

# Do something with binary data in memory
print(binary_data)