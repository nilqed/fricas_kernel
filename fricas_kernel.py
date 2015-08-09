#!/usr/bin/env python
# -*- coding: UTF-8 -*-


__author__ = "Kurt Pagani <nilqed@gmail.com>"
__svn_id__ = "$Id: theKernel.py 1 2015-08-07 20:00:41Z pagani $"


from IPython.kernel.zmq.kernelbase import Kernel
import re, os, tempfile

if os.name == 'nt':
    import winpexpect as xp
    spawn = xp.winspawn
else:
    import pexpect as xp
    spawn = xp.spawn


__version__ = '0.1'

#====================#
# User configuration #
#====================#

# theApp
executable = "fricas -nosman"
prompt_pat = "\([0-9]+\) ->"
cont_char = "_"
quit_cmd = ")quit"
readq = ')read "{}" )quiet'
tmpfile_kw = {'prefix':'ax$', 'suffix':'.input', 'delete':False}


# theKernel
_protocol_version_ = '5.0'
_implementation_ = 'fricas_kernel'
_language_ = 'spad'
_language_version_ = '0.1'
_language_info_ = {'name': 'spad', 'mimetype': 'text/plain'}
_banner_ = "FriCAS Kernel"
_help_links_ = {'text': 'FriCAS API', 'url': 'http://fricas.github.io/'}



#==============#
# theApp class #
#==============#

class theApp():

    def __init__(self, app = executable, re_prompt = prompt_pat ):

        # Store parameters
        self.app = app
        self.re_prompt = re_prompt

        # Define the App process
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
        Send the text + os.linesep to the App and expect the prompt. Moreover
        reset the error state. Return value is as in _axp_expect.
        """
        self.error = None
        n = self.axp.sendline(txt)
        return self._axp_expect()


    def start(self, **kwargs):
        """
        Action: Start (spawning) theApp.
        Return: True or False
        The following keywords (kwargs) may be used:
        args=[], timeout=30, maxread=2000, searchwindowsize=None
        logfile=None, cwd=None, env=None, username=None, domain=None
        password=None
        For details consult the pexpect manual as this parameters are
        the same as in the spawn/winspawn function respectively.
        Note: after start one may access the values as follows:
        <app_instance>.axp.<keyword>, e.g. a.axp.timeout -> 30.
        """
        if self.axp is None:
            self.axp = spawn(self.app, **kwargs)
            if os.name != "nt" : self.axp.setecho(False)
            #error on NT

        if self._axp_expect():
            self.banner = self.axp.before
            self.prompt = self.axp.after
            return True

        else:
            return False


    def stop(self):
        """
        Stop theApp (the hard way). One may also send the native quit command.
        to the App using writeln for example.
        The return value is that of the isalive() function.
        """
        if self.axp is not None:
            self.axp.close()
            self.axp = None
        return not self.isalive()


    def isalive(self):
        """
        Check if theApp is running.
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
        Write a line to theApp, i.e. as if it were entered into the
        interactive console. Output - if any - is (unmodified) stored
        in 'output'. Note: src should not contain any control characters;
        a newline (in fact os.linesep) will be added automatically.
        The continuation character, however, is no problem.
        """
        if self._axp_sendline(src):
            self.output = self.axp.before
            self.prompt = self.axp.after
            return True
        else:
            self.output = None
            return False


    def writef(self, filename):
        """
        Write the content of the file to theApp, i.e. urge theApp to read it
        in by itself.
        """
        if os.path.isfile(filename):
            return self.writeln(readq.format(filename))
        else:
            return False


    def write(self, src): # not needed here
        """
        Place the string src into a temp file and call writef, that
        is command theApp to read in the temp file. Note: the temp file
        will be deleted after having been read into theApp.
        This command allows multiline input in SPAD/Aldor form.
        """
        tmpf = tempfile.NamedTemporaryFile(**tmpfile_kw)
        tmpf.write(src)
        tmpf.close()
        rc = self.writef(tmpf.name)
        os.unlink(tmpf.name)
        return rc


    #=========================#
    # Generic part ends here. #
    #=========================#


    def cont_check(self, l):
        """
        Check if multiline code w. continuation characters is correct.
        Note: l = code.split('\n')
        """
        b = map(lambda x:x.strip()[-1] == cont_char, l[:-2])
        return reduce(lambda x,y:x and y ,b)


    def get_code_type(self, code):
        """
        Determine the code type:
        0 = single line
        1 = multiline with continuation
        2 = multiline with indentation
        """
        l = code.split('\n')
        if (len(l) == 2) and (l[1]==''):
            return 0
        if (len(l) > 2) and self.cont_check(l):
            return 1
        else:
            return 2


    def get_index(self, prompt):
        """
        Return the number N in the input prompt (N) -> of False.
        """
        m = re.match("\(([0-9]+)\)", prompt)
        if m is not None and len(m.groups()) == 1:
            return int(m.group(1))
        else:
            return False


    def get_type_and_value(self, output = None):
        """
        Get index, type and value in the 'output'.
        Default is the current output.
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
        Remove 'leqno'.
        """
        tex = re.sub(r"\\leqno\(\d*\)", "%", tex)
        tex = r"\begin{dmath*}" + "\n" + tex + "\n" + r"\end{dmath*}"
        return tex



#Issues: setecho in winpexpect!
#theKernel


#=================#
# theKernel class #
#=================#

class theKernel(Kernel):

    implementation = _implementation_
    implementation_version = __version__
    language = _language_
    language_version = _language_version_
    language_info = _language_info_
    banner = _banner_
    # help_links = _help_links_
    # protocol_version = _protocol_version_


    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.app = theApp()
        self.app.start()


    def do_execute(self, code, silent, store_history = True,
        user_expressions = None, allow_stdin = False):

        if not code.strip():
            return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}


        try:
            if code.strip() == quit_cmd:
                return self.do_shutdown(False)


            if self.app.get_code_type(code) == 2:
                self.app.write(code)
            else:
                self.app.writeln(code.rstrip())


            if self.app.hasoutput:
              output = self.app.output
              tex = self.app.extract_tex(output)
              pretex = r"$\def\sp{^}\def\sb{_}\def\leqno(#1){}$"
              #output = self.app.remove_tex(output, tex)
            else:
              output = None


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
            self.app.output = None


        try:
            exitcode = 0
            if not self.app.isalive():
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
        self.app.writeln(cmd)
        if self.app.hasoutput():
            output = self.app.output.rstrip()

        matches = output.split()
        if not matches:
            return default
        matches = [m for m in matches if m.startswith(token)]

        return {'matches': matches, 'cursor_start': start,
                'cursor_end': cursor_pos, 'metadata': dict(),
                'status': 'ok'}


    def do_inspect(self, code, cursor_pos, detail_level=0):
        data = dict()
        if (not code or not len(code) >= cursor_pos or
            not code[cursor_pos - 1] == '('):
            return {'status': 'ok', 'data': data, 'metadata': dict()}

        else:
            token = code[:cursor_pos - 1].split()[-1]
            self.app.writeln(")d op " + token)
            docstring = self.app.output
            self.app.output = None
            if docstring:
                data = {'text/plain': docstring}

            #attention: msg changed in version 5.0
            return {'status': 'ok', 'found': True,
                    'data': data, 'metadata': dict()}



    def do_shutdown(self, restart):
        "Changes in 5.0: <data> replaced by <text>"
        output = "-- Bye. Kernel shutdown "
        stream_content = {'name': 'stdout', 'text': output}
        self.send_response(self.iopub_socket, 'stream', stream_content)
        self.app.stop()
        return {'restart': False}



if __name__ == '__main__':

    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=theKernel)

