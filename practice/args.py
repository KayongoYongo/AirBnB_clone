#!/usr/bin/python3

def my_func(*args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", "abc", 123, "abc", key=123, abc=123)
