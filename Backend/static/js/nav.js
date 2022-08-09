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