import ssl
import os
import sys
import openai
from pydub import AudioSegment
from pytube import YouTube
from pytube.cli import on_progress
from tqdm import tqdm


if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# Set up your API keys
OPENAI_API_KEY = "YOUR_API_KEY_HERE"

# Initialize the OpenAI API
openai.api_key = OPENAI_API_KEY

# Define function to summarize text using OpenAI's GPT-3 API
def summarize_text(text):
    # Split text into 500-token chunks
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    # Initialize summary list
    summaries = []

    # Summarize each chunk using GPT-3 and append to summaries list
    for chunk in chunks:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Please give a summary of this video transcription in one sentence:\n{chunk}\nSummary:",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        summaries.append(response.choices[0].text.strip())

    # Join summaries into a single string
    summary = " ".join(summaries)

    return summary


def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        yt.register_on_progress_callback(on_progress)

        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = audio_stream.download(output_path="", filename="audio")
        os.rename(output_path, "audio.mp4")

        audio = AudioSegment.from_file("audio.mp4", format="mp4")
        audio.export("audio.mp3", format="mp3")

        # transcribe audio using OpenAI's Whisper ASR API
        with open("audio.mp3", "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file, file_name="audio.mp3")
            text = response["text"]
            if text.strip():
                print(text.strip())
                # Summarize the transcribed text
                summary = summarize_text(text)
                print("Summary:", summary)

        # Clean up temporary files
        os.remove("audio.mp3")
        os.remove("audio.mp4")

    except Exception as e:
        print("Error: Unable to download and transcribe the audio from the provided URL.")
        sys.exit(1)

# Main function to download and transcribe audio
def main():
    video_url = input("Enter a YouTube video URL: ")
    print("Downloading and transcribing audio... Please wait.")
    download_audio(video_url)

if __name__ == "__main__":
    main()
