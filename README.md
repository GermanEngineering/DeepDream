# DeepDream
Create a deep dream video using your own images.

Prerequisites:
	Python 3.6.6 from https://www.python.org/downloads/release/python-366/
	Git from https://git-scm.com/downloads
	Microsoft Visual C++ 2015 Redistributable Update 3 from https://www.microsoft.com/en-us/download/details.aspx?id=53587
	
1)	Clone GermanEngineering/DeepDream Git repository.
		Open command prompt
			WINDOWS cmd ENTER
		Create new directory for Git projects.
			mkdir GitProjects
		Navigate to created folder.
			cd GitProjects
		Clone repository.
			git clone https://github.com/GermanEngineering/DeepDream.git

2)	Install dependencies
		Navigate to folder containing the requirement files.
			cd DeepDream/DeepDream
		List all files.
			dir
		If you have a GPU (or can afford to buy one) you should execute:
		(It's WAY FASTER(!) =)
			pip install -r requirementsGPU.txt
		If you need to run on CPU execute:
			pip install -r requirements.txt
		You can check all installed modules by executing:
			pip list

3)	Select your start and end image.
		Create new folders in the DeepDream/DreamImages directory for the start as well as the end image.
		Copy your images in the respective folder and rename them to "img_0.jpg"		
		
3)	Configure the settings for your custom dream.
		Open the DeepDream.py file in a text editor.
		Change the dream1Folder and dream2Folder strings to the name of the folders you just created.
		Adapt other settings like the used layers, dream duration, fps, ... to your preferences (or leave them at default in case you're not sure)
	
4)	Run the script by executing:
	DeepDream.py
