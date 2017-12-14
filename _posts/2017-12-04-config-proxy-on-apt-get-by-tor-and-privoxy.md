---
layout: post
page_menu: Articles
title: "Config Proxy for 'apt-get' by Tor and Privoxy"
date: 2017-12-04
keywords: [apt, apt-get, proxy, config, tor, privoxy, server, service, linux]
tags: [tools, proxy, service, linux]
category: services
excerpt_separator: <!-- more -->
---
How to install packages by `apt-get` via proxy?  It was an issue in such cases that I needed to get packages via a proxy and  no other ways would be possible. 
<!-- more -->

To solve this issue, I've did some actions. First of all we to install `tor` .

### Install Tor
<pre>
$ apt-get install tor
</pre>

Then make sure that Tor connected (100%) successfully:
<pre>
$ tail -f /var/log/tor/log
</pre>

Then we need to install `privoxy`.
### Install Privoxy
<pre>
$ apt-get install privoxy
</pre>

Then config it:

### Config Privoxy
Update these lines in `/etc/privoxy/config`:

`listen-address  loclhost:8118` to `listen-address  127.0.0.1:8118`

Add these lines:
<pre>
forward-socks4   /               127.0.0.1:9050 .
forward-socks5   /               127.0.0.1:9050 .
</pre>

Now restart `privoxy` service:
<pre>
$ /etc/init.d/privoxy restrat
</pre>

Now it's time to config `apt-get` command:

### Apt-Get Command:
Create `01proxy` file in `/etc/apt/apt.conf.d/` with below settings:
<pre>
Acquire::http::Proxy "http://127.0.0.1:8118";
</pre>

Finally make sure that it works fine.

### Test apt-get
<pre>
$ apt-get update
</pre>
