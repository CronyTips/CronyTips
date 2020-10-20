---
title: "Acer Aspire A715 41g Linux Experience"
type: post
date: 2020-10-20T08:19:50+02:00
url: /2020/acer-aspire-a715-41g-linux-experience/
tags:
  - linux
  - open-source
draft: false
---

In this post I will talk about my experience with linux on Acer aspire 7 laptop.

<!--more-->
---

So recently I bought a new laptop that costs about 950 American dollars. Well I bought it for 770 American dollars (Got a good deal). This laptop was pretty good and I needed it because of school (Literally) so I have been on a hunt for a deal like this for 2 months. And I managed to find this one and have been pretty happy with the machine.

The specifications of this machine are: 8 GB ram, AMD Ryzen 5 3550H processor, Nvidia GTX 1650 graphics card and 512 GB SSD and a 1080p IPS display. Pretty good for the money I paid for it. First thing I did was install windows 10 so that I can install all the software that I need for school (And also a cople of games that dont work on linux). Since it had a integrated Vega 8 gpu it had Nvidia containers in windows 10 which enable me to use the dedicated 1650. The performance was good even thought I installed windows 10 on in so after a couple of days I decided to install linux on a different partition.

### 1. Artix linux

The first distro that I tried to install was a distro I used on my old machine. I took the base install (cli install like the arch linux) and installed the basic packages and everything else in less than 20 minutes. Then I easily pulled my dotfiles from github and placed them at their place and started installing my package list (after removing some uneeded packages from it). After that I made zsh my default shell and rebooted into the bspwm. Everything worked as expected, except for the 1650 which I couldn't get to work normally no matter what. And after breaking my xserver a couple of times I searched on the web for a distro that could do that for me.

### 2. Manjaro

Since I loved the pacman package manager and aur I tried Manjaro because it had prime drivers for AMD/Nvidia combinations. I got the architect ISO and then I installed the cli system and like with artix I pulled my dotfiles from github and installed my packages. After that I rebooted into bspwm to see that the 1650 was working with no "problems" with prime. That is when gaming came in and made me switch to another distro. Prime would sometimes on some games lock my xserver so I had to forcefully power off my laptop. And that is when I decided to go for a debian based distro that I heard had great configuration for this kind of laptops.

### 3. Pop OS

My experience on Pop OS was so good that this post is written in it. With its system76-power program I can easily switch between integrated and dedicated (even hybrid) gpu setups. The batter works for about 8 hours when on integrated and when on dedicated for about 5 hours. I didn't try out the hybrid setting because I don't need it. The performance was better than in windows 10 but I still don't like the fact that I have over 1600 packages installed on the fresh install and the 700mb usage on boot (bspwm used 200-300mb with mpd on) nut all in all it's working with no problems. And I can play games all I want with no guilt.

---

That is it for todays post and I hope that you will find this post helpful in deciding whether to buy one of these or not going to. Write in the comments your experiences.
