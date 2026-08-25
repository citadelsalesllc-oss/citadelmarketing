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
  var modal = document.getElementById('svcModal');
  var grid = document.getElementById('svcModalGrid');
  var title = document.getElementById('svcModalTitle');
  var closeBtn = document.getElementById('svcModalClose');
  var backdrop = document.getElementById('svcModalBackdrop');
  var cards = document.querySelectorAll('.svc-card[data-service]');
  if (!modal || !cards.length) return;

  var sets = {
    civil: {
      title: 'Civil & Subdivision Development',
      photos: [
        { src: '/assets/img/photo3.jpg', alt: 'Two excavators working a large open site', cap: 'Mass grading, wide site view' },
        { src: '/assets/img/photo4.jpg', alt: 'Komatsu dozer pushing a pile of dirt', cap: 'Dozer pushing structural fill' },
        { src: '/assets/img/photo6.jpg', alt: 'Excavator with a mulching attachment clearing land near a home', cap: 'Land clearing & mulching near a homesite' },
        { src: '/assets/img/photo9.jpg', alt: 'Two excavators mass grading a large subdivision lot near homes', cap: 'Mass grading a subdivision lot' }
      ]
    },
    road: {
      title: 'Road Building',
      photos: [
        { src: '/assets/img/svc-road-1.jpg', alt: 'Fleet of excavators, a compactor, and trucks staged on a finished gravel road', cap: 'Fleet staged on a freshly built gravel road' }
      ]
    },
    foundation: {
      title: 'Foundation Services',
      photos: [
        { src: '/assets/img/svc-foundation-1.jpg', alt: 'Poured concrete foundation walls with radiant floor tubing laid on gravel base', cap: 'Foundation walls and radiant floor prep' }
      ]
    },
    septic: {
      title: 'Septic Tank & Drainfield Installation',
      photos: [
        { src: '/assets/img/svc-septic-1.jpg', alt: 'Septic leach chamber installed in a gravel-lined trench', cap: 'Leach chamber install, drainfield trench', capped: true }
      ]
    }
  };

  var openModal = function(key){
    var set = sets[key];
    if (!set) return;
    title.textContent = set.title;
    grid.innerHTML = '';
    set.photos.forEach(function(p){
      var fig = document.createElement('figure');
      var img = document.createElement('img');
      img.src = p.src;
      img.alt = p.alt;
      img.loading = 'lazy';
      if (p.capped) img.classList.add('is-capped');
      var cap = document.createElement('figcaption');
      cap.textContent = p.cap;
      fig.appendChild(img);
      fig.appendChild(cap);
      grid.appendChild(fig);
    });
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
  };

  var closeModal = function(){
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
  };

  cards.forEach(function(card){
    card.addEventListener('click', function(){ openModal(card.getAttribute('data-service')); });
    card.addEventListener('keydown', function(e){
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(card.getAttribute('data-service')); }
    });
  });
  closeBtn.addEventListener('click', closeModal);
  backdrop.addEventListener('click', closeModal);
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && modal.classList.contains('is-open')) closeModal();
  });
})();

(function(){
  var svcScroll = document.getElementById('svcScroll');
  var svcPrev = document.getElementById('svcPrev');
  var svcNext = document.getElementById('svcNext');
  if (svcScroll && svcPrev && svcNext) {
    var step = function(){
      var card = svcScroll.querySelector('.svc-card');
      return (card ? card.offsetWidth : 300) + 16;
    };
    svcPrev.addEventListener('click', function(){ svcScroll.scrollBy({ left: -step(), behavior: 'smooth' }); });
    svcNext.addEventListener('click', function(){ svcScroll.scrollBy({ left: step(), behavior: 'smooth' }); });
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
