import os
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

# Get the Hugging Face API key from environment
HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY")
client = InferenceClient(token=HUGGINGFACE_API_KEY)

def generate_image(prompt: str) -> Image.Image:
    """Generate an image from a text prompt using Hugging Face API."""
    response = client.text_to_image(prompt)

    if isinstance(response, (bytes, bytearray)):
        return Image.open(BytesIO(response))

    raise Exception("❌ Unexpected response type from InferenceClient")




