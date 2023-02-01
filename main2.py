from moviepy.editor import *

VIDEO_SRC_REFIX = "./video"
VIDEO_SRC_NAMES = ["/reddit/1.mp4", "/undervideo/sutvideo2.mp4", "/undervideo/sutvideo3.mp4"]
DEST_FOLDER = "./test"
WIDTH = 1080
HEIGHT = 2340
txtclipsize = (1920,100)

clip1 = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[0])
clip2 = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[1]).without_audio()
clip3 = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[2])
intro = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[0]).subclip(0, 4)
txtclip1 = TextClip("Gefällt mir und Abonnement für die Veröffentlichung eines neuen Teils!" ,method='caption' ,size = txtclipsize,fontsize = 60 
, color = 'black' ,bg_color='white' , font="Amiri-Bold")

intro.resize(width = 360, height = 640)

redditdur = clip1.duration
relaxdur = clip2.duration
amount1 = round(clip1.duration / 60)
amount2 = round(clip2.duration / 60)
last = amount1
time = 0
videonumber = 1

while amount1 > 0:
    txtclip_part = TextClip("Teil "+str(videonumber) ,method='caption',size = txtclipsize , fontsize =60 , color = 'black' ,bg_color='white' 
    , font="Amiri-Bold")
 
    if videonumber == 1:
        reddit = clip1.subclip(time, time + 64)

        # reddit.resize(width = 360, height = 640)

        relax =  clip2.subclip(time , time + 64)
        # relax.resize(width = 360, height = 640)
    
        final_clip = clips_array([[txtclip_part],[reddit],[txtclip1], [relax]])
        # final_clip = CompositeVideoClip([final_clip, txtclip1])
        # final_clip.resize(width = 1080, height = 2340)
        final_clip.set_duration(64).write_videofile(DEST_FOLDER + "/video" + str(videonumber) + ".mp4")
        videonumber += 1
        time = time + 60
        amount1 -= 1
        

    elif videonumber == last :

        reddit = clip1.subclip(time, redditdur-12)
        # reddit.resize(width = 360, height = 640)

        
        redditfinal = concatenate_videoclips([intro, reddit])
        
        relax = clip2.subclip(time-3, relaxdur-10)
        # relax.resize(width = 360, height = 640)

        final_clip = clips_array([[txtclip_part],[redditfinal],[txtclip1], [relax]])
        # final_clip = CompositeVideoClip([final_clip, txtclip1])
        # final_clip.resize(width = 1080, height = 2340)
        final_clip.set_duration(64).write_videofile(DEST_FOLDER + "/video" + str(videonumber) + ".mp4")
        videonumber += 1
        time = time + 60
        amount1 -= 1

    else:
        reddit = clip1.subclip(time, time + 60)
        # reddit.resize(width = 360, height = 640)
        relax = clip2.subclip(time, time + 64)

        redditfinal = concatenate_videoclips([intro, reddit])
        
        # relax.resize(width = 360, height = 640)

        # final_clip = clips_array([[redditfinal], [relax]])
        # final_clip.write_videofile(DEST_FOLDER + "/video" + str(videonumber) + ".mp4")
        final_clip = clips_array([[txtclip_part],[redditfinal],[txtclip1], [relax]])
        
        # final_clip.resize(width = 1080, height = 2340)
        final_clip.set_duration(64).write_videofile(DEST_FOLDER + "/video" + str(videonumber) + ".mp4")
        videonumber += 1
        time = time + 60
        amount1 -= 1
