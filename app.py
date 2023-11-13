import os
from fastapi import FastAPI, Request, Response
from sarufi import Sarufi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SARUFI_API_KEY = os.getenv('SARUFI_API_KEY')
SARUFI_BOT_ID = os.getenv('SARUFI_BOT_ID')

# Initialize your FastAPI application and Sarufi instance
app = FastAPI()
sarufi = Sarufi(SARUFI_API_KEY)


def parse_message(response: dict) -> str:
    """ Parse the message from the Sarufi response. """
    if 'message' in response:
        return "\n".join(response['message']) if isinstance(response['message'], list) else response['message']
    elif 'actions' in response:
        return response['actions'].get("send_message", ["Invalid input. Please try again"])[0]
    return "Invalid input. Please try again"


def format_ussd_response(message: str, next_state: str) -> str:
    """ Format the USSD response. """
    return f"CON {message}" if next_state != "end" else f"END {message}"


def respond(session_id: str, phone_number: str, message: str) -> str:
    """ Respond to a USSD request. """
    chat_id = f"{session_id}-{phone_number}"
    message = message.split("*")[-1]
    response = sarufi.chat(
        bot_id=SARUFI_BOT_ID, chat_id=chat_id, message=message, message_type="text")

    parsed_message = parse_message(response)
    next_state = response.get("next_state", "")
    return format_ussd_response(parsed_message, next_state)


@app.post("/ussd")
async def ussd(request: Request) -> Response:
    """ Handle USSD requests. """
    form_data = await request.form()
    text = form_data.get("text", "default")
    session_id = form_data.get("sessionId")
    phone_number = form_data.get("phoneNumber")
    service_code = form_data.get("serviceCode")

    response = respond(session_id, phone_number, text)
    return Response(content=response, media_type='text/plain')
