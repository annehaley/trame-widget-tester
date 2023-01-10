===================
Trame Widget Tester
===================

An example Trame application


* Free software: Apache Software License


Getting data
----------

.. code-block:: console

    mkdir -p data
    wget -O data/skull.vti "https://github.com/Kitware/vtk-js-datasets/blob/master/data/vti/skull.vti?raw=true"


Installing
----------

Install the application

.. code-block:: console

    pip install -e .


Install widgets for testing

.. code-block:: console

    pip install [/absolute/path/to/widget_repo]


Run the application

.. code-block:: console

    trame-widget-tester
