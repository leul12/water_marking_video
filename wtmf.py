import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp


def choose_video_file():
    video_file_path = filedialog.askopenfilename(
        initialdir="/", title="Select Video", filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*")))
    video_file_label.config(text=video_file_path)
    return video_file_path


def choose_text_file():
    text_file_path = filedialog.askopenfilename(
        initialdir="/", title="Select Text File", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    with open(text_file_path, 'r') as file:
        watermark_text = file.readline()
    text_file_label.config(text=watermark_text)
    return watermark_text


def convert():
    video_file_path = video_file_label.cget("text")
    watermark_text = text_file_label.cget("text")
    position = position_var.get().lower()
    video = mp.VideoFileClip(video_file_path)

    # Create the text clip
    text_clip = mp.TextClip(watermark_text, font='Arial',
                            fontsize=30, color='white')

    # Position the text clip
    if position == 'bottom':
        text_clip = text_clip.set_pos('bottom')
    elif position == 'top':
        text_clip = text_clip.set_pos('top')
    elif position == 'left':
        text_clip = text_clip.set_pos('left')
    elif position == 'right':
        text_clip = text_clip.set_pos('right')
    elif position == 'upper right corner':
        text_clip = text_clip.set_pos((100, 200))

    text_clip = text_clip.set_duration(video.duration)

    # Overlay the text clip on the video
    final_video = mp.CompositeVideoClip([video, text_clip])

    # Save the final video
    final_video.write_videofile("output.mp4")

root = tk.Tk()
root.geometry("360x720")
root.config(bg='black')
root.title("Watermarker")

video_file_label = tk.Label(root, text='', bg='black', fg='white')
video_file_button = tk.Button(
    root, text='Choose Video', command=choose_video_file)

text_file_label = tk.Label(root, text='', bg='black', fg='white')
text_file_button = tk.Button(
    root, text='Choose Text', command=choose_text_file)

position_var = tk.StringVar(root)
position_var.set("Upper Right Corner")
position_dropdown = tk.OptionMenu(
    root, position_var, "Upper Right Corner", "Bottom", "Top", "Left", "Right")


convert_button = tk.Button(root, text='Convert', command=convert)

video_file_label.pack()
video_file_button.pack()
text_file_label.pack()
text_file_button.pack()
position_dropdown.pack()
convert_button.pack()

root.mainloop()
