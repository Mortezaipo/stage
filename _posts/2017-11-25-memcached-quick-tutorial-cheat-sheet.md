---
layout: post
title: "Memcached Quick Tutorial (Cheat Sheet)"
date: 2017-11-25
keywords: [cache, caching, memcached, server, service, linux]
category: services
excerpt_separator: <!-- more -->
---
memcached is an in-memory key-value data storage service. It doens't have any persistence feature to store your data in hdd.<!-- more -->

### Install Package
```
$ pacman -S memcached
```

### Enable and Start Service
```
$ systemctl enable memcached
$ systemctl start memcached
```

### Connect to Memcached
```
$ telnet 127.0.0.1 11211
```

### Basic Information About Current Running Service
```
stats 
```
result: multiline key value string

### Settings and Configuration Details of Current Running Daemon
```
stats settings
```
for example (maxbytes: maximum bytes which can be stored in cached server)

result: multiline key value string

### Storing Data
```
set mykey 0 100 4 \r\ndata\r\n
```
pattern: `set <KEY-NAME> <FLAGS> <MESSAGE-TIME-TO-LIVE> <MESSAGE-LENGTH> RET <MESSAGE> RET`

result: `STORED` on success and `ERROR` on fail.

**note:** `FLAGS` is 16-bit unsigned integer and it's an attribute of message which doesn't have any meaning for server, but it would be useful for your application if it has any meaning for you.

**note:** to store a message forever, just set "0" on `MESSAGE-TIME-TO-LIVE`.

### Retriving Data
```
get mykey
```
pattern: `get <KEY-NAME>`

result: value string

### Add New Key:
```
add mykey 0 10 4
```
pattern: `set <KEY-NAME> <FLAGS> <MESSAGE-TIME-TO-LIVE> <MESSAGE-LENGTH> RET`

### Retrive All Data
```
stats items
```
result: multiline key value string 

### Retrive All Keys
```
stats cachedump 1 10
```
pattern: `stats cachedump <SLABS> <LIMITS>`

result: multiline key value string 

### Clustring
to enable clustring you can run a new instance of memcached on other ports like so:
```
memcached -p 3000
memcached -p 3001
```
**note:** memcached doesn't do anything for clustring. actually it runs several instances (as you've seen) and you should distribute your data across them.

### Deleting a Key
```
delete mykey
```
pattern: `delete <KEY-NAME>`

result: `DELETED` on success and `ERROR` on fail.

### Flushing All Items
```
flush_all
```
result: `OK` on success and `ERROR` on fail.

### Increase Value of Key
```
incr mykey 10
```
pattern: `incr <KEY-NAME> <STEPS>`

result: number of total value which stored and `ERROR` on fail.

### Decrease Value of Key
```
decr mykey 10
```
pattern: `decr <KEY-NAME> <STEPS>`

result: number of total value which stored and `ERROR` on fail.

### Overriding Existing Key
```
replace mykey 0 10 4 \r\ndata\4\n
```
pattern: `set <KEY-NAME> <FLAGS> <MESSAGE-TIME-TO-LIVE> <MESSAGE-LENGTH> RET <MESSAGE> RET`

result: `STORED` on success and `ERROR` on fail.




Another good resource: <a href="http://lzone.de/cheat-sheet/memcached" target="_blank">Memcached Cheat Sheet</a>

To use in python: <a href="http://sendapatch.se/projects/pylibmc/" target="_blank">pylibmc</a>