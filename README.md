# Discord Token Tools

This Python program provides a set of tools for working with Discord tokens. You can validate your Discord token, retrieve user information, and perform various Discord API operations.

## Features

- **Login with Token**: Logs into Discord using the provided token.
- **Token Info**: Retrieves and displays token information, including user details, email, phone number, Nitro status, and badges.
- **Bomb Account**: Spams a channel with messages.
- **Token Generator**: Launches a token generator tool.
- **Spam Webhook**: Sends spam messages through a webhook.

## Requirements

- Python 3.x
- `requests` library
- `rich` library

You can install these libraries using the following command:
```bash
pip install requests rich
```

## Usage
Run the program to view the main menu. The menu includes the following options:

- **Bomb Account:** Enter a channel URL and start sending messages to spam.
- **Token Info:** Displays the information of the provided token.
- **Login with Token:** Logs into Discord with the token.
- **Token Generator:** Runs a token generator tool.
- **Spam Webhook:** Sends spam messages to a webhook.

## Token Information
The program retrieves token information and displays the following details for the user:

- **Username:** User's name
- **Discriminator:** User's tag
- **ID:** User's ID
- **Email:** Masked email address
- **Phone:** Masked phone number
- **Nitro Status:** Whether the user has Nitro
- **MFA Status:** Whether Two-Factor Authentication is enabled
- **Verification Status:** Whether the account is verified

## Badges
User badges are categorized as follows:

- **Good:** Good badges (e.g., Discord Staff, Partnered Server Owner)
- **Bad:** Bad badges (e.g., HypeSquad Bravery)

- 
