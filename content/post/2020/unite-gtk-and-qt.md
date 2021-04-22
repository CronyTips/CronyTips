---
title: "Unite Gtk and Qt"
type: post
date: 2020-09-08T15:17:26+02:00
url: /2020/unite-gtk-and-qt/
image: "https://raw.githubusercontent.com/CronyAkatsuki/screenshots/main/qt5ct.png"
tags:
  - linux
  - open-source
draft: false
---

In this post I will talk about how to unite gtk and qt themes.

<!--more-->

---

![](https://raw.githubusercontent.com/CronyAkatsuki/screenshots/main/qt5ct.png)

> example of a qt program using qt5ct

We all know the pain of trying to unite gtk and qt themes under linux. Most of the time the only thing that you can do is use same gtk and qt theme but there is another way that I have been using and that is using a program called qt5ct. Here you can check it's [sourceforge site](https://sourceforge.net/projects/qt5ct/).

Qt5ct works in a way that it sets the qt theme to either gtk2 or a style with custom colors. You can also change the icons, font and other stuff to make your theming look more consistent.

Now I'm not saying that this program is bug free because I had problems of needing to install a lot of other packages to make it work or the gtk2 option wouldn't work for some reason. And the best way to find the fixes is to look on the Internet for the fix.

# Installation

Qt5ct is from my knowledge available in most distro repository's so you can use your package manager to install the qt5ct package. You also need to install additional gtk engines.

It is also preferable that your themes also have a gtk2 version.

But before using the software first you need to set an environmental variable **QT_QPA_PLATFORMTHEME="qt5ct"**.

Depending on you shell you will need to save it in your _.profile_.

~~~
zsh > `export QT_QPA_PLATFORMTHEME="qt5ct"` inside .zprofile

bash > `export QT_QPA_PLATFORMTHEME="qt5ct"` inside .profile
~~~

---

I hope how this will help you get that perfect unified looks on your linux desktop. If you have any questions mention them in the comments section.
