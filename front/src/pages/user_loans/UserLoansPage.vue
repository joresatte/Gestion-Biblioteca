<template>
    <h1>Página de usuario</h1>
    <section>
        <h3>Libros reservados</h3>
        <article v-for="loan in loans" :key="loan.loan_id">
            <h2>{{loan.title}}</h2>
            <button>Devolver libro</button>
        </article> 
    </section>
  
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
    data(){
        return{
            loans:[],
            localUser: useStorage("user", {}),
        }
    },
    mounted(){
        this.loadData()
    },
    methods:{
        async loadData(){
            // const endpoint= "http://localhost:5000/user/loans"
            // let respone = await fetch (endpoint)
            // this.loans =await respone.json()
        this.loans = [{
            "loan_id": "loan_1",
            "book_id": "book_3",
            "title": "Pilares"
        },
        {
            "loan_id": "loan_2",
            "book_id": "book_2",
            "title": "Hobbit"
        }]
                }
            }
        }
</script>

<style scoped>
article{
    border: 2px solid black;
    margin: 3em 10em;
    display:grid;
    grid-template-columns: 3fr 1fr;
    padding: 1em;

}

</style>