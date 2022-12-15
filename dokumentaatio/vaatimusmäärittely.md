# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi testata kirjoitusnopeuttaan, ja saada tilastollisen palautteen joka harjoituksesta. Tilastot tallennetaan tietokantaan, jota pelaaja pystyy itse tarkastella myöhemmin. Käyttäjä kirjautuu sovellukseen uniikilla käyttäjätunnuksella.

## Käyttäjät

Sovelluksella on vain yksi käyttäjärooli, jolla on uniikki käyttäjänimi ja ei-tyhjä salasana. Jokaisella käyttäjällä on persoonalliset tilastot. Käyttäjät eivät ole vuorovaikutuksessa muiden käyttäjien kanssa.

## Käyttöliittymäluonnos

![Käyttöliittymäluonnos](./kuvat/k%C3%A4ytt%C3%B6liittym%C3%A4luonnos.jpg)

Sovellus aukeaa kirjautumisnäkymään, josta käyttäjä voi luoda uuden käyttäjän tai kirjautua sisään aikaisemmin luotuun käyttäjään. Kirjautumisen jälkeen käyttäjä voi tehdä kirjoitusharjoituksia, tarkastella tilastojaan, tai kirjautua ulos. 

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista (tehty)

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
    -   Käyttäjätunnuksen täytyy olla uniikki
- Käyttäjä voi kirjautua järjestelmään
    - Kirjautuminen toimii käyttäjän syöttäen aikaisemmin luodun käyttäjätunnuksen ja siihen vastaavan salasanan
    - Järjestelmä ilmoittaa, jos käyttäjätunnusta ei löydetä, tai salasana ei ole oikein

### Kirjautumisen jälkeen (tehty)

- Sovellus tervehtii käyttäjää, ja antaa käyttäjän valita kolme eri toiminnallisuutta
    - Aloita uusi kirjoitusharjoitus
        - Tämä harjoitus on valittu satunnaisesti tietokannasta
    - Tarkastele persoonallisia kokonaistilastoja
        - Total Tests taken
        - Average accuracy
        - Average words per minute
        - Fastest words per minute
        - Slowest words per minute
    - Kirjaudu ulos

### Kirjoitusharjoitus (tehty)

- Sovellus antaa satunnaisen tekstinäytteen internetistä, joka hänen pitää kirjoittaa tekstilomakkeelle

- Sovellus antaa real-time tilastoja kirjoituksen oikeudesta, kuten tarkkuus, words per minute etc.

- Sovellus pitää yllä kirjoitettujen sanojen määrää, ja harjoitus päättyy kun kirjoitettu teksti sisältää yhtä monta sanaa kuin esimerkkiteksti.

### Kirjoitusharjoituksen päättyminen (tehty)

- Sovellus näyttää lopputilastot kyseisestä harjoituksesta

- Käyttäjä voi valita palaavansa päävalikkoon, tai aloittaa uuden harjoituksen

## Jatkokehitysideoita

- High-score tilastot jossa näkyy top 10 nopeinta suoritusta harjoitusta kohden

- Mahdollisuus valita jokin tietty harjoitus satunnaisen sijasta

- Uusi käyttäjäluokka, joka voi lisätä ja poistaa harjoituksia

- Käyttäjätunnuksen poisto

- Historia aikaisemmista suorituksista tilastojen lisäksi




