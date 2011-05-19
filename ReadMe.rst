Facebook Engineering Puzzles
#############################

I love puzzles. So of course this repository is the tests and solutions to
the list of puzzles shown on `Facebook Puzzle
Masters <http://www.facebook.com/careers/puzzles.php> `_.


Instructions
============

Submissions should be sent via email to the address: **{0xFACEB00C>>2 in decimal}@fb.com**

The subject line of the email must **exactly match** the puzzle keyword.
Failure to do so means your submission will not be evaluated. Submissions
are evaluated and the results emailed back every four hours.

If you have a Facebook account, send your submission from the same email
address you login to Facebook, or we may not be able to find you!

The actual text body of the email will be ignored for grading purposes.
Make sure all solution materials are attachments (see below).

Your solution must build or supply an executable file/script whose name is
**exactly the same** as the puzzle keyword (case-sensitive). You do not have
to worry about file permissions for the main executable, they will be
checked and/or set for you.

You may compress/archive your solution files with **tar** or **zip**. The file
extensions of these archives must be **.zip, .tar, .tar.gz, .tgz, or
.tar.bz2**. If you compress your solution, only submit one compressed file.

If you compressed your solution, any Makefile/build.xml files (and the
executable file itself) need to be uncompressed and/or built into the **same
root directory** as the compressed archive itself or your submission will
result in a build error.

If your solutions uses one of the compiled languages, it must be buildable
using either **GNU Make 3.81 or Ant 1.7.0** using the commands **make or ant**
from the root directory where your submission is stored. You must supply
your own makefiles or build.xml files.

You may assume the compilers are within the execution environment's path.
The interpreted scripting languages have been installed in both
**/usr/bin** and **/usr/local/bin** (the only exceptions are 
**/bin/bash** and **/bin/sh**) 

If you make a mistake in your submission, you may send another email.
Prior incorrect or malformed submissions will not be counted against you.


Projects Used
==========================
Testing is done with
`nose <http://somethingaboutorange.com/mrl/projects/nose/1.0.0/>`_ and the
`sure <https://github.com/gabrielfalcao/sure>`_ testing tools.


Setup and Testing
=========================
Add `shelter <https://gist.github.com/975467>`_ to your ~/.bashrc (just a
simple alias to mkvirtualenv --no-site-packages that I use frequently).

    shelter facebook-puzzles
    pip install -r requirements.txt
    nosetests


