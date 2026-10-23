/* ============================================================
   JOY JUSTIN J — PORTFOLIO INTERACTIVITY & PARALLAX ENGINE
   ============================================================ */

'use strict';

/* ---- 1. EXACT REFERENCE PARALLAX SCROLL ENGINE ---- */
const textTop = document.getElementById('parallax-text-top');
const textBottom = document.getElementById('parallax-text-bottom');
const profileImg = document.getElementById('parallax-profile-img');
const fixedHeroBg = document.querySelector('.fixed-hero-bg');
let ticking = false;

const updateHeroParallax = () => {
  const scrollY = window.pageYOffset || window.scrollY || document.documentElement.scrollTop || 0;
  const viewportHeight = window.innerHeight || 800;

  if (scrollY <= viewportHeight * 1.5) {
    const progress = Math.min(1, Math.max(0, scrollY / viewportHeight));
    
    // Split text outwardly — safe distance on all screens
    const moveX = progress * Math.min(280, window.innerWidth * 0.35); 
    const moveYTop = -progress * 30;
    const moveYBottom = progress * 15;
    const opacityText = 1 - progress * 0.70;
    
    if (textTop) {
      textTop.style.transform = `translate3d(${-moveX}px, ${moveYTop}px, 0)`;
      textTop.style.opacity = opacityText;
      textTop.style.color = progress > 0.15 ? '#9E6A6A' : '#6B1C1C';
    }
    if (textBottom) {
      textBottom.style.transform = `translate3d(${moveX}px, ${moveYBottom}px, 0)`;
      textBottom.style.opacity = opacityText;
      textBottom.style.color = progress > 0.15 ? '#9E6A6A' : '#6B1C1C';
    }

    // Zoomed photo glides with natural parallax depth as white content sheet rises
    if (profileImg) {
      profileImg.style.transform = `translate3d(0, ${scrollY * 0.26}px, 0) scale(${1 - progress * 0.04})`;
    }
    
    if (fixedHeroBg) {
      fixedHeroBg.style.visibility = 'visible';
    }
  } else if (scrollY > viewportHeight * 1.5 && fixedHeroBg) {
    fixedHeroBg.style.visibility = 'hidden';
  }
  ticking = false;
};

const onScroll = () => {
  if (!ticking) {
    window.requestAnimationFrame(updateHeroParallax);
    ticking = true;
  }
};

window.addEventListener('scroll', onScroll, { passive: true });
window.addEventListener('resize', onScroll, { passive: true });
updateHeroParallax();

/* ---- 2. FLOATING PILL NAV ACTIVE TAB MONITORING & SCROLL REVEAL ---- */
const pillLinks = document.querySelectorAll('.pill-link');
const pillNavContainer = document.querySelector('.pill-nav-container');
const sections = [
  { id: 'home', element: document.getElementById('home') },
  { id: 'experience', element: document.getElementById('experience') },
  { id: 'skills', element: document.getElementById('skills') },
  { id: 'projects', element: document.getElementById('projects') },
  { id: 'contact', element: document.getElementById('contact') }
];

const updatePillNav = () => {
  const currentScrollY = window.scrollY;

  // Reveal floating navbar only after scrolling down from initial hero poster view
  if (pillNavContainer) {
    if (currentScrollY > 80) {
      pillNavContainer.classList.add('visible-nav');
    } else {
      pillNavContainer.classList.remove('visible-nav');
    }
  }

  // Active section spy
  sections.forEach(section => {
    if (!section.element) return;
    const elementRect = section.element.getBoundingClientRect();
    const isVisible = elementRect.top < window.innerHeight * 0.5 && elementRect.bottom >= 120;
    
    if (isVisible) {
      pillLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${section.id}`) {
          link.classList.add('active');
        }
      });
    }
  });
};

window.addEventListener('scroll', updatePillNav, { passive: true });
updatePillNav();

/* ---- 3. BOTTOM TAB ICON SWITCHER WITH GLOWING DOT ---- */
const tabButtons = document.querySelectorAll('.tab-icon-btn');
const tabWrappers = document.querySelectorAll('.tab-button-wrap');
const panels = document.querySelectorAll('.skill-panel');

tabButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const target = btn.getAttribute('data-target');

    // Deactivate all buttons and wrappers
    tabWrappers.forEach(wrap => wrap.classList.remove('active'));
    tabButtons.forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-selected', 'false');
    });

    // Activate selected tab and wrapper
    const currentWrap = btn.closest('.tab-button-wrap');
    if (currentWrap) currentWrap.classList.add('active');
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');

    // Hide all panels and display target panel
    panels.forEach(panel => {
      panel.classList.remove('active');
      panel.hidden = true;
    });

    const targetPanel = document.getElementById(`panel-${target}`);
    if (targetPanel) {
      targetPanel.hidden = false;
      setTimeout(() => targetPanel.classList.add('active'), 10);
    }
  });
});

/* ---- 4. SCROLL REVEAL (INTERSECTION OBSERVER) ---- */
const revealElements = document.querySelectorAll('.reveal-up, .reveal-stagger');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, idx) => {
      if (entry.isIntersecting) {
        const delay = entry.target.classList.contains('reveal-stagger') ? (idx % 3) * 100 : 0;
        setTimeout(() => entry.target.classList.add('visible'), delay);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px 60px 0px' });

  revealElements.forEach(el => observer.observe(el));
} else {
  revealElements.forEach(el => el.classList.add('visible'));
}

/* ---- 5. SMOOTH ANCHOR LINK SCROLLING ---- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    const targetId = anchor.getAttribute('href').slice(1);
    const target = document.getElementById(targetId);
    if (target) {
      e.preventDefault();
      const offset = 80;
      const targetTop = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({
        top: targetTop,
        behavior: 'smooth'
      });
    }
  });
});

/* ---- 6. CONTACT FORM SUBMISSION ---- */
const form = document.getElementById('contact-form');
const successAlert = document.getElementById('form-success');
const submitBtn = document.getElementById('submit-btn');

if (form && submitBtn) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const originalText = submitBtn.innerHTML;
    submitBtn.innerHTML = 'Sending Message...';
    submitBtn.disabled = true;

    // Simulate reliable dispatch
    await new Promise(resolve => setTimeout(resolve, 1000));

    successAlert.hidden = false;
    form.reset();
    submitBtn.innerHTML = originalText;
    submitBtn.disabled = false;

    setTimeout(() => { successAlert.hidden = true; }, 6000);
  });
}
