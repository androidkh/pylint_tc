===============
DevOps Hometask
===============

*The project contains sample Python script(s)*

:Script: count_symbols.py
:Description: counts non space symbols in the file and prints result as a table
:Usage: python count_symbols.py count_symbols.py 4
:Version: 2019-04-24


-----------------
TC Project export
-----------------

TeamCity_Hometask_20190429_031640.zip

-----------------------
Using Docker TC agent for pylint
-----------------------

1. Enter repository directory

2. Use Dockerfile to build a docker image:

.. code-block:: bash

        docker build . -t mypylint

3. Run container:

.. code-block:: bash

        docker run -it -e SERVER_URL="<url to TeamCity server>"  \
    -v <path to agent config folder>:/data/teamcity_agent/conf  mypylint

Note: af the first connection TC agent will upgrade itself from TC server. In order to avoid that during every Docker contariner restart
you may want to create a docker image as soon as agent is upgraded.
My docker image with updated TC agent (server version 2018.2.4 build 61678): https://drive.google.com/file/d/1GiufYGhOREtN5N4-fGScLJltN8KPYD_R/view?usp=sharing

