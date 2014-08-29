from distutils.core import setup
from distutils.command.install import install
import json
import os.path
import sys

kernel_json = {"argv":[sys.executable, "-m", "fricas_kernel", "-f",
               "{connection_file}"], "display_name":"FriCAS",
               "language":"fricas", "codemirror_mode":"shell"
}

class install_with_kernelspec(install):
    def run(self):

        install.run(self)

        # Kernel specification
        from IPython.kernel.kernelspec import KernelSpecManager
        from IPython.utils.path import ensure_dir_exists
        destdir = os.path.join(KernelSpecManager().user_kernel_dir, 'fricas')
        ensure_dir_exists(destdir)
        with open(os.path.join(destdir, 'kernel.json'), 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)

svem_flag = '--single-version-externally-managed'
if svem_flag in sys.argv:
    sys.argv.remove(svem_flag)

setup(name='fricas_kernel',
      version='0.1',
      description='A FriCAS kernel for IPython',
      long_description="None",
      author='Kurt Pagani',
      author_email='kp@scios.ch',
      url='https://bitbucket.com/kfp/fricas_kernel',
      py_modules=['fricas_kernel'],
      cmdclass={'install': install_with_kernelspec},
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Topic :: CAS :: FriCAS',
      ]
)