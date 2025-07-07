<template>
    <div id="app">
    <header class="header">
      <div class="nav-buttons">
        <button @click="currentPage = 'home'">ホーム</button>
        <button @click="currentPage = 'setting'">管理者</button>
      </div>
    </header>
    <component
      :is="currentPageComponent"
      :onChangePage="changePage"
    />
  </div>
</template>
<script setup>
import Home from './components/Home.vue'
import WomensOpen from './components/WomensOpen.vue'
import Setting from './components/Setting.vue'
import NameRecord from './components/NameRecord.vue'
import RefereeRegistration from './components/RefereeRegistration.vue'
import { ref, computed } from 'vue'

const currentPage = ref('home')
const currentPageComponent = computed(() => {
  switch (currentPage.value) {
    case 'home':
      return Home
    case 'womensOpen':
      return WomensOpen
    case 'setting':
      return Setting
    case 'nameRecord':
      return NameRecord
      case 'RefereeRegistration':
      return RefereeRegistration
  }
})

function changePage(page) {
  currentPage.value = page
}
</script>
<style>
#app {
  font-family: 'Arial';
  padding: 20px;
}
</style>