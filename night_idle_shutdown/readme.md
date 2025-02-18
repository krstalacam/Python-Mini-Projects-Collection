# **PC Auto Shutdown at Night 💤**  

This small but functional program helps automatically shut down your computer. If **there is no mouse movement for 1 hour** and the time is **before 08:00**, it will execute the shutdown command. However, if the mouse moves, the shutdown process is canceled. 🚀  

## Language Options 🌍
- [Türkçe (Readme)](readme.tr.md)
- [English (Readme)](readme.md)

## **How It Works? 🛠️**  
1. **Must be added to startup applications** 🖥️  
   - This ensures that the program runs automatically when the computer starts.  
2. **Monitors mouse movements** 🖱️  
   - If there is **no mouse movement for 1 hour** and the time is **before 08:00**, it triggers the shutdown command.  
3. **Cancels shutdown if the mouse moves** ❌  
   - When mouse movement is detected, the shutdown process is canceled.  

## **Why Use a `.pyw` File? 🤔**  
We use the `.pyw` extension because we want the script to **run in the background**. If we used `.py`, a terminal window would open when the program runs. With `.pyw`, we prevent this window from appearing. 🪄✨  

## **Installation & Usage 📌**  
1. Save the `night_idle_shutdown.pyw` file to your computer.  
2. **Add it to the startup folder:**  
   - Press `Win + R`.  
   - Type `shell:startup` and press `Enter`.  
   - Copy the `night_idle_shutdown.pyw` file into the opened folder.  
3. Now, the program will start automatically when the computer boots up! 🎉  

## **Notes 📢**  
- The program **only runs before 08:00**.  
- If **there is no mouse movement for 1 hour**, it will shut down the PC.  
- If the mouse moves, **shutdown is canceled**.  

Hope this helps! Enjoy using it 😊🚀  