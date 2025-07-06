<template>
    <header>
        <p>管理者メニュー</p> 
    </header>
  <div id="settings">
    <button @click="onChangePage('nameRecord')">選手登録</button>
  </div>
</template>
<script setup>
defineProps(['onChangePage'])
</script>
<style>
#app {
  font-family: 'Arial';
  padding: 20px;
}
</style>