function showFlashMessages() {
    const flashMessages = JSON.parse(document.getElementById('flash-messages').textContent);

    if (flashMessages && flashMessages.lenght > 0) {
        flashMessages.forEach(({ category, message }) => {
            Swal.fire({
                title: category.toUpperCase(),
                text: message,
                icon: category, // icon: category === 'success' ? 'success' : 'error', 
                confirmButtonText: 'OK' 
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', showFlashMessages);