from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor as ed

class ShortVideoMaker:
    """ShortVideoMaker constructor. Makes clips based on input data.
    @param full_video: VideoFileClip object of full video file
    @param subtitles: dictionary (?) representing subtitles with timestamps
    @param timestamps: list of integer timestamps in seconds to begin clips
    @param name: output file name prefix"""
    def __init__(self, full_video, subtitles, timestamps, name):
        self.video = full_video
        self.subtitles = subtitles
        self.timestamps = timestamps
        self.name = name # add file extension ?
        self.clips = [] # consider making different because we know size

    """Makes clips based on self.full_video, self.subtitles, and self.timestamps
    Stores them in self.clips"""
    def make_clips(self):
        for timestamp in self.timestamps:
            # validate ranges later
            clip = self.video.subclip(timestamp, timestamp+60)

            # dynamically generate text to put
            text_box = (ed.TextClip("House",fontsize=70,color='white')
                        .set_position('center')
                        .set_duration(10))

            # composite text <-- this will be more complicated later with many texts at different timestamps
            clip = ed.CompositeVideoClip([clip, text_box])
            # TODO: add music

            # finally, add clip to self.clips
            self.clips.append(clip)
    
    """Writes self.clips to artifacts directory
    @return list of clip file names"""
    def write_clips(self):
        names = []
        for i, clip in enumerate(self.clips):
            # could add variables for args
            clip_name = f"{self.name}_{i}"
            names.append(clip_name)
            clip.write_videofile(f"artifacts/{clip_name}.mp4", codec="libx264")
        return names


def main():
    video_file = "inputs/House-1x01-Pilot.mkv"
    timestamps = [120, 300]
    generator = ShortVideoMaker(VideoFileClip(video_file), {}, timestamps, "house_0x01")
    generator.make_clips()
    generator.write_clips()

if __name__ == "__main__":
    main()