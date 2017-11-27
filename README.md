# Flowvisor-SDN
***
VNX Scenario using flowvisor and POX controllers in order to communicate virtual hosts (SDN)

This is a project for Technical University of Madrid - DIT (Departamento de Ingeniería de Sistemas Telemáticos).

Flowvisor part has been followed in this tutorial: [Flowvisor Tutorial] (https://github.com/onstutorial/onstutorial/wiki/Flowvisor-Exercise).

In order to run the scenarios, these are the steps:

1. [Download VNX] (http://web.dit.upm.es/vnxwiki/index.php/Main_Page)

2. Download the appropriate filesystem: rootfs_lxc_ubuntu64 and have it in /usr/share/vnx/filesystems/rootfs_lxc_ubuntu64.

3. Download Flowvisor, mininet or a virtual machine that have both of them.

4. In order to start one of the scenarios, you have to write the commands:

# Switch of virtual machines
sudo vnx -f Name_of_scenario.xml -v -t
 
# Simple scenario (slices upper y lower)
sudo vnx -f Name_of_scenario.xmll -x start-all-scenario1
# Complex scenario (slices video y non-video)
sudo vnx -f Name_of_scenario.xml -x start-all-scenario2
 
# Destroy the scenario
sudo vnx -f Name_of_scenario.xml -x destroy-all-scenario1
sudo vnx -f Name_of_scenario.xml -x destroy-all-scenario2
 
# Switch off virtual machines
sudo vnx -f Name_of_scenario.xml --destroy

There are you scenarios (two xml files), the second one joins mininet with vnx, so you have to start mininet before starting the scenario:
sudo mn --custom flowvisor_topo_vnx.py --topo fvtopo --link tc --controller remote --mac --arp
