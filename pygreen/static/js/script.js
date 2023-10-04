var loginButton = document.querySelector("#login-button");
var closeLoginButton = document.querySelector("#close-login")
var container = document.querySelector("#login-screen");

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