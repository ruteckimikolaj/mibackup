

import os
import filecmp
import shutil


def compare_copy(dir1, dir2):
    comp_raport = filecmp.dircmp(dir1, dir2).report()
    comp_ari = filecmp.dircmp(dir1, dir2).left_only
    #print(dir1+r"\")
    if comp_ari != []:
        for f in comp_ari:
            shutil.copy2(dir1+r"\{}".format(f), dir2)
#            copylist.append(os.listdir(dir1+r"\n" + f))
            print(comp_ari)
    else:
        print("nothing to copy my frieeeeend.")
       # print(type(compare_copy)

if __name__=="__main__":
    compare_copy.run(debug=True)
