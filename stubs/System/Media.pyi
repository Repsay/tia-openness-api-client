# encoding: utf-8
# module System.Media calls itself Media
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class SoundPlayer(Component, ISerializable):  # skipped bases: <type 'IComponent'>, <type 'IDisposable'>
    """
    Controls playback of a sound from a .wav file.

    SoundPlayer()

    SoundPlayer(soundLocation: str)

    SoundPlayer(stream: Stream)
    """

    def Load(self):
        """
        Load(self: SoundPlayer)

            Loads a sound synchronously.
        """
        ...
    def LoadAsync(self):
        """
        LoadAsync(self: SoundPlayer)

            Loads a .wav file from a stream or a Web resource using a new thread.
        """
        ...
    def OnLoadCompleted(self, *args):  # cannot find CLR method
        """
        OnLoadCompleted(self: SoundPlayer, e: AsyncCompletedEventArgs)

            Raises the System.Media.SoundPlayer.LoadCompleted event.

            e: An System.ComponentModel.AsyncCompletedEventArgs  that contains the event data.
        """
        ...
    def OnSoundLocationChanged(self, *args):  # cannot find CLR method
        """
        OnSoundLocationChanged(self: SoundPlayer, e: EventArgs)

            Raises the System.Media.SoundPlayer.SoundLocationChanged event.

            e: An System.EventArgs that contains the event data.
        """
        ...
    def OnStreamChanged(self, *args):  # cannot find CLR method
        """
        OnStreamChanged(self: SoundPlayer, e: EventArgs)

            Raises the System.Media.SoundPlayer.StreamChanged event.

            e: An System.EventArgs that contains the event data.
        """
        ...
    def Play(self):
        """
        Play(self: SoundPlayer)

            Plays the .wav file using a new thread, and loads the .wav file first if it has not been loaded.
        """
        ...
    def PlayLooping(self):
        """
        PlayLooping(self: SoundPlayer)

            Plays and loops the .wav file using a new thread, and loads the .wav file first if it has not been loaded.
        """
        ...
    def PlaySync(self):
        """
        PlaySync(self: SoundPlayer)

            Plays the .wav file and loads the .wav file first if it has not been loaded.
        """
        ...
    def Stop(self):
        """
        Stop(self: SoundPlayer)

            Stops playback of the sound if playback is occurring.
        """
        ...
    @staticmethod  # known case of __new__
    def __new__(cls, *__args):
        """
        __new__(cls: type)

        __new__(cls: type, soundLocation: str)

        __new__(cls: type, stream: Stream)

        __new__(cls: type, serializationInfo: SerializationInfo, context: StreamingContext)
        """
        ...
    def __reduce_ex__(self, *args): ...
    @property
    def CanRaiseEvents(self):
        """Gets a value indicating whether the component can raise an event."""
        ...
    @property
    def DesignMode(self):
        """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode."""
        ...
    @property
    def Events(self):
        """Gets the list of event handlers that are attached to this System.ComponentModel.Component."""
        ...
    @property
    def IsLoadCompleted(self):
        """
        Gets a value indicating whether loading of a .wav file has successfully completed.

        Get: IsLoadCompleted(self: SoundPlayer) -> bool
        """
        ...
    @property
    def LoadTimeout(self):
        """
        Gets or sets the time, in milliseconds, in which the .wav file must load.

        Get: LoadTimeout(self: SoundPlayer) -> int

        Set: LoadTimeout(self: SoundPlayer) = value
        """
        ...
    @property
    def SoundLocation(self):
        """
        Gets or sets the file path or URL of the .wav file to load.

        Get: SoundLocation(self: SoundPlayer) -> str

        Set: SoundLocation(self: SoundPlayer) = value
        """
        ...
    @property
    def Stream(self):
        """
        Gets or sets the System.IO.Stream from which to load the .wav file.

        Get: Stream(self: SoundPlayer) -> Stream

        Set: Stream(self: SoundPlayer) = value
        """
        ...
    @property
    def Tag(self):
        """
        Gets or sets the System.Object that contains data about the System.Media.SoundPlayer.

        Get: Tag(self: SoundPlayer) -> object

        Set: Tag(self: SoundPlayer) = value
        """
        ...
    LoadCompleted = None
    SoundLocationChanged = None
    StreamChanged = None

class SystemSound:  # skipped bases: <type 'object'>
    """Represents a system sound type."""

    def Play(self):
        """
        Play(self: SystemSound)

            Plays the system sound type.
        """
        ...

class SystemSounds:  # skipped bases: <type 'object'>
    """Retrieves sounds associated with a set of Windows operating system sound-event types. This class cannot be inherited."""

    Asterisk = None
    Beep = None
    Exclamation = None
    Hand = None
    Question = None
