---
title: "Arch/Manjaro: Fix Gpg Keyserver Error"
type: post
date: 2020-08-06T13:02:33+02:00
url: /2020/arch-manjaro-fix-gpg-keyserver-error/
tags:
  - linux
draft: false
---

gpg: keyserver receive failed: General error. One of the most annoying errors.

<!--more-->

---

We all know that time when you try to install some program from **aur** sometimes you need to a gpg key for it to install and then your keyserver fails or when you do an update and it fails because it cant check the package keys. I know that feeling and it the worst because sometimes it can even destroy you installation like it destroy my xserver because of not updating all needed packages xserver packages.

For this problem there are two possible fixes about which I will be talking about now.

1. Fix

Manually adding the key using different keyserver.

To do that you need to use either of the two next commands with your keyserver of choice and the key you wish to add.

Aur

`gpg --keyserver ${KEYSERVER} --recv-keys ${KEY}`

Pacman

`sudo pacman-key --keyserver ${KEYSERVER} pacman-key --lsign-key keyid ${KEY}`

You use the first command for Aur and second for updates in Pacman.

2. Fix

Change the default keyserver.

You can change the default keyserver by changing the gpg and pacman keyserver default values. To do that you need to do this:

Add `keyserver ${KEYSERVER}` with the keyserver of your choosing at the end of the next two files at this locations. Using text editor of your choice here I used nano as an example.

Aur

`sudo nano /etc/pacman.d/gnupg/gpg.conf`

Pacman

`sudo nano ~/.gnupg/gpg.conf`

---

I hope that this was helpful to you and that you are now able to normally install your programs again. You can also write about any other methods to fix this problem in the comments.
