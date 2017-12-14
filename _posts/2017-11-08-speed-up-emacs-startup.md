---
layout: post
page_menu: Articles
title: "Speed up Emacs Startup"
date: 2017-11-08
keywords: [tools, emacs, ide, config, performance]
tags: [tools, emacs, ide, config]
category: tools
excerpt_separator: <!-- more -->
---
Emacs is a fantastic editor for developers with many features.
Unfortunatelly emacs boot time is not good enough and it takes a while to load server and client services.
<!-- more -->

To solve this issue, try to apply these steps:

Add this line in `/etc/profile`:
<pre>
if [ ! `ps -x | grep emacs | grep daemon | awk '{ print $2 }'` ]; then
  emacs --daemon 2> /dev/null
fi
</pre>
> Relogin again to start the daemon.

Now you can edit your files with `emacsclient` command like so:
<pre>
$ emacsclient sample.cpp
</pre>

If you want to run emacsclient in gui mode, run this command:
<pre>
$ emacsclient -c sample.cpp
</pre>

To make your default emacs application to run emacsclient instead of emacs command,
edit your `/usr/share/applications/emacs.desktop` file and change `Exec` line to this:
<pre>
Exec=emacsclient -c %F
</pre>
> If `emacs.desktop` has `Try` variable, change that too.

**Note:** if your emacsclient gui doens't load your theme or config, just load it via `M-x`+`load-file`+`~/.emacs`
