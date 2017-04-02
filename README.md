# Python学习笔记
![logo](https://raw.githubusercontent.com/xulongqiu/lxflearn/master/python-logo.jpg)

[廖老师官网](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
## Python 简介
> Python是著名的“龟叔”Guido van Rossum在1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言.

* **总括**
    总的来说，这几种编程语言各有千秋。C语言是可以用来编写操作系统的贴近硬件的语言，所以，C语言适合开发那些追求运行速度、充分发挥硬件性能的程序。而Python是用来编写应用程序的高级编程语言。
- **应用**
    首选是网络应用，包括网站、后台服务等等；
    其次是许多日常需要的小工具，包括系统管理员需要的脚本任务等等；
    另外就是把其他语言开发的程序再包装起来，方便使用。
    例子：[YouTube](https://www.youtube.com/)、[Instagram](https://www.instagram.com/) [豆瓣](https://www.douban.com/)
* **缺点**
    运行速度慢， Python是解释型语言，通过解释器翻译成机器码才能执行，翻译过程非常慢。
    代码不能加密，发布Python程序就等于公开源代码。

## Python 安装
Ubuntu 16.04 自带Python2.7, **不要删除**， 因为Ubuntu自带很多程序依赖Python2.7.
```
~$ sudo add-apt-repository ppa:fkrull/deadsnakes
[sudo] password for xxx:
~$ sudo apt-get update
~$ sudo apt-get install python3.5
~$ sudo cp /usr/bin/python /usr/bin/python_bak
~$ sudo rm /usr/bin/python
~$ sudo ln -s /usr/bin/python3.5 /usr/bin/python
~$ python
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
安装完成
## Python 解释器
* **Cpython**
当我们从[Python官方网站下载](https://www.python.org/)并安装好Python 3.5后，我们就直接获得了一个官方版本的解释器：CPython。这个解释器是用C语言开发的，所以叫CPython。在命令行下运行```python```就是启动CPython解释器。CPython是使用最广的Python解释器。

+ **IPython**
IPython是基于CPython之上的一个交互式解释器，也就是说，IPython只是在交互方式上有所增强，但是执行Python代码的功能和CPython是完全一样的。好比很多国产浏览器虽然外观不同，但内核其实都是调用了IE。
CPython用```>>>```作为提示符，而IPython用```In [序号]:```作为提示符

- **PyPy**
 PyPy是另一个Python解释器，它的目标是执行速度。PyPy采用[JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation)技术，对Python代码进行动态编译（注意不是解释），所以可以显著提高Python代码的执行速度。

 绝大部分Python代码都可以在PyPy下运行，但是PyPy和CPython有一些是不同的，这就导致相同的Python代码在两种解释器下执行可能会有不同的结果
[PyPy和CPython的不同点](http://pypy.readthedocs.io/en/latest/cpython_differences.htmlhttp://pypy.readthedocs.io/en/latest/cpython_differences.htmlhttp://pypy.readthedocs.io/en/latest/cpython_differences.html)

* **Jython**
Jython是运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。

## 第一个Python程序
```
~$ python
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

>>> 12+87
99

>>> print("%s, %s" %("Hello", "World!"))
Hello, World!

>>> exit()
~$

~$ echo 'print(1 + 3 + 3)' > calc.py
~$ python calc.py 
7
```
