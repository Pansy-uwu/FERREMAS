document.addEventListener("DOMContentLoaded", function() {
    const imageSlider = document.getElementById("image-slider");
    const images = imageSlider.getElementsByTagName("img");
    const arrowLeft = document.querySelector(".arrow-left");
    const arrowRight = document.querySelector(".arrow-right");
    let currentIndex = 0;
    let interval;
  
    // Función para mostrar la imagen actual
    const showImage = () => {
      for (let i = 0; i < images.length; i++) {
        images[i].style.display = "none";
      }
      images[currentIndex].style.display = "block";
    };
  
    // Función para avanzar a la siguiente imagen
    const nextImage = () => {
      currentIndex++;
      if (currentIndex >= images.length) {
        currentIndex = 0;
      }
      showImage();
    };
  
    // Función para retroceder a la imagen anterior
    const prevImage = () => {
      currentIndex--;
      if (currentIndex < 0) {
        currentIndex = images.length - 1;
      }
      showImage();
    };
  
    // Evento al hacer clic en la flecha izquierda
    arrowLeft.addEventListener("click", prevImage);
  
    // Evento al hacer clic en la flecha derecha
    arrowRight.addEventListener("click", nextImage);
  
    // Iniciar el carrusel automáticamente cada 4 segundos
    interval = setInterval(nextImage, 4000);
  
    // Detener el carrusel al pasar el cursor sobre el carrusel
    imageSlider.addEventListener("mouseover", function() {
      clearInterval(interval);
    });
  
    // Reanudar el carrusel al retirar el cursor del carrusel
    imageSlider.addEventListener("mouseout", function() {
      interval = setInterval(nextImage, 4000);
    });
  
    // Mostrar la primera imagen al cargar la página
    showImage();
  });