import myutilities.mymenu as mymenu

def main():

	mymenu(project_title='Automated EMR Login', 
	creators=['JJ Espinoza'], 
	version='0.1', 
	repo='none', 
	command_dict={'--h': 'help',
	'--listinstances': 'lists Cloud instances along with purpose',
	'--logininstances': 'commands to log into different Cloud instances'})
	# print('1. Dictionary of Cloud Instances Names with sub-dictionary of purpose (projects run) and login information')
	# print('2. Format Output of 1 Cloud Instance Nicely')
	# print('3. Print all EMRs Nicely')
	pass

def dict_aws_instances():
	aws_instances = {
		'Miguel 203': 
			{'purpose': 'x', 
			'loging': 'y'},
		'Fox DS Development': 
			{'purpose': 'x', 
			'loging': 'y'},
		'Fox DS Production': 
			{'purpose': 'x', 
			'loging': 'y'},
		'Assembly Blindal': 
			{'purpose': 'x', 
			'loging': 'y'},
		}
	return aws_instances
def pretty_print_instance():
	print('-' * 20)
	pass


def instances(provider):
	if provider == 'aws':
		print('AWS Instances: ')

	elif provider == 'gcs':
		print('gcs')
	return None


if __name__ == '__main__':
	print(dict_aws_instances())




