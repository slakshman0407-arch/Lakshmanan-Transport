document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const elementsToAnimate = document.querySelectorAll('.fade-up, .fade-in, .fade-left, .fade-right');
    elementsToAnimate.forEach(el => observer.observe(el));

    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    const mobileToggle = document.getElementById('mobile-toggle');
    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            alert("Mobile menu clicked (implement slide menu here)");
        });
    }

    // Initialize Map for Madhavaram
    const mapEl = document.getElementById('map');
    if (mapEl) {
        // Centered closer to Madhavaram truck terminal
        const madhavaramCoords = [13.1450, 80.2250];
        const map = L.map('map').setView(madhavaramCoords, 15);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap'
        }).addTo(map);

        const forkliftIcon = L.icon({
            iconUrl: 'assets/forklift-icon.png',
            iconSize: [64, 64],
            iconAnchor: [32, 64],
            popupAnchor: [0, -64],
            className: 'custom-isometric-forklift'
        });

        L.marker(madhavaramCoords, { icon: forkliftIcon }).addTo(map)
            .bindPopup('<b style="color: #121212;">Lakshmanan Transport</b><br><span style="color: #333;">Madhavaram Truck Hub</span>')
            .openPopup();
    }
});
