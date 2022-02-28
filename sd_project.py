###################### The aim of this program is to convert a file (csv, json, xml or yaml file) recieved form a user to a python dictionnary,
################################# and then to also convert this last one to a csv, json, xml and yaml file
from tkinter import filedialog
from tkinter import *

master = Tk()
master.geometry("400x300")
filename = filedialog.askopenfilename(title="Choose a file",
                                      filetypes=(("CSV Files", "*.csv"),
                                                 ("JSON Files", "*.json"),
                                                 ("XML Files", "*.xml"),
                                                 ("YAML FIles", "*.yaml")))

def convert_my_file():
    import csv
    import json
    import xmltodict
    import yaml
    from pprint import pprint
    #my_file = input('Enter a file with its extension :')
    extension_given = input('Enter an extension for which you wanna convert the file:')
    split_file = filename.split('.')
    file_extension = split_file[1]
    if file_extension == extension_given:
        print('The file is already in this format, choose another extension.')
        convert_my_file()
    if extension_given not in ['csv', 'json', 'xml', 'yaml']:
        print('This file is not required. It must be a csv, json, xml or yaml file.')
        convert_my_file()
    if file_extension == 'csv':
        dict_from_csv = list()
        with open(filename, 'r', newline='\n') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                dict_from_csv.append(row)
        ######## Convert dict_from_csv to a json file
        print("\n ***** This is our JSON file obtained through the CSV file ***** \n",
              json.dumps(dict_from_csv, indent=4))
        ######## Convert dict_from_csv to a xml file
        try:
            print("\n ***** This is our XML file obtained through the CSV file ***** \n",
              xmltodict.unparse(dict_from_csv, pretty=True))
        except ValueError:
            print("\n ***** This file could\'nt be converted in XML***** \n")
        ######## Convert dict_from_csv to a yaml file
        print("\n ***** This is our YAML file obtained through the CSV file ***** \n",
              yaml.dump(dict_from_csv, indent=4))

    elif file_extension == 'json':
        with open(filename, 'r') as f_json:
            dict_from_json = json.load(f_json)
        ############ Converting to CSV
        with open('json_converted_in_csv.csv', 'w') as ff_json:
            csv_writer = csv.writer(ff_json)
            for key, value in dict_from_json.items():
                csv_writer.writerow([key, value])
        ######## Reading the CSV and saving it to a container
        with open('json_converted_in_csv.csv', 'r') as fff_json:
            csv_reader = csv.reader(fff_json)
            list_csv_from_json = list()
            for device in csv_reader:
                list_csv_from_json.append(device)
        ######## Convert dict_from_json to a csv file
        print("\n ***** This is our CSV file obtained through the JSON file ***** :")
        pprint(list_csv_from_json)
        ######## Convert dict_from_json to a xml file
        try:
            print("\n ***** This is our XML file obtained through the JSON file ***** \n",
              xmltodict.unparse(dict_from_json, pretty=True))
        except ValueError:
            print("\n ***** This file could\'nt be converted in XML***** \n")
        ######## Convert dict_from_json to a yaml file
        print("\n ***** This is our YAML file obtained through the JSON file ***** \n",
              yaml.dump(dict_from_json, indent=4))

    elif file_extension == 'xml':
        with open(filename, 'r') as f_xml:
            dict_from_xml = xmltodict.parse(f_xml.read(), dict_constructor=dict)
        ###### Converting to CSV
        with open('xml_csv_converted.csv', 'w') as ff_xml:
            csv_writer = csv.writer(ff_xml)
            for key, value in dict_from_xml.items():
                csv_writer.writerow([key, value])
        ######## Reading the CSV and saving it to a container
        with open('xml_csv_converted.csv', 'r') as fff_xml:
            csv_reader = csv.reader(fff_xml)
            list_csv_from_xml = list()
            for item in csv_reader:
                list_csv_from_xml.append(item)
        ######## Convert dict_from_json to a csv file
        print("\n ***** This is our CSV file obtained through the XML file ***** :")
        pprint(list_csv_from_xml)
        ######## Convert dict_from_xml to a xml file
        try:
            print("\n ***** This is our JSON file obtained through the XML file ***** \n",
              json.dumps(dict_from_xml, indent=4))
        except ValueError:
            print("\n ***** This file could\'nt be converted in XML***** \n")
        ######## Convert dict_from_xml to a yaml file
        print("\n ***** This is our YAML file obtained through the XML file ***** \n",
              yaml.dump(dict_from_xml, indent=4))

    else:
        with open(filename, 'r') as f_yaml:
            dict_from_yaml = yaml.safe_load(f_yaml)
        with open('yaml_csv_converted.csv', 'w') as ff_yaml:
            csv_writer = csv.writer(ff_yaml)
            for key, value in dict_from_yaml.items():
                csv_writer.writerow([key, value])
            ######## Reading the CSV and saving it to a container
        with open('yaml_csv_converted.csv', 'r') as fff_yaml:
            csv_reader = csv.reader(fff_yaml)
            list_csv_from_yaml = list()
            for label in csv_reader:
                list_csv_from_yaml.append(label)
        ######## Convert dict_from_yaml to a csv file
        print("\n ***** This is our CSV file obtained through the yaml file ***** :")
        pprint(list_csv_from_yaml)
        print("\n ***** This is our JSON file obtained through the yaml file ***** \n",
              json.dumps(dict_from_yaml, indent=4))
        ######## Convert dict_from_yaml to a xml file
        try:
            print("\n ***** This is our XML file obtained through the yaml file ***** \n",
              xmltodict.unparse(dict_from_yaml, pretty=True))
        except ValueError:
            print("\n ***** This file could\'nt be converted in XML***** \n")


convert_my_file()
