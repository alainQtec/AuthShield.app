# authShield

authShield is a secure and reliable web application designed to help you conceal your Okta API key and access Okta resources securely. By using authShield, you can ensure that your API key remains protected and not exposed in your scripts or applications.

## Features

- **Secure API Key Storage**: authShield securely stores your Okta API key as an environment variable on a trusted machine, reducing the risk of unauthorized access.

- **Proxy Authentication**: The web application acts as a proxy, handling Okta API requests on your behalf, and returning the results to your scripts or applications.

- **User Access Control**: Restrict access to the machine hosting authShield to trusted individuals, ensuring the security of your Okta integration.

## Getting Started

To get started with authShield, follow these steps:

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/yourusername/authShield.git
   ```

2. Install the necessary dependencies for the web application.

   ```bash
   cd authShield
   npm install
   ```
   
4. Configure your Okta API credentials in the environment variables on the machine where authShield is hosted.
   
   ```bash
   export OKTA_API_KEY=your_api_key_here
   ```
   
6. Start the authShield web app.

   ```bash
   npm start
   ```
Your authShield instance is now ready to accept API requests from your scripts or applications.

## Usage

In your PowerShell or other scripts:

```PowerShell
$userId = "your_user_id"
$webAppUrl = "https://authShield.vercel.app/api/endpoint"

$response = Invoke-RestMethod -Uri $webAppUrl -Method Get -Headers @{ "Authorization" = "Bearer MY_TOKEN" }

# then process the response as needed :)
```

>TODO: "MY_TOKEN" with any authentication token or header required.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Contact
If you have any questions or need assistance, feel free to contact us at alainQtec@gmail.com.
