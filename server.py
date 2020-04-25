import sys, getopt, re, requests
from urllib.error import HTTPError

def main(argv):
    argv = sys.argv[1:]
    if len(argv) != 4:
        print('Incorrect arguments provided:-');
        print('Correct Usage:-');
        print('server.py -a <macaddress> -t <token> OR server.py --address <macaddress> --token <token>');
        sys.exit(2);
    try:
      opts, args = getopt.getopt(argv,'ha:t:',['help','address=','token='])
      macaddropt = opts[0]
      tokenopt   = opts[1]
      if opts == []:
          print('Wrong Input. Correct Command should be:-');
          print('server.py -a <macaddress> -t <token> OR server.py --address <macaddress> --token <token>');
          sys.exit();
    except getopt.GetoptError:
        print ('server.py -a <macaddress>');
        sys.exit(2);
    if (macaddropt[0] == '-a' or macaddropt[0] == '--address') and (tokenopt[0] == '-t' or tokenopt[0] == '--token'):
        macaddrinfo = macaddropt[1]
        API_TOKEN   = tokenopt[1]
        matched     = re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", macaddrinfo)
        is_match    = bool(matched)
        if is_match:
            print('MAC Address provided is ', macaddrinfo)
        else:
            print('Wrong Mac Address')
            sys.exit(2)
    macaddrpath = '/v1?output=json&search=';
    macaddrpath += macaddrinfo;
    #print('Mac Addr Path: ', macaddrpath)    
    API_ENDPOINT = 'https://api.macaddress.io/'+ macaddrpath
    headers      = {'Content-Type': 'application/json', 'X-Authentication-Token': API_TOKEN}
    try:
        response = requests.get(url = API_ENDPOINT, headers=headers)
        response.raise_for_status()
        jsonRes  = response.json()
        #for key, value in jsonRes.items():
        #    print(key, ":", value)
        print('Vendor Details of the provided MAC Address <', macaddrinfo, '> is: ', jsonRes["vendorDetails"]["companyName"] , ' having address: ', jsonRes["vendorDetails"]["companyAddress"])
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
if __name__ == "__main__":
   main(sys.argv[1:])