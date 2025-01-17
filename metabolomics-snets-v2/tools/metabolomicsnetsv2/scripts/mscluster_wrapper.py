#!/usr/bin/python

import sys
import os
import glob

def usage():
    print("<input spectra> <parameters filename> <output spectra> <output aligns> <main specnets filepath>")

def main():
    input_spectra_folder = sys.argv[1]
    parameters_filename = sys.argv[2]
    output_spectra_folder = sys.argv[3]
    output_alignments_folder = sys.argv[4]
    mainspecnets_binary = sys.argv[5]

    cmd = "%s %s -ll 9 -f mscluster" % (mainspecnets_binary, parameters_filename)
    ret_code = os.system(cmd)

    if ret_code != 0:
        exit(1)

    #Do clean up out output spectra folder
    all_pklbin_files = glob.glob(os.path.join(output_spectra_folder, "specs_ms_*.pklbin"))

    """Disabling Removing Files because they are needed in a later step"""
    #TODO: Move clusterinfo into this step so we can get rid of these files. 
    #for filetoremove in all_pklbin_files:
    #    print("Removing ", filetoremove)
    #    os.remove(filetoremove)

if __name__ == "__main__":
    main()
