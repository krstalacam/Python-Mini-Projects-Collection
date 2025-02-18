# 🤖 Voice Assistant README

Hello! 👋 This project helps you create a simple assistant using Python that works with voice commands. 🎙️💡 It recognizes voice commands, searches on Google, tells the time, and can even shut down. 🚀

## Language Options 🌍
- [Türkçe (Readme)](readme.tr.md)
- [English (Readme)](readme.md)

## 📌 Features  
- 🎤 **Recognizes voice commands** (Uses Google Speech Recognition)  
- 🕰️ **Can tell the time**  
- 🔍 **Can search on Google**  
- 📺 **Can search for videos on YouTube**  
- 🎵 **Converts text to speech and responds with voice** (Uses gTTS and pygame)  
- 🗑️ **Deletes old audio files**  
- ⏳ **Manages waiting time with timeout control**  

## 🚀 Installation  
To use the project, install the following libraries:  
```sh  
pip install -r requirements.txt  
```  
Additionally, ensure that your computer has the necessary audio drivers for **pygame** installed. 🎧  

## 🔥 Usage  
### Running the Program  
There are two different ways to run the program:  

1️⃣ **Running with Voice Control:**  
```sh  
python by_voice_control.py  
```  
With this method, the program listens to voice commands directly through the microphone and executes the given instructions. 🎙️  

2️⃣ **Running with Text Control:**  
```sh  
python by_text_control.py  
```  
In this method, instead of voice commands, you can control the assistant using written commands. You can enter commands via the keyboard. ⌨️  

### Available Commands  
- **"What time is it?"** ⏰ (Tells the time)  
- **"Search --> Python"** 🔍 (Searches for "Python" on Google)  
- **"Open video --> Lo-fi music"** 📺 (Searches for the specified keyword on YouTube)  
- **"Shut down"** 👋 (Terminates the program)  

## 🛠️ How It Works?  
- The `record()` function listens to the microphone and converts speech into text.  
- The `response()` function analyzes what the user said and generates a response.  
- The `speak()` function plays the response as audio.  
- The `remove_old_audio()` function deletes old audio files.  

## ⚠️ Important Notes  
- **An internet connection is required** because Google Speech Recognition and gTTS work online. 🌐  
- **Make sure microphone access is enabled in the background!** 🎤  
- If speech recognition does not work, check the `print(voice)` line to see what the assistant is detecting. 🧐  

🚀 **Happy coding!** 🧑‍💻💖  