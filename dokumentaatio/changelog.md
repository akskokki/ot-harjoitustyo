# Changelog

## Viikko 3
- Miinakentän perustoiminta toteutettu
  - Voidaan generoida halutun kokoinen ruudukko halutulla miinamäärällä
  - Solun voi avata hiiren vasemmalla näppäimellä ja merkata miinaksi oikealla
- Lisätty ensimmäinen testi LevelGenerator-luokalle

## Viikko 4
- Vaikeustasonvalinta lisätty
- Lisää testejä Level- ja LevelGenerator-luokille

## Viikko 5
- Lopputilalogiikka lisätty
  - Häviö, jos käyttäjä avaa miinaruudun
  - Voitto, jos käyttäjä on avannut kaikki miinattomat ruudut
  - Loppuruutu, josta voi aloittaa uuden pelin tai vaihtaa vaikeustasoa
  - Lisätty testit lopputilalogiikalle
- Chording-implementaatio
  - Tyhjän ruudun avautuessa se avaa automaattisesti kaikki ympärillään olevat ruudut
- UI-refaktorointi
  - Käyttöliittymäkoodi on viimeinkin eriytetty pois index-tiedostosta, ja jokainen käyttöliittymänäkymä on nyt oma luokkansa

## Viikko 6
- Aikalaskuri lisätty
  - Pelin loppuruutu näyttää nyt peliin käytetyn ajan, jos pelaaja voittaa
- Custom vaikeustaso
  - Pelaaja voi halutessaan valita mielivaltaisen kokoisen pelikentän haluamallaan miinamäärällä
  - **Tiedetty bugi:** Jos pelikenttä on todella suuri, ja miinamäärä suhteellisen pieni, peli kaatuu tyhjien ruutujen avausketjun pituuden takia (RecursionError). Tämä tullaan korjaamaan tulevissa versioissa optimoimalla ruutujen avausalgoritmin toiminnallisuutta.
- Paljon uutta docstring-dokumentaatiota
  - Kaikki pelilogiikkaluokat, sekä tärkeimmät käyttöliittymäluokat

## Viikko 7
- Pistetaulukot lisätty
  - Vaikeusvalintaruudulla näkyy parhaat saavutetu ajat jokaisella vaikeustasolla
- Loppuhiontaa ja optimisaatiota
  - Peli ei enää kaadu ruutujen avausketjun rekursiovirheeseen isommillakaan kentillä
- GameLoop-luokan testaus lisätty
- Docstring-dokumentaatio viimeistelty
