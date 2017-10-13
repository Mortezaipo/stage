---
layout: post
title: "Vim As An IDE"
date: 2017-10-13
keywords: [tools, emacs, ide, config]
category: tools
excerpt_separator: <!-- more -->
---
It's true that for fast developing and having easy-to-use environment
anybody prefer to switch on the modern IDEs like JetBrains IDEs, Eclipse,
Komodo IDE and so on. Consider me as this kind of person, but Vim is
something different.
<!-- more -->
It's completely clear that using development tools is so important.
So I don't prefer to talk about it because it's so clear and nobody cares about it.

Before talking about what I've done, let's look at my Vim:

![Vim screenshot]({{site.baseurl}}/images/vim-1.png)

Looks great?

This article refers to a meeting with my friend which he has talked about Vim features with me.

I remember that programming in editors like Vim or Emacs was my honor,
because these environments are so fantastic and make me feel good.

It's true that for fast developing and having easy-to-use environment anybody prefer
to switch on the modern IDEs like JetBrains IDEs, Eclipse, Komodo IDE and so on.
Consider me as this kind of person, but Vim is something different and is so preferable for me.

Well, I've involved in making my Vim as an IDE, and I've done it based on my requirements.

It supports:

* File manager
* Git
* Python auto completion
* PEP8 & Flake8 validations
* Using VENV of project
* Code folding
* Tag definitions
* Comment/Uncomment code
* Hot keys for buffers handling
* Hot keys for windows handling
* File status
* Terminal
* Table drawing

I've made my own config file which anybody can add it in his '~/.vimrc' file:

https://gist.github.com/Mortezaipo/638d4f7adeb564be0248fc2875295b7f

All config parts have comments, please read them for more information.

Open up your Vim in your terminal or in your desktop by GVim, then run these commands sequentially:
```
:PluginInstall
:VimProcInstall
```

Then close your Vim and open it again via: 'vim .' command.

Note: This config is based on my requirements like considering Python settings. If you are looking for something else, customize it.

Note: Read the comments of mentioned link before any action!
