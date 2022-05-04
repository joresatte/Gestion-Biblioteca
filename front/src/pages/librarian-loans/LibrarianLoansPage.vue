<template>
  <h1>Libros reservados</h1>
  <section>
        <article v-for="loan in loans" :key="loan.loan_id">
            <h2>Libro:{{loan.title}}</h2>
            <h2>Usuario: {{loan.user}}</h2>
        </article>
    </section>
  
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
  name: "LibrarianLoans",
   data(){
        return{
            loans:[],
            localUser: useStorage("user", {}),
        }
    },

  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
        // const endpoint= "http://localhost:5000/librarian/loans"
        // let respone = await fetch (endpoint)
        // this.loans =await respone.json()
    this.loans = [{
            "loan_id": "loan_1",
            "book_id": "book_3",
            "title": "Pilares",
            "user": "usuario_2"
        },
        {
            "loan_id": "loan_2",
            "book_id": "book_2",
            "title": "Hobbit",
            "user": "usuario_3"
        }]
                }
            }
        }
</script>

<style scoped>
h2 {
  font-style: italic;
}

article {
  margin: 2em;
  padding: 1em;
  border: 4px solid green;
  border-radius: 1em;
}
.edit {
  margin-left: 2em;
}
</style>
