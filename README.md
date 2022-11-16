# galaxy-tool-add-metadata-otutable
Add metadata such as BLAST, LCA and translated output to an otutable.

## Installation
### Manual
Clone this repo in your Galaxy ***Tools*** directory:  
`git clone https://github.com/naturalis/galaxy-tool-add-metadata-otutable`  

Make scripts executable:  
`chmod 755 galaxy-tool-add-metadata-otutable/add_metadata_otutable.sh`  
`chmod 755 galaxy-tool-add-metadata-otutable/add_metadata_otutable.py` 

Append the file ***tool_conf.xml***:    
`<tool file="/path/to/Tools/galaxy-tool-add-metadata-otutable/add_metadata_otutable.xml" />`  

### Ansible
Depending on your setup the [ansible.builtin.git](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html) module could be used.  
[Install the tool](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html#examples) 
by including the following in your dedicated ***.yml** file:  

`  - repo: https://github.com/naturalis/galaxy-tool-add-metadata-otutable`  
&ensp;&ensp;`file: add_metadata_otutable.xml`  
&ensp;&ensp;`version: master`  
