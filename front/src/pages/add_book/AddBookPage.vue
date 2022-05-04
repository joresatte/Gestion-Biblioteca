<template>
<form>
<label for="title" >Título:</label> 
<input type="text" name="título" v-model="title" required>
<label for="author">Autor: </label>
<input type="text" name="autor" v-model="author" required>
<label for="publisher">Editorial: </label>
<input type="text" name="editorial" v-model="publisher" required>
<label for="ean">Ean: </label>
<input type="text" name="ean" v-model="ean" required>
</form>
<button @click.prevent="addNewBook">Guardar</button>
</template>

<script>
import { useStorage } from "@vueuse/core";
import {v4 as uuidv4} from 'uuid';
export default {
    data(){
        return{
            title: "",
            author: "",
            publisher: "",
            ean:"",
            localUser: useStorage("user", {}),
        }
    },
    mounted(){
    },
    methods:{
        async addNewBook(){
            let bookId = uuidv4()
            if (this.title != "" && this.author != "" && this.publisher != "" && this.ean != ""){

            let newBook = {
                'id': bookId,
                'title': this.title ,
                'author': this.author ,
                'publisher': this.publisher,
                'ean': this.ean
            
            }

            const settings = {
                method: 'POST',
                body: JSON.stringify(newBook),
                headers: {
                    'Content-Type': 'application/json'
                }
            }

            let response = await fetch('http://localhost:5000/api/books', settings)

            this.$router.push(`/books`)
            return response
        }
        }

        }
    

}
</script>

<style scoped>
form{
display:grid;
grid-template-columns: 1fr 1fr;
margin: 0 1em 1em 0
}

</style>