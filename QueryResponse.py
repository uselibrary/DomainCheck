import socket

# query whois server by WHOIS protocol
# variable: domain and whois server
def get_whois(domain, whois_server):

    # timeout is 10 seconds
    socket.setdefaulttimeout(10)

    # if timeout, return "timeout"
    try:
        # connect to whois server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((whois_server, 43))
        s.send((domain + '\r\n').encode())
        response = ''
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data.decode()
        s.close()
        return response
    except socket.timeout:
        return 'timeout'


# https://www.iana.org/domains/root/db/??.html, ?? is the tld nic whois server


# exexute the function
if __name__ == '__main__':
    # input domain
    domain = input("Input domain: ")
    # input nic whois
    whois_server = input("Input whois server: ")
    # get response
    print(domain, whois_server)
    response = get_whois(domain, whois_server)
    # print response
    print(response)
    