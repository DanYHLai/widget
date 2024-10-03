# YouTube Watch Later Batch Removal
This script automatically removes videos from YouTube's "Watch Later" playlist by simulating mouse clicks. The script uses the PyAutoGUI library to interact with the YouTube interface.

## Features

- Automatically click the three-dot menu of each video.
- Select the "Remove from Watch Later" option.
- Repeats the process for a specified number of videos.

## Requirements

- Python 3.x
- PyAutoGUI

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/DanYHLai/youtube-watch-later-bulk-remove.git
   ```

2. Navigate to the project directory:
   ```bash
   cd youtube-watch-later-bulk-remove
   ```

3. Install the required Python libraries:
   ```bash
   pip install pyautogui
   ```

## Usage

1. Open YouTube in your browser and navigate to the "Watch Later" playlist.
2. Run the Python script.
   ```bash
   python remove_videos.py
   ```
3. The script will remove videos based on your coordinates. Ensure you have already adjusted the coordinates within the script to match your screen resolution and YouTube layout.

4. You can change the number of videos to remove by modifying the `repeat_times` parameter in the script:
   ```python
   remove_video_from_watch_later(10)  # Change 10 to the number of videos you want to remove
   ```

### Finding Mouse Coordinates

You can find the coordinates of different elements (such as the three-dot menu and the remove button) by running the following script. It will give you 5 seconds to move the mouse to the desired position, and then it will print the coordinates.

```python
import pyautogui
import time

print("Move the mouse to the target position within 5 seconds...")
time.sleep(5)
print(f"Current mouse position: {pyautogui.position()}")
```

### Example Configuration

You will need to adjust the `x` and `y` values in the main script for the following steps:

- Clicking the three-dot menu
- Hovering over the "Remove from Watch Later" option

## Disclaimer

This script simulates human interactions with the YouTube interface. Use responsibly and ensure it complies with YouTube's terms of service. Misuse of automation scripts may result in your account being restricted.
