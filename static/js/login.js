document.addEventListener("DOMContentLoaded", function () {
       const loginBox = document.querySelector('.card');
       loginBox.style.opacity = "0";
       setTimeout(() => {
           loginBox.style.opacity = "1";
           loginBox.style.transform = "translateY(0)";
       }, 200);
   });
