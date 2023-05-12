import ffmpeg
import os 
import tk
import easygui
def encode(file_in,file_out):
    if os.path.splitext(input_file)[1] != ".mp4":
        ffmpeg.input(input_file).output(output_file).run()
        print("File successfully converted to .mp4")
    else:
        print("File is already in .mp4 format")



input_file = easygui.fileopenbox()
print("Selected file:", input_file)
output_file = "output_file.mp4"
encode(input_file,output_file)
