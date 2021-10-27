// Toggle menu
/* 
    INDEX

    1. Main
    2. NavBar


*/

// 1. Main
document.addEventListener('DOMContentLoaded', () => {
    toggleMenu();
})

// 2. NavBar

/**
 * Toggle hamburger menu (mobile)
 */
function toggleMenu() {
    
        const hamburger = document.querySelector('.hamburger')
        const hamburgerOpen = document.querySelector('.hamburger-open');
        const hamburgerClose = document.querySelector('.hamburger-close');
        const navMenu = document.querySelector('.nav-list');
    
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active')
            hamburgerOpen.classList.toggle('active');
            hamburgerClose.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
}
