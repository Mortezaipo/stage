---
layout: post
title: "Python Ldap Get Modified Users"
date: 2017-11-11
keywords: [tools, code, python, ldap, openldap, server, service, linux]
tags: [tools, python, ldap, server, service, linux]
category: dev
excerpt_separator: <!-- more -->
---
In many systems when you want to implement an integration with LDAP services, normally you get all users details in every sync action which sometimes this amount of size is large and it's not good action to sync all users on every sync action.
<!-- more -->

To handle this situation we could implement several ways to increase sync performance and avoid duplicate or get already synced user again.

To handle this issue, you need to get openldap internal fields by adding a `+` sign at the end of search query like so:
```shell
$ ldapsearch -h localhost -w 'admin' -x -D "cn=admin,dc=example,dc=org" -b "DC=example,DC=org" +
```

And in python code it would like this:
```python
r = l.search_ext("dc=example,dc=org", ldap.SCOPE_SUBTREE, "objectClass=*", ["+",], 0)
```

Then it returns internal fields which are important like `modifyTimestamp`.

Or if you want to get all internal fields and user attributes in one request, just add `'*' '+'` like this:
```python
r = l.search_ext("dc=example,dc=org", ldap.SCOPE_SUBTREE, "objectClass=*", ["*", "+"], 0)
```

If you want to get last changed user after a specific date, try to add `modifyTimestamp` on query like this:
```shell
$ ldapsearch -h localhost -w 'admin' -x -D "cn=admin,dc=example,dc=org" -b "DC=example,DC=org" "modifyTimestamp>=20171012152507Z
```

To get more info about history, try to enable `overlay accesslog` in your ldap and use it:
```shell
$ ldapsearch -x -b cn=accesslog
```

Resources:

 - Active directory `whenChanged` field: <a href="https://msdn.microsoft.com/en-us/library/ms680921(v=vs.85).aspx" target="_blank">Microsoft MSDN doc</a>
 - Open ldap `modifyTimestamp` field: <a href="https://tools.ietf.org/html/rfc4512" target="_blank">RFC4512</a>
 - Open ldap all default attributes: <a href="http://www.phpldaptools.com/reference/Default-Schema-Attributes/" target="_blank">LDAP default schema attributes</a>
 - Active Directory all default attributes: <a href="https://msdn.microsoft.com/en-us/library/ms675090(v=vs.85).aspx" target="_blank">Active Directory default schema attributes</a>
 - <a href="https://www.ibm.com/support/knowledgecenter/en/SSKTMJ_9.0.1/admin/conf_usingldapsearchtoreturnoperationalattributes_t.html" target="_blank">ldapsearch to return operational attributes</a>
 - Internal attributs: <a href="https://mail.python.org/pipermail/python-ldap/2009q3/002593.html" target="_blank">Internal attributes (Python org mail)</a>
    - <a href="https://mail.python.org/pipermail/python-ldap/2009q3/002594.html" target="_blank">Internal attributes (conversation node on Python org mail)</a>
 - Access log: <a href="http://www.openldap.org/doc/admin24/overlays.html#Access%20Logging" target="_blank">OpenLDAP access logging</a>
 - How to check the login history of users on openldap: <a href="https://www.openldap.org/lists/openldap-technical/201505/msg00117.html" target="_blank">OpenLDAP login history of users</a>