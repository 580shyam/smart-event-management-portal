(() => {
  const carousel = document.querySelector('[data-hero-carousel]');
  if (!carousel) return;

  const slides = Array.from(carousel.querySelectorAll('[data-hero-slide]'));
  const dots = Array.from(document.querySelectorAll('[data-hero-dot]'));
  const currentLabel = document.querySelector('[data-hero-current]');
  const previous = document.querySelector('[data-hero-prev]');
  const next = document.querySelector('[data-hero-next]');
  if (slides.length < 2) return;

  let activeIndex = 0;
  let timerId = null;
  const intervalMs = 7000;
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function showSlide(index) {
    activeIndex = (index + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      const active = i === activeIndex;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', String(!active));
    });
    dots.forEach((dot, i) => {
      const active = i === activeIndex;
      dot.classList.toggle('is-active', active);
      dot.setAttribute('aria-current', String(active));
    });
    if (currentLabel) currentLabel.textContent = String(activeIndex + 1).padStart(2, '0');
  }

  function stopTimer() {
    if (timerId !== null) window.clearInterval(timerId);
    timerId = null;
  }

  function startTimer() {
    stopTimer();
    if (prefersReducedMotion || document.hidden) return;
    timerId = window.setInterval(() => showSlide(activeIndex + 1), intervalMs);
  }

  if (previous) previous.addEventListener('click', () => { showSlide(activeIndex - 1); startTimer(); });
  if (next) next.addEventListener('click', () => { showSlide(activeIndex + 1); startTimer(); });
  dots.forEach((dot) => dot.addEventListener('click', () => {
    const index = Number(dot.getAttribute('data-hero-dot'));
    if (Number.isInteger(index)) showSlide(index);
    startTimer();
  }));

  const pauseAreas = [carousel, document.querySelector('.hero-carousel-controls')].filter(Boolean);
  pauseAreas.forEach((area) => {
    area.addEventListener('mouseenter', stopTimer);
    area.addEventListener('mouseleave', startTimer);
    area.addEventListener('focusin', stopTimer);
    area.addEventListener('focusout', startTimer);
  });
  document.addEventListener('visibilitychange', () => document.hidden ? stopTimer() : startTimer());
  showSlide(0);
  startTimer();
})();
