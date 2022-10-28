import os, sys

dd = {"Grounded":"S3E1 - Grounded", "The Least Dangerous Game":"S3E2 - The Least Dangerous Game", "Mining the Mind's Mines":"S3E3 - Mining the Mind's Mines", "Room for Growth":"S3E4 - Room for Growth", "Reflections":"S3E5 - Reflections", "Hear All, Trust Nothing":"S3E6 - Hear All, Trust Nothing", "A Mathematically Perfect Redemption":"S3E7 - A Mathematically Perfect Redemption", "Crisis Point 2: Paradoxus":"S3E8 - Crisis Point 2: Paradoxus", "Trusted Sources":"S3E9 - Trusted Sources", "The Stars at Night":"S3E10 - The Stars at Night", "Asylum":"S3E11 - Asylum"}

# get all files from directory

def get_files(directory):
    filenames = next(os.walk(directory), (None, None, []))[2]  # [] if no file
    return filenames


# main function
if __name__ == "__main__":
    # get first commandline argument
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = r"Z:\Media\TV Shows\Star Trek Lower Decks"
    print(directory)
    # get all files from directory
    files = get_files(directory)
    # print(files)
    keys = dd.keys()
    # print(keys)
    for file in files:
        # print(any(key in file for key in keys))
        for key in keys:
            if key in file:
                # replace key substring with a dict value
                print(file.replace(key, dd[key]))
                new_path = os.path.join(directory, file.replace(key, dd[key]))
                old_path = os.path.join(directory, file)
                os.rename(old_path, new_path)
    #     # check if key from dict is in file name
    #     # get filename

