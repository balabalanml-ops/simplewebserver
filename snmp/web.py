from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCP/IP Protocols Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            width: 90%;
            margin: 0 auto;
            border-collapse: collapse;
            background-color: #fff;
        }
        th, td {
            padding: 12px 16px;
            border: 1px solid #ccc;
            text-align: left;
        }
        th {
            background-color: #0077cc;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f0f8ff;
        }
    </style>
</head>
<body>

<h1>TCP/IP Protocols and Their Explanation</h1>

<table>
    <thead>
        <tr>
            <th>Protocol</th>
            <th>Layer</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>HTTP</td>
            <td>Application</td>
            <td>HyperText Transfer Protocol – used for transferring web pages over the Internet.</td>
        </tr>
        <tr>
            <td>HTTPS</td>
            <td>Application</td>
            <td>Secure version of HTTP – encrypts data for secure communication.</td>
        </tr>
        <tr>
            <td>FTP</td>
            <td>Application</td>
            <td>File Transfer Protocol – used to transfer files between computers.</td>
        </tr>
        <tr>
            <td>SMTP</td>
            <td>Application</td>
            <td>Simple Mail Transfer Protocol – used for sending emails.</td>
        </tr>
        <tr>
            <td>DNS</td>
            <td>Application</td>
            <td>Domain Name System – translates domain names to IP addresses.</td>
        </tr>
        <tr>
            <td>DHCP</td>
            <td>Application</td>
            <td>Dynamic Host Configuration Protocol – assigns IP addresses to devices.</td>
        </tr>
        <tr>
            <td>TCP</td>
            <td>Transport</td>
            <td>Transmission Control Protocol – ensures reliable, ordered, and error-checked delivery of data.</td>
        </tr>
        <tr>
            <td>UDP</td>
            <td>Transport</td>
            <td>User Datagram Protocol – faster but less reliable, used in streaming and gaming.</td>
        </tr>
        <tr>
            <td>IP</td>
            <td>Internet</td>
            <td>Internet Protocol – routes data packets across networks using IP addresses.</td>
        </tr>
        <tr>
            <td>ICMP</td>
            <td>Internet</td>
            <td>Internet Control Message Protocol – used for error messages and diagnostics (e.g., ping).</td>
        </tr>
        <tr>
            <td>ARP</td>
            <td>Link</td>
            <td>Address Resolution Protocol – maps IP addresses to MAC (physical) addresses.</td>
        </tr>
        <tr>
            <td>Ethernet</td>
            <td>Link</td>
            <td>Standard for wired network connections in the data link layer.</td>
        </tr>
    </tbody>
</table>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()