---
title: "Windows 10: Fix Virtualitization Not Working for Third Party Programs"
type: post
date: 2021-07-14T09:57:15+02:00
url: /2021/windows-10-fix-virtualitization-not-working-for-third-party-programs/
tags:
  - windows 10
draft: false
---

In this post I will talk about how to fix virtualitization not working for third party programs in Windows 10.

<!--more-->

---

So you got a new laptop or pc and installed Kapersky free antivirus or wanted to run virtualbox for a bit but were not able to use it because virtualitization was not accessible even thought you enabled it in bios and all that. Well here I will be talking about how to fix that. You

#### 1. Disable Hyper-V

One of the most common fixes of this error is to disable hyper v. To do that follow this steps.

1. Open cmd as administrator (Press windows key, search cmd and open as administrator).
2. Run this command `dism.exe /Online /Disable-Feature:HypervisorPlatform` or this one if you have an older windows version `dism.exe /Online /Disable-Feature:Microsoft-Hyper-V`.
3. After running the command reboot.
4. Test if it worked and if it did great for you.

#### 2. Disable hypervisor start on boot

This is a fix that also saved me personally and it is very similar with the past one but you still need to do both of them. So to do it follow this steps.

1. Open cmd as administrator (Press windows key, search cmd and open as administrator).
2. Run this command `bcdedit /set hypervisorlaunchtype off`.
3. After running the command reboot.
4. Test if it worked and if it did great for you.

---

I hope that this helped you and you are now able to run virtualitization  software with no problems.