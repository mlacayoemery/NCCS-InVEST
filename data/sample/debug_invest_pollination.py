import os
import json

#for i in *.tif; do gdalinfo -json -stats $i > ${i/.tif/.json}; done

base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"output")
##rst_template = """   * - %s
##     - %s
##     - %s
##     - %s
##     - %s"""
rst_template = "|%s|%s|%s|%s|%s|"
for f in os.listdir(base_path):
    if f.endswith(".json"):
        j = json.load(open(os.path.join(base_path,f)))
        print(rst_template % (os.path.splitext(f)[0],
                              j["stac"]["raster:bands"][0]["stats"]["minimum"],
                              j["stac"]["raster:bands"][0]["stats"]["maximum"],
                              j["stac"]["raster:bands"][0]["stats"]["mean"],
                              j["stac"]["raster:bands"][0]["stats"]["stddev"]),)
