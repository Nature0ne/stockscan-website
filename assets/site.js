'use strict';
document.documentElement.classList.remove('no-js');
const gallery = document.querySelector('[data-gallery]');
if (gallery) {
  const previous = document.querySelector('[data-previous]');
  const next = document.querySelector('[data-next]');
  const update = () => {
    previous.disabled = gallery.scrollLeft <= 3;
    next.disabled = gallery.scrollLeft + gallery.clientWidth >= gallery.scrollWidth - 2;
  };
  const move = direction => gallery.scrollBy({
    left: direction * (gallery.querySelector('figure').getBoundingClientRect().width + 22),
    behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'
  });
  previous.addEventListener('click', () => move(-1));
  next.addEventListener('click', () => move(1));
  gallery.addEventListener('scroll', update, {passive:true});
  window.addEventListener('resize', update);
  update();
}
