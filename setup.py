'''
@Copyright 2020 <Rafael Sanz - (R)SELAB>

This software is MIT licensed (see terms below)

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
    modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
    IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import setuptools

setuptools.setup(
    name="qsAPI",
    version="1.9",
    description="",
    long_description="qsAPI is a client for Qlik Sense QPS and QRS interfaces"
    + " written in python that provides an environment for managing a Qlik"
    + " Sense site via programming or interactive console. The module provides"
    + " a set of commands for viewing and editing configuration settings,"
    + " as well as managing tasks and other features available through APIs.",
    author="Rafael Sanz",
    author_email="rafael.sanz@selab.es",
    url="https://github.com/rafael-sanz/qsAPI",
    packages=setuptools.find_packages(),
    install_requires=["requests>=2.22.0"])
