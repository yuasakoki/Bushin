<template>
  <div id="app">
    <h1>武神会</h1>
    <!-- <input v-model="name" placeholder="名前を入力" />
    <p>こんにちは、{{ name }}さん！</p> -->    
    <button @click="currentPage = 'home'">ホーム</button>
    <button @click="currentPage = 'about'">別ページ</button>
    <button @click="currentPage = 'nameRecord'">選手登録</button>

    <component :is="currentPageComponent" />
  </div>
</template>
<script setup>
import Home from './components/Home.vue'
import About from './components/About.vue'
import NameRecord from './components/NameRecord.vue'
import { ref, computed } from 'vue'

const currentPage = ref('home')
const currentPageComponent = computed(() => {
  switch (currentPage.value) {
    case 'home':
      return Home
    case 'about':
      return About
    case 'nameRecord':
      return NameRecord
    default:
      return Home // 万が一のときのフォールバック
  }
})

// const show = ref(true)
</script>
<style>
#app {
  font-family: 'Arial';
  padding: 20px;
}
</style>