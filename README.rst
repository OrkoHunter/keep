keep
====

Keep and view terminal commands in terminal only

.. code:: sh

    $ keep watch -n 1 free -m
    Description : To show RAM usage and time every second on terminal screen
    $ keep sl
    Description : Stop the Train !
    $ keep "fortune | cowsay"
    Description : What is cow's opoonion about you?

Review your saved commands by ``$ keep list``.

Use ``grep`` to search for a saved command.

Example :

::

    $ keep list | grep -i "ram usage"

    1. watch -n 1 free -m : To show RAM usage and time every second on terminal screen

USAGE : \* Save the commands you usually forget in ssh sessions

Installation
~~~~~~~~~~~~

::

    $ pip3 install keep

Happy Coding !
