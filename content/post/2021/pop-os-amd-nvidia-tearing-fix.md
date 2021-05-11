---
title: "Pop! OS Amd/Nvidia Tearing Fix"
type: post
date: 2021-05-11T21:10:52+02:00
url: /2021/pop-os-amd-nvidia-tearing-fix/
tags:
  - linux
  - open-source
  - pop os
draft: false
---

In this post I will be talking about how to fix screen tearing in pop os with amd/nvidia hybrid laptops.

<!--more-->

---

I'm sure that I'm not the only one who got a new laptop only to find out that amd igpu and nvidia dgpu isn't supported completely. So today I'm bringing up a fix for this problem. To be able to use nvidia mode in pop os with an amd/nvidia hybrid laptop we need to run 2 commands on user login, but also make sure that they are not runned when we are not using nvidia mode. And that is where my script comes in that also does a little more things.

> code

```
#!/bin/sh

mode=$(system76-power graphics)
nv_screen="eDP-1-0"
screen="eDP"

if [ "$mode" = "nvidia" ]; then
    xrandr --output $nv_screen --set TearFree on
    xrandr --output $nv_screen --set "PRIME Synchronization" 1
elif [ "$mode" = "integrated" ]; then
    xrandr --output $screen --set TearFree on
elif [ "$mode" = "hybrid" ]; then
    xrandr --output $screen --set TearFree on
fi
```

This may look a little confusing but I will explain it to you guys because you guys also need to do something first for the script to work correctly. You can see the **nv_screen** and **screen** variables? for them you guys need to find your screen name which you can find by running `xrandr --verbose` command.

> example output:

```
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 16384 x 16384
HDMI-A-0 disconnected (normal left inverted right x axis y axis)
	Identifier: 0x53
	Timestamp:  284435
	Subpixel:   unknown
	Clones:
	CRTCs:      0 1 2 3
	Transform:  1.000000 0.000000 0.000000
	            0.000000 1.000000 0.000000
	            0.000000 0.000000 1.000000
	           filter:
	GAMMA_LUT_SIZE: 4096
		range: (0, -1)
	DEGAMMA_LUT_SIZE: 4096
		range: (0, -1)
	GAMMA_LUT: 0
		range: (0, 65535)
	CTM: 0
	DEGAMMA_LUT: 0
		range: (0, 65535)
	TearFree: auto
		supported: off, on, auto
	HDCP Content Type: HDCP Type0
		supported: HDCP Type0, HDCP Type1
	Content Protection: Undesired
		supported: Undesired, Desired, Enabled
	vrr_capable: 0
		range: (0, 1)
	max bpc: 8
		range: (8, 16)
	underscan vborder: 0
		range: (0, 128)
	underscan hborder: 0
		range: (0, 128)
	underscan: off
		supported: off, on, auto
	scaling mode: None
		supported: None, Full, Center, Full aspect
	link-status: Good
		supported: Good, Bad
	CONNECTOR_ID: 78
		supported: 78
	non-desktop: 0
		range: (0, 1)
eDP connected primary 1920x1080+0+0 (0x56) normal (normal left inverted right x axis y axis) 344mm x 194mm
	Identifier: 0x54
	Timestamp:  284435
	Subpixel:   unknown
	Gamma:      1.0:1.0:1.0
	Brightness: 1.0
	Clones:
	CRTC:       0
	CRTCs:      0 1 2 3
	Transform:  1.000000 0.000000 0.000000
	            0.000000 1.000000 0.000000
	            0.000000 0.000000 1.000000
	           filter:
	_MUTTER_PRESENTATION_OUTPUT: 0
	EDID:
		00ffffffffffff0030e45a0600000000
		001d0104a5221378e238d5975e598e27
		1c505400000001010101010101010101
		010101010101243680a070381f403020
		350058c2100000190000000000000000
		00000000000000000000000000fe004c
		4720446973706c61790a2020000000fe
		004c503135365746432d5350443500e3
	GAMMA_LUT_SIZE: 4096
		range: (0, -1)
	DEGAMMA_LUT_SIZE: 4096
		range: (0, -1)
	GAMMA_LUT: 0
		range: (0, 65535)
	CTM: 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0
		0 1
	DEGAMMA_LUT: 0
		range: (0, 65535)
	TearFree: on
		supported: off, on, auto
	HDCP Content Type: HDCP Type0
		supported: HDCP Type0, HDCP Type1
	Content Protection: Undesired
		supported: Undesired, Desired, Enabled
	vrr_capable: 0
		range: (0, 1)
	abm level: 0
		range: (0, 4)
	max bpc: 16
		range: (8, 16)
	underscan vborder: 0
		range: (0, 128)
	underscan hborder: 0
		range: (0, 128)
	underscan: off
		supported: off, on, auto
	scaling mode: None
		supported: None, Full, Center, Full aspect
	link-status: Good
		supported: Good, Bad
	CONNECTOR_ID: 84
		supported: 84
	non-desktop: 0
		range: (0, 1)
  1920x1080 (0x56) 138.600MHz -HSync -VSync *current +preferred
        h: width  1920 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height 1080 start 1083 end 1088 total 1111           clock  59.98Hz
  1680x1050 (0x57) 138.600MHz -HSync -VSync
        h: width  1680 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height 1050 start 1083 end 1088 total 1111           clock  59.98Hz
  1280x1024 (0x58) 138.600MHz -HSync -VSync
        h: width  1280 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height 1024 start 1083 end 1088 total 1111           clock  59.98Hz
  1440x900 (0x59) 138.600MHz -HSync -VSync
        h: width  1440 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height  900 start 1083 end 1088 total 1111           clock  59.98Hz
  1280x800 (0x5a) 138.600MHz -HSync -VSync
        h: width  1280 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height  800 start 1083 end 1088 total 1111           clock  59.98Hz
  1280x720 (0x5b) 138.600MHz -HSync -VSync
        h: width  1280 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height  720 start 1083 end 1088 total 1111           clock  59.98Hz
  1024x768 (0x5c) 138.600MHz -HSync -VSync
        h: width  1024 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height  768 start 1083 end 1088 total 1111           clock  59.98Hz
  800x600 (0x5d) 138.600MHz -HSync -VSync
        h: width   800 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height  600 start 1083 end 1088 total 1111           clock  59.98Hz
  640x480 (0x5e) 138.600MHz -HSync -VSync
        h: width   640 start 1968 end 2000 total 2080 skew    0 clock  66.63KHz
        v: height  480 start 1083 end 1088 total 1111           clock  59.98Hz
```

You need to check you connected primary screen which in the case of the example is **eDP**. What you guys need to do is run this command in every mode (integrated, hybrid, nvidia) and replace if needed my screen names with the one's from your outputs. You guys need to save this program as any name with **.sh** extension. Make the file exacutable and add it into startup programs using the **Startup Applications** program.

---

Hope you guys had a good read and that this post helped you.