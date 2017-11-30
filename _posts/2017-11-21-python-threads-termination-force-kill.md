---
layout: post
title: "Python Threads Termination (Force Kill)"
date: 2017-11-21
keywords: [programming, develop, python, parallelism, concurrency, multiprocessing, thread, multithreading, high_performance]
tags: [python, concurrency, multiprocessing, multithreading, high_performance]
category: dev
excerpt_separator: <!-- more -->
---
In python when you want to kill a process immediately, you can do it by calling `terminate` method.

But what about thread? there is no `terminate` method for thread.<!-- more -->

By using <a href="https://docs.python.org/3/library/ctypes.html" target="_blank">`ctype`</a> library you can make a way to send termination request to a thread.

```python
import ctypes

def terminate(t):
  """Terminate thread.

  :param threading.Thread t: thread object
  """
  exec = ctypes.py_object(SystemExit)
  res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), exec))
  if res == 0:
    print("thread not found!")
  elif res > 1:
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(t.ident), None))
```

> **Note:** It's not a *certain* way and it might that your thread could not terminate as well as process.
