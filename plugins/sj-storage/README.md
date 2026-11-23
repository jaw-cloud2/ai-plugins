# SJ Storage for Claude

Self-storage units, prices, live availability, hours, policies and rental links for SJ Storage in Twin Falls, Idaho.

## Install

In Claude Code:

```
/plugin install sj-storage --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the SJ Storage MCP server at https://sjstorage.net/mcp, run by SJ Storage on its own website. This is the same server as the SJ Storage connector in the Claude directory.
- One skill, `storage-questions`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends the unit size, move-in date or search words you ask about to https://sjstorage.net/mcp. Every tool is read-only: nothing is booked, bought, sent or changed, and no account is needed.
The server answers with published information and source links. Privacy policy for the connector: https://sjstorage.net/privacy-policy.html#mcp

## Help

Connection guide and contact: https://sjstorage.net/connect/
