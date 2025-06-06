import os
import sys
import json

#for i in *.tif; do gdalinfo -json -stats $i > ${i/.tif/.json}; done
def json_to_rst(output_path):
    ##rst_template = """   * - %s
    ##     - %s
    ##     - %s
    ##     - %s
    ##     - %s"""
    table = ""
    rst_template = "|%s|%s|%s|%s|%s|\n"
    for f in os.listdir(output_path):
        if f.endswith(".json"):
            j = json.load(open(os.path.join(output_path,f)))
            table+=rst_template % (os.path.splitext(f)[0],
                                   j["stac"]["raster:bands"][0]["stats"]["minimum"],
                                   j["stac"]["raster:bands"][0]["stats"]["maximum"],
                                   j["stac"]["raster:bands"][0]["stats"]["mean"],
                                   j["stac"]["raster:bands"][0]["stats"]["stddev"])
    return table

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.realpath(__file__))
    try:
        #output dir passed
        output_path = os.path.join(base_path,sys.argv[1])
    except IndexError:
        #sticking with default output
        output_path = os.path.join(base_path,"output")

    #os.chdir(output_path)
    #os.system("for i in *.tif; do gdalinfo -json -stats $i > $(echo $i | awk  \'{ string=substr($0, 0, -4); print string; }\').json; done")
    table = json_to_rst(output_path)
    print(table)
