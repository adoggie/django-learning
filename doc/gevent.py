	
  
def run(self):
		from multiprocessing import Process
		self.init(init_script.GLOBAL_SETTINGS_FILE, init_script.GLOBAL_SERVICE_FILE)

		# - init http service
		cfg = self.conf['http']
		host = cfg['host']
		if not host:
			host = ''
		address = (host, cfg['port'])
		ssl = cfg['ssl']
		lemon.utils.app.BaseAppServer.run(self)

		print 'WebService serving on %s...' % str(address)
		#WSGIServer(address, WSGIHandler()).serve_forever()
		wsgi_server = WSGIServer(address, WSGIHandler())
		wsgi_server.start()

		forks = 3

		def _exec(server):
			server.serve_forever()

		for _ in xrange(forks):
			Process( target=_exec,args = (wsgi_server,)).start()
 
