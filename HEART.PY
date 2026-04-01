import time
import os

heart_frames = [
    """
   **   **
 ****** ******
**************
 ************
  **********
   ********
    ******
     ****
      **
    """,
    """
    ** **
  **********
 ************
 ************
  **********
   ********
    ******
     ****
      **
    """
]

for _ in range(10):  # animation loop
    for frame in heart_frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[91m" + frame + "\033[0m")  # red color
        time.sleep(0.5)