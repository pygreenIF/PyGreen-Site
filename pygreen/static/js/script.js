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

var formProfile = document.getElementById('form-profile')
var subProfile = document.getElementById('sub-title-profile')
var formSignup = document.getElementById('form-signup')
var subSignup = document.getElementById('sub-title-signup')
var btnSignup = document.getElementById('btn-registrar')

function swapForm() {
    formSignup.classList.remove('on')
    subSignup.classList.remove('on')
    formProfile.classList.add('on')
    subProfile.classList.remove('on')
}

btnSignup.addEventListener('click', swapForm)

var inputLogin = document.querySelector(".password");
var eye = document.querySelector(".fa-eye");
var eyeSlash = document.querySelector(".fa-eye-slash");
var inputSignup = document.querySelector(".password-signup")
var eye2 = document.querySelector(".signup1");
var eyeSlash2 = document.querySelector(".signup2");

function showPassword() {
    if(eye.classList.contains('open')) {
        eye.classList.remove('open')
        eye.classList.add('close')
        inputLogin.type = 'text';
    }
    else {
        eye.classList.add('open')
        eye.classList.remove('close')
        inputLogin.type = 'password';
    }

    if(eyeSlash.classList.contains('open')) {
        eyeSlash.classList.remove('open')
        eyeSlash.classList.add('close')
        inputLogin.type = 'password';
    }
    else {
        eyeSlash.classList.add('open')
        eyeSlash.classList.remove('close')
        inputLogin.type = 'text';
    }
}

function showPassword() {
    if(eye2.classList.contains('open')) {
        eye2.classList.remove('open')
        eye2.classList.add('close')
        inputSignup.type = 'text';
    }
    else {
        eye2.classList.add('open')
        eye2.classList.remove('close')
        inputSignup.type = 'password';
    }

    if(eyeSlash2.classList.contains('open')) {
        eyeSlash2.classList.remove('open')
        eyeSlash2.classList.add('close')
        inputSignup.type = 'password';
    }
    else {
        eyeSlash2.classList.add('open')
        eyeSlash2.classList.remove('close')
        inputSignup.type = 'text';
    }
}