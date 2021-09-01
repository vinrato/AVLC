from vlc import EventType


class AvlcEvent(object):
    def __init__(self):
        super(AvlcEvent, self).__init__()
        self.callback_fn = lambda: None

    def call(self):
        self.callback_fn()

    def set_callback(self, callback_fn):
        self.callback_fn = callback_fn


class AudioPlayerEvent(object):
    # internally used native vlc events is reserved but still can be utilized under other event name
    InternalTrackEndReached = EventType(265)

    # native vlc events
    Playing = EventType(260)
    Paused = EventType(261)
    Stopped = EventType(262)
    Error = EventType(266)
    VolumeChanged = EventType(283)

    # avlc custom events. can be called internally or externally
    TrackEndReached = AvlcEvent()
    PlaylistEndReached = AvlcEvent()
    NextTrack = AvlcEvent()
    PrevTrack = AvlcEvent()
    MediaAdded = AvlcEvent()
