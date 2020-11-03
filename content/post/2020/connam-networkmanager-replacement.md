---
title: "Connam NetworkManager Replacement"
type: post
date: 2020-11-03T21:46:22+01:00
url: /2020/connam-networkmanager-replacement/
tags:
  - linux
  - open-source
draft: false
---

In  this post I will be talking about a NetworkManager replacement called ConnMan.

<!--more-->
---

Everyone that uses Linux probably uses NetworkManager when connecting to wifi networks. I used NetworkManager also but recently I found a better solution. It is called ConnMan.

ConMan is a network manager that is much simpler than NetworkManager. From my experience connman is faster and more stable than NetworkManager.

It can also use iwd instead wpa_supplicant which is also much more faster and safer which makes it much more reliable than NetworkManager.

ConnMan has qt and gtk interface. Personally gtk version is simpler and nicer but if you wan't to get a lot of control over your network you will need to use the qt version.

Here are is the ConnMan and the gui interface repos:

ConnMan: https://git.kernel.org/pub/scm/network/connman/connman.git/about/

Qt interface: https://github.com/andrew-bibb/cmst

GTK interface: https://github.com/gke/connman-gtk

Also check out the arch wiki page: https://wiki.archlinux.org/index.php/ConnMan

---

If you guys found this post helpful like the post and tell me in the comments section if you have any questions.
