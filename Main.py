from pytube import YouTube
import ssl
import streamlit as st


def main():
    ssl._create_default_https_context = ssl._create_stdlib_context
    
    st.markdown("""# Download Youtube Video""")
    with st.form("my_form"):
        
        # User input url
        url = st.text_area(label='URL', placeholder='https://www.youtube.com/...')
        download_path = st.text_area(label='Download Path', placeholder='/Users/user/Desktop/downloaded-video')
        
        
        
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            # Create youtube object
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(f'{download_path}')
            
if __name__ == '__main__':
    main()