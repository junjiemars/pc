from distutils.core import setup, Extension

spam = Extension('spam', 
								sources = ['spam.c'])

setup ( name = 'spam',
				version = '1.0',
				description = 'Monty spam',
				author = 'Junjie Mars',
				author_email = 'junjiemars@gmail.com',
				ext_modules = [spam]
			)
