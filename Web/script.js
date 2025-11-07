// Simple Art & Culture Website Script

document.addEventListener("DOMContentLoaded", function () {
    // Active Nav Link
    const current = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll("nav a").forEach(a => {
        if (a.getAttribute("href") === current) a.classList.add("active");
    });

    // Simple text display
    const typed = document.querySelector(".typed-text");
    if (typed) {
        typed.innerHTML = "Exploring Art & Culture Worldwide";
    }

    // Gallery Lightbox
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modal-img");
    const caption = document.getElementById("modal-caption");
    const close = document.getElementById("close-modal");

    document.querySelectorAll(".gallery-item").forEach(item => {
        item.addEventListener("click", () => {
            const src = item.querySelector("img").src;
            const cap = item.querySelector(".gallery-caption p").innerText;
            modalImg.src = src;
            caption.innerText = cap;
            modal.style.display = "flex";
        });
    });

    if (close) close.onclick = () => modal.style.display = "none";
    window.onclick = (e) => { if (e.target === modal) modal.style.display = "none"; };

    // Simple Dark Mode Toggle
    const toggle = document.getElementById("dark-mode-toggle");
    if (toggle) {
        toggle.onclick = () => {
            document.body.classList.toggle("dark-mode");
            const isDark = document.body.classList.contains("dark-mode");
            toggle.innerHTML = isDark ? "🌙" : "☀";
        };
    }

    // Simple Form Validation
    const form = document.getElementById("contact-form");
    if (form) {
        form.onsubmit = (e) => {
            e.preventDefault();
            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            if (!name || !email || !message) {
                alert("Please fill all fields.");
                return;
            }
            if (!email.includes("@")) {
                alert("Please enter a valid email address.");
                return;
            }

            alert(`Thank you, ${name}! Your message has been sent.`);
            form.reset();
        };
    }
});