import netmiko

# Define the network device
router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "cisco",
    "password": "cisco"
}

# Connect to the network device
net_connect = netmiko.ConnectHandler(**router)

# Send a command to the network device
output = net_connect.send_command("show ip interface brief")

# Print the output of the command
print(output)

# Disconnect from the network device
net_connect.disconnect()
