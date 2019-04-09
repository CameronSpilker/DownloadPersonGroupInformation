# DonwloadPersonGroupInformation
Created As Convenience Utility For Integrating Project HoloRekognition And Azure Face Resource

Download Person Group Information from your Azure Face Resource

# Objective(s)
* Retrieve all People information from a Person Group from an Azure Face Resource and put into a CSV file.

# Prerequisite(s) 
* The script was written in Python 3.7.2. This version of Python is recommended. (download here https://www.python.org/downloads/release/python-372/)

# Execute Script
* There are three pieces of information at the beginning of the script you will need to input (using a text editor of your choice, my preference is VS Code)

1. #SUBSCRIPTION_KEY# (this can be found in your Face Resource (See https://github.com/nbarton915/CustomPersonMaker README.md towards the bottom)
2. #BASE_URL# (if you made your location for Face Resource West US you can use what is already there, we have also provided the link below)
    * https://westus.api.cognitive.microsoft.com/face/v1.0/ 
3. #PERSON_GROUP_ID# (this is created when you make your first person group (See https://github.com/nbarton915/CustomPersonMaker README.md)


Once you have set the defaults for the three variables mentioned above, you will be able to run the script.

To execute the script, using a terminal navigate to where the .py file is stored. 

Enter the following command:
* python3 main.py


A .csv file named "person_group_info <current-date>” will be created in the same location as the .py file. 


# Summary
Whenever you need an updated list of all the groups and people from your Azure Face Resource you can run this python script and get it. You can extend this code to add additional functionality.
