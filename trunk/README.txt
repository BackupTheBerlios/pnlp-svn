====
JNLP
====
:Author: Miki Tebeka <miki.tebeka@gmail.com>
:Date: 03/25/2008

Abstract
========
Python web start (a-la jnlp_), show run from a Python "vanilla" install.

We download all needed modules, set PYTHONPATH and call main script.

Building
========
`python setup.py install` should do the trick.

Testing
=======
We use nose_ testing framework, just go to the `tests` directory and run
`runtests`.

------

.. _jnlp: http://java.sun.com/products/javawebstart/download-spec.html
.. _nose: http://somethingaboutorange.com/mrl/projects/nose/

.. comment: vim:ft=rst spell
