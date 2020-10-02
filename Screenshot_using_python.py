import pyscreenshot as ImageGrab
# fullscreen
im=ImageGrab.grab()
im.show()

# part of the screen
im=ImageGrab.grab(bbox=(10,10,500,500))
im.show()

# asking the file to save the image in
file = input("by what name do you want to save the image?/n")

# to file
ImageGrab.grab_to_file(file)
