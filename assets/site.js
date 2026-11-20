// Yomo marketing site — shared behaviour.
(function () {
  // Mobile menu
  var toggle = document.getElementById('menu-toggle');
  var menu = document.getElementById('mobile-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var hidden = menu.classList.toggle('hidden');
      toggle.setAttribute('aria-expanded', String(!hidden));
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        menu.classList.add('hidden');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Any form with data-waitlist opens a pre-filled mail draft (no backend on Pages).
  document.querySelectorAll('form[data-waitlist]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var field = form.querySelector('input[type="email"]');
      var email = field && field.value ? field.value.trim() : '';
      var subject = encodeURIComponent(form.getAttribute('data-subject') || 'Yomo invite request');
      var body = encodeURIComponent(
        'Hey Yomo, please add me to the invite list.\n\nEmail: ' + email +
        '\nPlan I am interested in: ' + (form.getAttribute('data-plan') || 'Free')
      );
      window.location.href = 'mailto:hello@prasthana.in?subject=' + subject + '&body=' + body;
      var note = form.parentElement.querySelector('[data-sent]');
      if (note) note.classList.remove('hidden');
    });
  });

  // Scroll reveal
  var items = document.querySelectorAll('.rise');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -40px 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }
})();
