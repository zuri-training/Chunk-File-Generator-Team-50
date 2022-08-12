const sliderC = document.getElementById('slider-container');
let slider = document.querySelector('.slider');
let profile = document.querySelector('.profile');
let linksButton = document.querySelectorAll('.change');
const desktopSliderC = document.getElementById('desktop-container');
let desktopSlider = document.querySelector('.desktop-slider');

desktopSliderC.addEventListener('click',function () {
    if (desktopSlider.classList.contains('active')) {
        desktopSlider.classList.remove('active');
        desktopSlider.style.backgroundColor = 'lightgrey';
        profile.style.backgroundColor = '#3E8DE3';
        linksButton[0].style.backgroundColor = 'rgb(59, 91, 177)';
        linksButton[1].style.backgroundColor = 'rgb(59, 91, 177)';
        linksButton[2].style.backgroundColor = 'rgb(59, 91, 177)';
        linksButton[3].style.backgroundColor = 'rgb(59, 91, 177)';
        
   }
   else {
    desktopSlider.classList.add('active');
    profile.style.backgroundColor = '#3C3C3C';
    desktopSlider.style.backgroundColor = '#3E8DE3';
    linksButton[0].style.backgroundColor = '#3C3C3C';
    linksButton[1].style.backgroundColor = '#3C3C3C';
    linksButton[2].style.backgroundColor = '#3C3C3C';
    linksButton[3].style.backgroundColor = '#3C3C3C';

   }


});

sliderC.addEventListener('click', function () {
   if (slider.classList.contains('active')) {
        slider.classList.remove('active');
        slider.style.backgroundColor = '#3C3C3C';
        profile.style.backgroundColor = '#3E8DE3';
        linksButton[0].style.backgroundColor = 'rgb(59, 91, 177)';
        linksButton[1].style.backgroundColor = 'rgb(59, 91, 177)';
        linksButton[2].style.backgroundColor = 'rgb(59, 91, 177)';
        linksButton[3].style.backgroundColor = 'rgb(59, 91, 177)';
        
   }
   else {
    slider.classList.add('active');
    profile.style.backgroundColor = '#3C3C3C';
    slider.style.backgroundColor = '#3E8DE3';
    linksButton[0].style.backgroundColor = '#3C3C3C';
    linksButton[1].style.backgroundColor = '#3C3C3C';
    linksButton[2].style.backgroundColor = '#3C3C3C';
    linksButton[3].style.backgroundColor = '#3C3C3C';

   } 

});


let deleted = document.querySelectorAll('.delete');
let saved = document.querySelectorAll('.save');
let files = document.querySelectorAll('.files');
let bs = document.getElementsByClassName('.save');


for (let i = 0; i < deleted.length; i++) {
    deleted[i].addEventListener('click',function () {
        files[i].style.display = 'none';
        
    })
    console.log(deleted[i]);
};

for (i=0; i<saved.length; i++) {
    saved[i].addEventListener('click',function () {
        this.style.backgroundColor = 'rgb(178, 218, 153)';
        this.classList.add('saved');

    });
    console.log(saved);
}