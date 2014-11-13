def ejercicio7():
    import string, cgi, time, sys;
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer;
    from urllib2 import URLError, HTTPError, urlopen;
    class my_server(BaseHTTPRequestHandler):

        def do_GET(self):
            myDict={'Universidad':'University',
    'ingeniero':'engineer',
    'nuevo':'new',
    'estudiante':'student',
    'investigadores':'investiagators',
    'horario':'timetable',
    'contenedores':'containers',
    'firma':'sign',
    'ropa':'clothing',
    'valiosa':'valuable'
    };
            print "Client URL: "+self.client_address[0];
            if len(sys.argv) < 2:
                address="http://www.upv.es"+self.path;
            elif sys.argv[1].startswith('http://'):
                address=sys.argv[1]+self.path;
            else:
                address='http://'+sys.argv[1]+self.path;
            url=urlopen(address);
            data=url.read();
            tipo=url.info().getheader("Content-Type")
            if (tipo.find("html") != -1):
                data=data.replace("UPV","[[[UPV]]]");
                for key, value in myDict.iteritems():
                    data=data.replace(key, value);
            self.send_response(200);
            self.send_header("Content-type", tipo );
            self.end_headers();
            self.wfile.write(data);
            url.close();
            return 0;
        def log_message(self, format, *args):
            return
    try:
        server=HTTPServer(("",8081),my_server);
        server.serve_forever();
    except KeyboardInterrupt:
        print '\n^C recibido, cerrando servidor.'
        server.socket.close();



ejercicio7();
