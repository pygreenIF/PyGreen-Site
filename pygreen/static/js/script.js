var loginButton = document.querySelector("#login-button");
var closeLoginButton = document.querySelector("#close-login")
var container = document.querySelector("#login-screen");

const slide = document.querySelectorAll('.slide');
const carouselButtonLeft = document.getElementById('carousel-button-left');
const carouselButtonRight = document.getElementById('carousel-button-right');
let currentSlide = 0;

function hideSlide() {
    slide.forEach(item => item.classList.remove('on'))
}

function showSlide() {
    slide[currentSlide].classList.add('on')
}

function nextSlide() {
    hideSlide()
    if(currentSlide === slide.length-1){
        currentSlide = 0
    } else {
        currentSlide++
    }
    showSlide()
}

function prevSlide() {
    hideSlide()
    if(currentSlide ===0){
        currentSlide = slide.length -1
    } else {
        currentSlide--
    }
    showSlide()
}

carouselButtonLeft.addEventListener('click', prevSlide)
carouselButtonRight.addEventListener('click', nextSlide)

loginButton.addEventListener("click", function() {
    if(container.style.display === "none") {
        container.style.display = "block";
        document.querySelector("#body").classList.add('disable-scroll');
    } else {
        container.style.display = "none";
        document.querySelector("#body").classList.remove('disable-scroll');
    }
});

closeLoginButton.addEventListener("click", function() {
    if(container.style.display === "none") {
        container.style.display = "block";
        document.querySelector("#body").classList.add('disable-scroll');
    } else {
        container.style.display = "none";
        document.querySelector("#body").classList.remove('disable-scroll');
        document.querySelector("#login-screen").classList("fade-out")
    }
});

function showMenu() {
    let menuMobile = document.querySelector('.menu-mobile');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        // document.querySelector('.icon') = <i class="fa-solid fa-bars"></i>;
    } else {
        menuMobile.classList.add('open');
        // document.querySelector('.icon')= <i class="fa-solid fa-xmark"></i>;
    }
}