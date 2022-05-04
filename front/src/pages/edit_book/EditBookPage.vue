<template>
  <form>
    <label for="title">Título:</label>
    <input type="text" name="título" v-model="book.title" required />
    <label for="author">Autor: </label>
    <input type="text" name="autor" v-model="book.author" required />
    <label for="publisher">Editorial: </label>
    <input type="text" name="editorial" v-model="book.publisher" required />
    <label for="ean">Ean: </label>
    <input type="text" name="ean" v-model="book.ean" required />
  </form>
  <button @click.prevent="editBook">Guardar Cambios</button>
</template>

<script>
import { useStorage } from "@vueuse/core";
export default {
  data() {
    return {
      bookId: this.$route.params.id,
      book: {},
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
      this.book = await response.json();
    },
    async editBook(){
            if (this.book.title != "" && this.book.author != "" && this.book.publisher != "" && this.book.ean != ""){

            const settings = {
                method: 'POST',
                body: JSON.stringify(this.book),
                headers: {
                    'Content-Type': 'application/json'
                }}
            let endpoint = 'http://localhost:5000/api/books/'
            endpoint += this.bookId
            let response = await fetch(endpoint, settings)

            let route = '/books/'
            route += this.bookId
            this.$router.push(route)
            return response
        }
  },
  }
};
</script>

<style scoped>
form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin: 0 1em 1em 0;
}
</style>
