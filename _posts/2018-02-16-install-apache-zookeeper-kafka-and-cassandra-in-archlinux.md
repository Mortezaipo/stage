---
layout: post
page_menu: Articles
title: "Install Apache Zookeeper, Kafka and Cassandra in ArchLinux"
date: 2018-02-16
keywords: [apache, zookeeper, cassandra, kafka, installation]
tags: [apache, zookeeper, cassandra, kafka]
category: tools
excerpt_separator: <!-- more -->
---
In this tutorial we are going to install Apache Zookeeper, Kafka and Cassandra in ArchLinux.
Installing this way in other Linux distribution is the same but a little bit different.
<!-- more -->

## Pre installation
```
$ pacman -S jdk8-openjdk jre8-openjdk gradle scala
$ mkdir ~/Applications/
```

## Zookeepr
```
$ wget -c http://www-us.apache.org/dist/zookeeper/stable/zookeeper-3.4.10.tar.gz
$ tar xzf zookeeper-3.4.10.tar.gz -C ~/Applications/
$ mv ~/Applications/zookeeper-3.4.10 ~/Application/zookeeper
$ cd ~/Applications/zookeeper/
$ mkdir data
$ mv conf/zoo_sample.cfg zoo.cfg
```

Now open `conf/zoo.cfg` and update `dataDir` variable:
```
dataDir=data
```

Now add `~/Applications/zookeeper/bin/` in `$PATH` to make it easy to accessible.

Now run it:
```
$ zkServer.sh start
```

Success run message contains: `... STARTED`

## Apache Kafka
```
$ wget -c http://www-us.apache.org/dist/kafka/1.0.0/kafka-1.0.0-src.tgz
$ tar xzf kafka-1.0.0-src.tgz -C ~/Applications/
$ mv ~/Applications/kafka-1.0.0 ~/Applications/kafka
$ cd ~/Applications/kafka/
$ gradle jar
```

Now add `~/Applications/kafka/bin/` in `$PATH` to make it easy to accessible.

Now run it:
```
$ kafka-server-start.sh ~/Applications/kafka/config/server.properties
```

Success run message contains: `... started (kafka.server.KafkaServer)`


## Cassandra
```
$ wget -c http://www-eu.apache.org/dist/cassandra/3.11.1/apache-cassandra-3.11.1-bin.tar.gz
$ tar xzf apache-cassandra-3.11.1-bin.tar.gz ~/Applictions/
$ mv ~/Applications/apache-cassandra-3.11.1 ~/Applications/cassandra
$ cd ~/Applications/cassandra/
$ mkdir -p data/data
$ mkdir -p data/commitlog
$ mkdir -p data/saved_caches
$ mkdir -p logs
```

Now add `~/Applications/cassandra/bin/` in `$PATH` to make it easy to accessible.

Now run it:
```
$ cassandra -f
```

Success run message contains: `... Starting listening for CQL clients on localhost/127.0.0.1:9042`
