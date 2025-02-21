#Enforcing Interface Implementation: Create an interface using ABC and enforce its implementation in subclasses.
#Example: An interface Streamable with method stream() and subclasses like VideoStream and AudioStream.

from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Streamable(ABC):
    @abstractmethod
    def stream(self):
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

print(video.stream()) 
print(audio.stream())  
