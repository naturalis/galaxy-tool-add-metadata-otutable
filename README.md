# galaxy-tool-add-metadata-otutable
The old tool https://github.com/naturalis/galaxy-tool-add-blast-to-otutable will be replaced by this one. This script can add metadata such BLAST or LCA output to an otutable.

## Getting Started
### Installing
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
sudo git clone https://github.com/naturalis/galaxy-tool-add-metadata-otutable
sudo chmod 777 galaxy-tool-add-metadata-otutable/add_metadata_otutable.py
sudo ln -s /home/galaxy/Tools/galaxy-tool-add-metadata-otutable/add_metadata_otutable.py /usr/local/bin/add_metadata_otutable.py
sudo ln -s /home/galaxy/Tools/galaxy-tool-add-metadata-otutable/add_metadata_otutable.sh /home/galaxy/galaxy/tools/identify/add_metadata_otutable.sh
sudo ln -s /home/galaxy/Tools/galaxy-tool-add-metadata-otutable/add_metadata_otutable.xml /home/galaxy/galaxy/tools/identify/add_metadata_otutable.sh
```
Add the following line to /home/galaxy/galaxy/config/tool_conf.xml
```
<tool file="identify/add_metadata_otutable.xml" />
```
Restart Galaxy to see the tool in the menu
