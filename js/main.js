function consultarWhatsApp(nombreProducto) {
  const telefono = "3855150389"; // WhatsApp Dani Alisados

  const mensaje = `Hola 👋 
Me interesa el producto *${nombreProducto}* y quisiera más información.
¡Gracias!`;

  const url = `https://wa.me/${telefono}?text=${encodeURIComponent(mensaje)}`;
  window.open(url, "_blank");
}
