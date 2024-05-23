<h1 align="center"> 

<img src="static/images/logo.png" alt="Logo" width="250" height="80"><br><br>
Movies website<br>


</h1>


<h2>Despre proiect:</h2>
<h4>
Movies website, este o aplicatie web similara cu Netflix, realizata folosind framework-ul Django</h4><br>
<img src="https://i.imgur.com/kqW1QPD.png" alt="sc">
<h2>Features:<br></h2>
<h4>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Utilizatorii pot naviga prin diferite
filme , pot vedea informatii detaliate despre fiecare film si viziona.<br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Pot adauga filme in lista de favorite.<br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Pot cauta filmul dorit folosind cautare sau
pot cauta dupa genres in bara de navigare.<br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Pentru a folosi aplicatie web este necesara
inregistrarea.<br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Filme se pot adauga din interfata admin
doar de superuserul creat.
</h4>

<h2>Tehnologii si Tool-uri Utilizate:</h2>
<h4>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Python - limbaj programare<br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Pycharm - IDE  <br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Django - Webframework <br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Html si css pentru partea de frontend <br>
<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Sqlite - pentru baza date<br>
</h4>

<h2>Instructiuni de instalare si rulare a proiectului:</h2>

<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Cloneaza acest reposity local in folderul
dorit<br>

```sh
git clone https://github.com/h41pa/netflixmovies-clone-django.git
```

<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Instaleaza dependintele proiectului<br>

```sh
pip install –r requirements.txt
```

<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> in folderul proiectului ruleaza comanda pentru a porni serverul <br>

```sh
python manage.py runserver
```

<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Ruleaza comenzile pentru migrarea bazei de date (daca este necesar)<br>

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Dupa ce serverul porneste poti folosit aplicatia in broweser cu adresa <a href="http://127.0.0.1:8000/"> http://127.0.0.1:8000/</a> 
<br>
Pentru a folosi aplicatie trebuie sa te inregistrezi sau poti folosi datele (username= test si pass=1234)<br>
Pentru a adauga filme , sterge, edita, vedea baza de date trebuie sa te loghezi in panoul admin <a href="http://127.0.0.1:8000/admin"> http://127.0.0.1:8000/admin</a> cu datele(user = vanitas, pass = 1234) sau creezi un nou superuser cu comanda:<br>

```sh
python manage.py createsuperuser
```

<img src="https://i.imgur.com/yvW8NqT.png" alt="dot" width="12" height="12"> Aplica este incarca si pe webn pe adresa: <a href="https://movies-website-django.onrender.com"> https://movies-website-django.onrender.com</a>  <br>


<h2>Screenshots:</h2>

<img src="https://i.imgur.com/ohRc9Vr.png" alt="sc"><br>
<img src="https://i.imgur.com/ANhRjmB.png" alt="sc"><br>
<img src="https://i.imgur.com/xBq1dTN.png" alt="sc"><br>
<img src="https://i.imgur.com/i4QUYj9.png" alt="sc"><br>
<img src="https://i.imgur.com/hHwdTeM.png" alt="sc"><br>
<img src="https://i.imgur.com/quxrQwm.png" alt="sc"><br>
<img src="https://i.imgur.com/SLyr9ub.png" alt="sc"><br>
<img src="https://i.imgur.com/WuJxqeW.png" alt="sc"><br>
<img src="https://i.imgur.com/3gmDIs1.png" alt="sc"><br>
<img src="https://i.imgur.com/RAoK9Iu.png" alt="sc"><br>

<h2>Contributing:</h2>

If you want to contribute to this project you can e-mail me - yserved@gmail.com or you can pull request.