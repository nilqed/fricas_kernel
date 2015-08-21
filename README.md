fricas_kernel
=============

FriCAS (wrapper) kernel for IPython


Based on the IPython **bash** wrapper kernel by Thomas Kluyver (BSD lic.)
https://github.com/takluyver/bash_kernel and IPython doc
*Making simple Python wrapper kernels* (new in version 3.0)
http://ipython.org/ipython-doc/dev/development/wrapperkernels.html.
Instead of using pexepct's *replwrap* we use winpexpect/pexpect *spawn*
and *expect* functions wrapped in a class called **FriCAS**.


Update notes see at the end.

Current version: 0.5 / August 2015

There is a *docker* image: https://hub.docker.com/r/nilqed/ifricas/

Latest sample: http://kfp.bitbucket.org/tmp/test2.html


------------
Prerequisites
------------
A working IPython installation with pyzmq, tornado, pygments and so on.

IPython 3.0 or higher https://github.com/ipython/ipython

get it if necessary: 

> git clone https://github.com/ipython/ipython.git

Fricas: http://fricas.sourceforge.net/download.html

**Windows**: winpexpect 1.5 or higher, FriCAS for Cygwin

**Unix**: pexpect 3.3 or higher, FriCAS for Unix

--------------
Install kernel
--------------

Get this repo and do

`$python kernel_setup.py install`

(should push a kernel spec to ~/.ipython/kernels)

then start with:

`$ipython notebook`

and choose the **FriCAS** kernel in the drop down menu.


*Note*: you can install the kernel locally:

`$python kernel_setup.py install --user` 

**Test** directly from git clone directory *ipython*:

```
$cd to the gitted *ipython* directory
$python -m IPython qtconsole --kernel fricas
```

Otherwise, if you have version 3.x installed then start as usual.

#####Screenshots (updated; more in the folder)

New (V 0.5): Jupyter 3.2 (code completion)

![alt text](http://kfp.bitbucket.org/img/jupyter1.png "Jupyter 1")

New: introspection

![alt text](http://kfp.bitbucket.org/img/jupyter2.png "Jupyter 2")

QT console (V 0.1)

![alt text](https://github.com/scios/fricas_kernel/raw/master/screenshots/fkernel_cygc.png "QTconsole")


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

![alt text](https://github.com/scios/fricas_kernel/raw/master/screenshots/fkernel_nb.png "NB")


#####Update V0.2

The new version 0.2 can render MathJax if one sets

```
 )set output tex on

```

in the notebook. The assets and drawbacks of MathJax rendering of FriCAS output can be seen here:

https://rawgit.com/scios/fricas_kernel/master/screenshots/fricas_nb_mathjax.htm

One may compare this to the output of the *TeXmacs* plugin (exported Pdf):

https://rawgit.com/scios/fricas_kernel/master/screenshots/fricas_cmp.pdf

####Update V0.3

Comaptible to Jupyter (messages) V3.2 

Expect: self.axp.setecho(False) ... suppress nb echo

Kernel: languageinfo

New: introspection (principle)


####Update V0.4

Rewrite of classes (theApp & theKernel). Now more generic parts. The kernel
was tested with FriCAS, Axiom and OpenAxiom on Ubuntu 14.x and Windows 7. 
Simply change the parameter **executable** in the kernel source file (top).

Introspection and code completion reliably working.

Code type is now recognized. Either single line or multiline input with or
without continuation characters (indentation mode).

####Update V0.5

New LaTeX formatting (output w. MathJax)
Colors
Concepts: Inline images, Plotting (matplotlib) 





