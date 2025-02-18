# 🎧 Voice Recognition and Recording System  

Hello! 👋 This project records audio using Python and converts speech to text using the Google Speech Recognition API. 🎧💬  

## Language Options 🌍  
- [Türkçe (Readme)](readme.tr.md)  
- [English (Readme)](readme.md)  

## 🚀 Features 

✅ **Real-time audio recording**: Captures audio using a microphone.  
✅ **Parallel recording processes**: Manages multiple recording sessions simultaneously.  
✅ **Converts Turkish speech to text** using Google Speech Recognition. 🇹🇷📝  
✅ **Seamless recording**: Starts a new recording before the current one ends to prevent word loss. ⏳🎧  

---  

## 📌 Installation  

Follow these steps to run the project. 🛠️  

### 1️⃣ Install Required Packages  
Before running this project, install the necessary Python libraries:  

```bash  
pip install -r requirements.txt  
```  

And that’s it! 🎉 You can start recording and converting audio to text using your computer's microphone.  

---  

## 🛠️ How It Works?  

1️⃣ **Monitor Thread** ⏳  
   - Continuously listens to audio and starts new recordings at intervals.  

2️⃣ **Recording Threads** 🎧  
   - Starts recording audio and continues for a set duration.  
   - **A new recording starts just before the previous one ends** to ensure no words are lost.  

3️⃣ **Processing Thread** 🔄  
   - Saves recorded audio as a `.wav` file and converts it to text using Google Speech Recognition.  

4️⃣ **Results** 📝  
   - The recognized text is added to a list and displayed continuously on the screen.  

---  

## ⚠️ Important Notes  

❗ **Restart the program if you change the microphone!** 🚫🎤  
❗ **An internet connection is required since Google API is used for transcription.** 🌍💡  

---  

✨ Hope this project helps you! If you like it, feel free to leave a ⭐! 😊🚀