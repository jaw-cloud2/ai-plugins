# jwatte.com website tools for Claude

Find a free jwatte.com website audit tool, get a ready-to-run audit link, and search or list jwatte.com articles and books.

## Install

In Claude Code:

```
/plugin install jwatte-website-tools --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the jwatte.com website tools MCP server at https://jwatte.com/mcp, run by Josh Watte on its own website. This is the same server as the jwatte.com website tools connector in the Claude directory.
- One skill, `site-audit-and-articles`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends the search words, tool name, website address, topic or date you ask about to https://jwatte.com/mcp. Every tool is read-only: nothing is booked, bought, sent or changed, and no account is needed.
The server answers with published information and source links. Privacy policy for the connector: https://jwatte.com/privacy/#mcp

## Help

Connection guide and contact: https://jwatte.com/connect/
