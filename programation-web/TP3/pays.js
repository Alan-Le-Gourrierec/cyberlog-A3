getCountry();

async function getCountry(){
    const url = await fetch("https://restcountries.com/v3.1/all");
    const res = await url.json();
    res.forEach(element =>{
        showCountry(element);
    });
}

    
/**
 * Permet de créer une div pour un pays
 * @param {*} element 
 */
function showCountry(element) {
    let syntaxeimg = '<img class="img" src=' + element.flags.svg + '>'; //Ajoute le drapeau du pays
    let syntaxenom = '<p class="nom">' + element.name.common + '</p>'; //Ajoute le nom du pays
    let syntaxepop = '<p class="pop">Population : ' + element.population + '</p>';  //Ajoute la population du pays
    let syntaxecap = '<p class="cap">Capital    : ' + element.capital + '</p>'; //Ajoute la capital du pays
    let syntaxereg = '<p class="reg">Region     : ' + element.region + '</p>';  //Ajoute la region du pays

    document.getElementById("listepays").innerHTML += '<a href="https://fr.wikipedia.org/wiki/'+element.name.common+'"><div class="divcountry">' + syntaxeimg + syntaxenom + syntaxepop + syntaxecap + syntaxereg + '</div></a>'; //Créé la div du pays
}