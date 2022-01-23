|GitHub top language| |Repository size| |Issues| |License| |Commit
activity| |Last commit| |PyPI Downloads| |PyPI Total Downloads| |PyPI
Version|

.. raw:: html

   <!-- omit in toc -->

CatPandoc
=========

Cat multiple documents to the terminal. The continuation of CatMD

-  `Features <#features>`__

   -  `Document Compatability <#document-compatability>`__
   -  `Terminal ‘rendering’ <#terminal-rendering>`__

-  `Roadmap <#roadmap>`__
-  `Use <#use>`__

   -  `CLI <#cli>`__
   -  `Import <#import>`__

-  `Documentation <#documentation>`__
-  `Install With PIP <#install-with-pip>`__
-  `Language information <#language-information>`__

   -  `Built for <#built-for>`__

-  `Install Python on Windows <#install-python-on-windows>`__

   -  `Chocolatey <#chocolatey>`__
   -  `Windows - Python.org <#windows---pythonorg>`__

-  `Install Python on Linux <#install-python-on-linux>`__

   -  `Apt <#apt>`__
   -  `Dnf <#dnf>`__

-  `Install Python on MacOS <#install-python-on-macos>`__

   -  `Homebrew <#homebrew>`__
   -  `MacOS - Python.org <#macos---pythonorg>`__

-  `How to run <#how-to-run>`__

   -  `Windows <#windows>`__
   -  `Linux/ MacOS <#linux-macos>`__

-  `Download Project <#download-project>`__

   -  `Clone <#clone>`__

      -  `Using The Command Line <#using-the-command-line>`__
      -  `Using GitHub Desktop <#using-github-desktop>`__

   -  `Download Zip File <#download-zip-file>`__

-  `Community Files <#community-files>`__

   -  `Licence <#licence>`__
   -  `Changelog <#changelog>`__
   -  `Code of Conduct <#code-of-conduct>`__
   -  `Contributing <#contributing>`__
   -  `Security <#security>`__
   -  `Support <#support>`__
   -  `Rationale <#rationale>`__

-  `Screenshots <#screenshots>`__

   -  `Desktop <#desktop>`__
   -  `Themes <#themes>`__

Features
--------

Document Compatability
~~~~~~~~~~~~~~~~~~~~~~

Lightweight markup formats

-  Markdown (including CommonMark and GitHub-flavored Markdown)
-  reStructuredText
-  Emacs Org-Mode
-  Emacs Muse
-  Textile
-  txt2tags

HTML formats

-  (X)HTML 4
-  HTML5

Ebooks

-  EPUB version 2 or 3
-  FictionBook2

Documentation formats

-  Haddock markup

Roff formats

-  roff man

TeX formats

-  LaTeX

XML formats

-  DocBook version 4 or 5
-  JATS

Outline formats

-  OPML

Data formats

-  CSV tables

Word processor formats

-  Microsoft Word docx
-  OpenOffice/LibreOffice ODT

Interactive notebook formats

-  Jupyter notebook (ipynb)

Wiki markup formats

-  MediaWiki markup
-  DokuWiki markup
-  TikiWiki markup
-  TWiki markup
-  Jira wiki markup

Terminal ‘rendering’
~~~~~~~~~~~~~~~~~~~~

Highlights the following:

-  Headers 1-6
-  Unordered and ordered lists
-  Block quotes
-  Bold, Italic, Strikethrough, inline code
-  Line Break (br)

Renders the following

-  Tables
-  Images (uses catimage for this so they can look a bit blurry…)

Higlights code blocks

-  Uses pygments for code syntax highlighting

Roadmap
-------

For completed components, see the changelog (link below)

===================== ============================ ======
Feature               Description                  Status
===================== ============================ ======
pandoc2pysimplegui.py Generate PySimpleGUI widgets -
===================== ============================ ======

Use
---

CLI
~~~

.. code:: bash

   usage: application.py [-h] [--width WIDTH] [--theme THEME] file

Import
~~~~~~

Take a look at test/catcomplex.py for an example of how to use catpandoc
in your own project. Or take a look at the example below

.. code:: python

   import json
   import pypandoc
   from catpandoc import pandoc2ansi, processpandoc

   output = json.loads(pypandoc.convert_file("cheatsheet.md", 'json'))
   for block in output["blocks"]:
       pandoc = pandoc2ansi.Pandoc2Ansi(130, 5, (4, 0, 0))
       processpandoc.processBlock(block, pandoc)
       print(pandoc.genOutput())

Documentation
-------------

See the `Docs </DOCS/>`__ for more information.

Install With PIP
----------------

.. code:: python

   pip install catpandoc

Head to https://pypi.org/project/catpandoc/ for more info

Language information
--------------------

Built for
~~~~~~~~~

This program has been written for Python versions 3.7 - 3.10 and has
been tested with both 3.7 and 3.10

Install Python on Windows
-------------------------

Chocolatey
~~~~~~~~~~

.. code:: powershell

   choco install python

Windows - Python.org
~~~~~~~~~~~~~~~~~~~~

To install Python, go to https://www.python.org/downloads/windows/ and
download the latest version.

Install Python on Linux
-----------------------

Apt
~~~

.. code:: bash

   sudo apt install python3.x

Dnf
~~~

.. code:: bash

   sudo dnf install python3.x

Install Python on MacOS
-----------------------

Homebrew
~~~~~~~~

.. code:: bash

   brew install python@3.x

MacOS - Python.org
~~~~~~~~~~~~~~~~~~

To install Python, go to https://www.python.org/downloads/macos/ and
download the latest version.

How to run
----------

Windows
~~~~~~~

-  Module ``py -3.x -m [module]`` or ``[module]`` (if module installs a
   script)

-  File ``py -3.x [file]`` or ``./[file]``

Linux/ MacOS
~~~~~~~~~~~~

-  Module ``python3.x -m [module]`` or ``[module]`` (if module installs
   a script)

-  File ``python3.x [file]`` or ``./[file]``

Download Project
----------------

Clone
~~~~~

Using The Command Line
^^^^^^^^^^^^^^^^^^^^^^

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to clone
   to
4. Type ‘git clone’ followed by URL in step 2

.. code:: bash

   git clone https://github.com/FHPythonUtils/CatPandoc

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

Using GitHub Desktop
^^^^^^^^^^^^^^^^^^^^

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

Download Zip File
~~~~~~~~~~~~~~~~~

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

Community Files
---------------

Licence
~~~~~~~

MIT License Copyright (c) FredHappyface (See the
`LICENSE </LICENSE.md>`__ for more information.)

Changelog
~~~~~~~~~

See the `Changelog </CHANGELOG.md>`__ for more information.

Code of Conduct
~~~~~~~~~~~~~~~

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the `Code of
Conduct <https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md>`__
for more information.

Contributing
~~~~~~~~~~~~

Contributions are welcome, please see the `Contributing
Guidelines <https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md>`__
for more information.

Security
~~~~~~~~

Thank you for improving the security of the project, please see the
`Security
Policy <https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md>`__
for more information.

Support
~~~~~~~

Thank you for using this project, I hope it is of use to you. Please be
aware that those involved with the project often do so for fun along
with other commitments (such as work, family, etc). Please see the
`Support
Policy <https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md>`__
for more information.

Rationale
~~~~~~~~~

The rationale acts as a guide to various processes regarding projects
such as the versioning scheme and the programming styles used. Please
see the
`Rationale <https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md>`__
for more information.

Screenshots
-----------

Desktop
~~~~~~~

.. container::

Themes
~~~~~~

.. container::

.. |GitHub top language| image:: https://img.shields.io/github/languages/top/FHPythonUtils/CatPandoc.svg?style=for-the-badge
   :target: ../../
.. |Repository size| image:: https://img.shields.io/github/repo-size/FHPythonUtils/CatPandoc.svg?style=for-the-badge
   :target: ../../
.. |Issues| image:: https://img.shields.io/github/issues/FHPythonUtils/CatPandoc.svg?style=for-the-badge
   :target: ../../issues
.. |License| image:: https://img.shields.io/github/license/FHPythonUtils/CatPandoc.svg?style=for-the-badge
   :target: /LICENSE.md
.. |Commit activity| image:: https://img.shields.io/github/commit-activity/m/FHPythonUtils/CatPandoc.svg?style=for-the-badge
   :target: ../../commits/master
.. |Last commit| image:: https://img.shields.io/github/last-commit/FHPythonUtils/CatPandoc.svg?style=for-the-badge
   :target: ../../commits/master
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/catpandoc.svg?style=for-the-badge
   :target: https://pypistats.org/packages/catpandoc
.. |PyPI Total Downloads| image:: https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fcatpandoc
   :target: https://pepy.tech/project/catpandoc
.. |PyPI Version| image:: https://img.shields.io/pypi/v/catpandoc.svg?style=for-the-badge
   :target: https://pypi.org/project/catpandoc
