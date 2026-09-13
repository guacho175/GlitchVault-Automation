import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

BASE_DIR = r"C:\Users\galin\OneDrive\Documentos\Tiktok"
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
SCOPES = ['https://www.googleapis.com/auth/youtube.upload', 'https://www.googleapis.com/auth/youtube.readonly']

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            from google.auth.transport.requests import Request
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                return None
                
            redirect_uri = "http://localhost:3000/api/auth/callback"
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES, redirect_uri=redirect_uri)
            auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
            print(f"Visita esta URL para autorizar:\n{auth_url}")
            
            from http.server import BaseHTTPRequestHandler, HTTPServer
            from urllib.parse import urlparse, parse_qs
            import threading
            
            auth_code = None
            class AuthHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    nonlocal auth_code
                    query = parse_qs(urlparse(self.path).query)
                    if 'code' in query:
                        auth_code = query['code'][0]
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        self.wfile.write(b"Autorizacion completa para LEER y SUBIR. Puedes cerrar esta ventana.")
                    else:
                        self.send_response(400)
                        self.end_headers()
            
            server = HTTPServer(('localhost', 3000), AuthHandler)
            def handle_requests():
                while not auth_code: server.handle_request()
            t = threading.Thread(target=handle_requests)
            t.start()
            t.join()
            
            flow.fetch_token(code=auth_code)
            creds = flow.credentials
            
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def main():
    creds = get_credentials()
    youtube = build('youtube', 'v3', credentials=creds)
    
    channels_response = youtube.channels().list(mine=True, part='contentDetails').execute()
    uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while True:
        playlist_response = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        
        for item in playlist_response['items']:
            videos.append(item['snippet']['title'])
            
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token: break
            
    print(f"TITLES_START")
    for v in videos:
        print(v)
    print(f"TITLES_END")

if __name__ == '__main__':
    main()
