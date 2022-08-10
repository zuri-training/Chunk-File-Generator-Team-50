// for dropdown
const burger = document.getElementById('burger');
let navs = document.querySelectorAll('.dropdown')
console.log(navs);


burger.addEventListener('click', function () {
    if (navs[0].classList.contains('block') && navs[1].classList.contains('block')) {
        navs[0].classList.remove('block');
        navs[1].classList.remove('block');
    }
    else {
        navs[0].classList.add('block');
        navs[1].classList.add('block');
    }
})

$(document).ready(function () {

    $('ul.navbar-nav > li')
        .click(function (e) {
            $('ul.navbar-nav > li')
                .removeClass('active');
            $(this).addClass('active');
        });
});

// for search bar
function openPage() {
    let answer = document.getElementById('search').value;
    let home = /home/gi;
    let faq = /faq/gi;
    let faq2 = /question/gi;
    let terms = /term/gi;
    let split = /split/gi;
// if you have a valid link to this page try adding ,"_self" to make it appear on the same window
    if (home.test(answer)) {
        window.open("../HTML/home.html");
    }
    if (faq.test(answer) || faq2.test(answer)) {
        window.open("../HTML/faq.html");
    }
    if (terms.test(answer)) {
        window.open("../HTML/termsofservice.html");
    }
    if (split.test(answer)) {
        window.open("../HTML/splitjson.html");
    }
   
}