<template>
  <section>
      <div>
        <input type="text" class="searcher" v-model="bookFilter">
        <button class="search-book-button" @click="onClickedFilter">Buscar libro</button>
        <button class="search-book-button" @click="clearFilter">Ver todos los libros</button>
      </div>
      <div>
      <button class="add-book-button" @click="$router.push(`/books/add`)">Añadir libro</button>
      </div>
      <article v-for="card in filteredBooks" :key="card.ean">
        <h2 class="title">{{card.title}} </h2>
        <h3 class="author">Autor: {{card.author}} </h3>
        <h3 class="publisher">Editorial: {{card.publisher}}</h3>
        <h3 class="ean">EAN: {{card.ean}}</h3>
        <button @click="$router.push(`/books/${card.id}`)">Detalles del libro</button>
      </article> 
  </section>
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
    data(){
        return{
            cards: [],
            bookFilter: "",
            filteredBooks:[],
            localUser: useStorage("user", {}),
        }
    },
    mounted(){
        this.loadData()
    },
    methods:{
        async loadData(){
            const endpoint= "http://localhost:5000/api/books"
            let respone = await fetch (endpoint)
            this.cards =await respone.json()
        },
        onClickedFilter(){
            let book = [];
            for (let card of this.cards){
                if(card.title.toLowerCase().includes(this.bookFilter.toLowerCase())){
                book.push(card);}
            this.filteredBooks = book;
            }
        },
        clearFilter(){
            this.filteredBooks = this.cards
        }
    },

}
</script>

<style scoped>
article{
    border: 1px solid black;
    margin: 2em;
    padding: 1em;
    
}
.add-book-button{
float: left;
margin-left: 3em;
margin-top: 0.5em;
}


</style>
