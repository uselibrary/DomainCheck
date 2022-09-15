import socket
import json
import time
import os


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
        print("Timeout")
        exit(1)


def get_tld(tld):
    # open tld.json file, same directory
    # ask for input tld, if the input tld is in tld.json, return nic and response
    with open('tld.json', 'r') as f:
        tld_data = json.load(f)
        if tld in tld_data:
            return tld_data[tld]["nic"], tld_data[tld]["response"]
        else:
            print("TLD not found")
            exit(1)


def read_dict(dict_path):

    # if the dict file is not exist, exit
    try:
        list = []
        with open(dict_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                list.append(line)
        return list
    except FileNotFoundError:
        print("Dict file not found")
        exit(1)


def delay_second(delay_time):
    if not delay_time.isdigit():
        print("Not a number")
        exit(1)
    delay_time = int(delay_time)
    return delay_time


# write the data to a file, every domain in a line
def result_file(result_path, data):
    with open(result_path, 'a') as f:
        f.write(data + '\n')


def main():

    # try the following code, if error, print the error message
    try:
        # get tld name from user
        tld_name = input("Enter tld name: ")
        # get dict from user
        dict_name = input("Enter dict name: ")
        # get delay from user
        delay_time = input("Enter delay: ")

        # check if the input tld is in tld.json
        nic, response = get_tld(tld_name)
        if nic and response:
            # read dict
            dict_path = 'dict/' + dict_name
            list = read_dict(dict_path)

            # get delay time
            delay = delay_second(delay_time)

            # build result file path with tld name and dict name, time format is year-month-day-hour-minute-second
            result_path = os.getcwd() + '/result/' + tld_name + '_' + dict_name + '_' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.log'
            # write set up information to result file: tld name, dict name, delay time, time
            result_file(result_path, 'TLD: ' + tld_name + ' Dict: ' + dict_name + ' Delay: ' + delay_time + ' Time: ' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
            result_file(result_path, '****************************')

            print("Task Start")
            print("****************")

            for i in list:
                domain = i + '.' + tld_name
                #print(domain)
                whois_server = nic
                whois_data = get_whois(domain, whois_server)

                if response in whois_data.lower():
                    print(domain + ' is available')
                    result_file(result_path, domain + ' is available')
                else:
                    print(domain + ' is NOT available')

                # sleep for delay seconds
                time.sleep(delay)

            print("****************")
            print("Task Done")

    # if KeyboardInterrupt, print the message
    except KeyboardInterrupt:
        print("****Task Interrupted*****")
        exit(1)


if __name__ == '__main__':
    main()
