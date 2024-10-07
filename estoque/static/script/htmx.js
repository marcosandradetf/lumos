function updateMessages(event) {
        // Atualiza o conteúdo das mensagens diretamente a partir da resposta
        document.getElementById('messages-container').innerHTML = event.detail.xhr.responseText.split('<div id="messages-container">')[1];
    }