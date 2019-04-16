# HoloRekognition
HoloRekognition is a Microsoft HoloLens Facial identification and recognition application. It is an academic project planned and developed in the Winter of 2019 by the following individuals as a part of the capstone requirement for the BYU Marriott School of Business MISM Program: 

* [Levi Bowser](https://github.com/LeviBowser)
* [Nathan Barton](https://github.com/nbarton915)
* [Cameron Spilker](https://github.com/CameronSpilker)

Additional backend utilities were created through this capstone to interact with Azure Face API:

* [CustomPersonMaker](https://github.com/nbarton915/CustomPersonMaker): Created As Convenience Utility For Integrating Project HoloRekognition With Azure Face Resource - Create, train, fetch, update, and delete (people and groups)
* [Project HoloRekognition](https://github.com/LeviBowser/HoloRekognition): Project HoloRekognition 

# DonwloadPersonGroupInformation
Created As Convenience Utility For Integrating Project HoloRekognition And Azure Face Resource

Download Person Group Information from your Azure Face Resource

# Objective(s)
* Retrieve all People information from a Person Group from an Azure Face Resource and put into a CSV file.

# Prerequisite(s) 
* The script was written in Python 3.7.2. This version of Python is recommended.
   * https://www.python.org/downloads/release/python-372/

# Execute Script
* There are three pieces of information at the beginning of the script you will need to input (using a text editor of your choice, my preference is VS Code)

1. **SUBSCRIPTION_KEY** (this can be found in your Azure Face Resource)
    * https://github.com/nbarton915/CustomPersonMaker
    
2. **BASE_URL** (if you made your location is "West US" you can use the link below)
    * https://westus.api.cognitive.microsoft.com/face/v1.0/ 
    
3. **PERSON_GROUP_ID** (this ID is created when you make your first person group)
    * https://github.com/nbarton915/CustomPersonMaker


Once you have set the defaults for the three variables mentioned above, you will be able to run the script.

To execute the script, use a terminal navigate to where the main.py file is stored. 

Enter the following command:

```python
python3 main.py
```

A .csv file named "person_group_info <current-date>” will be created in the same location as the main.py file. 


# Summary
Whenever you need an updated list of all groups and people from your Azure Face Resource you can run this python script and retrieve it. You can extend this code to add additional functionality.
