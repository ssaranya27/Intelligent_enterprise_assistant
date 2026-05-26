async function sendMessage() {

    const input = document.getElementById("user-input");

    const message = input.value;

    if(message.trim() === "") return;

    const chatBox = document.querySelector(".chat-box");

    // USER MESSAGE

    chatBox.innerHTML += `

        <div class="user-message">

            ${message}

        </div>

    `;

    input.value = "";

    // TYPING

    chatBox.innerHTML += `

        <div class="bot-message typing">

            AI is typing...

        </div>

    `;

    const response = await fetch("/chat", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    document.querySelector(".typing").remove();

    // AI RESPONSE

    chatBox.innerHTML += `

        <div class="bot-message">

            ${data.response}

        </div>

    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}