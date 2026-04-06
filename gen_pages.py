import os

layout_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} services by Lakshmanan Transport">
    <title>{title} | Lakshmanan Transport</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css?v=4">
</head>
<body>
    <header class="navbar" id="navbar">
        <div class="container nav-container">
            <div class="logo">
                <a href="index.html#home">
                    <img src="assets/logo.png" alt="Lakshmanan Transport Logo" class="header-logo"
                        style="height: 60px; max-height: 60px; width: auto; object-fit: contain;">
                </a>
            </div>
            <nav class="nav-links">
                <a href="index.html#home">Home</a>
                <a href="index.html#about">About Us</a>
                <div class="nav-item">
                    <a href="index.html#services" style="display: flex; align-items: center; gap: 5px;">Services <i class='bx bx-chevron-down'></i></a>
                    <div class="dropdown-menu">
                        <a href="rental.html">Forklift Rental</a>
                        <a href="dealers.html">Forklift Dealers</a>
                        <a href="sales.html">Forklift Sales</a>
                        <a href="service.html">Forklift Service</a>
                    </div>
                </div>
                <a href="index.html#contact">Contact</a>
            </nav>
            <div class="header-contact">
                <div class="header-contact-details">
                    <a href="tel:+919962603684"><i class='bx bxs-phone'></i>+91 99626 03684</a>
                    <a href="mailto:lakshmanantransport16@gmail.com"><i class='bx bxs-envelope'></i>lakshmanantransport16@gmail.com</a>
                </div>
                <a href="tel:+919962603684" class="btn btn-primary nav-cta">Call Now</a>
            </div>
            <div class="mobile-toggle" id="mobile-toggle"><i class='bx bx-menu'></i></div>
        </div>
    </header>

    <main>
        <section class="page-hero" style="background-image: url('assets/hero.png'); background-size: cover; background-position: center; position: relative; padding: 150px 0 80px 0; text-align: center; color: #fff; display: flex; align-items: center; justify-content: center; min-height: 250px;">
            <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(24,51,89,0.95) 0%, rgba(24,51,89,0.7) 100%); z-index: 1;"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <h1 style="font-size: 3.5rem; margin-bottom: 15px; font-weight: 800; text-shadow: 0 4px 15px rgba(0,0,0,0.3);">{title}</h1>
                <p style="font-size: 1.1rem; color: rgba(255,255,255,0.9); font-weight: 500;">You are here: <a href="index.html" style="color: var(--primary); font-weight: 700;">Home</a> / {title}</p>
            </div>
        </section>

        <section class="service-detail section-padding" style="padding: 100px 0; background: #fafafa;">
            <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;">
                <div class="service-detail-content">
                    <h2 style="font-size: 2.8rem; color: var(--secondary); margin-bottom: 30px; font-weight: 800;">{title}</h2>
                    {paragraphs}
                    <a href="index.html#contact" class="btn btn-primary" style="margin-top: 10px;">Get a Quote Now <i class='bx bx-right-arrow-alt'></i></a>
                </div>
                <div class="service-detail-image" style="padding: 20px; background: #fff; border-radius: var(--radius-lg); box-shadow: 0 20px 50px rgba(0,0,0,0.08); border: 8px solid var(--primary); position: relative;">
                    <div style="position: absolute; top: -20px; left: -20px; background: var(--secondary); color: #fff; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 2rem; box-shadow: 0 10px 20px rgba(0,0,0,0.2);"><i class='bx bxs-check-shield'></i></div>
                    <img src="{image}" alt="{title} service" style="width: 100%; border-radius: var(--radius-md); display: block; object-fit: cover; aspect-ratio: 4/3;">
                </div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-brand">
                <div class="logo"><img src="assets/logo.png" alt="Lakshmanan Transport Logo" class="site-logo" style="height: 60px; max-height: 60px; width: auto; object-fit: contain; filter: brightness(0) invert(1) drop-shadow(0 2px 4px rgba(0,0,0,0.2));"></div>
                <p>Reliable forklift rental and industrial lifting services.</p>
                <div class="social-links">
                    <a href="#" aria-label="Facebook"><i class='bx bxl-facebook'></i></a>
                    <a href="#" aria-label="Instagram"><i class='bx bxl-instagram'></i></a>
                </div>
            </div>
            <div class="footer-links">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="index.html#home">Home</a></li>
                    <li><a href="index.html#about">About Us</a></li>
                    <li><a href="index.html#services">Our Services</a></li>
                    <li><a href="index.html#contact">Contact</a></li>
                </ul>
            </div>
            <div class="footer-contact">
                <h3>Contact Us</h3>
                <ul>
                    <li style="display: flex; gap: 10px; margin-bottom: 12px; align-items: flex-start;">
                        <i class='bx bxs-map' style="color: var(--primary); font-size: 1.2rem; margin-top: 4px;"></i>
                        <span style="color: rgba(255,255,255,0.8); line-height: 1.5;">Madhavaram Truck Hub,<br>Chennai, Tamil Nadu</span>
                    </li>
                    <li style="display: flex; gap: 10px; margin-bottom: 12px; align-items: center;">
                        <i class='bx bxs-phone' style="color: var(--primary); font-size: 1.2rem;"></i>
                        <a href="tel:+919962603684" style="color: rgba(255,255,255,0.8);">+91 99626 03684</a>
                    </li>
                    <li style="display: flex; gap: 10px; align-items: center;">
                        <i class='bx bxs-envelope' style="color: var(--primary); font-size: 1.2rem;"></i>
                        <a href="mailto:lakshmanantransport16@gmail.com" style="color: rgba(255,255,255,0.8);">lakshmanantransport16@gmail.com</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container">
                <p>&copy; 2026 Lakshmanan Transport. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>"""

pages = [
    {
        "filename": "rental.html",
        "title": "Forklift Rental",
        "image": "assets/rental_forklift.png",
        "paragraphs": '<p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">Moving on deep knowledge & industrial experience, we are offering a very effective solution for Forklift Rental Services. We procure the best quality equipments to offer optimum performance at varied industrial sites. Our provided rental services are appreciated in the market for their quality attributes like client centric approach.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">The range of services provided extends from taking on complete equipment operations for handling of raw materials and finished goods produced by our clients, warehouse management, repair and maintenance of client owned equipment, and manpower management.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 30px;">A dedicated and well-trained workforce consisting of technicians, forklift operators, and engineers have allowed us to achieve high proficiency and success in our operations.</p>'
    },
    {
        "filename": "dealers.html",
        "title": "Forklift Dealers",
        "image": "assets/dealer_forklifts.png",
        "paragraphs": '<p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">We are authorized dealers for premium forklift brands in multiple locations. With an extensive inventory of high-performance industrial machines, we guarantee top-tier lifting equipment built for endurance.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">Our dealership network leverages direct manufacturer connections to provide you with reliable machines at highly competitive prices. Partnering with us gives you dedicated local support, comprehensive warranties, and complete peace of mind.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 30px;">We actively assist you in choosing the optimum model based on your unique terrain, operational height requirements, and payload capabilities.</p>'
    },
    {
        "filename": "sales.html",
        "title": "Forklift Sales",
        "image": "assets/sales_forklift.png",
        "paragraphs": '<p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">Lakshmanan Transport offers a diverse catalog of both new and used forklifts for direct purchase. From compact electric reach trucks to heavy-duty diesel engines, we offer solutions custom-tailored for any business budget.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">Every pre-owned forklift we sell goes through an exhaustive multi-point inspection by certified mechanics, ensuring that it operates as efficiently and securely as a brand new model. We firmly believe in transparent pricing and lasting value.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 30px;">Speak to our sales experts today to find out which machine will maximize your industrial productivity and minimize downtime.</p>'
    },
    {
        "filename": "service.html",
        "title": "Forklift Service",
        "image": "assets/service_forklift.png",
        "paragraphs": '<p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">We are highly engaged in offering an optimum quality Forklift Repairing and Maintenance Service. Breakdown in the middle of a project can cost thousands in lost productivity—our rapid-response mechanics are on call exactly when you need them.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 24px;">We provide comprehensive servicing packages including routine checks, battery desulfation, hydraulic system flushes, engine overhauls, and preventative safety audits.</p><p style="color: var(--text-muted); line-height: 1.8; font-size: 1.15rem; margin-bottom: 30px;">Focus on your core operations while relying on us to keep your lifting equipment functionally pristine, fully compliant, and 100% safe.</p>'
    }
]

for p in pages:
    print(f"Writing {p['filename']}...")
    with open(p['filename'], "w", encoding="utf-8") as f:
        f.write(layout_template.format(**p))

print("Pages created successfully!")
