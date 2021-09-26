import json
from _io import TextIOWrapper
import pickle

obj="vhbdskjbjsbvsbvb"
#obj_in_bytes=pickle.dumps(obj)
#fs=open("obj.json",'wb')
#print(obj,"---after pickel data type:--->",obj_in_bytes)
#print(type(obj),"---after pickel data type:--->",type(obj_in_bytes))
with open("obj.json","w+") as xyz:
    json.dump(obj,xyz)
#fs.write(obj_in_bytes)
#print(type(obj),"---after pickel data type:--->",type(obj_in_bytes))
#print(obj,"---after pickel data type:--->",obj_in_bytes)

xyz.close()