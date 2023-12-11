<template>
  <div id="app">
    <nav>
      <router-link :to="{name: 'first'}">First</router-link> |
      <router-link :to="{name: 'second', params: {valueName:3}}">Second</router-link>|
      <router-link :to="{name: 'lunch'}">LUNCH</router-link> |
      <router-link 
      :to="{
        name: 'lotto',
        params: {
          lottoNum : 6
        }
        }">Lotto</router-link>
    
    </nav>
    <!-- router 의 부분만 변하는 것!! Django의 block -->
    <router-view/>
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
