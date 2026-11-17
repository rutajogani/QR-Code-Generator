const createQR = async () => {
    const urlInput = document.getElementById("url-input").value;
    const imgElement = document.getElementById("python-output");

    if (!urlInput) {
        alert("Please enter a valid URL!");
        return;
    }

    try {
        const response = await fetch(`http://localhost:8000/generate?url=${encodeURIComponent(urlInput)}`);
        
        if (!response.ok) {
            throw new Error("Failed to generate QR code");
        }

        const blob = await response.blob();
        imgElement.src = URL.createObjectURL(blob);
    } catch (error) {
        console.error("Error:", error);
        alert("Could not connect to the Python server.");
    }
};
