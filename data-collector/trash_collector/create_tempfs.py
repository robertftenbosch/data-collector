import os

# Size of temporary file system in bytes (150 GB)
temp_size = 150 * 1024 * 1024 * 1024

# Mount point for temporary file system
temp_mount_point = "/mnt/tempfile"

# Create temporary file system
os.system("sudo mkdir -p " + temp_mount_point)
os.system("sudo dd if=/dev/zero of=" + temp_mount_point + "/tempfile bs=1 count=0 seek=" + str(temp_size))
os.system("sudo mkfs.ext4 " + temp_mount_point + "/tempfile")

# Mount temporary file system
os.system("sudo mount -t ext4 -o loop " + temp_mount_point + "/tempfile " + temp_mount_point)
# sudo chown root:root /path/to/your/script/script.py
# sudo chmod +x /path/to/your/script/script.py
# sudo chmod u+s /path/to/your/script/script.py