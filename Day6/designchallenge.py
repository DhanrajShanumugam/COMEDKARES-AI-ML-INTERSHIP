```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Movie Ratings Dashboard</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

body {
    background: #0f1117;
    color: #fff;
}

/* SIDEBAR */
.sidebar {
    position: fixed;
    width: 230px;
    height: 100vh;
    background: #171a23;
    padding: 25px 18px;
}

.logo {
    font-size: 24px;
    font-weight: bold;
    color: #ffcc33;
    margin-bottom: 40px;
}

.logo span {
    color: white;
}

.menu {
    list-style: none;
}

.menu li {
    padding: 14px;
    margin: 8px 0;
    border-radius: 8px;
    cursor: pointer;
    color: #aeb3c2;
}

.menu li:hover,
.menu .active {
    background: #252a36;
    color: #ffcc33;
}

/* MAIN */
.main {
    margin-left: 230px;
    padding: 25px;
}

/* HEADER */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
}

.header h1 {
    font-size: 30px;
}

.search {
    background: #1c202a;
    border: 1px solid #303542;
    padding: 12px 18px;
    border-radius: 25px;
    color: white;
    width: 260px;
    outline: none;
}

/* STAT CARDS */
.stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 25px;
}

.card {
    background: #181c25;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #282d39;
}

.card h4 {
    color: #9ca3b5;
    font-size: 14px;
    margin-bottom: 10px;
}

.card h2 {
    font-size: 27px;
}

.yellow {
    color: #ffcc33;
}

.green {
    color: #46d39a;
}

.blue {
    color: #5aa9ff;
}

.red {
    color: #ff6678;
}

/* CONTENT GRID */
.content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
}

.panel {
    background: #181c25;
    border: 1px solid #282d39;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
}

.panel h2 {
    margin-bottom: 18px;
    font-size: 20px;
}

/* BAR CHART */
.chart {
    height: 240px;
    display: flex;
    align-items: end;
    justify-content: space-around;
    gap: 15px;
    padding: 20px 10px 0;
}

.bar-box {
    text-align: center;
    width: 50px;
}

.bar {
    width: 100%;
    background: #ffcc33;
    border-radius: 6px 6px 0 0;
    transition: 0.3s;
}

.bar:hover {
    background: #fff;
}

.bar-label {
    margin-top: 8px;
    color: #999;
    font-size: 12px;
}

/* GENRE */
.genre {
    margin-bottom: 17px;
}

.genre-title {
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
    font-size: 14px;
}

.progress {
    height: 8px;
    background: #292e39;
    border-radius: 10px;
    overflow: hidden;
}

.progress div {
    height: 100%;
    background: #ffcc33;
}

/* MOVIES */
.movies {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.movie {
    background: #20242e;
    border-radius: 10px;
    overflow: hidden;
    transition: 0.3s;
}

.movie:hover {
    transform: translateY(-5px);
}

.poster {
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 45px;
    background: linear-gradient(135deg,#363b48,#161920);
}

.movie-info {
    padding: 14px;
}

.movie-info h3 {
    margin-bottom: 7px;
}

.rating {
    color: #ffcc33;
    font-weight: bold;
}

.genre-tag {
    display: inline-block;
    background: #303543;
    color: #aaa;
    padding: 4px 8px;
    border-radius: 5px;
    font-size: 11px;
    margin-top: 8px;
}

/* TABLE */
table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    text-align: left;
    padding: 13px;
    border-bottom: 1px solid #292e38;
}

th {
    color: #9da4b5;
    font-size: 13px;
}

td {
    font-size: 14px;
}

.stars {
    color: #ffcc33;
}

/* RESPONSIVE */
@media(max-width: 1000px) {
    .stats {
        grid-template-columns: repeat(2,1fr);
    }

    .content {
        grid-template-columns: 1fr;
    }
}

@media(max-width: 700px) {
    .sidebar {
        display: none;
    }

    .main {
        margin-left: 0;
    }

    .stats,
    .movies {
        grid-template-columns: 1fr;
    }

    .header {
        flex-direction: column;
        align-items: flex-start;
        gap: 15px;
    }

    .search {
        width: 100%;
    }
}
</style>
</head>

<body>

<!-- SIDEBAR -->
<aside class="sidebar">

    <div class="logo">🎬 <span>Movie</span>Hub</div>

    <ul class="menu">
        <li class="active">📊 Dashboard</li>
        <li>🎞 Movies</li>
        <li>⭐ Ratings</li>
        <li>🎭 Genres</li>
        <li>🔥 Popular</li>
        <li>⚙ Settings</li>
    </ul>

</aside>


<!-- MAIN -->
<main class="main">

    <!-- HEADER -->
    <div class="header">
        <div>
            <h1>Movie Ratings Dashboard</h1>
            <p style="color:#8f96a8;margin-top:6px;">
                Explore movies, ratings & popularity
            </p>
        </div>

        <input
            type="text"
            class="search"
            id="search"
            placeholder="🔍 Search movies..."
            onkeyup="searchMovies()"
        >
    </div>


    <!-- STATISTICS -->
    <section class="stats">

        <div class="card">
            <h4>TOTAL MOVIES</h4>
            <h2 class="yellow">12,480</h2>
        </div>

        <div class="card">
            <h4>AVERAGE RATING</h4>
            <h2 class="green">7.8 ⭐</h2>
        </div>

        <div class="card">
            <h4>TOP GENRE</h4>
            <h2 class="blue">Drama</h2>
        </div>

        <div class="card">
            <h4>MOST POPULAR</h4>
            <h2 class="red">Inception</h2>
        </div>

    </section>


    <!-- CONTENT -->
    <section class="content">

        <!-- LEFT -->
        <div>

            <!-- RATING CHART -->
            <div class="panel">

                <h2>📈 Average Ratings by Year</h2>

                <div class="chart">

                    <div class="bar-box">
                        <div class="bar" style="height:110px"></div>
                        <div class="bar-label">2019</div>
                    </div>

                    <div class="bar-box">
                        <div class="bar" style="height:135px"></div>
                        <div class="bar-label">2020</div>
                    </div>

                    <div class="bar-box">
                        <div class="bar" style="height:150px"></div>
                        <div class="bar-label">2021</div>
                    </div>

                    <div class="bar-box">
                        <div class="bar" style="height:165px"></div>
                        <div class="bar-label">2022</div>
                    </div>

                    <div class="bar-box">
                        <div class="bar" style="height:185px"></div>
                        <div class="bar-label">2023</div>
                    </div>

                    <div class="bar-box">
                        <div class="bar" style="height:205px"></div>
                        <div class="bar-label">2024</div>
                    </div>

                    <div class="bar-box">
                        <div class="bar" style="height:220px"></div>
                        <div class="bar-label">2025</div>
                    </div>

                </div>

            </div>


            <!-- TOP MOVIES -->
            <div class="panel">

                <h2>🔥 Top Rated Movies</h2>

                <div class="movies" id="movieList">

                    <div class="movie">
                        <div class="poster">🌀</div>
                        <div class="movie-info">
                            <h3>Inception</h3>
                            <span class="rating">⭐ 8.8</span>
                            <br>
                            <span class="genre-tag">Sci-Fi</span>
                        </div>
                    </div>

                    <div class="movie">
                        <div class="poster">🦇</div>
                        <div class="movie-info">
                            <h3>The Dark Knight</h3>
                            <span class="rating">⭐ 9.0</span>
                            <br>
                            <span class="genre-tag">Action</span>
                        </div>
                    </div>

                    <div class="movie">
                        <div class="poster">🚀</div>
                        <div class="movie-info">
                            <h3>Interstellar</h3>
                            <span class="rating">⭐ 8.7</span>
                            <br>
                            <span class="genre-tag">Sci-Fi</span>
                        </div>
                    </div>

                    <div class="movie">
                        <div class="poster">🧙</div>
                        <div class="movie-info">
                            <h3>Harry Potter</h3>
                            <span class="rating">⭐ 8.5</span>
                            <br>
                            <span class="genre-tag">Fantasy</span>
                        </div>
                    </div>

                    <div class="movie">
                        <div class="poster">🦖</div>
                        <div class="movie-info">
                            <h3>Jurassic World</h3>
                            <span class="rating">⭐ 8.2</span>
                            <br>
                            <span class="genre-tag">Adventure</span>
                        </div>
                    </div>

                    <div class="movie">
                        <div class="poster">🕷️</div>
                        <div class="movie-info">
                            <h3>Spider-Man</h3>
                            <span class="rating">⭐ 8.4</span>
                            <br>
                            <span class="genre-tag">Action</span>
                        </div>
                    </div>

                </div>

            </div>

        </div>


        <!-- RIGHT -->
        <div>

            <!-- GENRES -->
            <div class="panel">

                <h2>🎭 Popular Genres</h2>

                <div class="genre">
                    <div class="genre-title">
                        <span>Drama</span>
                        <span>82%</span>
                    </div>
                    <div class="progress">
                        <div style="width:82%"></div>
                    </div>
                </div>

                <div class="genre">
                    <div class="genre-title">
                        <span>Action</span>
                        <span>75%</span>
                    </div>
                    <div class="progress">
                        <div style="width:75%"></div>
                    </div>
                </div>

                <div class="genre">
                    <div class="genre-title">
                        <span>Comedy</span>
                        <span>68%</span>
                    </div>
                    <div class="progress">
                        <div style="width:68%"></div>
                    </div>
                </div>

                <div class="genre">
                    <div class="genre-title">
                        <span>Sci-Fi</span>
                        <span>61%</span>
                    </div>
                    <div class="progress">
                        <div style="width:61%"></div>
                    </div>
                </div>

                <div class="genre">
                    <div class="genre-title">
                        <span>Horror</span>
                        <span>49%</span>
                    </div>
                    <div class="progress">
                        <div style="width:49%"></div>
                    </div>
                </div>

            </div>


            <!-- RECENT RATINGS -->
            <div class="panel">

                <h2>⭐ Recent Ratings</h2>

                <table>

                    <thead>
                        <tr>
                            <th>Movie</th>
                            <th>Rating</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr>
                            <td>Inception</td>
                            <td class="stars">★★★★★</td>
                        </tr>

                        <tr>
                            <td>Avatar</td>
                            <td class="stars">★★★★☆</td>
                        </tr>

                        <tr>
                            <td>Interstellar</td>
                            <td class="stars">★★★★★</td>
                        </tr>

                        <tr>
                            <td>Joker</td>
                            <td class="stars">★★★★☆</td>
                        </tr>

                        <tr>
                            <td>Oppenheimer</td>
                            <td class="stars">★★★★★</td>
                        </tr>
                    </tbody>

                </table>

            </div>

        </div>

    </section>

</main>


<script>

/* MOVIE SEARCH */
function searchMovies() {

    let input =
        document.getElementById("search")
        .value
        .toLowerCase();

    let movies =
        document.querySelectorAll(".movie");

    movies.forEach(movie => {

        let name =
            movie.querySelector("h3")
            .innerText
            .toLowerCase();

        if (name.includes(input)) {
            movie.style.display = "block";
        } else {
            movie.style.display = "none";
        }

    });
}

</script>

</body>
</html>
```

