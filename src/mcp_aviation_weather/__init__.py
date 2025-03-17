import argparse
from .server import mcp

def main():
    """MCP Aviation Weather tool."""
    parser = argparse.ArgumentParser(
        description="MCP Aviation Weather tool for retrieving aviation weather information."
    )
    parser.parse_args()
    mcp.run()

if __name__ == "__main__":
    main()