# -*- coding: UTF-8 -*-
#!/usr/bin/env python

__author__ = "Kurt Pagani <nilqed@gmail.com>"
__svn_id__ = "$Id:$"


# ========================================================================
# FriCAS (wrapper) kernel for IPython
# ========================================================================
# Based on the IPython "bash" wrapper kernel by Thomas Kluyver (BSD lic.)
# (url:https://github.com/takluyver/bash_kernel) and IPython doc
# "Making simple Python wrapper kernels" (new in version 3.0)
# (url:http://ipython.org/ipython-doc/dev/development/wrapperkernels.html).
# Instead of using pexepct's 'replwrap' we use winpexpect/pexpect spawn
# and expect functions wrapped in a class called 'FriCAS'.
#
# ------------
# Prerequsites
# ------------
# IPython 3.0dev or higher (https://github.com/ipython/ipython)
# -- get it if necessary: git clone https://github.com/ipython/ipython.git
#
# Windows: winpexpect 1.5 or higher, FriCAS for Cygwin
# Unix: pexpect 3.3 or higher, FriCAS for Un*x
#
# probably: jsonschema, jsonpointer, newer Tornado for nb
#
# --------------
# Install kernel
# --------------
# $python kernel_setup.py install
# (should push a kernel spec to ~/.ipython/kernels)
#
# Test directly from git clone direcotry "ipython":
# cd (git cloned)/ipython
# $python -m IPython qtconsole --kernel fricas
#
# Otherwise, if you have version 3.0dev installed then start as usual.
#

from IPython.kernel.zmq.kernelbase import Kernel

#from IPython.core.display import Latex, Image, display_latex, display

import re, os

if os.name == 'nt':
    import winpexpect as xp
    spawn = xp.winspawn
else:
    import pexpect as xp
    spawn = xp.spawn


__version__ = '0.2'

fricas_exe = "fricas -nosman"
prompt_pat = "\([0-9]+\) ->"

class FriCAS():
  """
  FriCAS base class. Handle the interaction with the console
  window and provide all low level routines for a device and
  os independent subclass.
    - start, stop
    - read header/banner
    - expect prompt
    - handle i/o (send input, read output)
    - detect/manage errors
    - store history
  """

  def __init__(self, app = fricas_exe, re_prompt = prompt_pat ):
    """
    Arguments:
        - app ....... start command
        - re_prompt .... re pattern for the prompt
    """

    # Store parameters
    self.app = app
    self.re_prompt = re_prompt

    # Define the FriCAS process
    self.axp = None

    # The header/banner read when started
    self.banner = None

    # The current prompt
    self.prompt = None

    # Output caught after a command has been sent (always unmodified)
    self.output = None

    # Last error enountered (0: OK, 1: EOF, 2: TIMEOUT)
    self.error = None

    # Log file ([win]spawn)
    self.logfile = None


  def _axp_expect(self):
    """
    Return True if the prompt was matched otherwise return False and
    set the error = 1 if EOF or error = 2 if TIMEOUT.
    """
    self.error = self.axp.expect([self.re_prompt, xp.EOF, xp.TIMEOUT])
    if self.error == 0:
      self.error = None
      return True
    else:
      return False


  def _axp_sendline(self, txt):
     """
     Send the text + os.linesep to FriCAS and expect the prompt. Moreover
     reset the error state. Return value is as in _axp_expect.
     """
     self.error = None
     n = self.axp.sendline(txt)
     return self._axp_expect()


  def start(self, **kwargs):
    """
    --- #YAML
    Action: Start (spawning) FriCAS.
    Return: True or False
    The following keywords (kwargs) may be used:
      args=[], timeout=30, maxread=2000, searchwindowsize=None
      logfile=None, cwd=None, env=None, username=None, domain=None
      password=None
    For details consult the pexpect manual as this parameters are the same
    as in the spawn/winspawn function respectively.
    Note: after start one may access the values as follows:
      <fricas_instance>.axp.<keyword>, e.g. a.axp.timeout -> 30.
    """
    if self.axp is None:
      self.axp = spawn(self.app, **kwargs)
      if self._axp_expect():
        self.banner = self.axp.before
        self.prompt = self.axp.after
        return True
      else:
        return False


  def stop(self):
    """
    Stop FriCAS (the hard way). One may also send the command ')quit'
    to FriCAS using writeln for example.
    The return value is that of the isalive() function.
    """
    if self.axp is not None:
      self.axp.close()
      self.axp = None
    return not self.isalive()


  def isalive(self):
    """
    Check if FriCAS is running.
    """
    if self.axp is not None:
      return self.axp.isalive()
    else:
      return False


  def haserror(self):
    """
    True if there was an error.
    """
    return self.error is not None


  def hasoutput(self):
    """
    True if there is output.
    """
    return self.output is not None


  def writeln(self, src):
    """
    Write a line to FriCAS, i.e. as if it were entered into the interactive
    console. Output - if any - is (unmodified) stored in 'output'.
    Note: src should not contain any control characters; a newline (in fact
    os.linesep) will be added automatically. FriCAS's continuation character,
    however, is no problem.
    """

    if self._axp_sendline(src):
      self.output = self.axp.before
      self.prompt = self.axp.after
      return True
    else:
      self.output = None
      return False


  def writef(self, filename): # not needed here
    """
    Write the content of the file to FriCAS, i.e. urge FriCAS to read it in
    by itself.
    """

    #if os.path.isfile(filename):
    #  return self.writeln(self.cfg.cmd_read_quiet.format(filename))
    #else:
    #  return False
    pass

  def write(self, src): # not needed here
    """
    Place the string src into a temp file and call writef, that is command
    FriCAS to read in the temp file. Note: the temp file will be deleted
    after having been read into FriCAS.
    This command allows multiline input in SPAD/Aldor form.
    """

    #tmpf = tempfile.NamedTemporaryFile(**self.cfg.tmpfile_kw)
    #tmpf.write(src)
    #tmpf.close()
    #rc = self.writef(tmpf.name)
    #os.unlink(tmpf.name)
    #return rc
    pass

    #+ FriCAS0 ends here ;
    # some special methods for the use of the magic %axsys.
    # *** not needed here

  def get_index(self, prompt):
    """
    Return the number N in the input prompt (N) ->.
    """
    m = re.match("\(([0-9]+)\)", prompt)
    if m is not None and len(m.groups()) == 1:
      return int(m.group(1))
    else:
      return False


  def get_type_and_value(self, output = None):
    """
    Get index, type and value in the 'output'. Default is the current output.
    """
    if output is None: output = self.output

    r = output.strip(" \n").split("Type:")
    ri = re.match("^\(([0-9]+)\)", r[0]).group(1)
    rv = re.split("^\([0-9]+\)",r[0])[1].strip(" \n")
    rv = re.sub("_\n","", rv)
    rt = r[1].strip()
    return ri, rt, rv


  def extract_types(self, data):
    """
    Extract the type(s) returned (if any).
    """
    ty = re.findall('Type:[a-zA-Z0-9_. ]*', data)
    ty = map(lambda x: x.replace('Type:',''), ty)
    return map(lambda x: x.strip(), ty)


  def extract_tex(self, data):
    """
    Extract TeX code from data.
    """
    tex = re.findall('\$\$[^\$]*\$\$', data)
    return tex


  def remove_tex(self, data, tex = []):
    """
    Remove TeX code from data.
    """
    for s in tex:
      data = data.replace(s,'')
    return data


  def split_tex(self, data):
    """
    Split the output by TeX code into text substrings .
    """
    return re.split('\$\$[^\$]*\$\$', data)


  def tex_breqn(self, tex):
    """
    Transform TeX code for using the breqn package.
    """
    # remove leqno's
    tex = re.sub(r"\\leqno\(\d*\)", "%", tex)
    tex = r"\begin{dmath*}" + "\n" + tex + "\n" + r"\end{dmath*}"
    return tex




class FricasKernel(Kernel):

    implementation = 'fricas_kernel'
    implementation_version = __version__
    language = 'fricas'
    language_version = '0.1'
    banner = "FriCAS Kernel"


    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.fricas = FriCAS()
        self.fricas.start()


    def do_execute(self, code, silent, store_history = True,
        user_expressions = None, allow_stdin = False):

        if not code.strip():
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}


        try:
            if code.strip() == ")quit":
                return self.do_shutdown(False)

            self.fricas.writeln(code.rstrip())

            if self.fricas.hasoutput: 
              output = self.fricas.output
              tex = self.fricas.extract_tex(output)
              pretex = r"$\def\sp{^}\def\sb{_}\def\leqno(#1){}$"
              #output = self.fricas.remove_tex(output, tex)
              
    
            else:
              output = "none"

            if tex == []:
                data = {'text/plain':output}
            else:
                data = {'text/plain':output,'text/latex':pretex+tex[0]}

            if not silent:
                #stream_content = {'name': 'stdout', 'data': output}
                #self.send_response(self.iopub_socket, 'stream', stream_content)
                
                display_data = {'source':'me', 'data':data, 'metadata':{}}
                self.send_response(self.iopub_socket, 'display_data', display_data) 
                
            if interrupted:
                return {'status': 'abort', 'execution_count': self.execution_count}

        except:
            pass


        try:
            exitcode = 0
            if not self.fricas.isalive():
                exitcode = 1

        except Exception:
            exitcode = 1

        if exitcode:
            return {'status': 'error', 'execution_count': self.execution_count,
                    'ename': '', 'evalue': str(exitcode), 'traceback': []}
        else:
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

    def do_complete(self, code, cursor_pos):
        code = code[:cursor_pos]
        default = {'matches': [], 'cursor_start': 0,
                   'cursor_end': cursor_pos, 'metadata': dict(),
                   'status': 'ok'}

        if not code or code[-1] == ' ':
            return default

        tokens = code.replace(';', ' ').split()
        if not tokens:
            return default

        token = tokens[-1]
        start = cursor_pos - len(token)
        cmd = ')what operations %s' % token
        self.fricas.writeln(cmd)
        if self.fricas.hasoutput():
            output = self.fricas.output.rstrip()

        matches = output.split()
        if not matches:
            return default
        matches = [m for m in matches if m.startswith(token)]

        return {'matches': matches, 'cursor_start': start,
                'cursor_end': cursor_pos, 'metadata': dict(),
                'status': 'ok'}


    def do_shutdown(self, restart):
        output = "-- Bye. Kernel shutdown "
        stream_content = {'name': 'stdout', 'data': output}
        self.send_response(self.iopub_socket, 'stream', stream_content)
        self.fricas.stop()
        #self.fricas.writeln(")quit")


if __name__ == '__main__':

    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=FricasKernel)






