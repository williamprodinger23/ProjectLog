from http.server import BaseHTTPRequestHandler, HTTPServer
import func as func
import os

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/log':      
            
            commits = func.get_commit_comments()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("<html>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            
            for commit in commits:
                self.wfile.write(bytes("<p>", "utf-8"))

                self.wfile.write(bytes("<h1>", "utf-8"))
                self.wfile.write(bytes("<a href=\"/info/" +commit.hexsha.strip()+ "\">" + commit.hexsha.strip() + "</a>", "utf-8"))
                self.wfile.write(bytes("</h1>", "utf-8"))

                self.wfile.write(bytes("<p>", "utf-8"))

                self.wfile.write(bytes("<p> author = " + commit.author.name.strip() + "</p>", "utf-8"))
                self.wfile.write(bytes("<p> message = " + commit.message.strip() + "</p>", "utf-8"))

            self.wfile.write(bytes("</body>", "utf-8"))
            self.wfile.write(bytes("</html>", "utf-8"))

        elif self.path == '/log_ajax':
            
            commits = func.get_commit_comments()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            for commit in commits:
                self.wfile.write(bytes("<div class=\"datadiv\">", "utf-8"))
                self.wfile.write(bytes("<h1 class=\"link\"><a href=\"/info/" +commit.hexsha.strip()+ "\">" +str(commit.committed_datetime)[:-6], "utf-8"))
                self.wfile.write(bytes("</h1></a>", "utf-8"))
                self.wfile.write(bytes("<p class=\"content\">", "utf-8"))
                self.wfile.write(bytes("- " + commit.message, "utf-8"))
                self.wfile.write(bytes("</p>", "utf-8"))
                self.wfile.write(bytes("</div", "utf-8"))
            
        elif self.path.startswith('/info'):
            info = self.path[6:]
            
            data = func.get_specific_commit(info)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes("<html>", "utf-8"))

            self.wfile.write(bytes("<body>", "utf-8"))
            
            self.wfile.write(bytes("<p> HexSha: " + str(data.hexsha) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Author: " + str(data.author) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Authored Date: " + str(data.authored_datetime) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Author TZ Offset: " + str(data.author_tz_offset) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> BinSha: " + str(data.binsha) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Committed Date: " + str(data.committed_datetime) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Committer: " + str(data.committer) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Conf Encoding: " + str(data.conf_encoding) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Co Authors: " + str(data.co_authors) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Data Stream: " + str(data.data_stream) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Committer: " + str(data.default_encoding) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Env Author Date: " + str(data.env_author_date) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Env Committer Date: " + str(data.env_committer_date) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> GPGSIG: " + str(data.gpgsig) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Message: " + str(data.message) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Parents: " + str(data.parents) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Repo: " + str(data.repo) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Size: " + str(data.size) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Stats: " + str(data.stats) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Name Rev: " + str(data.name_rev) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Summary: " + str(data.summary) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> TIOBJ Tuple: " + str(data.TIobj_tuple) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Trailers: " + str(data.trailers) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Trailers Dict: " + str(data.trailers_dict) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Trailers List: " + str(data.trailers_list) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Tree: " + str(data.tree) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> Type: " + str(data.type) + "</p>", "utf-8"))
            self.wfile.write(bytes("<p> ID Attribute: " + str(data._id_attribute_) + "</p>", "utf-8"))

            self.wfile.write(bytes("</body>", "utf-8"))
            self.wfile.write(bytes("</html>", "utf-8"))
            
        else:
            file = self.path
            try:
                
                if os.path.splitext(self.path)[1] == ".jpg":
                    file = "../"+file
                    with open(file, 'rb') as file_handle:
                        content = file_handle.read()
                else:
                    f = open("../"+file, "r")
                    content = f.read()
                    
                fileext = os.path.splitext(self.path)[1]
                
                self.send_response(200)
                
                if fileext == ".html":
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(bytes(content, "utf-8"))
                elif fileext == ".css":
                    self.send_header("Content-type", "text/css")
                    self.end_headers()
                    self.wfile.write(bytes(content, "utf-8"))
                elif fileext == ".jpg":
                    self.send_header("Content-type", "image/jpg")
                    self.end_headers()
                    self.wfile.write(content)
                    
            except:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("Not found\n", "utf-8"))
            
        
if __name__ == "__main__":
    webserver = HTTPServer((hostName, serverPort), MyServer)
    print("Server Started http://%s:%s" % (hostName, serverPort))
    
    try:
        webserver.serve_forever() 
    except KeyboardInterrupt:
        pass
    
    webserver.server_close()
    print("Server_Stopped")
        