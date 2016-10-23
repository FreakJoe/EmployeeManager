import os

for root, dirs, files in os.walk(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui')):
	for f in files:
		if f.endswith('.ui'):
			filepath = os.path.join(root, f)
			print(filepath)
			os.system('pyuic5 %s > %s' % (filepath, filepath.replace('.ui', '.py')))