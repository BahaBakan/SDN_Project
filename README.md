# SDN-Based Dynamic Network Management and Security

Bu proje, Yazılım Tanımlı Ağlar (SDN) mimarisi kullanılarak kurumsal bir ağ topolojisinde dinamik erişim kontrolü (ACL), hizmet kalitesi (QoS) yönetimi ve trafik izleme (Port Mirroring) özelliklerini simüle eder.

## 🚀 Proje Özellikleri

Proje kapsamında dört temel senaryo uygulanmıştır:

1. **Tekil Cihaz Bazlı ACL:** `lab1` (10.0.0.101) cihazının `pc16` (10.0.0.16) cihazına gönderdiği ICMP (ping) paketleri spesifik olarak engellenir.
2. **Subnet Seviyesi Kısıtlama:** `LAB` alt ağı (10.0.0.96/27) ile `BRANCH` alt ağı (10.0.0.16/28) arasındaki tüm IP iletişimi toplu olarak izole edilir.
3. **Hizmet Kalitesi (QoS) Yönetimi:** Kritik cihazlar (`pc1`, `pc2`) arasındaki trafik, Linux HTB (Hierarchical Token Bucket) kuyruk yapısı kullanılarak yüksek öncelikli (Queue 1) olarak iletilir.
4. **Port Mirroring:** Güvenlik analizi için `pc1` ve `pc2` arasındaki trafik, iletişimi aksatmadan `pc19` cihazına eş zamanlı olarak kopyalanır.

## 🛠 Kullanılan Teknolojiler

* **Simülasyon:** Mininet
* **SDN Controller:** POX Controller (Python)
* **Protokol:** OpenFlow 1.0
* **İzleme:** tcpdump

## 📐 Ağ Topolojisi

Ağ, merkezi bir çekirdek anahtar (`sw_pc0`) etrafında şekillenmiş yıldız topolojisine sahiptir. Cihaz grupları şu şekildedir:
* **CORE:** pc1, pc2 (Kritik cihazlar)
* **LAB:** lab1 - lab6
* **BRANCH:** pc12 - pc19

## 🖥️ Kurulum ve Çalıştırma

1. **Topolojiyi Başlatın:**
   ```bash
   sudo mn --custom topo.py --topo realcorp --controller remote
