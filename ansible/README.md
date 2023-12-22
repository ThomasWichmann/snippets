# Ansible playbooks for Debian system customization

Optimized for very special requirements. So this might not be widespread usable but may provide hints on how to do customization for Debian with Ansible.

## Trouble shooting

In case of errors 

	ERROR! couldn't resolve module/action 'community.general.snap'. This often indicates a misspelling, missing collection, or incorrect module path.
	
run

	ansible-galaxy collection install community.general
	
	

