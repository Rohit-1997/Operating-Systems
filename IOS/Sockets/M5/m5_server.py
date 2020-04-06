'''
    This file implements the multithreading concept
    for handling the requests
'''
import socket
import threading
import os
import mimetypes

class HTTPServer:
    def __init__(self, IP, Port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.server:
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((IP, Port))
            self.server.listen()
            # Starting the server
            while True:
                client_socket, address = self.server.accept()
                # here we assign the job of receiving the requests
                # to threads
                self.delegate_request(client_socket)

    
    def accept_request(self, client_socket):
        '''
        accepts the requests
        '''
        client_request = client_socket.recv(1024).decode('UTF-8')
        print(client_request)
        if len(client_request) > 0:
            client_request = client_request.split()[1]
            print("The client req", client_request)
            if client_request == "/favicon.ico":
                # print('here')
                return
        else:
            return
        code, c_type, c_length, data = self.load_dynamic_content(client_request)
        header = self.response_headers(code, c_type, c_length).encode()
        if c_type == "image/png" or c_type == "image/gif":
            client_socket.sendall(header + data)
        else:
            client_socket.sendall(header + data.encode())
        count = threading.active_count()
        print("The number of threads active: ", count)
        client_socket.close()


    def delegate_request(self, client_socket):
        '''
        This methods starts a new thread to handle
        the request
        '''
        threading._start_new_thread(self.accept_request,(client_socket,))


    def load_dynamic_content(self, uri):
        """
        loads the dynamic content
        executes the executable files and sends the output
        to the browser
        """
        # print("The uri", uri)
        if uri == "/bin":
            path = uri.split("/")[1]
            path = os.getcwd() + "/scripts/"
            # display the files in the contents directory
            file_list = os.listdir(path)
            directory_data = ""
            for file_name in file_list:
                href = self.buil_href(file_name, uri)
                temp_string = "<a " + "href = " + href + ">" + file_name + "</a>"
                directory_data += temp_string
                directory_data += "<br/>"
            http_response = '''
            <!DOCTYPE html>
                <html>
                <head>
                    <title>Home page</title>
                </head>
                <body>
                <h1>The list of the file present in the root directory</h1>
            ''' + directory_data + "</body>\n</html>"
            return 200, 'text/html', len(http_response), http_response
        else:
            # here we have to process the executable files
            parentStdin, childStdout  = os.pipe()
            childStdin, parentStdout = os.pipe()
            command = uri.split("/")[-1]
            path = os.getcwd() + "/scripts/" + command
            
            

    def build_href(self, path, file_name, uri):
        """
        This method builds the href attributes
        for the files passed as the parameter
        """
        if uri == "/":
            return uri + file_name
        else:
            return uri + "/" + file_name
        

    def response_headers(self, status_code, content_type, length):
        """
        This method creates the response headers
        for the http response
        """
        line = "\n"
        
        # TODO update this dictionary for 404 status codes
        response_code = {200: "200 OK", 404: "404 Not Found"}
        
        headers = ""
        headers += "HTTP/1.1 " + response_code[status_code] + line
        headers += "Content-Type: " + content_type + line
        headers += "Content-Length: " + str(length) + line
        headers += "Connection: close" + line
        headers += line
        return headers



def main():
    HTTPServer("127.0.0.1", 8888)


if __name__ == "__main__":
    main()