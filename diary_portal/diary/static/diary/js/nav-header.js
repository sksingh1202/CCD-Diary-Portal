const currentLocation = location.href;
const navItem  = document.querySelectorAll('a.nav-link');
const navLength = navItem.length;
for(var i=0;i<navLength;i++){
    if(navItem[i].href === currentLocation)
    {
        navItem[i].className += " active"
    }
}
