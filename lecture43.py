# pip install virtualenv (package to create virtual environment in any folder)
# virtualenv par (create a virtual environment with the name specifiend (par) in which our python will get cloned so that we can install the libraries according to us.)
# .\par\Scripts\activate (to activate the created virtual environment. Before using the virtual environment we have to activate it.)

# Note- IF the above command does not work- first open the windows powershell (run as administrator) and then type "set-executionpolicy remotesigned" and then try.

# deactivate - this command allows you to get out of the virtual environment.
# pip install package-name to install the package in virtual environment.

# python- to get into python interpreter and exit() to get out of the python interpreter.
# pip unistall package-name to uninstall the package from our virtual environment
# pip freeze > requiremnts.txt - to create the list of all the libraries installed in our virtual environments with their respective versions
# pip install package_name==version_number - to install the specific verison of a specific package in python
# pip install -r .\requirements.txt - to install all the dependencies at once saved in the requirements.txt file


# virtalenv --system-site-packages parth - create a new virtual environment with name parth and include all the dependencies which are already previously installed in the computer.