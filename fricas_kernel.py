#!/usr/bin/env python
# -*- coding: UTF-8 -*-


__author__ = "Kurt Pagani <nilqed@gmail.com>"
__svn_id__ = "$Id: theKernel.py 3 2015-08-18 03:28:01Z pagani $"


from IPython.kernel.zmq.kernelbase import Kernel
import re, os, tempfile

if os.name == 'nt':
    import winpexpect as xp
    spawn = xp.winspawn
else:
    import pexpect as xp
    spawn = xp.spawn


__version__ = '0.5'

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
type_color = r"blue"
type_size = r"\scriptsize"
tex_color = r"black"
tex_size = r"\normalsize"


# theKernel
_protocol_version_ = '5.0'
_implementation_ = 'fricas_kernel'
_language_ = 'spad'
_language_version_ = '0.1'
_language_info_ = {'name': 'spad', 'mimetype': 'text/plain'}
_banner_ = "FriCAS Kernel"
_help_links_ = {'text': 'FriCAS API', 'url': 'http://fricas.github.io/'}


# Templates (TeX)

pretex1 = r"\(\def\sp{^}\def\sb{_}\def\leqno(#1){}\)"
pretex2 = r"\(\def\erf\{\mathrm{erf}}\def\sinh{\mathrm{sinh}}\)"
pretex3 = r"\(\def\zag#1#2{{{ \left.{#1}\right|}\over{\left|{#2}\right.}}}\)"
pretex4 = r"\(\require{color}\)"
pretex = pretex1+pretex2+pretex3+pretex4
ljax = r"$$"  # variants: r"\("
rjax = r"$$"  #           r"\)"

# texout_types.format(tex_color,tex_size,tex,type_color,type_size,type)
texout_types = r"""
{{\color{{{0}}} {1} {2}}} \\[0.9ex] {{\color{{{3}}} {4} \text{{{5}}}}} \\
"""

# texout.format(tex_color,tex_size,tex)
texout = r"""
{{\color{{{0}}} {1} {2}}}
"""



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
        ty = re.findall('Type:[a-zA-Z0-9_.\(\) ]*', data)
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

            if code.startswith(")python"):
                # compile/exec , namespaces ?
                result = str(eval(code.replace(")python","").lstrip()))
                data = {'text/plain':result}
                display_data = {'source':'me', 'data':data, 'metadata':{}}
                self.send_response(self.iopub_socket, 'display_data', display_data)
                return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}


            if code.startswith(")logo"):
                data = {'image/png':logo}
                display_data = {'source':'me', 'data':data, 'metadata':{}}
                self.send_response(self.iopub_socket, 'display_data', display_data)
                return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

            if code.startswith(")plot"):
                try:
                    import matplotlib.pyplot as plt
                    from io import BytesIO
                    import base64
                except:
                    return False
                plt.figure()
                plt.plot([1,2,3,4,5,6,7], [1,4,9,16,25,36,49])
                plt.title('PyPlot Test')
                #
                figfile = BytesIO()
                plt.savefig(figfile, format='png')
                figfile.seek(0) # rewind
                figdata_png = base64.b64encode(figfile.getvalue())
                #
                # <img src="data:image/png;base64,{{ result }}"\>
                #
                data = {'image/png':figdata_png}
                display_data = {'source':'me', 'data':data, 'metadata':{}}
                self.send_response(self.iopub_socket, 'display_data', display_data)
                return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}



            if self.app.get_code_type(code) == 2:
                self.app.write(code)
            else:
                self.app.writeln(code.rstrip())


            if self.app.hasoutput:
              output = self.app.output
              tex = self.app.extract_tex(output)
            else:
              output = None



            if tex == []:
                data = {'text/plain':output}
            else:
                ty = self.app.extract_types(output)
                if len(ty) >= len(tex):
                    b = ""
                    for j in range(0,len(tex)):
                        b += texout_types.format(tex_color,tex_size,
                                  tex[j].strip().strip('$$'), type_color,
                                  type_size, ty[j])

                    texstr = pretex + ljax + b + rjax
                    data = {'text/plain':output,'text/latex':texstr}
                else:
                    b = ""
                    for j in range(0,len(tex)):
                        b += texout.format(tex_color,tex_size,
                                  tex[j].strip().strip('$$'))
                    texstr = pretex + ljax + b + rjax
                    data = {'text/plain':output,'text/latex':texstr}



            if not silent:
                display_data = {'source':'pax', 'data':data, 'metadata':{}}
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



#import base64
#with open("t.png", "rb") as imageFile:
#    str = base64.b64encode(imageFile.read())
#    print str
logo = """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"""



if __name__ == '__main__':

    from IPython.kernel.zmq.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=theKernel)

