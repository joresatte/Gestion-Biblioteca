<template>
<header><h1>Biblioteca Puri</h1>
  <router-link to="/">Home</router-link>|
  <router-link to="/books">Libros</router-link>
</header>
  
  <router-view />
</template>

<style>

  * {
    margin: 0;
  }

  header {
    background: green;
    padding-bottom: 2ex;
    padding-top: 2ex;
    margin-bottom: 2ex;
    color: rgb(255, 255, 255);
  }
  a {
    padding:0.5em;
    text-decoration: none;
    color: aquamarine;
    font-size: 1.5em;
    text-decoration: underline;

    
  }
  
</style>