import subprocess
def get_sw_port_number(switch_name, port_name):
    cmd = 'sudo ovs-ofctl show ' + switch_name + '| grep ' + port_name + '| sed -e "s/(.*//"'
    num = subprocess.Popen( cmd,
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE).communicate()[0].rstrip().lstrip()
    return num

subprocess.call("sudo service flowvisor start", shell=True)
#Create the slices
#Esto pide passwords
subprocess.call("fvctl  -f /dev/null add-slice -p '\n' upper tcp:localhost:10001 admin@upperslice", shell=True)
subprocess.call("fvctl  -f /dev/null add-slice -p '\n' lower tcp:localhost:10002 admin@lowerslice", shell=True)

#Create the flowspaces
#Upper slice
subprocess.call("fvctl -f /dev/null add-flowspace s1-port1 1 1 in_port=1 upper=7", shell=True)
num = get_sw_port_number('s1', 'h1-')
subprocess.call("fvctl -f /dev/null add-flowspace s1-port3 1 1 in_port="+num+" upper=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s2 2 1 any upper=7", shell=True)
num = get_sw_port_number('s4', 's2')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port1 4 1 in_port=1 upper=7", shell=True)
num = get_sw_port_number('s4', 'h3-')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port3 4 1 in_port="+num+" upper=7", shell=True)

#Lower slice
num = get_sw_port_number('s1', 's3')
subprocess.call("fvctl -f /dev/null add-flowspace s1-port2 1 1 in_port=2 lower=7", shell=True)
num = get_sw_port_number('s1', 'h2-')
subprocess.call("fvctl -f /dev/null add-flowspace s1-port4 1 1 in_port="+num+" lower=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s3 3 1 any lower=7", shell=True)
num = get_sw_port_number('s4', 's3')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port2 4 1 in_port=2 lower=7", shell=True)
num = get_sw_port_number('s4', 'h4-')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port4 4 8 in_port="+num+" lower=7", shell=True)
subprocess.call("sleep 1m", shell=True)




