************
INTRODUCTION
************
This file describes how to set up and use the Python wrapper code for Melissa DATA's Address Object.
*************
PREREQUISITES
*************

To make use of the Address Object Python wrapper you will need:

* An installation of Python. This Wrapper was tested with Python 2.5.2.

* The Melissa DATA Address Object library and data files installed.
  These files are installed automatically if you run setup.exe. By default, the Address Object 
  Library (mdAddr.dll) is installed in:
	C:\Program Files\Melissa DATA\DQT\AddrObj\dll_64bit
* 32bit version available in C:\Program Files\Melissa DATA\DQT\AddrObj\dll_32bit
  and the Address Object data files in:
	C:\Program Files\Melissa DATA\DQT\Data

You will need to know the location of these items in order to install and run the Python wrapper.


**********************
Wrapper compatibility
**********************

If the provided pre-compiled wrappers are not compatible with your environment, the necessary files for compilation can be found in the 'interfaces' folder of the object's main directory.


***********
Demo Mode
***********

Address Object will function in Demo mode without a valid license string. In Demo mode, only Nevada addresses will be validated. Please contact your sales representative at 1-800-MELISSA ext. 3 for a valid license.


*************
Installation
*************

Copy the entire folder that contains this readme.txt into a local directory on your computer.


*****
Setup
*****

You will need to allow _mdAddrPythonWrapper.pyd to find mdAddr.dll. You can do this by:

	1. Adding the directory containing mdAddr to your PATH environment variable. 
	   ex: set PATH=%PATH%;C:\Program Files\Melissa DATA\DQT\AddrObj\dll_64bit
	* 32bit version available in C:\Program Files\Melissa DATA\DQT\AddrObj\dll_32bit

	or

	2. Copy mdAddr.dll into the directory with _mdAddrPythonWrapper.pyd.



**************************
Setting up the Sample Code
**************************

Open AddressSample.py for editing. You can set the license string:

	License = "Demo"

and also the path to the Address Object Data Files:

	DataPath = r"C:\Program Files\Melissa Data\DQT\Data"


***********************
Running the Sample Code
***********************

Navigate to the directory containing the python wrapper using command line and type:
	python AddressSample.py


*******
Updates
*******

The files generated/included in this wrapper do not need to be changed for DQ Suite updates unless there is a method signature change in the object. If a new method is added, you will need to rebuild the wrapper to use the new method. 

****
Note
****

Here are some general solutions if you run into problems:

Q. I get an error saying "can't find mdAddr.dll."
A. This means that _mdAddrPythonWrapper.pyd cannot link to mdAddr.dll. Please follow the steps in
the Setup section above.

Q. I get an error saying "cannot import module mdAddrPythonWrapper"
A. The current _mdAddrPythonWrapper.pyd was compiled using Python 2.5.2. You might be using another version of Python. You will need another version of _mdAddrPythonWrapper.pyd that uses the version of Python on your system. 
Please look in the "Source" folder and read the readme for instructions. 


COPYRIGHT NOTICE

(C) 2014 Melissa Data Corporation. All rights reserved.
