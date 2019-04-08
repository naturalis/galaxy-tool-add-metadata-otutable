# galaxy-tool-add-metadata-otutable
The old tool https://github.com/naturalis/galaxy-tool-add-blast-to-otutable will be replaced by this one. This script can add metadata such as BLAST, LCA and translated output to an otutable.

## Getting Started
### Installing
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
sudo git clone https://github.com/naturalis/galaxy-tool-add-metadata-otutable
sudo chmod 777 galaxy-tool-add-metadata-otutable/add_metadata_otutable.py
```
Add the following line to /home/galaxy/galaxy/config/tool_conf.xml
```
<tool file="/home/galaxy/Tools/galaxy-tool-add-metadata-otutable/add_metadata_otutable.xml" />
```
Restart Galaxy to see the tool in the menu
