# 📡 Simple Socket Chat Application

Hello! 👋 In this project, we developed a basic client-server chat application using Python's `socket` module. The server (`server.py`) can accept only one client and only the server can send messages. The client (`client.py`) receives these messages and displays them but cannot send messages back. 💬💻

---
## Language Options 🌍
- [Türkçe (Readme)](readme.tr.md)
- [English (Readme)](readme.md)

## 📂 File Descriptions

### 1️⃣ `server.py`
🔹 Retrieves the computer name and IP address.  
🔹 Listens for a single client on a specified port.  
🔹 Sends messages to the connected client.  
🔹 Manages the client connection.  

### 2️⃣ `client.py`
🔹 Connects to the server and displays incoming messages.  
🔹 Waits for messages as long as the server is active.  
🔹 Runs until the server closes the connection.  

---

## 🚀 Setup and Usage

### 🛠️ Requirements
- Python 3.x  

### 🏗️ Installation  

1. **Start the Server** 🖥️  
   ```bash
   python server.py
   ```
   When the server runs, it displays the IP address and connection port. ✨  

2. **Run the Client** 💻  
   ```bash
   python client.py
   ```
   Once connected, the client displays messages from the server. 📩  

---

## 📝 Notes  
- The server can accept only one client.  
- The client can only receive messages from the server and cannot send messages.  
- The connection remains active until the server is closed.  
- If the client loses connection, the program terminates.  

🔧 If you encounter any issues or have improvement suggestions, feel free to contribute! 🛠️🤓  

---

🚀 **Happy coding!** 🎉  