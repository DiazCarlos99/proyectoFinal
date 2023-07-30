//contador
const updateCount = (el) => {
    const value = el.dataset.value;
    const increment = Math.ceil(value / 1000);
    let initialValue = 0;
    const increaseCount = setInterval(() => {
    initialValue += increment;
    if (initialValue > value) {
      el.textContent = `${value}+`;
      clearInterval(increaseCount);
      return;
    }
    el.textContent = `${initialValue}+`;
  }, 1);
};

const items = [...document.querySelectorAll('.number')];

items.forEach((item) => {
  updateCount(item);
});

var swiper = new Swiper(".slide-content", {
  slidesPerView: 3,
  spaceBetween: 25,
  loop: true,
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints:{
      0: {
          slidesPerView: 1,
      },
      520: {
          slidesPerView: 2,
      },
      950: {
          slidesPerView: 3,
      },
  },
});

// Obtener el formulario y los campos de correo y mensaje por su id
        const formulario = document.querySelector('#formulario');
        const campoCorreo = document.getElementById('id_email');
        const campoMensaje = document.getElementById('id_mensaje');

        // Agregar un evento de escucha para la presentación del formulario
        formulario.addEventListener('submit', function(event) {
            // Verificar si el campo de correo está vacío o no es un correo válido
            if (campoCorreo.value.trim() === '' || !isValidEmail(campoCorreo.value)) {
                //alert('Por favor, ingrese un correo electrónico válido.');
                showAlert('Por favor, ingrese un correo electrónico válido.');
                e.preventDefault(); // Detener el envío del formulario
                return;
            }

            // Verificar si el campo de mensaje está vacío
            if (campoMensaje.value.trim() === '') {
                //alert('Por favor, ingrese un mensaje.');
                showAlert('Por favor, ingrese un mensaje.');
                event.preventDefault(); // Detener el envío del formulario
                return;
            }
        });

        // Función para verificar si el correo es válido
        function isValidEmail(email) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }

//alert

// Función para cerrar el alert personalizado
// Función para mostrar el alert personalizado
function showAlert(message) {
  const customAlert = document.getElementById('custom-alert');
  const alertMessage = document.getElementById('alert-message');

  alertMessage.textContent = message;
  customAlert.style.display = 'block';
  customAlert.style.zIndex = 10;


  // Ocultar el alert después de unos segundos (opcional)
  setTimeout(function() {
    closeAlert();
  }, 3000); // Cierra el alert después de 3 segundos (puedes ajustar el tiempo según tus necesidades)
}

// Función para cerrar el alert personalizado
function closeAlert() {
  const customAlert = document.getElementById('custom-alert');
  customAlert.style.display = 'none';
}


