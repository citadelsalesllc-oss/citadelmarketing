(function(){
  var rm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var heroVideo = document.querySelector('.hero-video');
  if (heroVideo) {
    if (rm) {
      heroVideo.pause();
      heroVideo.removeAttribute('autoplay');
    } else {
      heroVideo.muted = true;
      var tryPlay = function(){ var p = heroVideo.play(); if (p && p.catch) p.catch(function(){}); };
      tryPlay();
      ['touchstart','click','scroll'].forEach(function(evt){
        document.addEventListener(evt, tryPlay, { once: true, passive: true });
      });
    }
  }

  var revealEls = document.querySelectorAll('[data-reveal]');
  if (!rm && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add('is-in'); });
  }

  var ctaBand = document.querySelector('.cta-band');
  if (ctaBand && !rm) {
    var ticking = false;
    var updateParallax = function(){
      ticking = false;
      var rect = ctaBand.getBoundingClientRect();
      var vh = window.innerHeight;
      var center = rect.top + rect.height / 2;
      var offset = (center - vh / 2) / vh;
      ctaBand.style.setProperty('--ctaPar', (offset * -70).toFixed(1) + 'px');
    };
    window.addEventListener('scroll', function(){
      if (!ticking) { window.requestAnimationFrame(updateParallax); ticking = true; }
    }, { passive: true });
    updateParallax();
  }
})();

(function(){
  var navToggle = document.getElementById('navToggle');
  var mobileNav = document.getElementById('mobileNav');
  if (navToggle && mobileNav) {
    navToggle.addEventListener('click', function(){
      var open = mobileNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mobileNav.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        mobileNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
    document.addEventListener('click', function(e){
      if (mobileNav.classList.contains('open') && !mobileNav.contains(e.target) && e.target !== navToggle && !navToggle.contains(e.target)) {
        mobileNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
})();

(function(){
  var filterRow = document.getElementById('workFilters');
  var workGrid = document.getElementById('workGrid');
  if (filterRow && workGrid) {
    filterRow.addEventListener('click', function(e){
      var btn = e.target.closest('.filter-pill');
      if (!btn) return;
      filterRow.querySelectorAll('.filter-pill').forEach(function(p){ p.classList.remove('active'); });
      btn.classList.add('active');
      var f = btn.getAttribute('data-filter');
      workGrid.querySelectorAll('.work-card').forEach(function(card){
        var show = (f === 'all' || card.getAttribute('data-cat') === f);
        card.classList.toggle('is-hidden', !show);
      });
    });
  }
})();
