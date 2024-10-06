document.querySelectorAll('[data-dismiss-target]').forEach(function (button) {
    button.addEventListener('click', function () {
        const target = document.getElementById(button.getAttribute('data-dismiss-target').replace('#', ''));
        if (target) {
            target.style.display = 'none';  // Ou target.remove(); para remover completamente
        }
    });
});

setTimeout(function () {
    document.querySelectorAll('[id^="alert-border-"]').forEach(function (alert) {
        alert.style.display = 'none';  // Esconde automaticamente após um tempo
    });
}, 60000);  // 5000 milissegundos = 5 segundos
