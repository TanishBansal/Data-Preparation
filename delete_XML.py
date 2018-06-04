import os
directory = r"E:\Master_Data_10K\Night"
test = os.listdir( directory )

for item in test:
    if item.endswith(".xml"):
        os.remove( os.path.join( directory, item ) )