# IP Allow List Update Script
# Author: jojo2500

allow_list_file = "allow_list.txt"
remove_list_file = "remove_list.txt"

# Read current allow list
with open(allow_list_file, "r") as f:
    ip_addresses = f.read().split()

# Read remove list
with open(remove_list_file, "r") as f:
    remove_list = f.read().split()

# Remove IPs found in remove_list from ip_addresses
for ip in remove_list:
    if ip in ip_addresses:
        ip_addresses.remove(ip)

# Write updated allow list back to file
with open(allow_list_file, "w") as f:
    f.write("\n".join(ip_addresses))
