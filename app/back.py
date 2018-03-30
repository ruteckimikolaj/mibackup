import os
import filecmp
import shutil


def compare_copy (dir1=r'C:\Users\rutec\Envs\mibackup\test\one' , dir2=r'C:\Users\rutec\Envs\mibackup\test\two'):
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
    return print("Success!")

compare_copy()

def _recursive_dircmp(dir1, dir2, prefix='.'):
    """Return a recursive dircmp comparison report as a dictionary."""

    comparison = filecmp.dircmp(dir1, dir2)

    data = {
        'left': [r'{}/{}'.format(prefix, i) for i in comparison.left_only],
        'right': [r'{}/{}'.format(prefix, i) for i in comparison.right_only],
        'both': [r'{}/{}'.format(prefix, i) for i in comparison.common_files],
    }

    for datalist in data.values():
        datalist.sort()

    if comparison.common_dirs:
        for folder in comparison.common_dirs:
            # Update prefix to include new sub_folder
            prefix += '/' + folder

            # Compare common folder and add results to the report
            sub_folder1 = os.path.join(dir1, folder)
            sub_folder2 = os.path.join(dir2, folder)
            sub_report = _recursive_dircmp(sub_folder1, sub_folder2, prefix)

            # Add results from sub_report to main report
            for key, value in sub_report.items():
                data[key] += value

    return data


"""
if __name__=="__main__":
    main.run(debug=True)
"""