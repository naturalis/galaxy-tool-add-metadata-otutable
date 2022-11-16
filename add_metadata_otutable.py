#!/usr/bin/env python
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
requiredArguments.add_argument('-n', dest='naValues', type=str, required=True)
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
    metadataHeaderList = metadataHeader.split("\t")
    if args.type == "automatic":
        if "#Identity percentage" in metadataHeader:
            return "blast"
        elif "#lca rank" in metadataHeader:
            return "lca"
        elif "#Frame 1 stop codons" in metadataHeaderList and "#Frame 1" in metadataHeaderList:
            return "translation6andstopcodons"
        elif "#Frame 1" not in metadataHeaderList and "#Frame 1 stop codons" in metadataHeaderList:
            return "stopcodons"
        elif "#Frame 1" in metadataHeaderList and "#Frame 1 stop codons" not in metadataHeaderList:
            return "translation6"
    else:
        return str(args.type)


def add_general_to_otutable(metadataDict, metadataHeader, inputType):
    with open(args.output, "a") as output, open(args.otutable, "r") as otutable:
        output.write(otutable.readline().strip()+"\t"+metadataHeader+"\n")
        for line in otutable:
            if line.split("\t")[0] in metadataDict:
                output.write(line.strip()+"\t"+metadataDict[line.split("\t")[0]])
            else:
                if args.naValues == "yes":
                    emptyValue = "\tN/A"
                    unknownTaxonomy = "unknown / unknown / unknown / unknown / unknown / unknown / unknown"
                else:
                    emptyValue = "\t"
                    unknownTaxonomy = ""

                if inputType == "blast":
                    naString = 8*emptyValue
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\t"+unknownTaxonomy+"\n")
                elif inputType == "lca":
                    naString = 10*emptyValue
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\n")
                elif inputType == "translation6":
                    naString = 6*emptyValue
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\n")
                elif inputType == "translation6andstopcodons":
                    naString = 12*emptyValue
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\n")
                elif inputType == "stopcodons":
                    naString = 6*emptyValue
                    output.write(line.strip() +"\t"+line.split("\t")[0]+naString+"\n")

def main():
    metadataDict = metadata_to_dict()
    metadataHeader = get_metadata_header()
    inputType = detect_input(metadataHeader)
    inputTypes = ["blast", "lca", "translation6", "translation6andstopcodons", "stopcodons"]
    if inputType in inputTypes:
        add_general_to_otutable(metadataDict, metadataHeader, inputType)
    if inputType == "other":#option to expand this tool
        pass

if __name__ == '__main__':
    main()
