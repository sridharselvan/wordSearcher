####### Import Statements ############
import os
import sys
from PyInquirer import style_from_dict, prompt, Separator
from examples import custom_style_2
####### Global Variables ############


class DirectoryList:
	"""
	Class used to list the home folders and its child based on click.
	"""

	def __init__(self):
		""" Init method """
		self.path = os.path.expanduser("~")

	def get_directory_list(self, path=None):
		"""
		Method used to get the list of directories in home path. It will skip the hidden files.
		"""
		if not path:
			path = self.path
		folder_list = []
		for folder in os.listdir(path):
			if not folder.startswith('.'):
				folder_list.append(folder)
		folder_list.append('Exit')
		return folder_list

	def ask_directory_name(self, path=None):
		"""
		Method used to prompt the folder list for user selection.
		"""
		folder_list = self.get_directory_list(path)
		home_dir_prompt = [{
		    'type': 'list',
		    'name': 'folder',
		    'message': 'Please select the folder path to search.',
		    'choices': folder_list
			}]
		directory = prompt(home_dir_prompt, style=custom_style_2).get('folder')
		if directory != 'Exit':
			self.path = os.path.join(self.path, directory)
			self.ask_directory_name(self.path)
		else:
			print(self.path)

class WordSearcher:
	"""
	Class used to grep the word in the given folder and search in the mentioned file extension.
	Retruns: line number and file.
	"""
	pass

d = DirectoryList()
d.ask_directory_name()


