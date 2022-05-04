<template>
<h1>{{localUser.user}}</h1>
<li class="dashboard">
<ul><router-link to="/books"><button>Lista de libros</button></router-link></ul>
<ul><router-link to="/librarian/loans"><button>Prestamos de Usuarios</button></router-link></ul>
</li>
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
    data(){
        return{
            localUser: useStorage("user", {}),
        }
    },
    mounted(){
    },
    methods:{
    }

}
</script>

<style scoped>
    button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 1em 2em;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 1em 0;
    }
    .dashboard {
        display:grid;
        grid-template-columns: 1fr;
    }
</style>