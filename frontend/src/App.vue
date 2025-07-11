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
import MenAdvanced from './components/result_page/MenAdvanced.vue'
import MenIntermediate from './components/result_page/MenIntermediate.vue'
import MenBeginner from './components/result_page/MenBeginner.vue'
import WomenAdvanced from './components/result_page/WomenAdvanced.vue'
import WomenIntermediate from './components/result_page/WomenIntermediate.vue'
import WomenBeginner from './components/result_page/WomenBeginner.vue'
import WomensOpen from './components/result_page/WomensOpen.vue'
import Setting from './components/setting_page/Setting.vue'
import PlayerRegistration from './components/setting_page/PlayerRegistration.vue'
import RefereeRegistration from './components/setting_page/RefereeRegistration.vue'
import { ref, computed } from 'vue'

const currentPage = ref('home')
const currentPageComponent = computed(() => {
  switch (currentPage.value) {
    case 'home':
      return Home
    case 'womensOpen':
      return WomensOpen
    case 'menAdvanced':
      return MenAdvanced
    case 'menIntermediate':
      return MenIntermediate
    case 'menBeginner':
      return MenBeginner
    case 'womenAdvanced':
      return WomenAdvanced
    case 'womenIntermediate':
      return WomenIntermediate
    case 'womenBeginner':
      return WomenBeginner
    case 'setting':
      return Setting
    case 'playerRegistration':
      return PlayerRegistration
    case 'refereeRegistration':
      return RefereeRegistration
  }
})

function changePage(page) {
  currentPage.value = page
}
</script>