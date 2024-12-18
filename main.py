from tkinter import*
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from moviepy import VideoFileClip
from datetime import datetime, timedelta
import threading

win = Tk()
tcl=[]
rcl=[]
fpl=[]

def display(messagee):
    view.configure(state=NORMAL)
    view.insert(END,messagee)
    view.configure(state=DISABLED)

def gen_clip_thread():
    global tcl, rcl, fpl
    cf_val=cfentry.get()
    if len(cf_val)!=0 and cf_val!=" ":
        st="00:00:00"
        ed=stentry.get()

        t1=time_difference_in_seconds(st,ed)

        st1="00:00:00"
        ed1=etentry.get()
        ct_val=float(ctentry.get())
        
        t2=time_difference_in_seconds(st1, ed1)
        
        display("Clip generation has started!\n")
        
        for i in range(1,int(tcl[-1])+1):
            video = VideoFileClip(fpl[-1])
            trimmed_video = video.subclipped(t1, t1+ct_val)
            out_path=f"output\\{cf_val}({i}).mp4"
            print(out_path)
            trimmed_video.write_videofile(out_path)
            gen_info=f"Generated Video: {out_path}\n"
            display(gen_info)
            t1=t1+ct_val
        
        if rcl[-1]==float(0):
            pass
        else:
            video = VideoFileClip(fpl[-1])
            trimmed_video = video.subclipped(t1, t1+rcl[-1])
            out_path=f"output\\{cf_val}(last).mp4"
            trimmed_video.write_videofile(out_path)
            view.configure(state=NORMAL)
            gen_info=f"Generated Video: {out_path}\n"
            view.insert(END,gen_info)
            view.configure(state=DISABLED)
            display("All clips generated!\n")
    else:
        messagebox.showerror('File name Error','You must enter the file name of the clip!')

def gen_clip():
    # This is the function that runs when you click the button to generate clips
    threading.Thread(target=gen_clip_thread, daemon=True).start()

def time_difference_in_seconds(time1, time2):
    try:
        # Define the time format
        time_format = "%H:%M:%S"

        # Convert the strings to datetime objects
        t1 = datetime.strptime(time1, time_format)
        t2 = datetime.strptime(time2, time_format)

        # If time2 is earlier than time1, add 24 hours to time2
        if t2 < t1:
            messagebox.showerror('Timing Error', 'Please enter correct time format[hh:mm:ss]')
        else:
        # Calculate the difference in seconds
            delta = t2 - t1
            total_seconds = delta.total_seconds()

            return total_seconds
    except ValueError:
        messagebox.showerror('Value Error','Given Wrong Value somewhere!')
    
    
    
def count_clip():
    global tcl, rcl
    try:
        time1 = stentry.get()
        time2 = etentry.get()
        t=time_difference_in_seconds(time1, time2)
        if t!=None:
            try:
                ct_val=float(ctentry.get())
                total_clips=t//ct_val
                remain_clip=t%ct_val
                tcl.append(total_clips)
                rcl.append(remain_clip)

                view_message=f"You have {total_clips} clips of {ct_val} seconds,\nOne clip of {remain_clip} seconds\n"
                view.configure(state=NORMAL)
                view.insert(END,view_message)
                view.configure(state=DISABLED)
                cc_vid.place_forget()
                cc_vid1.place(relx=0.5,rely=0.74,anchor='center')

            except ZeroDivisionError:
                messagebox.showerror('Clip length error','You cannot have length of the \n clip 0 seconds')
    except ValueError:
        messagebox.showerror('Value Error','Given Wrong Value somewhere!')

    
def get_video_details(file_path):
    # Get the file size
    file_size = os.path.getsize(file_path)

    # Get video details using moviepy
    with VideoFileClip(file_path) as video:
        resolution = video.size  # resolution is a tuple (width, height)
        duration = video.duration  # duration in seconds
        fps = video.fps  # frames per second
        total_frames = int(fps * duration)  # total frames = fps * duration

    # Convert size to MB
    file_size_mb = file_size / (1024 * 1024)

    # Prepare the results
    details = {
        "size": round(file_size_mb, 2),  # in MB
        "resolution": resolution,
        "duration": round(duration, 2),  # in seconds
        "total_frames": total_frames
    }

    return details

def get_vid():
    global fpl
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    _, extension = os.path.splitext(file_path)
    fpl.append(file_path)

    if extension=='.mp4':
        os.startfile(file_path)
        video_details = get_video_details(file_path)
        pth=f"File Path:{file_path}"
        frmt=f"Format:{extension}"
        fs=f"File Size: {video_details['size']} MB"
        res=f"Resolution: {video_details['resolution'][0]}x{video_details['resolution'][1]}"
        dur=f"Duration: {video_details['duration']} seconds"
        frm=f"Total Frames: {video_details['total_frames']}"
        data=f'''
    {pth}
    {frmt}
    {fs}
    {res}
    {dur}
    {frm}\n
        '''
        view.configure(state=NORMAL)
        view.insert(END,data)
        view.configure(state=DISABLED)
    else:
        messagebox.showerror('Format Error','The format of the video should be mp4!')

win.title('Reel Maker')
win.geometry("900x450")
win.iconbitmap("Assets\\video.ico")
frame=Frame(win,bg='#e5e8e8')
frame.propagate(False)
frame.pack(fill='both',expand=True)

upload_vid=Button(frame,text="Upload Video", font=('Cascadia Code',16), bg='#f4d03f',
                         fg="#17202a",height=1,cursor='hand2',relief='raised',bd=3,command=get_vid)
upload_vid.place(relx=0.5,rely=0.09,anchor='center')

opt_frm=ctk.CTkFrame(frame,fg_color='#e5e8e8',height=300,width=500,border_color='#1abc9c',border_width=3)
opt_frm.propagate(False)
opt_frm.pack(side='left',anchor='n',padx=10,pady=(90,0))

start_time=LabelFrame(opt_frm,text='Start Time(HH:MM:SS)', font=('Cascadia Code',10), height=50, width=200,
                      fg='#5b2c6f', bg='#e5e8e8' )
start_time.propagate(False)
start_time.pack(side=LEFT, anchor='n', padx=10, pady=10)

end_time=LabelFrame(opt_frm,text='End Time(HH:MM:SS)', font=('Cascadia Code',10), height=50, width=200, fg='#5b2c6f',
                     bg='#e5e8e8')
end_time.propagate(False)
end_time.pack(side=RIGHT, anchor='n', padx=10, pady=10)

stentry=StringVar()
start_time_entry=Entry(start_time,width=23, font=('Calibri (Body)',12), bg='#e5e8e8',relief='flat', textvariable=stentry)
start_time_entry.pack()

etentry=StringVar()
end_time_entry=Entry(end_time,width=23, font=('Calibri (Body)',12), bg='#e5e8e8',relief='flat', textvariable=etentry)
end_time_entry.pack()

clip_time=LabelFrame(opt_frm,text='Clip Length(in Seconds)', font=('Cascadia Code',10), height=50, width=200, fg='#5b2c6f',
                 bg='#e5e8e8')
clip_time.propagate(False)
clip_time.place(relx=0.5, rely=0.37, anchor='center')

ctentry=StringVar()
clip_time_entry=Entry(clip_time,width=23, font=('Calibri (Body)',12), bg='#e5e8e8',relief='flat', textvariable=ctentry)
clip_time_entry.pack()

clip_file=LabelFrame(opt_frm,text='Clip Name', font=('Cascadia Code',10), height=50, width=200, fg='#5b2c6f',
                     bg='#e5e8e8')
clip_file.propagate(False)
clip_file.place(relx=0.5, rely=0.56, anchor='center')

cfentry=StringVar()
clip_file_entry=Entry(clip_file,width=23, font=('Calibri (Body)',12), bg='#e5e8e8',relief='flat', textvariable=cfentry)
clip_file_entry.pack()

cc_vid=ctk.CTkButton(opt_frm,text="Count Clips", font=('Cascadia Code',17), fg_color='#5b2c6f',
                         text_color="#f4f6f7",height=40, width=100, cursor='hand2', command=count_clip)
cc_vid.place(relx=0.5,rely=0.74,anchor='center')

cc_vid1=ctk.CTkButton(opt_frm,text="Generate Clips", font=('Cascadia Code',17), fg_color='#5b2c6f',
                         text_color="#f4f6f7",height=40, width=100, cursor='hand2',command=gen_clip)

reset_vid=ctk.CTkButton(opt_frm,text="Reset", font=('Cascadia Code',17), fg_color='#c0392b',
                         text_color="#f4f6f7",height=40, width=100, cursor='hand2', hover_color='#e74c3c')
reset_vid.place(relx=0.5,rely=0.9,anchor='center')

info_frm=ctk.CTkFrame(frame,fg_color='#e5e8e8',height=300,width=400,border_color='#34495e',border_width=3)
info_frm.propagate(False)
info_frm.pack(side='left',anchor='n',padx=(0,10),pady=(90,0))

view=ctk.CTkTextbox(info_frm,scrollbar_button_color='#8e44ad',state=DISABLED,font=('Calibri (Body)',12), text_color='#8e44ad')
view.pack(fill='both',expand=True, padx=10,pady=10)

win.mainloop()