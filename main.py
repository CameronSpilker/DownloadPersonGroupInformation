#!/usr/bin/env python3
import cognitive_face as CF
import csv
import json
import datetime


def csv_face_api_people():

   #Input Face API information
   SUBSCRIPTION_KEY = ''
   BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'
   PERSON_GROUP_ID = ''

   #Sets the Face API information to cognitive_face (CF)
   CF.BaseUrl.set(BASE_URL)
   CF.Key.set(SUBSCRIPTION_KEY)

   #assign list of all people to the variable "group"
   group = CF.person.lists(PERSON_GROUP_ID)

   #Start of exporting the Face API to a csv
   with open('person_group_info ' + str(datetime.datetime.today().strftime('%Y-%m-%d')) + '.csv', mode='w') as csv_file :

         #create array for the headers in the csv
         fieldnames = ['personGroupID','personId', 'name']
         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

         #loops through each person in group and assigns the UserData to the value "x"
         for person in group:
            #check to see if userData is None or empty ({})
            if (person['userData'] != None) and (person['userData'] != '{}'):
               x = json.loads(person['userData'])
            
            #for each data label in the Face API we append it to the fieldnames (or csv headers)
               for value in x:
                  if 'DataLabel: ' + value["UserDataLabel"] not in fieldnames:
                     #concat "DataLabel: " to the UserDataLabel so in the csv it shows the full column name. 
                     fieldnames.append('DataLabel: ' + value["UserDataLabel"])

         #write out the headers to the csv
         print('')
         print('-------Writing Headers-------')
         writer.writeheader()
         #prints out the headers
         for name in fieldnames:
            print(name + '...')


         #create a blank dictionary with all of the headers 
         person_dict = {}
         for name in fieldnames:
            person_dict[name] = ''
         
         #print statements to break up headers and rows
         print('')
         print('-------Writing Rows-------')
         #loop through each person and add their values to the "person_dict"
         for person in group:

            #check to see if userData is None or empty ({})
            if person['userData'] != None and person['userData'] != '{}':
               x = json.loads(person['userData'])

               #make a new dictionary that inputs all of the labels and values. Gets recreated for each person in the group.
               all_dict = {}
               all_dict['personId'] = person['personId']
               all_dict['name'] = person['name']
               all_dict['personGroupID'] = PERSON_GROUP_ID
               for value in x:

                  #concat the "DataLabel: " to the value to make sure it matches the fieldnames array
                  all_dict['DataLabel: ' + value['UserDataLabel']] = value['UserDataValue']
                  for label in person_dict:
                        #if the person doesn't have a value for the data label, we just input a blank value
                        if all_dict.get(label) is None:
                           person_dict[label] = ''
                        elif all_dict.get(label) == 'person group id':
                           person_dict[label] = PERSON_GROUP_ID
                        else:
                           person_dict[label] = all_dict.get(label)
                           
            #If there is no userData this else statement puts blank values for the labels
            else:
               for label in person_dict:
                  if label == 'personGroupID':
                     person_dict['personGroupID'] = PERSON_GROUP_ID
                  elif label == 'name':
                     person_dict['name'] = person['name']
                  elif label == 'personId':
                     person_dict['personId'] = person['personId']
                  else:
                     person_dict[label] = ''
            
            #write out each person to the csv
            writer.writerow(person_dict)

            #prints the name of each person that got written to the csv
            print(person_dict['name']+ '...')

#calls the method
csv_face_api_people()