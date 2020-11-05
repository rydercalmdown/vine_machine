# Vine Machine
This repository contains code for building a simple vine machine with a raspberry pi.


## Installation
To install, clone this repository onto your raspberry pi
```
git clone https://github.com/rydercalmdown/vine_machine
```

Next, install the mpg321 library:
```
sudo apt-get update && sudo apt-get install -y mpg321
```

Populate the audio directory in this repository with any mp3 files of vines you want to play - I've included one as a sample file. Modify pin numbers for GPIO pins in-code as necessary.

```python
# default is pin 12
pin_number = 12
```
