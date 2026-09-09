const chatMessages = document.getElementById("chatMessages");
const chatInput = document.getElementById("chatInput");
const chatForm = document.getElementById("chatForm");

async function sendQuestion(question) {
    const cleanQuestion = question.trim();

    if (cleanQuestion === "") {
        return;
    }

    // Show user's message
    addMessage(cleanQuestion, "user");

    // Clear input
    chatInput.value = "";

    // Disable input while waiting
    chatInput.disabled = true;

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: cleanQuestion
            })
        });

        const data = await response.json();

        if (response.ok) {
            addMessage(data.reply, "bot");
        } else {
            addMessage(
                data.reply || "Sorry, something went wrong.",
                "bot"
            );
        }

    } catch (error) {
        console.error("Chat error:", error);

        addMessage(
            "Sorry, I could not connect to the BioPattern server.",
            "bot"
        );
    }

    // Enable input again
    chatInput.disabled = false;
    chatInput.focus();
}


function addMessage(text, sender) {
    const message = document.createElement("div");

    message.classList.add("message", sender);

    if (sender === "bot") {
        const avatar = document.createElement("span");

        avatar.classList.add("avatar");
        avatar.textContent = "⌁";

        message.appendChild(avatar);
    }

    const paragraph = document.createElement("p");

    paragraph.textContent = text;

    message.appendChild(paragraph);

    chatMessages.appendChild(message);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


// Send button
chatForm.addEventListener("submit", function (event) {
    event.preventDefault();

    sendQuestion(chatInput.value);
});


// Suggested question buttons
document.querySelectorAll(".prompt-chip").forEach(function (button) {

    button.addEventListener("click", function () {

        sendQuestion(button.textContent);

    });

});