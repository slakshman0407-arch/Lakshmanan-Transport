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
    const navLinks = document.querySelector('.nav-links');
    const headerContact = document.querySelector('.header-contact');

    if (mobileToggle && navLinks && headerContact) {
        // Create mobile menu container
        const mobileMenu = document.createElement('div');
        mobileMenu.className = 'mobile-menu-container';

        // Clone elements
        const clonedNav = navLinks.cloneNode(true);
        const clonedContact = headerContact.cloneNode(true);
        // Correct display style from stylesheet since cloned elements might get 'display: none' inline somehow if hidden but they don't here because it's CSS media query
        clonedNav.style.display = 'flex';
        clonedContact.style.display = 'flex';

        mobileMenu.appendChild(clonedNav);
        mobileMenu.appendChild(clonedContact);

        // Add close X button inside the menu
        const closeBtn = document.createElement('button');
        closeBtn.className = 'mobile-menu-close';
        closeBtn.innerHTML = "<i class='bx bx-x'></i>";
        closeBtn.addEventListener('click', () => {
            document.body.classList.remove('menu-open');
            mobileToggle.innerHTML = "<i class='bx bx-menu'></i>";
        });
        mobileMenu.appendChild(closeBtn);

        document.body.appendChild(mobileMenu);

        // Handle Mobile Dropdown
        const mobileNavItems = mobileMenu.querySelectorAll('.nav-item');
        mobileNavItems.forEach(item => {
            const link = item.querySelector('a');
            link.addEventListener('click', (e) => {
                e.preventDefault();
                item.classList.toggle('active');
                const icon = link.querySelector('i');
                if (icon) {
                    if (item.classList.contains('active')) {
                        icon.classList.replace('bx-chevron-down', 'bx-chevron-up');
                    } else {
                        icon.classList.replace('bx-chevron-up', 'bx-chevron-down');
                    }
                }
            });
        });

        // Close menu when clicking regular links
        const allLinks = mobileMenu.querySelectorAll('a:not(.nav-item > a)');
        allLinks.forEach(link => {
            link.addEventListener('click', () => {
                document.body.classList.remove('menu-open');
                mobileToggle.innerHTML = "<i class='bx bx-menu'></i>";
            });
        });

        mobileToggle.addEventListener('click', () => {
            document.body.classList.toggle('menu-open');
            if (document.body.classList.contains('menu-open')) {
                mobileToggle.innerHTML = "<i class='bx bx-x'></i>";
            } else {
                mobileToggle.innerHTML = "<i class='bx bx-menu'></i>";
            }
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

    // WhatsApp Form Submission Handler
    const whatsappForm = document.getElementById('whatsappForm');
    if (whatsappForm) {
        whatsappForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const company = document.getElementById('company').value;
            const phone = document.getElementById('phone').value;

            const message = `Hello Lakshmanan Transport, I have an enquiry.\n\nName: ${name}\nCompany: ${company}\nPhone: ${phone}\n\nPlease get back to me.`;
            const whatsappUrl = `https://wa.me/919962603684?text=${encodeURIComponent(message)}`;

            window.open(whatsappUrl, '_blank');
        });
    }
});
