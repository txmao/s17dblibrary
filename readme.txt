Library Management System (LMS)

###
For design document and user guide, please refer to ./Doc/lmsDesignDoc.pdf, and ./Doc.lmsUserGuide.pdf
###

###
Technical Dependencies:
  Languages:
  - Python 2.7.12
  - PyQt4
  - mysql  Ver 14.14 Distrib 5.7.11, for Linux (x86_64) using  EditLine wrapper
  - bash
  OS:
  - Ubuntu 16.04.1 LTS
###

###
How to compile and run:
  1. Execute the SQL script file ./Schema/s17-library.sql to create the schema, in command line;
  2. Initial popularize the database with .csv file provided in ./Data by typing following in command line:
       sh iniDB.sh
  3. Run the GUI by typing following in command line:
       sh LMS.sh
###

References:
https://pythonspot.com/qt4-table/
http://blog.csdn.net/lainegates/article/details/8314287