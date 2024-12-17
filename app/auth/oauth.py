from httpx_oauth.clients.google import GoogleOAuth2
from app.config import AUTH_SECRET_KEY

# Get these from Google Cloud Console
GOOGLE_OAUTH_CLIENT_ID = "your-client-id"  # Add to .env file
GOOGLE_OAUTH_CLIENT_SECRET = "your-client-secret"  # Add to .env file

google_oauth_client = GoogleOAuth2(
    client_id=GOOGLE_OAUTH_CLIENT_ID,
    client_secret=GOOGLE_OAUTH_CLIENT_SECRET
)
