// 1. Light Ambient Space Starfield Canvas
(function initStars() {
  const canvas = document.getElementById('space-canvas');
  const ctx = canvas.getContext('2d');
  let stars = [];
  let width = 0;
  let height = 0;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    stars = [];
    const count = Math.floor((width * height) / 9000);
    for (let i = 0; i < count; i++) {
      stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 1.2 + 0.3,
        alpha: Math.random() * 0.7 + 0.2,
        speed: Math.random() * 0.05 + 0.01,
        pulseSpeed: Math.random() * 0.02 + 0.005,
        pulseOffset: Math.random() * Math.PI * 2
      });
    }
  }

  function render(time) {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < stars.length; i++) {
      const s = stars[i];
      const brightness = s.alpha + Math.sin(time * 0.001 * s.pulseSpeed + s.pulseOffset) * 0.2;
      ctx.fillStyle = `rgba(220, 235, 255, ${Math.max(0.1, Math.min(1, brightness))})`;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
      ctx.fill();
    }
    requestAnimationFrame(render);
  }

  window.addEventListener('resize', resize);
  resize();
  requestAnimationFrame(render);
})();

// 2. Progressive Scroll-Driven Story Beat Highlighting
(function initStoryObserver() {
  const storyBeats = document.querySelectorAll('.story-beat');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const beat = entry.target;
      const indicator = beat.querySelector('span:first-child');
      const title = beat.querySelector('span:last-child');
      const isMars = beat.closest('#mars-environment') !== null;
      const accentColor = isMars ? 'border-mars-accent/70' : 'border-cyan-400/60';
      const bgActive = isMars ? 'bg-mars-accent' : 'bg-cyan-400';
      const textActive = isMars ? 'text-mars-accent' : 'text-cyan-300';
      const shadowActive = isMars ? 'shadow-[0_0_25px_rgba(226,109,92,0.25)]' : 'shadow-[0_0_25px_rgba(103,232,249,0.2)]';

      if (entry.isIntersecting) {
        // Emphasize current active story beat
        beat.classList.add(accentColor, shadowActive, 'scale-[1.01]', 'opacity-100');
        beat.classList.remove('border-white/10', 'opacity-40');
        if (indicator) {
          indicator.className = `w-2.5 h-2.5 rounded-full ${bgActive} animate-pulse`;
        }
        if (title) {
          title.className = `font-bold ${textActive}`;
        }
      } else {
        // Demote subtle background beats
        beat.classList.remove(accentColor, shadowActive, 'scale-[1.01]', 'opacity-100');
        beat.classList.add('border-white/10', 'opacity-45');
        if (indicator) {
          indicator.className = 'w-2 h-2 rounded-full bg-slate-600';
        }
        if (title) {
          title.className = 'font-bold text-slate-500';
        }
      }
    });
  }, {
    root: null,
    rootMargin: '-30% 0px -40% 0px', // Center active detection
    threshold: 0.2
  });

  storyBeats.forEach(beat => observer.observe(beat));
})();