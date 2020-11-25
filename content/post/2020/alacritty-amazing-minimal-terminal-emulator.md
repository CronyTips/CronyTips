---
title: "Alacritty: Amazing Minimal Terminal Emulator"
type: post
date: 2020-07-14T10:04:13+02:00
url: /2020/alacritty-amazing-minimal-terminal-emulator/
tags:
  - linux
  - open-source
draft: false
---

In this post I will be talking about terminal emulator that I use named Alacritty.

<!--more-->

---

> Sample Alacritty configuration

![](https://raw.githubusercontent.com/CroLinuxGamer/Photos/master/terminal.png)

[Alacritty](https://github.com/alacritty/alacritty) is a minimal terminal emulator that has all the basic features that you need to have a comfortable experience. It also has gpu support which setts it apart among all other terminal emulators. According to the Alacritty github page `Alacritty is the fastest terminal emulator in existence. Using the GPU for rendering enables optimizations that simply aren't possible without it`. And in my case it is the truth.

Alacritty on my system has almost no different load time that `st` with difference in only of about 0.1 seconds. In therms of speed of dong tasks and stuff like that. For example `time tree /` took about 25 seconds on Alacritty while on `st` it took about 2 minutes. Yes difference is that big.

To install Alacritty you can use your distros package manager since it is in most repository's. In therms of configuration you will need to [Alacritty releases github page](https://github.com/alacritty/alacritty/releases) and download `alacritty.yml` the you need to save the file in one of there directories:

1. `$XDG_CONFIG_HOME/alacritty/alacritty.yml`
2. `$XDG_CONFIG_HOME/alacritty.yml`
3. `$HOME/.config/alacritty/alacritty.yml`
4. `$HOME/.alacritty.yml`

You can edit Alacritty configuration with any kind of text editor and config file has a lot of comments to help you understand every option so I don't think you will have any problems with it.

{{< notice warning >}}
You need to be careful with spaces in Alacritty configuration or you will be getting errors all the time like I did in the beginning
{{< /notice >}}

I hope that you found this all helpful and that you will try out Alacritty. Also write about what terminal are you using because I would love to hear your recommendations.
