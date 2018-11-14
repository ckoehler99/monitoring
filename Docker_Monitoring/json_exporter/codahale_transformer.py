#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer

import os
import json
from urllib import parse, request 
import base64
import logging
import logging.config
from urllib import request
from urllib.error import HTTPError
import ssl as SSL
# from ssl import SSLContext

class HttpRestApiHandler(BaseHTTPRequestHandler):
#
#    HTTP Method -GET-
#
    def do_GET(handler):
        handler.protocol_version = 'HTTP/1.1'
        try:
            if handler.path == '/favicon.ico':
                return
            elif not handler.path.startswith('/metrics'):
                logging.error(handler.path)
                raise Exception('in valid URL')
            else:
                uri = handler.path.split("?")
                if( uri == None or len(uri) == 1 ):
                    raise Exception('No parameter')
                
                uri = parse.unquote_plus(uri[1])
                logging.debug('plus'+uri)
                parameter = parse.parse_qs(uri,True);
                
                logging.debug('Parameter: "%s"',str(parameter))
                target = parameter.get('target')
                if target == None:
                    raise Exception('No target parameter')
                
                header = {}
                addHeader = parameter.get('additional_headers')
                if addHeader != None :
                    logging.debug('Has Header: '+addHeader[0]);
                    header = json.loads(addHeader[0])
                
                credential = parameter.get('credential')
                if credential != None:
                    logging.debug('Has Credential');
                    header['Authorization'] = credential[0]
                
                handler.send_response(200)
                handler.send_header('Content-type', 'text/plain')
                handler.end_headers()
                exportData(handler, target[0], header)
        except HTTPError as e:
            logging.critical(e)
            handler.send_error(e.code, e.reason)
            handler.end_headers()
        except Exception as e:
            logging.critical(e)
            handler.send_response(500, '%s' %e)
            handler.end_headers()
#
#
#
def exportData(handler, endpoint, additonalHeader):
    logging.info("Endpoint: '%s'", endpoint)
    logging.info("Header  : '%s'", additonalHeader)

    target = request.Request(url=endpoint)
    if additonalHeader != None:
        for key in additonalHeader:
          target.add_header(key, additonalHeader[key])
    
    ctx = SSL.create_default_context(capath='/etc/ssl/certs/')
    ctx.check_hostname = False
    ctx.verify_mode = SSL.CERT_NONE
    #
    httpResult = request.urlopen(target, context=ctx)
    result = json.loads(httpResult.read())
    
    for key in result:
        next_level(result[key], key,handler.wfile)
    
    handler.wfile.write("\n".encode("utf-8"))
#
#
#
def next_level(value, parent, out):
    if type(value) is dict:
        for key in value:
            next_level(value[key], parent+'_'+key, out)
#
    elif type(value) is str:
        logging.debug('is ein string "%s"', value)
        write_to_handle(out, parent, "NaN")
#
    elif type(value) is int:
        logging.debug('is number "%s"', str(value))
        write_to_handle(out, parent, str(value))
    elif type(value) is float:
        logging.debug('is number "%s"', str(value))
        write_to_handle(out, parent, str(value))#
    else:
        logging.error('is ein unbekannt Type "%s"',type(value))
        write_to_handle(out, parent, "NaN")
#
def write_to_handle(out, key, value):
    msg = key.replace(".","_").replace("-","_")+" "+value
    logging.debug(msg)
    msg +="\n"
    out.write(msg.encode("utf-8"))
#
#
#
def main():
    try:
        server = HTTPServer(('', 9101), HttpRestApiHandler)
        logging.critical('started httpserver...')
        server.serve_forever()
    except KeyboardInterrupt:
        logging.critical('^C received, shutting down server')
        server.socket.close()
#
#
#
if __name__ == '__main__':
    logging.config.fileConfig('conf/logging.ini')
    main()
