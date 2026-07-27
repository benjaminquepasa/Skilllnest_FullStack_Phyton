document.addEventListener('DOMContentLoaded', () => {
  const themeBtn = document.getElementById('themeBtn');
  const themeIcon = document.getElementById('themeIcon');
  const btnAll = document.getElementById('btnAll');
  const btnFive = document.getElementById('btnFive');
  const cards = document.querySelectorAll('.card');

  // Funcionalidad de cambiar tema (Día / Noche)
  themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
      themeIcon.classList.remove('fa-sun');
      themeIcon.classList.add('fa-moon');
    } else {
      themeIcon.classList.remove('fa-moon');
      themeIcon.classList.add('fa-sun');
    }
  });

  // Mostrar solo 5 Pokémon
  btnFive.addEventListener('click', () => {
    cards.forEach(card => {
      const index = parseInt(card.getAttribute('data-index'));
      card.style.display = index > 5 ? 'none' : 'block';
    });
  });

  // Mostrar Todos
  btnAll.addEventListener('click', () => {
    cards.forEach(card => card.style.display = 'block');
  });
});