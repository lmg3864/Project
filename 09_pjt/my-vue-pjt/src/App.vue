<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-info bg-opacity-10">
      <div class="container-fluid mx-5">
        <img class="navbar-brand ms-5" src="@/assets/ssafy-logo.png" style="width: 80px;" alt="">
        <div class="collapse navbar-collapse d-flex justify-content-end">
          <div class="navbar-nav me-5 fw-bold">
            <router-link :to="{name: 'movies'}" class="nav-link">Movies    </router-link>
            <router-link :to="{name: 'random'}" class="nav-link">Random    </router-link>
            <router-link :to="{name: 'watch-list'}" class="nav-link">WatchList</router-link>
          </div>
        </div>
      </div>
    </nav>
    <div class="container mt-5">
      <router-view/>
    </div>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
