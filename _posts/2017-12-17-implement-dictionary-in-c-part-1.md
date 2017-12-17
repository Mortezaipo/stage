---
layout: post
page_menu: Articles
title: "Implement Dictionary in C - Part 1"
date: 2017-12-17
keywords: [c, hash_table, dictionary]
tags: [c]
category: dev
excerpt_separator: <!-- more -->
---
As you know, C programming language doesn't have any built-in dictionary. There are plenty of implementation such as [Apache APR](https://apr.apache.org/) and so on. But let's build a simple one to know whats going on in the background.
<!-- more -->

We are going to implement a library which support creating dictionary and manipulating items easily.

### Basic implementation

Well, first we list our basic functions which are responsible to work with dictionary directly:

<pre>
void dict_add_item(dict* d, char* key, char* value);
void dict_update_item(dict* d, char* key, char* value);
void dict_del_item(dict* d);
void dict_print(dict* d);
</pre>

We store dictionary data in a `struct` :

<pre>
typedef struct Dict {
    char *key;
    char *value;
} dict;
</pre>

Required libraries are `stdio.h` , `stdlib.h`, `string.h` .

Let's Implement `dict_add_item` function which is responsible to allocate memory and add passed data to  created dictionary:

<pre>
void dict_add_item(dict* d, char* key, char* value) {
    d->key = malloc(sizeof(char) * strlen(key));
    d->value = malloc(sizeof(char) * strlen(value));
    strcpy(d->key, key);
    strcpy(d->value, value);
}
</pre>

Now, implement `dict_update_item` function which is responsible to update dictionary data and if it has different value size,
it will reallocate the allocated memory:

<pre>
void dict_update_item(dict* d, char* key, char* value) {
    if (strlen(d->value) != strlen(value)) {
        free(d->value);
        d->value = malloc(sizeof(char) * strlen(value));
    }
    strcpy(d->value, value);
}
</pre>

Now, implement `dict_del_item` function which is responsible to destroy a dictionary and free allocated memory:

<pre>
void dict_del_item(dict *d) {
    free(d->key);
    free(d->value);
}
</pre>

Finally, implement `dict_print` function which is responsible to print dictionary like Python print function:

<pre>
void dict_print(dict* d) {
    printf("{ %s: %s }\n", d->key, d->value);
}
</pre>

Now let's test our code by some sample data:

<pre>
int main() {
    dict test;
    dict_add_item(&amp;test, "name", "Sara");
    dict_print(&amp;test);

    dict_add_item(&amp;test, "name", "Mike");
    dict_print(&amp;test);

    dict_del_item(&amp;test);
    dict_print(&amp;test);
}
</pre>

Output:

<pre>
{ name: Sara }
{ name: Mike }
{ : �fk��U }
</pre>

> Note: last line is nonsence because we released (free) the allocated area in memory.

So, it's complete source code of part 1:

<pre>
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;

typedef struct Dict {
    char *key;
    char *value;
} dict;

void dict_add_item(dict* d, char* key, char* value) {
    d->key = malloc(sizeof(char) * strlen(key));
    d->value = malloc(sizeof(char) * strlen(value));
    strcpy(d->key, key);
    strcpy(d->value, value);
}

void dict_update_item(dict* d, char* key, char* value) {
    if (strlen(d->value) != strlen(value)) {
        free(d->value);
        d->value = malloc(sizeof(char) * strlen(value));
    }
    strcpy(d->value, value);
}

void dict_del_item(dict *d) {
    free(d->key);
    free(d->value);
}

void dict_print(dict* d) {
    printf("{ %s: %s }\n", d->key, d->value);
}

int main() {
    dict test;
    dict_add_item(&amp;test, "name", "Sara");
    dict_print(&amp;test);

    dict_add_item(&amp;test, "name", "Mike");
    dict_print(&amp;test);

    dict_del_item(&amp;test);
    dict_print(&amp;test);
}
</pre>

This code works fine, but it doesn't satisfy us. Because we are looking for dictionary which provided multiple keys and values
like this:

<pre>
{"name": "Sara", "age": "27", "email": "sara@gmail.com"}
</pre>

But our code provides just one key/value as we've seen.

In the next section I will explain and implement how to provide this facility.