#!/usr/bin/env python3
"""
Exploit Framework - Main Entry Point
A comprehensive penetration testing and exploit development framework.
"""

import sys
import os
import argparse

# Ensure framework package is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def banner():
    """Print the startup banner (minimal — main banner shown by console)."""
    pass  # Banner is displayed by InteractiveConsole.start()


def main():
    """Main function - parse args and launch the framework."""
    parser = argparse.ArgumentParser(
        description="Exploit Framework - Penetration Testing Suite",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--no-banner", action="store_true", help="Suppress the startup banner"
    )
    parser.add_argument(
        "--api", action="store_true", help="Start the REST API server"
    )
    parser.add_argument(
        "--api-host", default="0.0.0.0", help="API server host (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--api-port", type=int, default=5000, help="API server port (default: 5000)"
    )
    parser.add_argument(
        "-r", "--resource", help="Execute commands from a resource script file"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Quiet mode (minimal output)"
    )
    
    args = parser.parse_args()
    
    if not args.no_banner and not args.quiet:
        banner()
    
    try:
        from exploit_framework.cli.console import InteractiveConsole
        
        console = InteractiveConsole()
        
        # Start API server if requested
        if args.api:
            try:
                from exploit_framework.api.server import FrameworkAPI
                api = FrameworkAPI(console.framework)
                api.start(host=args.api_host, port=args.api_port)
            except Exception as e:
                print(f"[-] Failed to start API server: {e}")
        
        # Execute resource script if provided
        if args.resource:
            if os.path.isfile(args.resource):
                print(f"[*] Loading resource script: {args.resource}")
                with open(args.resource, "r") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            print(f"> {line}")
                            console.execute_command(line)
            else:
                print(f"[-] Resource script not found: {args.resource}")
        
        # Start interactive console
        console.run()
        
    except KeyboardInterrupt:
        print("\n[*] Exiting framework...")
    except ImportError as e:
        print(f"\n[-] Import error: {e}")
        print("[*] Make sure all dependencies are installed:")
        print("    pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"\n[-] Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
