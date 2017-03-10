# -*- coding: utf-8 -*


import sys


file_data = sys.argv[1]
output_file = sys.argv[2]


# create the vector of features
file_in = open(file_data, "r", encoding="ISO-8859-1")
features = []
for line in file_in:
    values = line.split("::")
    line = values[0]
    values = values[2].split("|")
    for feature in values:
        feature = feature.rstrip()
        if not (feature in features):
            features.append(feature)

# create the feature of items
file_out = open(output_file + "featuresItems.txt", "w")
file_out.write("::".join(features))
file_out.write("\n")
file_in = open(file_data, "r", encoding="ISO-8859-1")
for i in file_in:
    i = i.rstrip()
    values = i.split("::")
    item_id = values[0]
    features_item = values[2].split("|")

    feature = [0] * len(features)
    for j in range(len(features_item)):
        for k in range(len(features)):
            if features_item[j] == features[k]:
                feature[k] = 1

    file_out.write(item_id + " ")
    for k in range(len(features)):
        file_out.write(str(feature[k]) + " ")
    file_out.write("\n")

file_out.close()
file_in.close()
