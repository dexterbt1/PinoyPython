Pinoy-Python Users Group
========================

Dependencies
------------

- python >= 2.6
- python header files
- pip
- virtualenv
- header files for: (check with your OS package manager)
    - libjpeg
    - libpng
    - libfreetype


Quick Setup
-----------

    git clone git://github.com/dexterbt1/PinoyPython.git
    cd PinoyPython && ./setup-virtualenv.sh
    cd ppugweb && source bin/activate
    python manage.py syncdb
    python manage.py runserver

