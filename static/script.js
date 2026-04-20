async function sendMessage() {

    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if (message === "") return;

    let chatBox = document.getElementById("chatBox");

    // User message
    let userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    input.value = "";

    // Bot typing
    let botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.innerText = "Typing...";
    chatBox.appendChild(botDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    let response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    let data = await response.json();

    botDiv.innerText = data.reply;

    chatBox.scrollTop = chatBox.scrollHeight;
}


// ✅ Enter key sends message
document.getElementById("userInput").addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }

});