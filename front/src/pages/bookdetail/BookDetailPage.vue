<template>
  <h1>Detalles del libro</h1>
  <article>
    <h3>Título : {{ card.title }}</h3>
    <h3>Autor : {{ card.author }}</h3>
    <h3>Editorial: {{ card.publisher }}</h3>
    <h3>EAN : {{ card.ean }}</h3>
  </article>
  <button class="delete" @click="deleteBook">Eliminar</button>
  <button class="edit" @click="$router.push(`/books/edit/${card.id}`)">
    Editar libro
  </button>
  <button class="reserve" @click="reserveBook">Reservar libro</button>
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
  name: "BookDetail",
  data() {
    return {
      card: {},
      bookId: this.$route.params.id,
      localUser: useStorage("user", {}),
    };
  },

  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
      let endpoint = "http://localhost:5000/api/books/";
      endpoint += this.bookId;
      let response = await fetch(endpoint);
      this.card = await response.json();
    },
    async deleteBook() {
      let endpoint = "http://localhost:5000/api/books/";
      endpoint += this.bookId;
      const settings = {
        method: "DELETE",
      };
      let response = await fetch(endpoint, settings);
      this.$router.push(`/books`);
      return response;
    },

    async reserveBook() {
      let endpoint = "http://localhost:5000/api/loans";
      const settings = {
        method: "POST",
        body: {
          loan_id: "loan-1",
          book_id: "libro-1",
          user_id: "usuario-1",
        },
      };

      let response = await fetch(endpoint, settings);
      this.$router.push(`/loans`);
      console.log(response);
      return response;
    },
  },
};
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
