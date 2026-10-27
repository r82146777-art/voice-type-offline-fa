# Requested changes for the supplied APK

This checklist is tied to the uploaded APK, not an older Vosk repository.

## Recognition / duplicate speech
- Inspect the real recording and recognition lifecycle before changing it.
- Prevent recognition from capturing the screen reader's own TTS output where possible: pause capture during app TTS, use a short post-TTS guard interval, and avoid reinserting recognized text that duplicates the last committed segment.
- Keep partial recognition separate from final recognition so partial words are not repeatedly committed.
- Inspect and tune the existing Silero VAD configuration and the existing int8 ONNX model before swapping models.

## Keyboard switching
- Preserve Android's system input-method picker rather than hard-coding Gboard or Samsung Keyboard.
- Provide an accessible action that opens the system input-method picker, and a separate action that opens Android input-method settings so the user can enable this keyboard or switch back.

## Read aloud / clipboard
- Add a clipboard read-aloud action that first checks clipboard availability and announces a clear accessible status.
- Provide a separate screen to paste/type text and read it aloud; PDF support should extract selectable text and explain when a PDF is image-only.
- A bundled offline Persian/English TTS engine requires an actual compatible voice model. Do not label Android's built-in TTS as a bundled engine.

## Accessibility and validation
- Label controls for TalkBack, provide meaningful state announcements, and ensure keyboard actions are reachable without sight.
- Test Persian and English separately, test TalkBack enabled and disabled, and verify duplicate text behavior.
- Build and verify the APK before publishing a download link.

## Current blocker
The available source ZIP is incomplete for rebuilding: it does not include the ASR model assets found in the original APK and is not a Gradle project. The original app's core behavior must be recovered from the APK's native/Unity payload before safe code-level changes can be made.