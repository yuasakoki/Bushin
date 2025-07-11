<template>
  <div id="app">
    <header class="header">
      <div class="nav-buttons">
        <button @click="currentPage = 'home'">ホーム</button>
        <button @click="currentPage = 'setting'">管理者</button>
      </div>
    </header>
    <component :is="currentPageComponent" :onChangePage="changePage" :category="currentPage" />
  </div>
</template>
<script setup>
import Home from './components/Home.vue'
// 試合結果ページ
import ResultView from './components/result_page/ResultView.vue'
// 管理者ページ
import Setting from './components/setting_page/Setting.vue'
import PlayerRegistration from './components/setting_page/PlayerRegistration.vue'
import RefereeRegistration from './components/setting_page/RefereeRegistration.vue'
import { ref, computed } from 'vue'

const currentPage = ref('home')
const currentPageComponent = computed(() => {
  console.log('currentPage:', currentPage.value)
  switch (currentPage.value) {
    case 'home':
      return Home
    case 'womensOpenResult':
    case 'menAdvancedResult':
    case 'menIntermediateResult':
    case 'menBeginnerResult':
    case 'womenAdvancedResult':
    case 'womenIntermediateResult':
    case 'womenBeginnerResult':
      return ResultView
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