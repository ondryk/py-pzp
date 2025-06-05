from pzp.client import PzpClient
from pzp.pages.temps import TemperatureParser
from pzp.pages.states import RunningStateParser
from pzp.pages.allvalues import AllValuesParser
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect to PZP heat pump and read values")
    # Add sarguments
    parser.add_argument('server_base', type=str, help='PZP heat pump web interface base url, eg. https://192.168.1.2/')
    parser.add_argument('--output', type=str, default="temps", help='Output values, "temps" for temperatures, "states" for binary values of running states, "all" for all values possible')
    parser.add_argument('--print-headers', action='store_true', default=False, help='Print CSV headers to output')
    parser.add_argument('--username', type=str, default="admin", help='Username for login, defaults to admin')
    parser.add_argument('--password', type=str, default="admin", help='Password for login, defaults to admin')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode, a lot of stuff printed, useful for debug only.')

    args = parser.parse_args()

    if args.verbose:
        print(f"Logging into {args.server_base} as user {args.username}")

    client = PzpClient.create_and_login(args.server_base, args.username, args.password)
    try:        
        if args.verbose:
            print("Logged in successfully")    

        if args.output == 'temps':
            temps = TemperatureParser(client)
            temps.print(args.print_headers, ";")
        if args.output == 'states':
            states = RunningStateParser(client)
            states.print(args.print_headers, ";")
        if args.output == 'all':
            states = AllValuesParser(client)
            states.print(args.print_headers, ";")

    finally:
        client.logout()
        if args.verbose:
            print("Logged out successfully")
