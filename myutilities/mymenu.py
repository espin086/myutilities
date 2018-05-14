#!/usr/bin/env python3
def print_commands(command_dict):
	print('-' * 30, 'Commands', '-' * 30)
	for key in command_dict:
		print(key.ljust(45, ' '), command_dict[key])
	print()
	
def print_header(project_title, creators, 
	version, repo):
	
	print('_' * 79)
	print()
	print('-' * 30, project_title, '-' * 30)
	print()
	print("Contributors: ")
	print('-' * 15)
	for name in creators:
		print(name)
	print()
	print("Version: {}".format(version))
	print()
	print("Repo: {}".format(repo))
	print()

def print_menu(project_title, creators, version, repo, command_dict):
	print_header(project_title, 
		creators, version,repo)
	print_commands(command_dict)

def user_input():
	pass
def mymenu(project_title, creators, version, repo, command_dict):
	"""Creates Menu.

    Prints standardized menu for a project ran at the command lione

    Args:
        project_title (int): The title of the project
        creators (list): A list of creaters in str format
        version (str): The version of the release
        repo (str): url of github repo where one can contribute
        command_dict (str): A dictionary of commands and their description

    Returns:
        None: this prints objects to the screen

    Example: 
    	import myutilities.mymenu as mymenu
		mymenu.mymenu('Test Project', ['JJ Espinoza'], '0.1', 'test.git', {'test': 'test explanation'})
        
    """
	print_menu(project_title, creators, version, repo, command_dict)
	
if __name__ == '__main__':

	project_title = 'Project Title'
	creators = ['Author 1']
	version = '0.1'
	repo = 'https://github.com/espin086'
	command_dict = {'-h': 'help menu',
		'-command1': '[arguments] description of command 1'}

	mymenu(project_title, creators, version, repo, command_dict)
