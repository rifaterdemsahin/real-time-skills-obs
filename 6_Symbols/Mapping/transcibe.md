Sure! Below is a simple C# .NET program that uses the Windows API to capture microphone input and write it to a text file. This example uses the `System.Speech` namespace for speech recognition.

1. **Create a new Console Application** in Visual Studio.

2. **Add a reference** to `System.Speech`:
   - Right-click on your project in Solution Explorer.
   - Select **Add** > **Reference**.
   - Check **System.Speech** and click **OK**.

3. **Write the following code** in your `Program.cs` file:

```csharp
using System;
using System.IO;
using System.Speech.Recognition;

namespace MicToTextFile
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a new SpeechRecognitionEngine instance.
            SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine();

            // Configure the input to the recognizer.
            recognizer.SetInputToDefaultAudioDevice();

            // Create and load a grammar.
            recognizer.LoadGrammar(new DictationGrammar());

            // Attach event handlers.
            recognizer.SpeechRecognized += new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);

            // Start asynchronous, continuous speech recognition.
            recognizer.RecognizeAsync(RecognizeMode.Multiple);

            // Keep the console window open.
            Console.WriteLine("Speak into your microphone.");
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        static void recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            // Write the recognized text to a file.
            string text = e.Result.Text;
            File.AppendAllText("transcription.txt", text + Environment.NewLine);
            Console.WriteLine("Recognized: " + text);
        }
    }
}
```

This program sets up a speech recognizer that listens to the default audio device (usually the microphone), recognizes spoken words, and writes them to a file named `transcription.txt`.

### Steps to Run the Program:
1. **Build and run the application** in Visual Studio.
2. **Speak into your microphone**. The recognized text will be appended to `transcription.txt` in the application's directory.

Would you like any further customization or details on this program?