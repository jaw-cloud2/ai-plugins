# TF Rooms for Claude

Rooms, rates, quotes and booking requests for thirteen New Leaf properties: twelve motels and extended stays in Twin Falls, Idaho, plus High Country Motel in Bellevue.

## Install

In Claude Code:

```
/plugin install tf-rooms --marketplace jaw-cloud2/ai-plugins
```

## What this plugin contains

- A connection to the TF Rooms MCP server at https://tfrooms.com/mcp, run by New Leaf Properties on its own website. This is the same server as the TF Rooms connector in the Claude directory.
- One skill, `room-search-and-booking`, that tells Claude when to use these tools and the rules for answering (for example, quoting published prices with their source link).

It contains no hooks, scripts, local programs or package installs. Nothing runs on your computer.

## What it sends and where

When Claude uses a tool, it sends your dates and room type, and, only when you ask to book, the name, email, phone and notes you give for the booking request to https://tfrooms.com/mcp. Most tools only read published information. The booking tools are the exception: when you ask to book, they send the details you give to New Leaf Properties, which emails you a code; a room is held only after you enter that code, and staff confirm within 24 hours. Looking up or cancelling a reservation happens on tfrooms.com, not in chat: the connector gives the link to https://tfrooms.com/reservation.html, where the guest enters the reservation number and the last four digits of the contact phone. Cancelling there needs a six-digit code emailed to the booking address and is available more than 48 hours before the 3 PM check-in during office hours; otherwise the guest calls the property.
The server answers with published information and source links. Privacy policy for the connector: https://tfrooms.com/privacy.html#ai-assistants

## Help

Connection guide and contact: https://tfrooms.com/connect.html
