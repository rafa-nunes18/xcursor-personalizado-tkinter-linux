#!/usr/bin/env python  
#  
# Script de configuração para tkXcursor  
#  
# Copyright (c) 2009 Igor E. Novikov  
#
# Versão 2.0.0 - 2024 Editado por Rafael A. Nunes 
#  
# Esta biblioteca é software livre; você pode redistribuí-la e/ou  
# modificá-la sob os termos da Licença Pública Geral Menor GNU  
# conforme publicada pela Free Software Foundation; seja  
# a versão 2.1 da Licença, ou (a seu critério) qualquer versão posterior.  
#  
# Esta biblioteca é distribuída na esperança de que seja útil,  
# mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de  
# COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO. Veja a GNU  
# Licença Pública Geral Menor para mais detalhes.  
#  
# Você deve ter recebido uma cópia da Licença Pública Geral Menor GNU  
# junto com esta biblioteca; se não, escreva para a Free Software  
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, EUA  
#  
# Uso:  
# --------------------------------------------------------------------------  
# Para compilar o pacote: python3 setup.py build  
# Para instalar o pacote: python3 setup.py install  
# Para criar uma distribuição de código fonte:   python3 setup.py sdist  
# Para criar um pacote binário Debian:  python3 setup.py bdist_deb  
#   
# Certifique-se de que você tem as dependências do sistema instaladas:  
# sudo apt install tcl-dev tk-dev libxcursor-dev  
#   
# Ajuda sobre os formatos de distribuição disponíveis: python3 setup.py bdist --help-formats

from setuptools import setup, Extension  
import os  

if __name__ == "__main__":  

    share_dirs = ['GNU_LGPL_v2', 'COPYRIGHTS']  

    src_path = 'src/'  
 
    tcl_include_path = "/usr/include/tcl8.6"  
    tcl_ver = "8.6" if os.path.isdir(tcl_include_path) else ""  
    tcl_include_dirs = [tcl_include_path] if tcl_ver else []  
 
    tkXcursor_include_dirs = ['/usr/include/X11/Xcursor'] + tcl_include_dirs  
    tkXcursor_src = os.path.join(src_path, '_tkXcursor.c')  

    tkXcursor_module = Extension(  
        'tkXcursor._tkXcursor',  
        define_macros=[('MAJOR_VERSION', '2'), ('MINOR_VERSION', '0')],  
        sources=[tkXcursor_src],  
        include_dirs=tkXcursor_include_dirs,  
        libraries=['tk' + tcl_ver, 'tcl' + tcl_ver, 'Xcursor']  
    )  

    setup(  
        name='tkXcursor',  
        version='2.0.0',  
        description='Xcursor python extension for Tkinter widgets',  
        author='Igor E. Novikov',  
        author_email='sk1.project.org@gmail.com',  
        maintainer='Igor E. Novikov',  
        maintainer_email='sk1.project.org@gmail.com',  
        license='LGPL v2',  
        url='http://sk1project.net',  
        download_url='https://github.com',         
        long_description='''  
        tkXcursor é uma extensão Python que fornece gerenciamento de cursores RGBA/animados personalizados para widgets Tkinter.
        Este pacote funciona no Linux Mint 22.     
        ''',  
        classifiers=[  
            'Development Status :: 5 - Stable',  
            'Environment :: X11 Applications',  
            'Operating System :: POSIX',  
            'Operating System :: Linux',  
            'License :: OSI Approved :: LGPL v2',  
            'Programming Language :: Python',  
            'Programming Language :: C',  
            'Topic :: Desktop Environment',  
            'Topic :: Multimedia :: Graphics',  
        ],  
        packages=['tkXcursor'],  
        package_dir={'tkXcursor': 'src'},  
        ext_modules=[tkXcursor_module],  
        python_requires='>=3.6' 
    )  
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
