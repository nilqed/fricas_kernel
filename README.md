fricas_kernel
=============

FriCAS (wrapper) kernel for IPython


Based on the IPython **bash** wrapper kernel by Thomas Kluyver (BSD lic.)
https://github.com/takluyver/bash_kernel and IPython doc
*Making simple Python wrapper kernels* (new in version 3.0)
http://ipython.org/ipython-doc/dev/development/wrapperkernels.html.
Instead of using pexepct's *replwrap* we use winpexpect/pexpect *spawn*
and *expect* functions wrapped in a class called **FriCAS**.

------------
Prerequisites
------------
A working IPython installation with pyzmq, tornado, pygments and so on.

IPython 3.0dev or higher https://github.com/ipython/ipython

get it if necessary: 

> git clone https://github.com/ipython/ipython.git

Fricas: http://fricas.sourceforge.net/download.html

**Windows**: winpexpect 1.5 or higher, FriCAS for Cygwin

**Unix**: pexpect 3.3 or higher, FriCAS for Unix

--------------
Install kernel
--------------

Get this repo and 

`$python kernel_setup.py install`

(should push a kernel spec to ~/.ipython/kernels)


**Test** directly from git clone directory *ipython*:

```
$cd to the gitted *ipython* directory
$python -m IPython qtconsole --kernel fricas
```

Otherwise, if you have version 3.0dev installed then start as usual.

#####Screenshot (more in the folder)

![alt text](https://github.com/scios/fricas_kernel/blob/master/screenshots/fkernel_cygc.png "QTconsole")


#####Note
This is a prototype version (0.1) and was tested with FriCAS 1.2.3 on Windows7/Cygwin and on Ubuntu 12. Only the **qtconsole** frontend has been tested. The **notebook** version needs a full install of IPython. That means if you overwrite your existing installation with the 3.0dev version do not blame me.

If you want to have *code completion* in a *pop-up window* instead of *inline text* one has to check this in the IPython configuration file. 


#####Update
The same kernel also works for the notebook. One needs IPython 3.0dev and

 * jinja2
 * jsonschema
 * jsonpointer

which can be installed wirh `pip install <package>`. 

Start command:

```
$ ipython notebook --profile=fricas
```

Then choose the fricas kernel when creating a new notebook.

![alt text](https://github.com/scios/fricas_kernel/blob/master/screenshots/fkernel_nb.png "NB")


ToDo: see the Wiki https://github.com/scios/fricas_kernel/wiki

