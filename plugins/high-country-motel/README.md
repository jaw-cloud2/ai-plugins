# High Country Motel for Claude

Rooms, rates and price estimates, ski trips to Sun Valley, crew, weekly and monthly stays, pets and policies at High Country Motel in Bellevue, Idaho.

## Install

In Claude Code:

```
/plugin install high-country-motel --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the High Country Motel MCP server at https://highcountrymotelid.com/mcp, run by New Leaf Properties on its own website. This is the same server as the motel's own High Country Motel connector.
- One skill, `bellevue-motel-questions`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends your dates, room type, topic, language or search words to https://highcountrymotelid.com/mcp. Every tool is read-only: nothing is booked, bought, sent or changed, and no account is needed.
The server answers with published information and source links. Privacy policy for the connector: https://highcountrymotelid.com/privacy.html#ai-assistants

## Help

Connection guide and contact: https://highcountrymotelid.com/connect.html
