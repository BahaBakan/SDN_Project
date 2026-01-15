'''
mininet> dump
<Host lab1: lab1-eth0:10.0.0.101 pid=35117> 
<Host lab2: lab2-eth0:10.0.0.102 pid=35119> 
<Host lab3: lab3-eth0:10.0.0.103 pid=35121> 
<Host lab4: lab4-eth0:10.0.0.104 pid=35123> 
<Host lab5: lab5-eth0:10.0.0.105 pid=35125> 
<Host lab6: lab6-eth0:10.0.0.106 pid=35127> 
<Host pc1: pc1-eth0:10.0.0.1 pid=35129> 
<Host pc2: pc2-eth0:10.0.0.2 pid=35131> 
<Host pc3: pc3-eth0:10.0.0.3 pid=35133> 
<Host pc4: pc4-eth0:10.0.0.4 pid=35135> 
<Host pc5: pc5-eth0:10.0.0.5 pid=35137> 
<Host pc6: pc6-eth0:10.0.0.6 pid=35139> 
<Host pc12: pc12-eth0:10.0.0.12 pid=35141> 
<Host pc13: pc13-eth0:10.0.0.13 pid=35143> 
<Host pc14: pc14-eth0:10.0.0.14 pid=35145> 
<Host pc15: pc15-eth0:10.0.0.15 pid=35147> 
<Host pc16: pc16-eth0:10.0.0.16 pid=35149> 
<Host pc17: pc17-eth0:10.0.0.17 pid=35151> 
<Host pc18: pc18-eth0:10.0.0.18 pid=35153> 
<Host pc19: pc19-eth0:10.0.0.19 pid=35155> 
<OVSSwitch{'protocols': 'OpenFlow10'} hub_0: lo:127.0.0.1,hub_0-eth1:None,hub_0-eth2:None,hub_0-eth3:None,hub_0-eth4:None,hub_0-eth5:None pid=35160> 
<OVSSwitch{'protocols': 'OpenFlow10'} sw_3: lo:127.0.0.1,sw_3-eth1:None,sw_3-eth2:None,sw_3-eth3:None,sw_3-eth4:None,sw_3-eth5:None pid=35163> 
<OVSSwitch{'protocols': 'OpenFlow10'} sw_4: lo:127.0.0.1,sw_4-eth1:None,sw_4-eth2:None,sw_4-eth3:None,sw_4-eth4:None,sw_4-eth5:None pid=35166> 
<OVSSwitch{'protocols': 'OpenFlow10'} sw_lab: lo:127.0.0.1,sw_lab-eth1:None,sw_lab-eth2:None,sw_lab-eth3:None,sw_lab-eth4:None,sw_lab-eth5:None,sw_lab-eth6:None,sw_lab-eth7:None pid=35169> 
<OVSSwitch{'protocols': 'OpenFlow10'} sw_pc0: lo:127.0.0.1,sw_pc0-eth1:None,sw_pc0-eth2:None,sw_pc0-eth3:None,sw_pc0-eth4:None,sw_pc0-eth5:None,sw_pc0-eth6:None pid=35172> 
<RemoteController{'ip': '127.0.0.1', 'port': 6633} c0: 127.0.0.1:6633 pid=35111> 
'''

from mininet.topo import Topo

class RealCorporateTopo(Topo):
    def build(self):

        # Switches (dpid veriyoruz ki hata olmasın)
        sw_lab = self.addSwitch('sw_lab', dpid='0000000000000011')
        sw_pc0 = self.addSwitch('sw_pc0', dpid='0000000000000012')
        hub_0  = self.addSwitch('hub_0',  dpid='0000000000000013')
        sw_3   = self.addSwitch('sw_3',   dpid='0000000000000031')
        sw_4   = self.addSwitch('sw_4',   dpid='0000000000000032')

        # Basit omurga
        self.addLink(sw_pc0, sw_lab)
        self.addLink(sw_pc0, sw_3)
        self.addLink(sw_pc0, sw_4)

        # Hub segment
        self.addLink(sw_pc0, hub_0)

        # ================= LAB HOSTS =================
        # lab1–lab6 → 10.0.0.101–106
        for i in range(1, 7):
            ip = f"10.0.0.{100 + i}/24"
            h = self.addHost(f'lab{i}', ip=ip)
            self.addLink(sw_lab, h)

        # ================= PC CORE =================
        # pc1–pc2 → 10.0.0.1–2
        for i in [1, 2]:
            ip = f"10.0.0.{i}/24"
            h = self.addHost(f'pc{i}', ip=ip)
            self.addLink(sw_pc0, h)

        # ================= HUB ARKASI =================
        # pc3–pc6 → 10.0.0.3–6
        for i in [3, 4, 5, 6]:
            ip = f"10.0.0.{i}/24"
            h = self.addHost(f'pc{i}', ip=ip)
            self.addLink(hub_0, h)

        # ================= BRANCH-1 =================
        # pc12–pc15 → 10.0.0.12–15
        for i in range(12, 16):
            ip = f"10.0.0.{i}/24"
            h = self.addHost(f'pc{i}', ip=ip)
            self.addLink(sw_3, h)

        # ================= BRANCH-2 =================
        # pc16–pc19 → 10.0.0.16–19
        for i in range(16, 20):
            ip = f"10.0.0.{i}/24"
            h = self.addHost(f'pc{i}', ip=ip)
            self.addLink(sw_4, h)

topos = {'realcorp': RealCorporateTopo}
