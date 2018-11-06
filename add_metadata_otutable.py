#!/usr/bin/python
"""

"""
import argparse, sys
# Retrieve the commandline arguments
parser = argparse.ArgumentParser(description='')
requiredArguments = parser.add_argument_group('required arguments')

requiredArguments.add_argument('-im', '--input-metadata', dest='metadata', type=str, required=True)
requiredArguments.add_argument('-io', '--input-otutable', dest='otutable', type=str, required=True)
requiredArguments.add_argument('-o', '--output', dest='output', type=str, required=True)
requiredArguments.add_argument('-t', '--input-type', metavar='metadata type (Blast or LCA input)', dest='type', type=str,
                               required=True, choices=['blast', 'lca','automatic'])
args = parser.parse_args()

def metadata_to_dict():
    metadataDict = {}
    duplicatesCheck = set()
    with open(args.metadata, "r") as metadata:
        for line in metadata:
            if line.split("\t")[0] not in duplicatesCheck:
                duplicatesCheck.add(line.split("\t")[0])
                metadataDict[line.split("\t")[0]] = line
            else:
                sys.exit("Duplicates found")
    return metadataDict

def get_metadata_header():
    with open(args.metadata, "r") as metadata:
        header = metadata.readline()
    return header.strip()

def detect_input(metadataHeader):
    """
    Makes the life of the user a little easier, it saves an extra click in galaxy.
    """
    if args.type == "automatic":
        if "#Identity percentage" in metadataHeader:
            return "blast"
        elif "#lca rank" in metadataHeader:
            return "lca"
    elif args.type == "blast":
        return "blast"
    elif args.type == "lca":
        return "lca"

def add_blast_or_lca_to_otutable(metadataDict, metadataHeader, inputType):
    with open(args.output, "a") as output, open(args.otutable, "r") as otutable:
        output.write(otutable.readline().strip()+"\t"+metadataHeader+"\n")
        for line in otutable:
            if line.split("\t")[0] in metadataDict:
                output.write(line.strip()+"\t"+metadataDict[line.split("\t")[0]])
            else:
                if inputType == "blast":
                    naString = 8*"\tN/A"
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\tunknown / unknown / unknown / unknown / unknown / unknown / unknown\n")
                elif inputType == "lca":
                    naString = 10*"\tN/A"
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\n")

def main():
    metadataDict = metadata_to_dict()
    metadataHeader = get_metadata_header()
    inputType = detect_input(metadataHeader)

    if inputType == "blast" or inputType == "lca":
        add_blast_or_lca_to_otutable(metadataDict, metadataHeader, inputType)
    if inputType == "other":#option to expand this tool
        pass

if __name__ == '__main__':
    main()
