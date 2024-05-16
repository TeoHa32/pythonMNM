from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Phạm vi truy cập để thực hiện hành động "like"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def main():
    # Cập nhật đường dẫn đến tệp client_secrets_file.json
    flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\file\pythonMNM\client_secrets.json', SCOPES)
    
    # Sử dụng run_local_server để lấy thông tin xác thực
    credentials = flow.run_local_server(port=0)

    # Xây dựng dịch vụ API YouTube
    youtube = build('youtube', 'v3', credentials=credentials)

    # ID của video mà bạn muốn like
    video_id = 'VIDEO_ID_HERE'

    # Thực hiện hành động like
    youtube.videos().rate(
        id=video_id,
        rating='like'
    ).execute()

    print(f"Video {video_id} đã được like thành công.")

if __name__ == '__main__':
    main()
