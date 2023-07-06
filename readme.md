# KBDKID3

![KBDKID3](img/kbdkid.png "KBDKID3")

## Info

Since the second attempt failed miserably due to the stabilizer situation, I am now rethinking on how to best utilize my
Kailh Choc V2 switches. My idea now is to go for an ortholinear setup in order to dodge the stabilizers alltogether. A
split Ergodox EZ-like keyboard makes the most sense here. Although this probably still requires custom PCB and plate,
with a little luck I might be able to use an off-the-shelf cases, feets, and wrist-rests.

The idea is to use the impossibly small ESP32 based LilyGo T-Micro32 V2.0 modules, one for each half. There should be
optional tethering between the halfs, used to transfer power during charging. Each half will show up as an individual
keyboard via bluetooth.

Note that normal keycaps do not fit on these switches if used with a plate, they bottom out too low. DSA wont work
either, since the underside of the cap hits the skirt on the switch. There might be some keycap that actually fits, such
as G20, but I haven't tried them out. On the other hand, if the plate is skipped, we could use XDA, where they barely
fit under the thick sides of the cap.

Features include wireless operation (maybe, hw prep), USB pass-through.

PCB can (soon) be found [here](https://github.com/Tubbles/kbdkid3-pcb).

## BOM

### Case

* Plain PCB + rubber feet
* Extra 3d-printed "ramp"

### PCB

* Custom (hot swap?) split "Ergodox EZ"
* ESP32-S3-WROOM-2-N32R8V based for USB-OTG and hardware prep for wireless operation
* Hot swap sockets Mill-Max 7305 https://mou.sr/3NydSza

### Plate

*

### Switch

* Kailh Choc V2 Red https://kono.store/collections/switches/products/kailh-choc-mx-switches

### Stabs

*

### Keycaps

*

### Accessories

* Lube

### Preliminary Components BOM

* 2x ESP32-S3-WROOM-2-N32R8V
* 2x Lipo batteries
* 2x Lipo chargers (PD/QC?)
* 4x USB-C ports (upstream + tether)
*
* Downstream USB ports acting as a USB hub?
