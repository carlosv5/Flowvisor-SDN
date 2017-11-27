#!/bin/bash
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
subprocess.call("fvctl -f /dev/null  add-slice -p '\n' video tcp:localhost:10001 admin@videoslice", shell=True)
subprocess.call("fvctl -f /dev/null add-slice -p '\n' non-video tcp:localhost:10002 admin@nonvideoslice", shell=True)


#Create the flowspaces

num = get_sw_port_number('s1', 'h1-')
subprocess.call("fvctl -f /dev/null add-flowspace s1-port3-video-src 1 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_src=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s1-port3-video-dst 1 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_dst=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s1-port3-non-video 1 1 in_port="+num+" non-video=7", shell=True)


num = get_sw_port_number('s1', 'h2-')
subprocess.call("fvctl -f /dev/null add-flowspace s1-port4-video-src 1 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_src=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s1-port4-video-dst 1 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_dst=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s1-port4-non-video 1 1 in_port="+num+" non-video=7", shell=True)


num = get_sw_port_number('s4', 'h3-')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port3-video-src 4 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_src=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s4-port3-video-dst 4 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_dst=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s4-port3-non-video 4 1 in_port="+num+" non-video=7", shell=True)


num = get_sw_port_number('s4', 'h4-')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port4-video-src 4 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_src=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s4-port4-video-dst 4 100 in_port="+num+",dl_type=0x0800,nw_proto=6,tp_dst=9999 video=7", shell=True)
subprocess.call("fvctl -f /dev/null add-flowspace s4-port4-non-video 4 1 in_port="+num+" non-video=7", shell=True)


num = get_sw_port_number('s1', 's3')
subprocess.call("fvctl -f /dev/null add-flowspace s1-port2-video 1 100 in_port=2 video=7", shell=True)


subprocess.call("fvctl -f /dev/null add-flowspace s3-video 3 100 any video=7", shell=True)


num = get_sw_port_number('s4', 's3')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port2-video 4 100 in_port=2 video=7", shell=True)


num = get_sw_port_number('s1', 's2')
subprocess.call("fvctl -f /dev/null add-flowspace s-port1-non-video 1 1 in_port=1 non-video=7", shell=True)


subprocess.call("fvctl -f /dev/null add-flowspace s2-non-video 2 1 any non-video=7", shell=True)


num = get_sw_port_number('s4', 's2')
subprocess.call("fvctl -f /dev/null add-flowspace s4-port1-non-video 4 1 in_port=1 non-video=7", shell=True)

subprocess.call("sleep 1m", shell=True)



