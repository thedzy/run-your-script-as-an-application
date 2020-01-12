# Run your script as an Application
You can use these shell applications to host and run your script as if it where native application.

## Simply your script distribution to users
Allows you to easily distribute your code to novice users and eliminates the need for the user to make the script execuatble in order to run.

### Script-py-droplet.app
Distribute your Python script as an application accepting files.
Works only when files are dropped on the application
1. Change the icon cmd.icns (/Contents/Resources/cmd.icns)
2. Edit the plist (/Contents/info.plist)
3. Edit the code (Contents/Resources/Scripts/main.py)
4. Ensure main.py is executable `chmod a+x main.py`
5. Send

### Script-py.app
Distribute your Python script as an application
1. Change the icon cmd.icns (/Contents/Resources/cmd.icns)
2. Edit the plist (/Contents/info.plist)
3. Edit the code (Contents/MacOS/main.py)
4. Ensure main.py is executable `chmod a+x main.py`
5. Send

### Script-sh.app
Distribute your Shell script as an application
1. Change the icon (/Contents/Resources/cmd.icns)
2. Edit the plist (/Contents/info.plist)
3. Edit the code (/Contents/MacOS/main.command)
4. Ensure main.command is executable `chmod a+x main.command`
5. Send
