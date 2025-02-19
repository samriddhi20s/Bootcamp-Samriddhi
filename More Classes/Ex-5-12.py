#Enforcing Interface Implementation: Create an interface using ABC and enforce its implementation in subclasses.
#Example: An interface Streamable with method stream() and subclasses like VideoStream and AudioStream.

from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Streamable(ABC):
    @abstractmethod
    def stream(self):
        """The method that must be implemented by any subclass."""
        pass

# Subclass for Video Streaming
class VideoStream(Streamable):
    def stream(self):
        return "Streaming video content..."

# Subclass for Audio Streaming
class AudioStream(Streamable):
    def stream(self):
        return "Streaming audio content..."

# Testing the classes
video = VideoStream()
audio = AudioStream()

print(video.stream())  # Should print "Streaming video content..."
print(audio.stream())  # Should print "Streaming audio content..."
