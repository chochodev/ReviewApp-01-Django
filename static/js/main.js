//*****************************************//
/* PRELOADER */

let loader = document.querySelector('#preloader')

window.addEventListener('load', function(){
    loader.style.display = 'none'
})

//*****************************************//
/* SCROLL BUTTON */
let scrollBtn = document.querySelector('#scroll-btn')
let scrollUp = document.querySelector('#scroll-up')
let scrollDown = document.querySelector('#scroll-down')

window.onscroll = function() {
    scrollFunction()
}

function scrollFunction(){
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200){
        scrollBtn.style.display = 'grid'
        scrollUp.style.display = ''
        scrollDown.style.display = ''
    }
    else{
        scrollBtn.style.display = 'none'
        scrollUp.style.display = 'none'
        scrollDown.style.display = 'none'
    }
}

function showScroll(){
    scrollUp.classList.toggle('scroll-active')
    scrollDown.classList.toggle('scroll-active')
}

function topFunction(){
    window.scrollTo(0, document.body.scrollTop)
}

function downFunction(){
    window.scrollTo(0, document.body.scrollHeight)
}

//*****************************************//

// NAVBAR FUNCTION //

let list = document.querySelectorAll('.list')
let menuToggle = document.querySelector('.toggle')
let navigation = document.querySelector('.navigation')
let profile_display = document.querySelector('.nav-profile')

let body = document.querySelector('#body')
let settings = document.querySelector('.main-settings')


for (let i = 0; i < list.length; i++){
    list[i].onclick = function(){
        let j = 0;

        while(j < list.length){
            list[j++].className = 'list';
        }
        
        list[i].className = 'list active'
    }
}

function MenuToggle(){

    // TOGGLE NAVBAR SECTION
    menuToggle.classList.toggle('active')
    navigation.classList.toggle('active')
    profile_display.classList.toggle('active')
}


//*****************************************//

/* SETTINGS FUNCTION */

// SETTINGS FUNCTIONS
let darkmodeBtn = document.querySelector('.darkmode-btn');
let darkmodeSlider = document.querySelector('.darkmode-slider');
let darkmodeOn = document.querySelector('.darkmode-on')
let darkmodeOff = document.querySelector('.darkmode-off')

////////
let notificationBtn = document.querySelector('.notification-btn');
let notificationSlider = document.querySelector('.notification-slider');
let notificationOn = document.querySelector('.notification-on')
let notificationOff = document.querySelector('.notification-off')

////////
let cookieBtn = document.querySelector('.cookie-btn');
let cookieSlider = document.querySelector('.cookie-slider');
let cookieOn = document.querySelector('.cookie-on')
let cookieOff = document.querySelector('.cookie-off')

// DARK MODE FUNCTION
const toggleBtn = document.querySelector('#toggle-display');
const theme = document.body;
let darkMode = localStorage.getItem('dark-mode');

darkmodeOn.style.display = 'none'

const enableDarkMode = () => {
    theme.classList.add('dark');
    theme.classList.remove('light');

    darkmodeBtn.classList.add('lightmode-btn');
    darkmodeSlider.classList.add('lightmode-slider');

    darkmodeOff.style.display = 'none'
    darkmodeOn.style.display = 'block'

    localStorage.setItem('dark-mode', 'enabled');
}

const disableDarkMode = () => {
    theme.classList.remove('dark');
    theme.classList.add('light');

    darkmodeBtn.classList.remove('lightmode-btn');
    darkmodeSlider.classList.remove('lightmode-slider');
    
    darkmodeOff.style.display = 'block'
    darkmodeOn.style.display = 'none'

    localStorage.setItem('dark-mode', 'disabled');
}

if (darkMode === 'enabled'){
    enableDarkMode();
}

toggleBtn.addEventListener('click', (e) => {
    darkMode = localStorage.getItem('dark-mode')
    if (darkMode === 'disabled'){
        enableDarkMode();
    }
    else{
        disableDarkMode();
    }
});

//NOTIFICATION FUNCTION
let notification = localStorage.getItem('notification-mode');

notificationOn.style.display = 'none'

const enableNotification = () => {
    notificationBtn.classList.add('lightmode-btn');
    notificationSlider.classList.add('lightmode-slider');

    notificationOff.style.display = 'none'
    notificationOn.style.display = 'block'

    localStorage.setItem('notification-mode', 'enabled');
}

const disableNotification = () => {
    notificationBtn.classList.remove('lightmode-btn');
    notificationSlider.classList.remove('lightmode-slider');
    
    notificationOff.style.display = 'block'
    notificationOn.style.display = 'none'

    localStorage.setItem('notification-mode', 'disabled');
}

if (notification === 'enabled'){
    enableNotification();
}

notificationBtn.addEventListener('click', (e) => {
    notification = localStorage.getItem('notification-mode')
    if (notification === 'disabled'){
        enableNotification();
    }
    else{
        disableNotification();
    }
});


//COOKIE FUNCTION
let cookie = localStorage.getItem('cookie-mode');

cookieOn.style.display = 'none'

const enableCookie = () => {
    cookieBtn.classList.add('lightmode-btn');
    cookieSlider.classList.add('lightmode-slider');

    cookieOff.style.display = 'none'
    cookieOn.style.display = 'block'

    localStorage.setItem('cookie-mode', 'enabled');
}

const disableCookie = () => {
    cookieBtn.classList.remove('lightmode-btn');
    cookieSlider.classList.remove('lightmode-slider');
    
    cookieOff.style.display = 'block'
    cookieOn.style.display = 'none'

    localStorage.setItem('cookie-mode', 'disabled');
}

if (cookie === 'enabled'){
    enableCookie();
}

cookieBtn.addEventListener('click', (e) => {
    cookie = localStorage.getItem('cookie-mode')
    if (cookie === 'disabled'){
        enableCookie();
    }
    else{
        disableCookie();
    }
});

//*****************************************//

/* SIGNOUT FUNCTION  */

let signout = document.querySelector('.signout-prompt')

function SignOut(){
    let signout = document.querySelector('.signout-prompt')
    signout.classList.toggle('signout-prompt-show')
}

function _SignOut(){
    let signout = document.querySelector('.signout-prompt')
    signout.className = 'signout-prompt'
}


//*****************************************//

/* PROFILE FUNCTION */


let profile = document.querySelector('.profile')

function ProfilePage(){
    profile.classList.toggle('profile-show')
}

function _ProfilePage(){
    profile.className = 'profile'
}

//*****************************************//
