# Reel-Maker
Reel Maker is a Python-based GUI application that allows you to create automated video clip.
<br>
<img src="Screenshot 2024-12-18 214958.png" >
<br>
# Reel Maker - Help Guide

## Overview:
Reel Maker is a Python-based application that allows you to create a clip, specify the start and end times for clips, 
and generate multiple smaller video clips from a larger video file.
This can be useful for creating short, shareable video segments or for extracting specific parts of a video.

## Requirements:
- Python 3.x
- tkinter (for GUI)
- customtkinter (for enhanced GUI components)
- moviepy (for video processing)

## Installation Instructions:
1. Install Python 3.x from [Python Official Website](https://www.python.org/downloads/).
2. Install the required Python packages:
   - `tkinter` (usually pre-installed with Python)
   - `customtkinter` (can be installed via pip: `pip install customtkinter`)
   - `moviepy` (can be installed via pip: `pip install moviepy`)

## Usage:

### 1. **Upload a Video**:
   - Click on the "Upload Video" button to select and upload a video file (only MP4 format supported).
   - Once uploaded, the video details such as file path, format, size, resolution, duration, and total frames will be displayed.

### 2. **Set Time Parameters for Clips**:
   - **Start Time (HH:MM:SS)**: Enter the start time for the section of the video you want to clip.
   - **End Time (HH:MM:SS)**: Enter the end time for the section of the video you want to clip.
   - **Clip Length (in Seconds)**: Define the length of each clip you want to generate (e.g., 10 seconds).

### 3. **Count Clips**:
   - After entering the time parameters, click on the "Count Clips" button to calculate how many clips will be generated from the video based on the given clip length.
   - The program will display the total number of clips and any remaining time (if the video duration is not perfectly divisible by the clip length).

### 4. **Generate Clips**:
   - Once the clips are counted, click the "Generate Clips" button to start creating the smaller video clips.
   - The clips will be saved in the "output" folder with filenames based on the clip name you provide.
   - The program will process the video and generate the clips sequentially.

### 5. **Reset**:
   - Use the "Reset" button to clear all entered values and prepare for processing another video.

## Error Handling:
- If a non-MP4 video file is selected, an error message will appear.
- If the start time is later than the end time, an error will occur.
- If a zero or invalid clip length is provided, an error will be shown.
- If a clip name is not provided, the program will prompt you to enter a file name.

## Important Notes:
- The program uses `moviepy` for video processing, which may take some time depending on the length of the video and clip length.
- The generated clips will be saved in the "output" folder. Ensure that this folder exists in the same directory as the program or it will need to be created manually.

## Troubleshooting:
- If the program is not responding, make sure you have installed the required dependencies and that there are no conflicting software versions.
- If the clips are not generating correctly, ensure that the input times are in the correct format (HH:MM:SS).

For further assistance or to report bugs, please contact [Your Contact Information or Email].

Enjoy using Reel Maker!
