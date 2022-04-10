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

Note that normal keycaps does not fit on these switches, they bottom out too low, so we need
to go with eg. XDA, DSA, or similar "lower" caps.

PCB can (soon) be found [here](https://github.com/Tubbles/kbdkid3-pcb).

## BOM
### Case
*

### PCB
* Custom (hot swap?) split Ergodox EZ

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
* 2x LilyGo T-Micro32 V2.0
* 2x Lipo batteries
* 2x Lipo chargers (PD/QC?)
* 4x USB-C ports (upstream + tether)
*
* Downstream USB ports acting as a USB hub?
