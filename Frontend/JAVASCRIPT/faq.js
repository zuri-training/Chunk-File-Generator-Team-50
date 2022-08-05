//#############################//
//##  Ochiche Juicio Wisdom ##//
// ##     faq accordion    ##//
//##########################//


//Variables
const accordion = document.getElementsByClassName('accordion-container');

for(i = 0; i < accordion.length; i++) {
   accordion[i].addEventListener('click', function () {
        this.classList.toggle('active');
   } )
}