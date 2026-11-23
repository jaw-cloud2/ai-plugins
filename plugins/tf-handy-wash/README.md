# TF Handy Wash for Claude

Prices, machines, cycle times, hours, payment methods and problem-reporting steps for TF Handy Wash, a 24-hour laundromat in Twin Falls, Idaho.

## Install

In Claude Code:

```
/plugin install tf-handy-wash --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the TF Handy Wash MCP server at https://tfhandywash.com/mcp, run by TF Handy Wash on its own website. This is the same server as the TF Handy Wash connector in the Claude directory.
- One skill, `laundromat-questions`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends the topic, machine number, language or search words you ask about to https://tfhandywash.com/mcp. Every tool is read-only: nothing is booked, bought, sent or changed, and no account is needed.
The server answers with published information and source links. Privacy policy for the connector: https://tfhandywash.com/privacy.html#mcp-privacy

## Help

Connection guide and contact: https://tfhandywash.com/connect.html
