# PackagingSystem

Clone the repository to your local system
-------------------------------------------
McAfee_Project.zip
McAfee.zip to D drive

Installation
----------------------
Step 1 :  Install Python 3.7.X or greater

Step 2 :  Create virtual Environment
       2.1 : pip install virtualenv
       2.2 : In AutomationFrameworkPOM repo, open command prompt and type -"virtualenv env"
       2.3 : Activate virtual environment, type : .\env\Scripts\activate
       2.4 : Install required python module, type : pip install -r requirement.txt

Run
-------------------------
pytest -v -s --html=./Reports/report.html testCases/test_system.py --dest_file D:\McAfee\Result --cfg_file_path .\configuration --layout_type Release
