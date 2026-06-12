from mcp.server.fastmcp import Fastmcp
from gmail import get_unread_emails
 

mcp = Fastmcp("Email Assistant")

@mcp.tool()
def unread_email():
    """get unread email"""
    return get_unread_emails

if __name__ == "__main__":
    mcp.run()