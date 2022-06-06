import re

ipv4_regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
address = input("Adres IP:")
print(bool(ipv4_regex.match(address)))
