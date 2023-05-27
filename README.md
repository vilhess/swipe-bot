# Swipe Application

This Python script utilizes the DeepFace library to analyze facial expressions and genders in real-time for the Tinder WebApp. It captures screenshots of a specific region on the screen and performs facial analysis on those images. Based on the dominant emotion and gender detected, it simulates keyboard inputs to swipe left or right.

## Prerequisites
- Python 3
- OpenCV (cv2) library
- Pillow (PIL) library
- Keyboard library
- DeepFace library

## Installation

1. Clone the repository or download the script file: `swipe.py`.

2. Install the required libraries using pip:

   `pip install -r requirements.txt`

## Usage

1. Run the Python script by executing the following command:

   ```bash
   python swipe.py
   ```

2. The script will continuously capture screenshots of the specified screen region and analyze the facial expressions and genders of the detected faces.

3. If a face is detected, the script will determine the dominant emotion and gender. If the emotion is "happy" or "neutral" and the gender is "Woman," it will simulate a right swipe by pressing the right arrow key. Otherwise, it will simulate a left swipe by pressing the left arrow key.

4. Press the "Esc" key to stop the script and exit.

## Customization

- Adjust the screen region to capture by modifying the `bbox` parameter in the following line:

  ```python
  image = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(765, 180, 1125, 855))), cv2.COLOR_RGB2BGR)
  ```

  Note: The `bbox` values correspond to the coordinates of the top-left and bottom-right corners of the region to capture. You may need to customize these values based on your screen resolution and the desired region.

- Customize the swiping behavior by modifying the conditions in the following line:

  ```python
  if emotion in ['happy', 'neutral'] and sex == "Woman":
      keyboard.press_and_release('right')
  else:
      keyboard.press_and_release('left')
  ```

  You can change the emotions, genders, and key inputs according to your preferences.
  For additional conditions and functionalities, refer to the DeepFace library documentation.

## Notes

- The script requires an active internet connection for the DeepFace library to perform facial analysis.

- In case a face is not detected, the script will simulate a left swipe by default.

- Please use this script responsibly and adhere to the terms and conditions of the platform you are swiping on.
