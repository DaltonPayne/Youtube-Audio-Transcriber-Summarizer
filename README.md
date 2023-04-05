# Youtube-Audio-Transcriber/Summarizer

This project provides a Python script that downloads the audio of a given YouTube video, transcribes it using OpenAI's Whisper ASR API, and then summarizes the transcribed text using OpenAI's GPT-3 API.

## Prerequisites

- Python 3.6 or higher
- [OpenAI Python](https://github.com/openai/openai) (version 0.27.0 or higher)
- [PyDub](https://github.com/jiaaro/pydub) (version 0.25.1 or higher)
- [Pytube](https://github.com/pytube/pytube) (version 11.0.1 or higher)
- An OpenAI API key with access to the Whisper ASR and GPT-3 APIs

## Installation

1. Clone the repository:

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/Youtube-Audio-Transcriber-Summarizer.git
\`\`\`

2. Change into the project directory:

\`\`\`bash
cd Youtube-Audio-Transcriber-Summarizer
\`\`\`

3. Create a virtual environment (optional, but recommended):

\`\`\`bash
python -m venv venv
\`\`\`

4. Activate the virtual environment:

- On Windows:

\`\`\`bash
venv\Scripts\activate
\`\`\`

- On Linux/Mac:

\`\`\`bash
source venv/bin/activate
\`\`\`

5. Install the required packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage

1. Replace `YOUR_API_KEY_HERE` in the `transcribe_summarize.py` file with your OpenAI API key.

2. Run the script:

\`\`\`bash
python transcribe_summarize.py
\`\`\`

3. Enter a YouTube video URL when prompted.

The script will download the audio from the video, transcribe it using the Whisper ASR API, and then summarize the transcription using the GPT-3 API. The transcribed text and the summary will be printed to the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
