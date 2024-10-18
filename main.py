from pzp.client import PzpClient
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Connect to PZP heat pump and read values")

    # Add sarguments
    parser.add_argument('server_base', type=str, help='PZP heat pump web interface base url, eg. https://192.168.1.2/')
    parser.add_argument('--username', type=str, default="admin", help='Username for login, defaults to admin')
    parser.add_argument('--password', type=str, default="admin", help='Password for login, defaults to admin')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode, a lot of stuff printed, useful for debug only.')

    args = parser.parse_args()

    if args.verbose:
        print(f"Logging into {args.server_base} as user {args.username}")

    client = PzpClient.create_and_login(args.server_base, args.username, args.password)
    if args.verbose:
        print("Logged in successfully")    
    # Get temperatures
    print("Fetching temperatures...")
    client.print_temps(print_header=True, sep=";")

    # Logout
    client.logout()
    if args.verbose:
        print("Logged out successfully")
