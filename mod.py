def mod():
	import config
	config.x = config.x + 1
	return str(config.x).zfill(4)