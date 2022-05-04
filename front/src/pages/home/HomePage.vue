<template>
  <div class="home">
    <img alt="Vue logo" src="@/assets/img/puri.jpg" />
    <h1>Welcome home</h1>
  </div>
  
    <select v-model="selectedUser">
      <option :value="null" disabled>Selecciona un usuario</option>
      <option v-for="user in users" :value="user" :key="user.id">
        {{ user.user }}
      </option>
    </select>
    <button @click="onButtonClicked">Acceder</button>

</template>

<script>
import { useStorage } from "@vueuse/core";

export default {
  name: 'Home',
  data() {
    return {
      info: {},
      users: [],
      selectedUser: null,
      localUser: useStorage("user", {}),
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {

      const response = await fetch('http://localhost:5000/api/users')
      this.users = await response.json()
      
    },
    onButtonClicked (){

    this.localUser = {
      userId: this.selectedUser.user_id,
      user: this.selectedUser.user,
      isLibrarian: this.selectedUser.is_librarian
    }
    if (this.localUser.isLibrarian == 1){
      this.$router.push("/librarian/dashboard")
      } else {
      this.$router.push("/user/dashboard")
      }
   } 
  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}
</style>
