from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import ChatMessage
from .serializers import ChatMessageSerializer
import requests
import os

# Strip to avoid hidden spaces/newlines
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL = "llama3-8b-8192"  # Change if needed

@api_view(['POST'])
@permission_classes([AllowAny])
def chatbot_query(request):
    user_message = request.data.get('message', '').strip()

    if not user_message:
        return Response({"error": "No message provided"}, status=400)

    # Save user message only
    ChatMessage.objects.create(user_message=user_message)

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""You are a Barangay Official of Barangay Mabini. Respond politely and clearly about government services, complaints, permits, announcements, and community events.

User: {user_message}
Official:"""

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful Barangay Official."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    # Debug: print API key and headers (remove in production)
    print(f"GROQ_API_KEY: '{GROQ_API_KEY}'")
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")

    try:
        groq_response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )
        # Debug: print status and response content
        print(f"Response status: {groq_response.status_code}")
        print(f"Response text: {groq_response.text}")

        groq_response.raise_for_status()
        reply = groq_response.json()['choices'][0]['message']['content']

        # Save bot reply
        ChatMessage.objects.create(user_message=user_message, bot_reply=reply)

        return Response({"reply": reply.strip()})
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {str(e)}")  # Log error
        return Response({"error": str(e)}, status=500)
