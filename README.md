# TornadoVMDashboard
Made by Kushagra Srivastava for the TornadoVM team.

A dashboard to visualise benchmarks for the TornadoVM project. 

## Installation

1. Clone the repository 

2. To activate virtual environment, you must navigate to the 

```TornadoDashProject/TornadoVisualiser``` 

directory and call 

```source venv/bin/activate``` 

to start the virtual environment. You will need to have installed ```virtualenv```.

3. Install project dependencies using

```pip install -r requirements.txt```

4. Migrate the database to set it up using

```python3 manage.py migrate```

5. Run the server with the following command

```python3 manage.py runserver```

The server will now be hosted locally.

## Database Usage

The db_dash.ipynb notebook is designed to perform the following tasks:

1. Create a directory structure for storing information files related to the TornadoVM project.
2. Generate various information files, including version details, benchmark results, and system information.
3. Save the output of each command to its respective file.


Clicking "Run All" will compile all relevant information into files within the info_files directory.




