

    const header = document.getElementById("mainHeader");
    const banner = document.getElementById("topBanner");
  
    window.addEventListener("scroll", () => {
      if (window.scrollY > 50) {
        header.classList.add("shrink-header");
        banner.classList.add("shrink-banner");
      } else {
        header.classList.remove("shrink-header");
        banner.classList.remove("shrink-banner");
      }
    });
  
    /* about footer and hearder*/
    document.addEventListener('DOMContentLoaded', function () {
      const OFFSET = 320; // adjust this to your navbar height
  
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
          anchor.addEventListener('click', function (e) {
              e.preventDefault();
  
              const targetID = this.getAttribute('href').slice(1);
              const targetElement = document.getElementById(targetID);
  
              if (targetElement) {
                  const elementPosition = targetElement.getBoundingClientRect().top;
                  const offsetPosition = elementPosition + window.pageYOffset - OFFSET;
  
                  window.scrollTo({
                      top: offsetPosition,
                      behavior: 'smooth'
                  });
  
                  // Highlight the section briefly
                  targetElement.classList.add('highlight');
                  setTimeout(() => {
                      targetElement.classList.remove('highlight');
                  }, 5000);
              }
          });
      });
  });


  window.onload = function() {
    // Delay for fading in text in the carousel
    const attractionText1 = document.getElementById('attractionText1');
    const attractionText2 = document.getElementById('attractionText2');
    
    // Fade-in effect for text after the page is loaded
    setTimeout(() => {
        attractionText1.style.opacity = 1;
    }, 500); // Delay for the first text

    setTimeout(() => {
        attractionText2.style.opacity = 1;
    }, 1000); // Delay for the second text, slightly longer
};


// submenu js//
// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    const isLargeScreen = () => window.innerWidth >= 992;

    document.querySelectorAll('.dropdown-submenu > a').forEach(function (el) {
        el.addEventListener('click', function (e) {
            if (!isLargeScreen()) {
                e.preventDefault();
                const submenu = this.nextElementSibling;
                if (submenu && submenu.classList.contains('dropdown-menu')) {
                    submenu.classList.toggle('show');
                }
            }
        });
    });

    // Close submenus when clicking outside
    document.addEventListener('click', function (e) {
        document.querySelectorAll('.dropdown-submenu .dropdown-menu').forEach(function (menu) {
            if (!menu.contains(e.target)) {
                menu.classList.remove('show');
            }
        });
    });
});



AOS.init({
    once: false, // Ensures the animation triggers every time the element comes into view
    duration: 2000, // Animation duration
    easing: 'ease-out', // Smooth easing function
});

document.addEventListener('DOMContentLoaded', () => {
const title = document.getElementById('collection-title');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                title.classList.add('visible');
                observer.unobserve(title);
            }
        });
    }, {
        threshold: 0.5
    });

    observer.observe(title);
});



// its a new start for desktop and mobile navbar
document.addEventListener("DOMContentLoaded", function () {
  const params = new URLSearchParams(window.location.search);
  const keyword = params.get("highlight");

  if (keyword) {
      const regex = new RegExp(`(${keyword})`, "gi");
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);

      let node;
      while (node = walker.nextNode()) {
          if (node.nodeValue.trim() !== "") {
              const span = document.createElement("span");
              span.innerHTML = node.nodeValue.replace(regex, '<span class="highlight">$1</span>');
              if (span.innerHTML !== node.nodeValue) {
                  const parent = node.parentNode;
                  const wrapper = document.createElement("span");
                  wrapper.innerHTML = span.innerHTML;
                  parent.replaceChild(wrapper, node);
              }
          }
      }
  }
});
