import pickle
import numpy as np
import json

# Utilities:
location_weights = {}

property_type_map = {}

type_map = {}

# Loading artifacts:

with open('Artifacts\model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
with open("Artifacts\location_weights.json", "r") as json_file:
    location_weights = json.load(json_file)
with open("Artifacts\property_type.json", "r") as json_file:
    property_type_map = json.load(json_file)
with open("Artifacts/room_type.json", "r") as json_file:
    type_map = json.load(json_file)
# Test:
# print(location_weights)
# print(property_type_map)
# print(type_map)



def predict_price(area,no_bedrooms,location,property_type,room_type):
    input = [area]+[no_bedrooms]+[location_weights[location]] +property_type_map[property_type] + [type_map[room_type]]
    print(location)
    print(input)
    output = loaded_model.predict([input])[0]
    print(f'Predicted Price: INR {output} Lakhs')
    return output

# predict_price(800,3,'Chembur','Apartment','BHK')

