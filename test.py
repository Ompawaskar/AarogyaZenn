import os
import yogadata
from elevenlabs import save
from elevenlabs import stream
from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="e17b2961a5a3c736f403281f86a27652", # Defaults to ELEVEN_API_KEY
)

for item in yogadata.data[30:]:
  filename = str(item["id"]) + ".mp3"
  path = os.getcwd()
  p = os.path.join(path,"audios",filename)


  audio = client.generate(
    text=item["pose_description"],
    voice="Emily",
    model="eleven_multilingual_v2"
    )

  save(audio,p)
  

