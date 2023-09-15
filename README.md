# OktaGuardian

OktaGuardian is a secure and reliable web application designed to help you conceal your Okta API key and access Okta resources securely. By using OktaGuardian, you can ensure that your API key remains protected and not exposed in your scripts or applications.

## Features

- **Secure API Key Storage**: OktaGuardian securely stores your Okta API key as an environment variable on a trusted machine, reducing the risk of unauthorized access.

- **Proxy Authentication**: The web application acts as a proxy, handling Okta API requests on your behalf, and returning the results to your scripts or applications.

- **User Access Control**: Restrict access to the machine hosting OktaGuardian to trusted individuals, ensuring the security of your Okta integration.

## Getting Started

To get started with OktaGuardian, follow these steps:

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/yourusername/oktaguardian.git
   ```

2. Install the necessary dependencies for the web application.

   ```bash
   cd oktaguardian
   npm install
   ```
   
4. Configure your Okta API credentials in the environment variables on the machine where OktaGuardian is hosted.
   
   ```bash
   export OKTA_API_KEY=your_api_key_here
   ```
   
6. Start the OktaGuardian web app.

   ```bash
   npm start
   ```
Your OktaGuardian instance is now ready to accept API requests from your scripts or applications.

## Usage

In your PowerShell or other scripts:

```PowerShell
$userId = "your_user_id"
$webAppUrl = "https://oktaguardian.vercel.app/api/endpoint"

$response = Invoke-RestMethod -Uri $webAppUrl -Method Get -Headers @{ "Authorization" = "Bearer MY_TOKEN" }

# then process the response as needed :)
```

>TODO: "MY_TOKEN" with any authentication token or header required.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Contact
If you have any questions or need assistance, feel free to contact us at alainQtec@gmail.com.
