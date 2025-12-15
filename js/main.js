function consultarWhatsApp(producto) {
  const telefono = "5493855150389"; // CAMBIÁ SI HACE FALTA
  const mensaje = `Hola! Me interesa el producto: ${producto}. Quisiera más información.`;
  const url = `https://wa.me/${telefono}?text=${encodeURIComponent(mensaje)}`;
  window.open(url, "_blank");
}

// Animaciones al scroll
const elementos = document.querySelectorAll(".fade-up");

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    }
  });
});

elementos.forEach(el => observer.observe(el));
