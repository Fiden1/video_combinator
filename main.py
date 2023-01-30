from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips

VIDEO_SRC_REFIX = "./src/videos"
VIDEO_SRC_NAMES = ["/1.mp4", "/2.mp4"]
DEST_FOLDER = "./dest"


clip1 = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[0])
clip2 = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[1])

intro = VideoFileClip(VIDEO_SRC_REFIX + VIDEO_SRC_NAMES[0]).subclip(0, 4)

amount1 = clip1.duration / 60
time = 0
videonumber = 1

while amount1 > 0:
    if videonumber != 1:
        reddit = clip1.subclip(time, time + 60)
        redditfinal = concatenate_videoclips([intro, reddit])
        redditfinal.resize(width=540, height=960)

        relax1 = clip2.subclip(time, time + 63.5)
        relax = relax1.without_audio()
        relax.resize(width=540, height=960)

        final_clip = clips_array([[redditfinal], [relax]])

        final_clip.write_videofile(DEST_FOLDER + "/result_" + str(videonumber) + ".mp4")
        videonumber += 1
        time = time + 60
        amount1 -= 1
    else:
        reddit = clip1.subclip(time, time + 60)

        reddit.resize(width=540, height=960)

        relax1 = clip2.subclip(time, time + 63.5)
        relax = relax1.without_audio()
        relax.resize(width=540, height=960)

        final_clip = clips_array([[reddit], [relax]])

        final_clip.write_videofile(DEST_FOLDER + "/result_" + str(videonumber) + ".mp4")
        videonumber += 1
        time = time + 60
        amount1 -= 1
