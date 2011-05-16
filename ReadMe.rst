Facebook Engineering Puzzles
#############################

I love puzzles. So of course this repository is the tests and solutions to
the list of puzzles shown on `Facebook Puzzle
Masters<http://www.facebook.com/careers/puzzles.php>`_.

Projects Used
==========================
Testing is done with
`nose<http://somethingaboutorange.com/mrl/projects/nose/1.0.0/>`_ and the
`sure<https://github.com/gabrielfalcao/sure>`_ testing tools.

Setup and Testing
=========================
Add `shelter<https://gist.github.com/975467>`_ to your ~/.bashrc (just a
simple alias to mkvirtualenv --no-site-packages that I use frequently).

    shelter facebook-puzzles
    pip install -r requirements.txt
    nosetests
