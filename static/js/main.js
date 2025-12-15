// DBSCAN Fraud Detection - Interactive Features
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll animation for all internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all content sections
    document.querySelectorAll('.content-section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        observer.observe(section);
    });

    // Counter animation for statistics
    function animateCounter(element, target, duration = 2000) {
        const start = 0;
        const increment = target / (duration / 16);
        let current = start;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target.toLocaleString();
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current).toLocaleString();
            }
        }, 16);
    }

    // Trigger counter animations when stats are visible
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                const h3 = entry.target.querySelector('h3');
                if (h3) {
                    const target = parseInt(h3.textContent.replace(/,/g, ''));
                    if (!isNaN(target)) {
                        animateCounter(h3, target);
                        entry.target.dataset.animated = 'true';
                    }
                }
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.stat-card').forEach(card => {
        statsObserver.observe(card);
    });

    // Animate progress bars
    const progressObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fills = entry.target.querySelectorAll('.metric-bar-fill, .importance-bar');
                fills.forEach(fill => {
                    const width = fill.style.width;
                    fill.style.width = '0';
                    setTimeout(() => {
                        fill.style.width = width;
                    }, 100);
                });
            }
        });
    }, { threshold: 0.3 });

    document.querySelectorAll('.metric-card, .feature-card').forEach(card => {
        progressObserver.observe(card);
    });

    // Add hover effect to table rows
    const tableRows = document.querySelectorAll('.cluster-table tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(5px)';
        });
        row.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    });

    // Tooltip functionality
    const tooltips = document.querySelectorAll('.metric-tooltip');
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', function(e) {
            const title = this.getAttribute('title');
            if (title) {
                const tooltipBox = document.createElement('div');
                tooltipBox.className = 'tooltip-box';
                tooltipBox.textContent = title;
                tooltipBox.style.cssText = `
                    position: absolute;
                    background: rgba(26, 29, 41, 0.95);
                    color: #e2e8f0;
                    padding: 0.5rem 1rem;
                    border-radius: 0.5rem;
                    font-size: 0.875rem;
                    z-index: 1000;
                    pointer-events: none;
                    white-space: nowrap;
                    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
                    border: 1px solid rgba(102, 126, 234, 0.3);
                `;
                document.body.appendChild(tooltipBox);
                
                const rect = this.getBoundingClientRect();
                tooltipBox.style.left = rect.left - tooltipBox.offsetWidth - 10 + 'px';
                tooltipBox.style.top = rect.top + (rect.height / 2) - (tooltipBox.offsetHeight / 2) + 'px';
                
                this.tooltipBox = tooltipBox;
            }
        });
        
        tooltip.addEventListener('mouseleave', function() {
            if (this.tooltipBox) {
                this.tooltipBox.remove();
                this.tooltipBox = null;
            }
        });
    });

    // Parallax effect on hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const particles = document.querySelector('.particles-bg');
        if (particles) {
            particles.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });

    // Add loading animation to images
    const images = document.querySelectorAll('.viz-image');
    images.forEach(img => {
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.5s ease';
        
        if (img.complete) {
            img.style.opacity = '1';
        } else {
            img.addEventListener('load', function() {
                this.style.opacity = '1';
            });
        }
    });

    // Console Easter Egg
    console.log('%c🔍 DBSCAN Fraud Detection System', 'color: #667eea; font-size: 20px; font-weight: bold;');
    console.log('%cDesarrollado con ❤️ para el análisis de fraude bancario', 'color: #a0aec0; font-size: 12px;');
    console.log('%c⚡ Tecnologías: Python, Flask, Scikit-learn, DBSCAN', 'color: #00f2fe; font-size: 11px;');

    // Performance monitoring
    if (window.performance) {
        const perfData = window.performance.timing;
        const loadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log(`%c⏱️ Tiempo de carga: ${loadTime}ms`, 'color: #feca57; font-size: 11px;');
    }
});

// Add custom cursor effect (optional, for extra uniqueness)
document.addEventListener('mousemove', function(e) {
    const cursor = document.querySelector('.custom-cursor');
    if (!cursor) {
        const newCursor = document.createElement('div');
        newCursor.className = 'custom-cursor';
        newCursor.style.cssText = `
            width: 20px;
            height: 20px;
            border: 2px solid rgba(102, 126, 234, 0.5);
            border-radius: 50%;
            position: fixed;
            pointer-events: none;
            z-index: 9999;
            transition: all 0.15s ease;
            mix-blend-mode: difference;
        `;
        document.body.appendChild(newCursor);
    }
    
    const cursor2 = document.querySelector('.custom-cursor');
    if (cursor2) {
        cursor2.style.left = e.clientX - 10 + 'px';
        cursor2.style.top = e.clientY - 10 + 'px';
    }
});

// Add click ripple effect
document.addEventListener('click', function(e) {
    const ripple = document.createElement('div');
    ripple.style.cssText = `
        position: fixed;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(102, 126, 234, 0.3);
        pointer-events: none;
        z-index: 9998;
        animation: rippleEffect 0.6s ease-out;
        left: ${e.clientX - 25}px;
        top: ${e.clientY - 25}px;
    `;
    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes rippleEffect {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    
    if (!document.querySelector('#ripple-style')) {
        style.id = 'ripple-style';
        document.head.appendChild(style);
    }
    
    document.body.appendChild(ripple);
    setTimeout(() => ripple.remove(), 600);
});
