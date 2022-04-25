window.addEventListener('scroll', function(){
  if(pageYOffset >= 100){
    item1.classList.add('reveal')
  }
  if(pageYOffset >= 800){
    item2.classList.add('reveal')
  }
  if(pageYOffset >= 1600){
    item3.classList.add('reveal')
  }
})
