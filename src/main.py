def print_author():
	from dotenv import load_dotenv
	import os
	load_dotenv(dotenv_path='C:/Users/shval/Git/first_project/.env')
	author = os.getenv('AUTHOR')
	print(f"Автор проекта: {author}")
