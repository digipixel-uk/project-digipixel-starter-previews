/* Functional mobile navigation and non-collecting preview enquiry demonstration. */
(() => {
  'use strict';
  const trigger = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-navigation');
  if (trigger && nav) {
    const closeMenu = () => { nav.classList.remove('open'); trigger.setAttribute('aria-expanded','false'); };
    trigger.addEventListener('click', () => {
      const open = trigger.getAttribute('aria-expanded') !== 'true';
      trigger.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('open', open);
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
    document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeMenu(); });
    document.addEventListener('click', (event) => {
      if (!nav.contains(event.target) && !trigger.contains(event.target)) closeMenu();
    });
  }
  const form = document.querySelector('[data-demo-form]');
  if (form) {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const status = form.querySelector('.form-status');
      const required = [...form.querySelectorAll('[required]')];
      required.forEach(el => el.removeAttribute('aria-invalid'));
      const firstInvalid = required.find(el => !el.checkValidity());
      if (firstInvalid) {
        firstInvalid.setAttribute('aria-invalid','true');
        status.hidden = false;
        status.textContent = 'Please complete the highlighted field using a valid value to see the example confirmation.';
        firstInvalid.focus();
        return;
      }
      status.hidden = false;
      status.textContent = 'This is where the real website would confirm your enquiry. For this DigiPixel demo, nothing was sent, recorded or stored.';
      form.reset();
      status.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'nearest' });
    });
  }
})();