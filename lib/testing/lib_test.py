#!/usr/bin/env python3

from functions import greet_programmer, greet, greet_with_default, \
                        add, halve

import io
import sys


class TestGreetProgrammer:
    '''function greet_programmer()'''

    def test_greet_programmer(self):
        '''prints "Hello, programmer!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_programmer()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello, programmer!\n")

class TestGreet:
    '''function greet()'''

    def test_greet_programmer(self):
        '''prints "Hello, {name}!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet("Guido")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello, Guido!\n")

class TestGreetWithDefault:
    '''function greet_with_default()'''

    def test_greet_with_default(self):
        '''prints "Hello, programmer!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello, programmer!\n")

    def test_greet_with_default_with_param(self):
        '''prints "Hello, {name}!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_with_default("Guido")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello, Guido!\n")


def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, (int, float)):
        return number / 2
