# sarufi-africastalking-ussd-blueprint
A  boilerplate code to easy that provides a USSD service that interfaces with the Sarufi API. It's designed to handle USSD requests, process them using the Sarufi service, and return appropriate responses.

## Features

- USSD request handling using FastAPI.
- Integration with Sarufi for processing chat messages.
- Environmental variable support for secure configuration.

## Setup

To set up the project, follow these steps:

### Prerequisites

- Python 3.6+
- pip (Python package manager)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Neurotech-HQ/sarufi-africastalking-ussd-blueprint.git
   cd sarufi-africastalking-ussd-blueprint
   ```

   Install Dependencies

### Use pip to install the required Python packages.


```bash
pip install -r requirements.txt
```
### Environment Variables

Set up the necessary environment variables. Create a .env file in the root directory of the project and add the following:

```bash 
SARUFI_API_KEY=your_sarufi_api_key
SARUFI_BOT_ID=your_sarufi_bot_id
```

> Replace your_sarufi_api_key and your_sarufi_bot_id with your actual Sarufi API key and bot ID.

### Running the Application

To run the application, execute:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on the default port 8000.

### Usage

Once the server is running, it will be listening for POST requests at the /ussd endpoint. The request should contain the following form data:

text: The USSD input text.
sessionId: The session ID of the USSD session.
phoneNumber: The phone number of the user.
serviceCode: The service code of the USSD request.
The application will process this information and respond accordingly.

### Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License.

