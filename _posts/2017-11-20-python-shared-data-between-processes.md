---
layout: post
page_menu: Articles
title: "Python Shared Data Between Processes"
date: 2017-11-20
keywords: [programming, develop, python, parallelism, concurrency, multiprocessing, shared_data, shared_state, high_performance]
tags: [python, concurrency, multiprocessing, shared_data, shared_state, high_performance]
category: dev
excerpt_separator: <!-- more -->
extra_css: [prism.css]
extra_js: [prism.js]
references:
  - '<a href="https://docs.python.org/3.6/library/multiprocessing.html#sharing-state-between-processes" target="_blank">Sharing state between processes</a>'
comments: true
---
Providing a shared data or state between different processes is so useful and great idea because in many
cases when you want to implement parallel systems, you should provide a way that each process can
communicate with others.<!-- more -->

Fortunately, Python supports many kinds of shared data such as `Value`, `Array`, `Dict`, and `Queue` and so on.

Let's try an example:

We have 2 processes which are:
* Process-1 is responsible to check the value (shared data).
* Process-2 is responsible to set the value (shared data).

{%- highlight python -%}
from multiprocessing import Process, Value
from ctypes import c_char
from time import sleep


def process_1(shared_data):
    """Process-1 is responsible to check the value."""
    while shared_data.value != b"my_data":
      sleep(0.5)
    print("process-1 got the value. exit.")

def process_2(shared_data):
    """Process-2 is responsible to set value."""
    sleep(1)
    shared_data.value = b"my_data"
    sleep(1)
    print("process-2 set the value. exit.")

if __name__ == "__main__":
    # create a shared data with 10 character length
    shared_data = Value(c_char * 10)
    p1 = Process(target=process_1, args=(shared_data,))
    p2 = Process(target=process_2, args=(shared_data,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
{%- endhighlight -%}

Try to implement your projects and idea with this great features which help you to
have high performance and scalable systems.
