function detect() {
    const detectElement = document.getElementById("detect");
    if (!detectElement) {
      console.error("Could not find element with id 'detect'");
      return;
    }
    detectElement.value = "Hang on...";
  
    const { spawn } = require("child_process");
  
    const pythonProcess = spawn("python", [
      "yolov5/detect.py"
    ]);
  
    // Notify the user that the script is starting to run
    pythonProcess.on("spawn", () => {
      alert("Detection Started");
      detectElement.value = "Running...";
    });
  
    // Notify the user about any messages printed by the script
    pythonProcess.stdout.on("data", (data) => {
      console.log(`Received message from script: ${data}`);
      alert(data);
    });
  
    // Notify the user if the script encounters an error
    pythonProcess.on("error", (err) => {
      console.error(`Script encountered an error: ${err}`);
      alert(`Error: ${err}`);
    });
  
    // Notify the user when the script has finished running
    pythonProcess.on("close", (code, signal) => {
      console.log(`Script exited with code ${code} and signal ${signal}`);
      detectElement.value = "Detect";
      alert("Script finished running.");
    });
  }
  