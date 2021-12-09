import json
import pandas as pd

with open('timestep_data.json', 'r') as file_:
    data = json.load(file_)

print(type(data))

data_arr, timestep_arr = [], []

for item in data:
    data_arr.append(item['vehicle'])

    timestep_arr.append(item['_time'])

# 1744th index is NaN in data_arr

coll = list(zip(timestep_arr, data_arr))

# coll is a list of tuples
# 0th index: timestep number
# 1st index: either a dict (single value) or a list (multiple values) of dicts

# todo: parse such that it forms a multi-indexed data frame with timestep and car id as the indexes

preprocessed_coll = []

for item in coll:
    if isinstance(item[1], list):
        for val in item[1]:
            preprocessed_coll.append((item[0], val))
    else:
        preprocessed_coll.append((item[0], item[1]))


# print(preprocessed_coll)
final_data = {
    'Timestep' : [],
    'Vehicle_ID' : [],
    '_X' : [],
    '_Y'  : [],
    '_Angle' : [],
    '_Pos'  : [],
    '_Speed' : [],
    '_Lane' : [],
    '_Slope' : [],
}

for item in preprocessed_coll:
    # check: timestep already exists
    # final_data['Timestep'] = [(item[0])]
    # final_data['Vehicle_ID'] = [(item[1]['_id'])]
    # final_data['_X'] = [(item[1]['_x'])]
    # final_data['_Y'] = [(item[1]['_y'])]
    # final_data['_Angle'] = [(item[1]['_angle'])]
    # final_data['_Pos'] = [(item[1]['_pos'])]
    # final_data['_Speed'] = [(item[1]['_speed'])]
    # final_data['_Lane'] = [(item[1]['_lane'])]
    # final_data['_Slope'] = [(item[1]['_slope'])]
    # if item[0] in final_data:
    #     final_data['Timestep'] = final_data['Timestep'].append((item[0]))

    final_data['Timestep'].append(item[0])
    final_data['Vehicle_ID'].append(item[1]['_id'])
    final_data['_X'].append(item[1]['_x'])
    final_data['_Y'].append(item[1]['_y'])
    final_data['_Angle'].append(item[1]['_angle'])
    final_data['_Pos'].append(item[1]['_pos'])
    final_data['_Speed'].append(item[1]['_speed'])
    final_data['_Lane'].append(item[1]['_lane'])
    final_data['_Slope'].append(item[1]['_slope'])

df = pd.DataFrame({
    'TimeStep': final_data['Timestep'],
    'Vehicle_ID': final_data['Vehicle_ID'],
    '_X': final_data['_X'],
    '_Y': final_data['_Y'],
    '_Angle': final_data['_Angle'],
    '_Pos': final_data['_Pos'],
    '_Speed': final_data['_Speed'],               
    '_Lane': final_data['_Lane'],
    '_Slope': final_data['_Slope'],
    })

# done
# Vehicle_ID ==