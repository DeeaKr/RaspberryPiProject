# Play a song when you enter the room
## Overview
This project will detect when you enter a room  (or when you open the fridge) via a magnetic reed switch and will play a song to the speakers connected to the raspberry pi. In my project I didn't fix the magentic reed switch anywhere but you can fix it to the fridge and when you open it, the raspberry will play the song "Oops I did it again" and maybe it will remind you that you "did it again".



## Demo 
The projects works as follows:
<ul>
  <li> First you run the projectGood.py file with `python projectGood.py`  </li>
  <li> After that the magnetic reed switch is not yet activated, for that you have to push the button near the led </li>
  
  ![giphy](https://user-images.githubusercontent.com/61203639/115377420-46eee000-a1d8-11eb-8400-4088eeef6544.gif)

  <li> The led starts flashing and after 5 seconds it stops and stays on so you will know that it is active. </li>
  <li> You open the magnetic reed switch(or open the door of the room or of the fridge) and the song will start playing </li>
  
  ![giphyMagnetic](https://user-images.githubusercontent.com/61203639/115379072-db0d7700-a1d9-11eb-9cc8-35d938c4d4bd.gif)




  ![DSC_0713](https://user-images.githubusercontent.com/61203639/115377988-cb416300-a1d8-11eb-8481-114893983734.JPG)

  <li> You can stop the song whenever you want by pushing the other button, the one close to the magnetic reed switch and the light of the led will also be turned off</li>
  
  ![giphyStop](https://user-images.githubusercontent.com/61203639/115379730-7868ab00-a1da-11eb-83f0-6acb8e43b728.gif)


  
  
</ul>Play the demo with sound!


https://user-images.githubusercontent.com/61203639/115552778-5728bd00-a2b5-11eb-902c-5d56c258c4fb.mp4



https://user-images.githubusercontent.com/61203639/115377704-8a494e80-a1d8-11eb-9fd7-85631066b4f9.mp4

### Some pictures
![DSC_0700](https://user-images.githubusercontent.com/61203639/115378481-43a82400-a1d9-11eb-8962-3809076f4118.JPG)
![DSC_0720](https://user-images.githubusercontent.com/61203639/115378513-4b67c880-a1d9-11eb-9c8a-a1ffb113d088.JPG)
![DSC_0702](https://user-images.githubusercontent.com/61203639/115378531-502c7c80-a1d9-11eb-95d8-8bd9a3ba910b.JPG)

## Schema

![FritzingSchema](https://user-images.githubusercontent.com/61203639/115379805-8caca800-a1da-11eb-983a-a37727ab0d92.png)

## Pre-requisites

<ul>
  <li> A Raspberry Pi any model (I used a Raspberry Pi 4)  </li>
  <li> Resistors : 
    <ul>
      <li> 220 ohm x1 </li>
      <li> 1k ohm x1 </li>
      <li> 10k ohm x3 </li>
    </ul>
  </li>
  <li> One magnetic reed switch </li>
  <li> One led </li>
  <li> Push-button switch x2 </li>
  <li> One breadboard with 830 points </li>
  <li> Hook-up cables (male to female wires) </li>
  <li> Jumper wires (male to male wires)</li>
  <li> Computer speaker </li>
</ul>

## Setup and run

1. First you will need a micro SD which needs to be bootable. For flashing the micro SD you can use balenaEtcher https://www.balena.io/etcher/.
2. Configure your raspberry pi such that you can use it remotely. First you will need a screen, a mouse and a keyboard. After you inserted the micro sd card in the raspberry pi and plugged it in you should follow the steps you see on your screen. Then enable the `ssh` and the `vnc` from raspi-config. Install also VNC viewer on your laptop or computer and enter the ip from your raspberry pi.
3. Now you should connect the buttons, wires, the led and the magnetic reed switch as you see in the schema above(`unplug your raspberry pi first`).
4. Now plug your raspberry pi in a power source.
5. Make sure you have pyhton3 installed. If you don't, then install it via `sudo apt install python3`.
6. Clone the repository and now you have to download a song (I downloaded the song by converting the youtube video to an mp3 via youtube converter) and then place it in the `\home\pi` folder. After that in the function `watchDoor()` you should change from `"Oops-crop.mp3"` to the name of your mp3 file and save the python file.
7. Run the `projectGood.py` file with `python projectGood.py` in your terminal.
8. If you are not sure of how to use the app you should see the `Demo` part.

  








