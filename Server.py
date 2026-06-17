from mcp.server.fastmcp import FastMCP
from mail import get_unread_emails
 

mcp = FastMCP("Email Assistant")

@mcp.tool()
def unread_email():
    print("📧 Tool called: unread_emails")
    """get unread email"""
    return get_unread_emails

if __name__ == "__main__":
    print("✅ MCP is running...")
    mcp.run()