document.addEventListener('DOMContentLoaded', function() {
    const botonBorrar = document.getElementById('borrar');

    if (botonBorrar) {
        botonBorrar.addEventListener('click', function() {
            document.getElementById('nombre').value = '';
            document.getElementById('mensaje').value = '';
            // Limpiar los resultados mostrados
            document.getElementById('resultado-nombre').textContent = '';
            document.getElementById('resultado-mensaje').textContent = '';
        });
    } else {
        console.error('El botón "Borrar" no se encontró en el DOM.');
    }
});