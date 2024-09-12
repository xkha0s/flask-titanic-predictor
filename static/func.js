document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const inputs = document.querySelectorAll("input, select");
    const submitButton = document.querySelector("button");
    
    form.addEventListener("submit", function(event) {
        let valid = true;
        // Reiniciar estilos de errores
        inputs.forEach(input => {
            input.style.borderColor = "#ccc";
        });
        
        // Validación de campos vacíos
        inputs.forEach(input => {
            if (input.value.trim() === "") {
                input.style.borderColor = "red";
                valid = false;
            }
        });
        
        if (!valid) {
            event.preventDefault(); // Prevenir el envío si hay errores
            alert("Por favor, completa todos los campos.");
        }
    });
    
    // Añadir efecto de foco en los inputs
    inputs.forEach(input => {
        input.addEventListener("focus", function() {
            input.style.borderColor = "#4CAF50";
        });
        input.addEventListener("blur", function() {
            input.style.borderColor = "#ccc";
        });
    });
});
