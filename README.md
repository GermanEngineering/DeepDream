# DeepDream
Create a deep dream video using your own images.

Credits and many thanks to:
&nbsp;&nbsp;&nbsp;Magnus Pedersen - https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/14_DeepDream.ipynb
&nbsp;&nbsp;&nbsp;Harrison Kinsley - https://pythonprogramming.net/deep-dream-python-playing-neural-network-tensorflow/

Prerequisites:
&nbsp;&nbsp;&nbsp;Python 3.6.6 from https://www.python.org/downloads/release/python-366/
&nbsp;&nbsp;&nbsp;Git from https://git-scm.com/downloads
&nbsp;&nbsp;&nbsp;Microsoft Visual C++ 2015 Redistributable Update 3 from https://www.microsoft.com/en-us/download/details.aspx?id=53587
	
1)	Clone GermanEngineering/DeepDream Git repository.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open command prompt
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WINDOWS cmd ENTER
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create new directory for Git projects.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mkdir GitProjects
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Navigate to created folder.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd GitProjectscd DeepDream
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clone repository.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git clone https://github.com/GermanEngineering/DeepDream.git

2)	Install dependencies
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Navigate to folder containing the requirement files.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd DeepDream/DeepDream
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List all files.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dir
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you have a GPU you should execute:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirementsGPU.txt
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If you need to run on CPU execute:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirements.txt
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can check all installed modules by executing:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip list

3)	Select your start and end image.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create new folders in the DeepDream/DreamImages directory for the start as well as the end image.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy your images in the respective folder and rename them to "img_0.jpg"		
		
3)	Configure the settings for your custom dream.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open the DeepDream.py file in a text editor.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Change the dream1Folder and dream2Folder strings to the name of the folders you just created.
&nbsp;&nbsp;&nbsp;Adapt other settings like the used layers, dream duration, fps, ... to your preferences (or leave them at default in case you're not sure)
	
4)	Run the script by executing:
&nbsp;&nbsp;&nbsp;DeepDream.py
