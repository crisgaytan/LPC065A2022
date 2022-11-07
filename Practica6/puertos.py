import nmap

host = input(" Introduce la IP objetivo: ")
nm = nmap.PortScanner()
results=nm.scan(host)

print("Host : %s" % host)
print("State : %s" % nm[host].state())
for proto in nm[host].all_protocols():
	print("Protocol : %s" % proto)
	lport = nm[host][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port: %s\tstate : %s" % (port, nm[host][proto][port]["state"]))
